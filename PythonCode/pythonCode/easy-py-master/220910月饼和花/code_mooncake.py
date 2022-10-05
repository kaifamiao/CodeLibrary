# 获取教程、习题、案例，共同学习、讨论、打卡
# 请关注：Crossin的编程教室
# QQ群：155816967，微信：sunset24678

from math import sin, cos, pi
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge

length = 20
R = 3**0.5*length/(3**0.5*cos(pi/12)-sin(pi/12))
r = 2*sin(pi/12)*R/3**0.5

fig, ax = plt.subplots(figsize=(8, 6))
ax.set_aspect('equal')

for i in range(12):
    ax.add_patch(Circle((length*cos(pi*i/6),length*sin(pi*i/6)), r, ec='orange', fc='khaki', linewidth=4))

ax.add_patch(Circle((0,0), R, ec='orange', fc='khaki', linewidth=4))

for i in range(4):
    pos = [2, 5]
    rr = [5, 12]
    for j in range(2):
        ax.add_patch(Wedge([(-1) ** (i // 2 + 1) * pos[j], (-1) ** ((i + 1) // 2) * pos[j]], R - rr[j], 90 * (i+1), 90 * (i + 2),
              ec='orange', fc=r'khaki', linewidth=4))

fig.canvas.set_window_title('Happy Mid-autumn Day')
plt.text(-19, -2.5, 'CROSSIN', bbox=dict(boxstyle='square', fc="khaki", ec='orange', linewidth=4),  fontsize=40, color='orange')
plt.axis('off')
plt.ylim([-35, 35])
plt.xlim([-35, 35])
plt.show()
