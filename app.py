from ps4_controler.controler_service import ControlerService
from drone.drone_service import DroneService
from video.video_service import VideoService
from video.face_detection_service import FaceDetectionService

from log_service import Log
import sys, time

def awaitStart(ctrl, drone):
	till = True
	print('Press "X" to take off...')
	while till:
		_, b, _ = ctrl.getData()
		if b['x'] == 1:
			till = False
			drone.takeOff()

def flightMode(ctrl, drone, videoSvc, face_detect_ctrl, log, devMode = False):
	faceDetectorControllerOverride = False
	if not devMode: videoSvc.startRecording()

	while True:
		move_instr, btns, _ = ctrl.getData()
		drone.execute(btns)
		if not faceDetectorControllerOverride:
			r = drone.move(move_instr)
			#print(r)

		if btns['triangle'] == 1:
			if faceDetectorControllerOverride:
				faceDetectorControllerOverride = False
			else:
				faceDetectorControllerOverride = True
			print('sleepin')
			time.sleep(0.05)

		frame = drone.getVideoData()
		if faceDetectorControllerOverride:
			face_data = face_detect_ctrl.detect_faces(frame, number=1)
			move_instr, followed_face_data, isFine = face_detect_ctrl.follow_face(move_instr, face_data)
			frame = videoSvc.put_faces_on_frame(frame, face_data, faceFollowed = followed_face_data, isFine = isFine)
			drone.move(move_instr)

		videoSvc.feedVideoData(frame)
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
	videoSvc.setup(devMode = devMode)
	face_detect_ctrl = FaceDetectionService()
	face_detect_ctrl.setup(devMode = devMode) # dev mode here for now jsut print
	try:
		drone.setup(devMode = devMode)
		awaitStart(ctrl, drone)
		flightMode(ctrl, drone, videoSvc, face_detect_ctrl, log, devMode = devMode)
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
