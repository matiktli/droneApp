import cv2
class FaceDetectionService():
	cx, cy = 640/2, 360/2 # point that drone is aiming at
	cw, ch = 160, 360/4 # width, height of face that skynet prefer to aim at
	happyBuffer_x, happyBuffer_y, happyBuffer_z = 30, 30, 5 # buffer that skynet is fine being in
	speedVector = 0.6

	def __init__(self):
		self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

	def setup(self, devMode = False):
		self.devMode = devMode

	def detect_faces(self, frame, number=None):
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)
		return faces

	def getMainFaceData(self, faces):
			def getW(item):
				return item[2]
			def getH(item):
				return item[3]
			c = 0
			fcx, fcy = self.cx, self.cy
			if len(faces) > 0:
				faces = sorted(faces, key=getW, reverse=True)
				x,y,w,h = faces[0]
				fcx, fcy = (x+x+w)/2, (y+y+h)/2
				return (x,y, w, h, fcx, fcy)

	def follow_face(self, move_instr, faces):

		def releaseTheSkynet(face_data):
			def move(moves, direction):
				if self.devMode: print('Skynet saying: {}'.format(direction))
				speedVector = self.speedVector
				moves[direction] = speedVector

			def makeMoveHorizontaly(moves, face_data_x):
				if (self.cx + self.happyBuffer_x) < face_data_x:
					move(moves,'right')
				elif (self.cx - self.happyBuffer_x) > face_data_x:
					move(moves,'left')
				else:
					if self.devMode: print("Skynet saying: None - H")
					return True

			def makeMoveVerticaly(moves, face_data_y):
				if (self.cy + self.happyBuffer_y) < face_data_y:
					move(moves, 'down')
				elif (self.cy - self.happyBuffer_y) > face_data_y:
					move(moves, 'up')
				else:
					if self.devMode: print("Skynet saying: None - V")
					return True

			def makeMoveForwardBackward(moves, face_data_w, face_data_h):
				if (self.cw + 2*self.happyBuffer_z) < face_data_w:
					move(moves, 'backward')
				elif (self.cw - 2*self.happyBuffer_z) > face_data_w:
					move(moves, 'forward')
				else:
					if self.devMode: print("Skynet saying: None - Z")
					return True


			moves = move_instr
			if face_data != None:
				makeMoveHorizontaly(moves, face_data[4])
				makeMoveVerticaly(moves, face_data[5])
				#makeMoveForwardBackward(moves, face_data[2], face_data[3])

		faceData = self.getMainFaceData(faces)
		moves = releaseTheSkynet(faceData)
		return moves, faceData



