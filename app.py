from ps4_controler.controler_service import ControlerService
from drone.drone_service import DroneService
from video.video_service import VideoService
from log_service import Log
import sys

def awaitStart(ctrl, drone):
	till = True
	print('Press "X" to take off...')
	while till:
		_, b, _ = ctrl.getData()
		if b['x'] == 1:
			till = False
			drone.takeOff()

def flightMode(ctrl, drone, videoSvc, log, devMode = False):
	while True:
		move_instr, btns, _ = ctrl.getData()
		drone.execute(btns)
		drone.move(move_instr)

		videoData = drone.getVideoData()
		if not devMode: videoSvc.feedVideoData(videoData)
		
		log.info(drone.getData())

if __name__ == "__main__":
	devMode = False
	arguments = str(sys.argv)
	if 'dev' in arguments: 
		print('--- DEV MODE ---')
		devMode = True
	log = Log()
	ctrl = ControlerService()
	drone = DroneService()
	videoSvc = VideoService()
	try:
		drone.setup(devMode = devMode)
		drone.video()
		awaitStart(ctrl, drone)
		flightMode(ctrl, drone, videoSvc, log, devMode = devMode)
		videoSvc
	except(KeyboardInterrupt):
		print('interrupted!')
		drone.shutdown()
		sys.exit(0)
	except(IOError):
		print('interrupted!')
		drone.shutdown()
		sys.exit(0)
	finally:
		if not devMode: videoSvc.endRecording()
