# Mandelbrot

A ready-to-go tool to explore the Mandelbrot set in the complex domain. 

Learn about the math here: https://en.wikipedia.org/wiki/Mandelbrot_set

### Usage
The script requires 3 command line arguments:
1. "side" (-s, --side): the limit of the area to visualize (recommended value: ~2)
2. "resolution" (-r, --res): the resolution of the resulting square picture (recommended value: >300)
3. "iterations" (-i, --iter): the max number of recursive computations for each point of the discretized plane (recommended value: >50)

### Examples

```
mandelbrot.py -s 3.5 -r 500 -i 50
```
![example screenshot](https://i.imgur.com/1GbS5BB.png)


```
mandelbrot.py -s 1 -r 500 -i 100
```
![example screenshot](https://i.imgur.com/TPxfUpS.png)
