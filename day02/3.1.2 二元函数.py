import matplotlib.pyplot as plt
import numpy as np

x1_array = np.linspace(-3, 3, 301)
x2_array = np.linspace(-3, 3, 301)
xx1, xx2 = np.meshgrid(x1_array, x2_array)


ff = xx1 * np.exp(-xx1**2 - xx2**2)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# 绘制二元函数网格曲面
ax.plot_wireframe(xx1, xx2, ff, rstride=10, cstride=10)

plt.show()
