import time
import phue
from PIL import ImageGrab

def get_gamma_corrected_value(x):
	return pow((x+0.055)/(1.055),2.4) if x > 0.04045 else x/12.92

def get_xy_from_rgb(r,g,b):
	r,g,b = [get_gamma_corrected_value(x/255) for x in (r,g,b)]

	# Wide gamut conversion D65
	X = r * 0.649926 + g * 0.103455 + b * 0.197109
	Y = r * 0.234327 + g * 0.743075 + b * 0.022598
	Z = g * 0.053077 + b * 1.035763
	
	# Calculate xy from XYZ
	x = X / (X + Y + Z) if X != 0.0 else 0.0
	y = Y / (X + Y + Z) if Y != 0.0 else 0.0
		
	return x,y

def get_average_color():
	screen_shot = ImageGrab.grab()
	left, top, width, height = screen_shot.getbbox()
	r,g,b = 0.0,0.0,0.0
	for x in range(left, width, 10):
		for y in range(top, height, 10):
			pixel = screen_shot.getpixel((x,y))
			r += pixel[0]
			g += pixel[1]
			b += pixel[2]
	pixel_count = width/10 * height/10
	return [x/pixel_count for x in (r,g,b)]
	
if __name__ == '__main__':
	bridge = phue.Bridge("192.168.1.8")
	while True:
		loop_start_time = time.time()
		r,g,b = get_average_color()
		xy = get_xy_from_rgb(r,g,b)
		bri = (int)(r+g+b)/3
		bridge.set_light(1,{'transitiontime': 1, 'bri': bri, 'xy': xy})
		time.sleep(loop_start_time + 0.1 - time.time())