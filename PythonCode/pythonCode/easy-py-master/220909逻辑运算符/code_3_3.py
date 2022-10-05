# 获取教程、习题、案例，共同学习、讨论、打卡
# 请关注：Crossin的编程教室
# QQ群：155816967，微信：sunset24678

会打篮球 = True
if 会打篮球:
    print('你是运动员')

会唱跳 = True
if 会唱跳:
    print('你是艺人')

会打篮球 = True
会唱跳 = True
if 会唱跳 and 会打篮球:
    print('你是****')

会打篮球 = False
会唱跳 = True
if 会唱跳 or 会打篮球:
    print('你是****')

会唱跳 = False
if not 会唱跳:
    print('你是颜值担当吗？')

会打篮球 = False
会唱跳 = False
if not 会唱跳 and not 会打篮球:
    print('你是菜鸡')

