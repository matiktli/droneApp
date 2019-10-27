import cv2
class FaceDetectionService():

	def __init__(self):
		self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

	def detect_face_and_put_on_frame(self, frame):
		print('Trying to detect....')

		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		frame = faces
		#faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)
		#for (x, y, w, h) in faces:
		#	print('Face detected....')
			#cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
		return frame