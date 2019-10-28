import cv2
class FaceDetectionService():

	cx, cy = 640/2, 360/2

	def __init__(self):
		self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

	def detect_face(self, frame, number=None):
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)
		return faces

	def follow_face(self, move_instr, faces):
		# res['forward'] 
		# res['backward']
		# res['left']
		# res['right'] 
		# res['up'] 
		# res['down']
		# res['rotate_left']
		# res['rotate_right']
		def getMainFaceData(faces):
			c = 0
			fcx, fcy = 640/2, 360/2
			# bad way...
			for x,y,w,h in faces:
				if c >= 1:
					break
				c += 1
				fcx, fcy = (x+x+w)/2, (y+y+h)/2
			return (fcx, fcy)

		def decideMove(face_data):
			happyBuffer = 30
			def move(moves, direction):
				print('I want to move: {}'.format(direction))
				speedVector = 0.6
				moves[direction] = speedVector

			moves = move_instr
			moves['forward'] = 0
			moves['backward'] = 0
			if (self.cx + happyBuffer) < face_data[0]:
				move(moves,'right')
			elif (self.cx - happyBuffer) > face_data[0]:
				move(moves,'left')
			else:
				print("I want to move: None - H")
		faceData = getMainFaceData(faces)
		moves = decideMove(faceData)

		return moves



