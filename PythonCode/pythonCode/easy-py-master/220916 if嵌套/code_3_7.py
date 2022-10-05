# 获取教程、习题、案例，共同学习、讨论、打卡
# 请关注：Crossin的编程教室
# QQ群：155816967，微信：sunset24678

x = float(input('x:'))
y = float(input('y:'))

if x > 0 and y > 0:
    print('第1象限')
if x < 0 and y > 0:
    print('第2象限')
if x < 0 and y < 0:
    print('第3象限')
if x > 0 and y < 0:
    print('第4象限')
if x == 0 or y == 0:
    print('不属于任何象限')


if x > 0 and y > 0:
    print('第1象限')
elif y > 0:
    print('第2象限')
elif x < 0:
    print('第3象限')
elif x > 0:
    print('第4象限')
else:
    print('不属于任何象限')


if x == 0 or y == 0:
    print('不属于任何象限')
else:    
    if x > 0:
        if y > 0:
            print('第1象限')
        else:
            print('第4象限')
    else:
        if y > 0:
            print('第2象限')
        else:
            print('第3象限')


print((('第1象限' if y > 0 else '第4象限') if x > 0 else ('第2象限' if y > 0 else '第3象限')) if x*y else '不属于任何象限')




