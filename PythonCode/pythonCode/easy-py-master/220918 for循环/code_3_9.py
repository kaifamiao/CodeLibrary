# 获取教程、习题、案例，共同学习、讨论、打卡
# 请关注：Crossin的编程教室
# QQ群：155816967，微信：sunset24678

for i in range(5):
    print(i)

n = int(input("输入n："))

# 正整数版1
for i in range(6, n, 6):
    print(i)

# 正整数版2
for i in range(1, n):
    if i % 2 == 0 and i % 3 == 0:
        print(i)

# 正整数版3
i = 1
while i * 6 < n:
    print(i * 6) 
    i += 1

# 常数版（考虑n为任意常数）
if n > 0:
    for i in range(6, int(n), 6):
        print(i)
else:
    for i in range(-6, int(n-1), -6):
        print(i)








