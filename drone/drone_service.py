import ps_drone as ps_drone
import time
import cv2

class DroneService():

	def __init__(self):
		self.drone = ps_drone.Drone()
		self.inAir = False
		self.isFrontCam = True

	def setup(self, speedVector = 0.5, videoData = True, devMode = False):
		self.devMode = devMode
		self.speedVector = speedVector
		self.drone.startup()
		self.reset()
		self.drone.trim()                                       # Recalibrate sensors
		self.drone.getSelfRotation(5)                           # Get auto-alteration of gyroscope-sensor
		print "Auto-alt.:"+str(self.drone.selfRotation)+"dec/s" # Showing value for auto-alteration
		#self.drone.useDemoMode(True)
		self.drone.setSpeed(self.speedVector)
		#self.drone.getNDpackage(["demo"])      # mb here ??
		self.drone.setConfigAllID()
		if videoData:
			self.drone.sdVideo()
			self.drone.frontCam()
			self.drone.videoFPS(30)
			CDC = self.drone.ConfigDataCount
			while CDC == self.drone.ConfigDataCount: time.sleep(0.001)
			self.drone.startVideo()
			print("Battery: "+str(self.drone.getBattery()[0])+"% "+str(self.drone.getBattery()[1]))


	def takeOff(self):
		print('Taking off...')
		if not self.devMode:
			self.drone.takeoff()
			while self.drone.NavData["demo"][0][2]: time.sleep(0.1)
		self.inAir = True

	def land(self):
		print('Ladning...')
		self.drone.land()
		self.inAir = False

	def shutdown(self):
		print('Shutting down...')
		self.drone.shutdown()

	def reset(self):
		self.drone.reset()
		while (self.drone.getBattery()[0] == -1): time.sleep(0.1)

	def getVideoData(self):
		IMC = self.drone.VideoImageCount
		while (self.drone.VideoImageCount == IMC):
			time.sleep(0.01)
		IMC = self.drone.VideoImageCount
		return self.drone.VideoImage

	def move(self, data):
		if data == None:
			return None
		proportionVector = self.speedVector

		#
		# changed from if to elif down there, verify if helped	
		#
		if 'forward' in data and data['forward'] > 0:
			self.drone.moveForward(proportionVector * data['forward'])
		elif 'backward' in data and data['backward'] > 0:
			self.drone.moveBackward(proportionVector * data['backward'])
		elif 'left' in data and data['left'] > 0:
			self.drone.moveLeft(proportionVector * data['left'])
		elif 'right' in data and data['right'] > 0:
			self.drone.moveRight(proportionVector * data['right'])
		elif 'rotate_left' in data and data['rotate_left'] > 0:
			self.drone.turnLeft(proportionVector * data['rotate_left'])
		elif 'rotate_right' in data and data['rotate_right'] > 0:
			self.drone.turnRight(proportionVector * data['rotate_right'])
		elif 'up' in data and data['up'] > 0:
			self.drone.moveUp(proportionVector * data['up'])
		elif 'down' in data and data['down'] > 0:
			self.drone.moveDown(proportionVector * data['down'])
		time.sleep(0.1) # this is question...

		return data

	def execute(self, btns_data):
		# This kind of nesting make it easier for me to read
		self.execute_shutdown(btns_data)
		self.execute_land(btns_data)
		self.execute_switchCamera(btns_data)
		self.execute_faceDetectMode(btns_data)
		time.sleep(0.1) # In purpose to d not repeat. funny but working

	def execute_switchCamera(self, btns_data):
		if btns_data['square'] == 1:
			if self.isFrontCam:
				self.drone.groundCam()
				self.isFrontCam = False
			else:
				self.drone.frontCam()
				self.isFrontCam = True

	def execute_shutdown(self, btns_data):
		if btns_data['options'] == 1:
			self.shutdown()

	def execute_land(self, btns_data):
		if btns_data['circle'] == 1:
			self.land()

	def execute_faceDetectMode(self, btns_data):
		# TODO we need to implement it here rather than in main app.py
		pass

	def getData(self):
		data = ''
		return data