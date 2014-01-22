import time
from phue import Bridge

bridge = Bridge("192.168.1.8")
#bridge.connect()

lights = bridge.get_light_objects()
light = lights[0]

light.on
light.name = "Hue Lamp 1"
light.brightness = 255
light.hue = 65000

for i in range(1000000000):
	light.hue = 30000
	time.sleep(0.5)
	light.hue = 65000
	time.sleep(0.5)
	