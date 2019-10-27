import cv2
import time
from face_detection_service import FaceDetectionService


class VideoService():

	def __init__(self, path='out_video', size = (640, 360)):
		self.path = path
		fileName = '{}/droneFlight_{}.avi'.format(self.path, time.time())
		self.out = cv2.VideoWriter(fileName, cv2.VideoWriter_fourcc('M','J','P','G'), 10, size)

	def setup(self, faceDetectionModule = True, devMode = False):
		self.devMode = devMode
		if faceDetectionModule:
			self.face_detection = FaceDetectionService()

	def feedVideoData(self, video_data):
		frame = self.formatFrame(video_data)
		if self.face_detection != None:
			print('hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')
			frame = self.face_detection.detect_face_and_put_on_frame(frame)
		if not self.devMode: self.out.write(frame)
		if self.devMode: cv2.imshow('XD', frame)
		cv2.waitKey(1)

		return 
	
	def formatFrame(self, frame_data):
		return frame_data

	def endRecording(self):
		self.out.release()



