import thread
import time

class SurroundLightingController():
	def start_lighting(self):
		self.stop_thread_flag = False
		thread.start_new_thread(self.surround_lighting,())
	
	def stop_lighting(self):
		self.stop_thread_flag = True
	
	def surround_lighting(self):
		while not self.stop_thread_flag:
			screenshot = self.get_screenshot()
			colour = self.get_colour(screenshot)
			self.update_light(colour)
			time.sleep(1)
		
	def get_screenshot(self):
		return "Hello"
		
	def get_colour(self,screenshot):
		return "Hello"
		
	def update_light(self,colour):
		print "Hello"
		
slc = SurroundLightingController()
slc.start_lighting()

time.sleep(4)

slc.stop_lighting()