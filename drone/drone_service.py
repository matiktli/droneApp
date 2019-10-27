import ps_drone as ps_drone
import time
import cv2

class DroneService():

	def __init__(self):
		self.drone = ps_drone.Drone()
		self.inAir = False
		self.isFrontCam = True

	def setup(self, speedVector = 0.5, videoData = True):
		self.speedVector = speedVector
		self.drone.startup()
		self.reset()
		self.drone.useDemoMode(True)
		self.drone.setSpeed(self.speedVector)
		self.drone.getNDpackage(["demo"])
		self.drone.setConfigAllID()
		if videoData:
			self.drone.sdVideo()
			self.drone.frontCam()
			self.drone.videoFPS(60)
			CDC = self.drone.ConfigDataCount
			while CDC == self.drone.ConfigDataCount: time.sleep(0.001)
			print("Battery: "+str(self.drone.getBattery()[0])+"% "+str(self.drone.getBattery()[1]))


	def takeOff(self):
		print('Taking off...')
		self.drone.takeoff()
		while self.drone.NavData["demo"][0][2]: time.sleep(0.1)
		self.inAir = True

	def land(self):
		print('Ladning...')
		self.drone.land()
		self.inAir = False

	def shutdown(self):
		print('Shutting down...')
		cv2.destroyAllWindows()
		self.drone.shutdown()

	def reset(self):
		self.drone.reset()
		while (self.drone.getBattery()[0] == -1): time.sleep(0.1)

	def video(self):
		self.drone.startVideo()
		self.drone.showVideo()

	def getVideoData(self):
		IMC = self.drone.VideoImageCount
		while (self.drone.VideoImageCount == IMC):
			time.sleep(0.01)
		IMC = self.drone.VideoImageCount
		return self.drone.VideoImage

	def move(self, data):
		proportionVector = self.speedVector
		if data['forward'] > 0:
			self.drone.moveForward(proportionVector * data['forward'])
		if data['backward'] > 0:
			self.drone.moveBackward(proportionVector * data['backward'])
		if data['left'] > 0:
			self.drone.moveLeft(proportionVector * data['left'])
		if data['right'] > 0:
			self.drone.moveRight(proportionVector * data['right'])
		if data['rotate_left'] > 0:
			self.drone.turnLeft(proportionVector * data['rotate_left'])
		if data['rotate_right'] > 0:
			self.drone.turnRight(proportionVector * data['rotate_right'])
		if data['up'] > 0:
			self.drone.moveUp(proportionVector * data['up'])
		if data['down'] > 0:
			self.drone.moveDown(proportionVector * data['down'])
		return data

	def execute(self, btns_data):
		if btns_data['circle'] == 1:
			self.shutdown()
		self.execute_switchCamera(btns_data)

		time.sleep(0.1)


	def getData(self):
		data = self.drone.getNDpackage(["demo"])
		return data

	def execute_switchCamera(self, btns_data):
		if btns_data['square'] == 1:
			if self.isFrontCam:
				self.drone.groundCam()
				self.isFrontCam = False
			else:
				self.drone.frontCam()
				self.isFrontCam = True