# from x256 import x256
import src.x256numpy as x256

c0 = 0x297331
r, g, b = c0 & 0xff, (c0 >> 8) & 0xff, (c0 >> 16) & 0xff
x0e = x256.from_rgb(r, g, b, weighted=False, n_color=232)
x0w = x256.from_rgb(r, g, b, weighted=True, n_color=232)
x1e = x256.from_rgb(r, g, b, weighted=False, n_color=256)
x1w = x256.from_rgb(r, g, b, weighted=True, n_color=256)

print('%06x %d %06x %d %06x %d %06x %d %06x' % (
    c0,
    x0e, x256.to_rgb(x0e),
    x0w, x256.to_rgb(x0w),
    x1e, x256.to_rgb(x1e),
    x1w, x256.to_rgb(x1w)
))

# 297331 23 005f5f 2 008000 238 444444 239 4e4e4e
