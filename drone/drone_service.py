import ps_drone as ps_drone

class DroneService():

	def __init__(self):
		self.drone = ps_drone.Drone()

	def setup(self, speedVector = 0.5, videoData = True):
		self.speedVector = speedVector
		self.drone.startup()
		self.reset()
		self.drone.useDemoMode(True)                        # Set 15 basic dataset/sec (default anyway)
		self.drone.setSpeed(self.speedVector)
		self.drone.getNDpackage(["demo"])                       # Packets, which shall be decoded
		self.drone.setConfigAllID()                           # Go to multiconfiguration-mode
		if videoData:
			self.drone.sdVideo()                                     # Choose lower resolution (try hdVideo())
			self.drone.frontCam()                                  # Choose front view
			self.drone.videoFPS(60)
			CDC = self.drone.ConfigDataCount
			while CDC == self.drone.ConfigDataCount: time.sleep(0.001) 		 # Wait until it is done (after resync)
		print("Battery: "+str(self.drone.getBattery()[0])+"% "+str(self.drone.getBattery()[1])) # Battery-status


	def takeOff(self):
		self.drone.takeoff()
		while self.drone.NavData["demo"][0][2]: time.sleep(0.1) # Wait until drone is completely flying

	def shutdown(self):
		self.drone.shutdown()

	def reset(self):
		self.drone.reset()
		while (self.drone.getBattery()[0] == -1): time.sleep(0.1) # Wait until drone has done its reset

	def video(self):
		self.drone.startVideo()
		self.drone.showVideo()

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

	def getData(self):
		data = self.drone.getNDpackage(["demo"])
		return data