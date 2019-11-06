# TODO: fix the imports to access everything you need to implement the route / and /mandelbrot
from flask import send_file


# TODO: make a route where a png image with the mandelbrot set is returned
# To compute the PNG image, you may use the following code
# def clamp(x, low=-2, high=2):
#     return min(high, max(x, low))
#
# # compute frame from center coordinate and step size. Clamp to -2, 2, -2, 2
# xa, xb, ya, yb = x - w/2 * step, x + w/2 * step, y - h/2 * step, y + h/2 * step
# xa, xb, ya, yb = tuple(map(clamp, [xa, xb, ya, yb]))
#
# img_io = generate_mbrot(xa, xb, ya, yb)
# return send_file(img_io, mimetype='image/png')


# TODO: make the plotter application accessible under /