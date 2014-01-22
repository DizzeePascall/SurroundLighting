import kivy
kivy.require('1.7.2')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

import time
from phue import Bridge

class StartButton(Button):
	lightingThreadActive = False

	def __init__(self,**kwargs):
		super(StartButton, self).__init__(**kwargs)
		self.text = 'Start'
		
	def _do_press(self):
		super(StartButton, self)._do_press()
		self.text = 'Start' if self.lightingThreadActive else 'Stop'
		self.lightingThreadActive = not self.lightingThreadActive
		
		bridge = Bridge("192.168.1.8")

		lights = bridge.get_light_objects()
		light = lights[0]

		light.on
		light.name = "Hue Lamp 1"
		light.brightness = 255
		light.hue = 65000

		#for i in range(1000):
		#	light.hue = 30000
		#	time.sleep(1)
		#	light.hue = 65000
		#	time.sleep(1)

class MyApp(App):

    def build(self):
        return StartButton()


if __name__ == '__main__':
    MyApp().run()