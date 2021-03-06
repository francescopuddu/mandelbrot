# Mandelbrot

A ready-to-go script to visualize the Mandelbrot set, powered by Python. 

Learn about the math behind the code here: https://en.wikipedia.org/wiki/Mandelbrot_set

### Dependencies
OpenCV - https://pypi.org/project/opencv-python/

### Usage
The script takes 3 parameters:
1. "side" (-s, --side): the side of the considered square area, that will be centred in (0,0). It looks better if this value is around 2. 
2. "resolution" (-r, --res): the resolution of the resulting square picture. 
3. "iterations" (-i, --iter): the max number of iterations tested for every point of the discretized plane. The more, the better ... but also every number >50 should be fine.


### Screenshots
Here are some examples of the script in action: 

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
