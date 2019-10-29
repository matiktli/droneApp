import cv2
import time


class VideoService():

	def __init__(self, path='out_video', size = (640, 360)):
		self.path = path
		self.size = size
		self.out = None
		
	def setup(self, devMode = False):
		self.devMode = devMode

	def feedVideoData(self, frame):
		if not self.devMode and self.out != None: self.out.write(frame)
		cv2.imshow('Drone view', frame)
		cv2.waitKey(1)

	def startRecording(self):
		fileName = '{}/droneFlight_{}.avi'.format(self.path, time.time())
		self.out = cv2.VideoWriter(fileName, cv2.VideoWriter_fourcc('M','J','P','G'), 10, self.size)

	def endRecording(self):
		if self.out != None: self.out.release()

	def put_faces_on_frame(self, frame, face_data, faceFollowed, isFine=False):
		cv2.circle(frame, (640/2, 360/2), 10, (0,0,255), 2)
		for (x, y, w, h) in face_data:
			face_cx, face_cy = (x+x+w)/2, (y+y+h)/2
			cv2.circle(frame, (face_cx, face_cy), 10, (0,255,0), 2)
			color = (255, 0, 0)
			if x == faceFollowed[0] and y == faceFollowed[1] and w == faceFollowed[2] and h == faceFollowed[3]: 
				color = (0, 0, 255)
				cv2.line(frame, (640/2,360/2), (faceFollowed[4], faceFollowed[5]), color,2)
				if isFine:
					cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 4)
				else:
					cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
			else:
				cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)


		return frame




