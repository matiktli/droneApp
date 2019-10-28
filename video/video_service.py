import cv2
import time


class VideoService():

	def __init__(self, path='out_video', size = (640, 360)):
		self.path = path
		fileName = '{}/droneFlight_{}.avi'.format(self.path, time.time())
		self.out = cv2.VideoWriter(fileName, cv2.VideoWriter_fourcc('M','J','P','G'), 10, size)

	def setup(self, devMode = False):
		self.devMode = devMode

	def feedVideoData(self, frame):
		if not self.devMode: self.out.write(frame)
		cv2.imshow('Drone view', frame)
		cv2.waitKey(1)

	def endRecording(self):
		self.out.release()

	def put_face_on_frame(self, frame, face_data):
		cv2.circle(frame, (640/2, 360/2), 10, (0,0,255), 2)
		for (x, y, w, h) in face_data:
			face_cx, face_cy = (x+x+w)/2, (y+y+h)/2
			cv2.circle(frame, (face_cx, face_cy), 10, (0,255,0), 2)
			cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
		return frame




