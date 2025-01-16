import numpy as np
import x256offline
import x256numpy

y, x = 96, 54
img = np.random.randint(0, 256, (x, y, 3), dtype=np.uint8)

print(np.min(img))
print(np.max(img))


COLOR_X256E = 'x256e'
COLOR_X256W = 'x256w'
COLOR_X232E = 'x232e'
COLOR_X232W = 'x232w'

COLOR_X256_LIST = [COLOR_X256E, COLOR_X256W, COLOR_X232E, COLOR_X232W]

img = img.astype(np.int32)

for color in COLOR_X256_LIST:
    weighted = color in [COLOR_X256W, COLOR_X232W]
    n_color = 232 if color in [COLOR_X232E, COLOR_X232W] else 256
    ans = x256numpy.from_rgb(img[:, :, 2], img[:, :, 1], img[:, :, 0], weighted, n_color)
    print(ans.shape)
    for j in range(x):
        for k in range(y):
            b, g, r = img[j, k]
            _l = x256offline.from_rgb(
                r, g, b, weighted, n_color
            )
            _r = ans[j, k]
            assert int(_l) == int( _r), (color, j, k, _l, ans[j, k])
        # print(j)
    print(color, 'OK')
