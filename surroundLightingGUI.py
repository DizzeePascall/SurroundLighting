import kivy
kivy.require('1.7.2')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.config import Config


# import time
# from phue import Bridge


class MyGUI(GridLayout):
	def __init__(self, **kwargs):
		super(MyGUI, self).__init__(**kwargs)
		self.cols = 2
		self.add_widget(StartStopButton(size_hint_x=0.3))
		self.add_widget(MessageArea())


class MessageArea(Label):
	def __init__(self, **kwargs):
		super(MessageArea, self).__init__(**kwargs)
		self.text = 'Hello World'


class StartStopButton(Button):
	lightingThreadActive = False

	def __init__(self, **kwargs):
		super(StartStopButton, self).__init__(**kwargs)
		self.text = 'Start'

	def _do_press(self):
		super(StartStopButton, self)._do_press()
		self.text = 'Start' if self.lightingThreadActive else 'Stop'
		self.lightingThreadActive = not self.lightingThreadActive


		# bridge = Bridge("192.168.1.8")

		# lights = bridge.get_light_objects()
		# light = lights[0]

		# light.on
		# light.name = "Hue Lamp 1"
		# light.brightness = 255
		# light.hue = 65000



class MyApp(App):
	def build(self):
		self.title = 'Surround Lighting'
		Config.set('graphics', 'width', '300')
		Config.set('graphics', 'height', '80')
		return MyGUI()

if __name__ == '__main__':
	MyApp().run()
	
