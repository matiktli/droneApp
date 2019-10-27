import cv2
class FaceDetectionService():

	def __init__(self):
		self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

	def detect_face(self, frame, number=None):
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)
		return faces

	def follow_face(self, move_instr, faces):
		print('!!! AI is now CONTROLLING YOUR DRONE !!!')
		# TODO bring face follower logic
		return move_instr

