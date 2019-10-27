class Log():

	def __init__(self):
		self.data = {}

	def info(self, infoData):
		formated = self.formatInfoData(infoData)
		#print('{}'.format(formated))

	def formatInfoData(self, data):
		return data