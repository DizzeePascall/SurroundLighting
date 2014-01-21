from phue import Bridge

bridge = Bridge("192.168.1.8")
bridge.connect()

lights = bridge.get_light_objects()
light = lights[0]

light.off
light.name = "Hue Lamp 1"
light.brightness = 255
