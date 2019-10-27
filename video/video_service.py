import cv2
import time

class VideoService():

	def __init__(self, path='out_video', size = (640, 360)):
		self.path = path
		fileName = '{}/droneFlight_{}.avi'.format(self.path, time.time())
		self.out = cv2.VideoWriter(fileName, cv2.VideoWriter_fourcc('M','J','P','G'), 10, size)

	def feedVideoData(self, video_data):
		frame = self.formatFrame(video_data)
		self.out.write(frame)
		cv2.waitKey(1)
	
	def formatFrame(self, frame_data):
		return frame_data

	def endRecording(self):
		self.out.release()