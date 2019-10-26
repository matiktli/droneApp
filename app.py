from ps4_controler.controler_service import ControlerService
from drone.drone_service import DroneService
from log_service import Log

def flightMode(ctrl, drone, log):
	drone.takeOff()
	cont = True
	while cont:
		instr = ctrl.getData()
		drone.move(data = instr)
		log.info(drone.getData())

if __name__ == "__main__":
	log = Log()
	ctrl = ControlerService()
	drone = DroneService()
	try:
		drone.setup()
		drone.video()
		flightMode(ctrl, drone, log)
	except(KeyboardInterrupt):
		print('interrupted!')
		drone.shutdown()
		sys.exit(0)
	except(IOError):
		print('interrupted!')
		drone.shutdown()
		sys.exit(0)
