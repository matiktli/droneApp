class Log():

	def __init__(self):
		self.data = {}

	def info(self, infoData):
		formated = self.formatInfoData(infoData)
		print(formated)

	def formatInfoData(self, data):
		return data