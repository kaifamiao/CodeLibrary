# 获取教程、习题、案例，共同学习、讨论、打卡
# 请关注：Crossin的编程教室
# QQ群：155816967，微信：sunset24678

身高 = float(input('输入你的身高(cm):'))
体重 = float(input('输入你的体重(kg):'))
#算出bmi指数
bmi = 体重 / (身高 / 100) ** 2
#判断并输出
if bmi < 18.5:
    print('体重偏轻')
if bmi > 24:
    print('体重偏重')
if 18.5 <= bmi <= 24:
    print('体重正常')





