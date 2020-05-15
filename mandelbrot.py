from tkinter import *
import sys
import getopt


def color(window, comp, count):
	red = hex(count % 4 * 64)[2:].zfill(2)
	blue = hex(count % 8 * 32)[2:].zfill(2)
	green = hex(count % 16 * 16)[2:].zfill(2)
	color = "#" + red + green + blue
	x, y = (comp.real), (comp.imag)
	window.create_oval(x, y, x, y, outline=color)


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
	origin_x = int(res/2)
	origin_y = int(res/2)

	master = Tk()
	master.title("Enjoy the Mandelbrot Set")
	w = Canvas(master, width=res, height=res)
	w.pack(expand=YES, fill=BOTH)

	for re in range(-int(res/2)+1,int(res/2)+1):
		for im in range(-int(res/2)+1,int(res/2)+1):
			comp = complex(re*gran, im*gran)
			mandelbrot(w, comp, gran, origin_x, origin_y, max_iterations)

	mainloop()

if __name__ == "__main__":

	side = 0.0
	resolution = 0
	iterations = 0

	try:
		opts, args = getopt.getopt(sys.argv[1:],"hs:r:i:",["help", "side=", "resolution=", "iterations="])
	except getopt.GetoptError:
		print('Wrong arguments. Please use option -h to get help.')
		sys.exit(2)

	if(len(sys.argv)==2 and opts and opts[0][0] in ("-h", "--help")):
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
			elif opt not in ("-i", "--iter", "-r", "--res", "-s", "--side"):
				print('Wrong arguments. Please use option -h to get help.')
				sys.exit()

		main((side, resolution, iterations))
	else:
		print('Wrong arguments. Please use option -h to get help.')
		sys.exit()
