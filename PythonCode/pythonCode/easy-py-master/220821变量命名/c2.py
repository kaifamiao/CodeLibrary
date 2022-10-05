d1tb = 7
d2tb = 8
d3tb = 9

sjxzc = d1tb + d2tb + d3tb
print(sjxzc)

sjxbzc = sjxzc / 2
sjxmj = (sjxbzc * (sjxbzc - d1tb) * (sjxbzc - d2tb) * (sjxbzc - d3tb)) ** 0.5
print(sjxmj)