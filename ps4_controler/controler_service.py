import os
from ps4_controler import PS4Controller

class ControlerService():

	def __init__(self, ps4_controler = PS4Controller()):
		self.joy = ps4_controler
		self.joy.init()

	def getData(self):
		btns, axis, smh = self.joy.listen()
		axis_data = self.translate_axis(axis)
		btns_data = self.translate_btns(btns)
		other_data = smh
		return axis_data, btns_data, other_data

	def translate_axis(self, axis):
		result = {}
		result['rh'] = axis.get(3) if axis.get(3) != None else 0
		result['lh'] = axis.get(0) if axis.get(4) != None else 0
		result['rv'] = axis.get(4) * (-1) if axis.get(4) != None else 0
		result['lv'] = axis.get(1) * (-1) if axis.get(1) != None else 0
		def transformFunction(data):
			def getFromOptional(optionalData):
				return optionalData if optionalData != None else 0
			res = {}
			res['forward'] = max(getFromOptional(data['lv']), 0)
			res['backward'] = max((-1) * getFromOptional(data['lv']), 0)
			res['left'] = max((-1) * getFromOptional(data['lh']), 0)
			res['right'] = max(getFromOptional(data['lh']), 0)
			res['up'] = max(getFromOptional(data['rv']), 0)
			res['down'] = max((-1) * getFromOptional(data['rv']), 0)
			res['rotate_left'] = max((-1) * getFromOptional(data['rh']), 0)
			res['rotate_right'] = max(getFromOptional(data['rh']), 0)
			return res
		return transformFunction(result)

	def translate_btns(self, btns):
		result = {}
		return btns

if __name__ == "__main__":
	controler = ControlerService()
	while True:
		axis, btns, smh = controler.getData()
		print(axis)