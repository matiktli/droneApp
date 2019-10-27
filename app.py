from ps4_controler.controler_service import ControlerService
from drone.drone_service import DroneService
from video.video_service import VideoService
from log_service import Log

def awaitStart(ctrl, drone):
	till = True
	print('Press "X" to take off...')
	while till:
		_, b, _ = ctrl.getData()
		if b['x'] == 1:
			till = False
			drone.takeOff()

def flightMode(ctrl, drone, videoSvc, log):
	while True:
		move_instr, btns, _ = ctrl.getData()
		drone.execute(btns)
		drone.move(move_instr)

		videoData = drone.getVideoData()
		videoSvc.feedVideoData(videoData)
		
		log.info(drone.getData())

if __name__ == "__main__":
	log = Log()
	ctrl = ControlerService()
	drone = DroneService()
	videoSvc = VideoService()
	try:
		drone.setup()
		drone.video()
		awaitStart(ctrl, drone)
		flightMode(ctrl, drone, videoSvc, log)
	except(KeyboardInterrupt):
		print('interrupted!')
		drone.shutdown()
		sys.exit(0)
	except(IOError):
		print('interrupted!')
		drone.shutdown()
		sys.exit(0)
