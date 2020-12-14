import sys
import getopt
import cv2
import numpy as np

def color(window, comp, count):
	red = int(hex(count % 4 * 64)[2:].zfill(2), 16)
	blue = int(hex(count % 8 * 32)[2:].zfill(2), 16)
	green = int(hex(count % 16 * 16)[2:].zfill(2), 16)

	x, y = round((comp.real)), round((comp.imag))
	window[y,x] = (blue,green,red)


def map_to_canvas(comp, origin_x, origin_y, granularity):
	return complex(origin_x + comp.real/granularity, origin_y + comp.imag/granularity)


def mandelbrot(w, comp, granularity, origin_x, origin_y, iterations):
	ris = 0 
	for it_count in range(0,iterations):
		ris = ris**2 + comp
		if abs(ris)>=2.0: 
			color(w, map_to_canvas(comp, origin_x, origin_y, granularity), it_count)
			return
	return color(w, map_to_canvas(comp, origin_x, origin_y, granularity), 0)


def main(args):

	interval, res, max_iterations = args

	gran = interval / res
	origin_x = res//2
	origin_y = res//2
	w = np.zeros((res,res,3), np.uint8)

	for re in range(-res//2,res//2):
		for im in range(-res//2,res//2):
			comp = complex(re*gran, im*gran)
			mandelbrot(w, comp, gran, origin_x, origin_y, max_iterations)

	out_img = cv2.resize(w, (1000, 1000))
	out_img = cv2.fastNlMeansDenoisingColored(out_img,None,10,10,7,21)
	cv2.imshow('mandelbrot',out_img)
	cv2.waitKey(0)

if __name__ == "__main__":

	side = 0.0
	resolution = 0
	iterations = 0
	opts = []

	try:
		opts, args = getopt.getopt(sys.argv[1:],"hs:r:i:",["help", "side=", "resolution=", "iterations="])
	except getopt.GetoptError:
		print('Wrong arguments. Please use option -h to get help.')
		sys.exit(2)

	if len(opts)==1 and opts[0][0] in ("-h", "--help"):
		print('mandelbrot.py -s <side> -r <resolution> -i <iterations>')
		sys.exit()

	if len(opts)==3:
		for opt, arg in opts:
			if opt in ("-s", "--side"):

				try: 
					side = float(arg)
					assert side > 0
				except:
					print("Invalid side size: it must be a positive number.")
					sys.exit(2)

			elif opt in ("-r", "--res"):

				try: 
					resolution = int(arg)
					assert resolution > 0
				except:
					print("Invalid picture resolution: it must be a positive number.")
					sys.exit(2)

			elif opt in ("-i", "--iter"):

				try: 
					iterations = int(arg)
					assert iterations > 0
				except:
					print("Invalid number of iterations: it must be a positive number.")
					sys.exit(2)
			else:
				print('Wrong arguments. Please use option -h to get help.')
				sys.exit()

		main((side, resolution, iterations))
	else:
		print('Wrong arguments. Please use option -h to get help.')
		sys.exit()
