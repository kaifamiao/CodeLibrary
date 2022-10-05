import random

num_change_win = 0
num_change_lose = 0
num_stay_win = 0
num_stay_lose = 0

def game():
    global num_change_win, num_change_lose, num_stay_win, num_stay_lose
    doors = ['羊', '羊', '车']
    random.shuffle(doors)              # 打乱3扇门
    choice = random.randint(0, 2)      # 第1次随机选择
    # 从剩下的2个里去掉一个羊
    others = list(range(3))
    others.remove(choice)
    if doors[others[0]] == '羊':
        other = others[1]
    else:
        other = others[0]
    # 随机选择 换 或者 不换，并记录
    is_changed = random.choice([True, False])
    if is_changed:      # 如果换了，选择变成剩下的另一扇门
        choice = other
    # 核对结果
    if doors[choice] == '车':    # 赢了
        if is_changed:           # 更换之后赢的
            num_change_win += 1
        else:                    # 不换之后赢的
            num_stay_win += 1
    else:                        # 输了
        if is_changed:           # 更换之后输的
            num_change_lose += 1
        else:                    # 不换之后输的
            num_stay_lose += 1

count = int(input('输入游戏次数：'))

UP = "\x1B[2A"
CLR = "\x1B[0K"
print("\n")  # set up blank lines so cursor moves work

for i in range(count):
    game()
    if num_change_win+num_change_lose > 0 and num_stay_win+num_stay_lose > 0:
        # print(f'{UP}【 换 】赢 {num_change_win:<7} 输 {num_change_lose:<7} 胜率 {num_change_win/(num_change_win+num_change_lose):.5f} {CLR}\n【不换】赢 {num_stay_win:<7} 输 {num_stay_lose:<7} 胜率 {num_stay_win/(num_stay_win+num_stay_lose):.5f}{CLR}\n', end='', flush=True)
        print(f'{UP}【 换 】赢 {num_change_win:<7} 输 {num_change_lose:<7}{CLR}\n【不换】赢 {num_stay_win:<7} 输 {num_stay_lose:<7}{CLR}\n', end='', flush=True)

