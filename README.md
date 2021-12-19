# Mandelbrot

A ready-to-go script to visualize the Mandelbrot set.

Learn about the math behind the code here: https://en.wikipedia.org/wiki/Mandelbrot_set

### Dependencies
OpenCV - https://pypi.org/project/opencv-python/

### Usage
The script takes 3 parameters:
1. "side" (-s, --side): the height of the focus area, that will be centred in (0,0). Recommended value: 2. 
2. "resolution" (-r, --res): the resolution of the resulting square picture. Recommended value: >300
3. "iterations" (-i, --iter): the max number of iterations tested for every point of the discretized plane. Recommended value: >50.


### Examples

```
mandelbrot.py -s 3.5 -r 500 -i 50
```
![example screenshot](https://i.imgur.com/1GbS5BB.png)




```
mandelbrot.py -s 1 -r 500 -i 100
```
![example screenshot](https://i.imgur.com/TPxfUpS.png)


## Authors

* **Francesco Puddu** - [francescopuddu](https://github.com/francescopuddu)
