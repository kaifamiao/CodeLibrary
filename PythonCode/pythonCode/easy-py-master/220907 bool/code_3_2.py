# 获取教程、习题、案例，共同学习、讨论、打卡
# 请关注：Crossin的编程教室
# QQ群：155816967，微信：sunset24678

a = True
b = False
print(a, type(a))
print(b, type(b))



print(8 > 7)
print(-2 <= -3)
print(1 + 1 == 2)
print('ab' != 'cd')



练习时长 = 2.5
爱好 = '🎤💃🏻🕶🏀'
print(练习时长 >= 2.5)
print('🎤' + '💃🏻' + '🕶' + '🏀' == 爱好)



name = input()
print(name == '小白')



# 如果是空值或者0值，结果就是False
print(bool(0))
print(bool(0.0))
print(bool(''))
# 如果是非空值或者非0值，结果就是True
print(bool(-1))
print(bool(3.14))
print(bool('abc'))




name = input()
if name:
    print('Hello', name)
