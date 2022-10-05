import pandas

df = pandas.read_excel('excels/小测验1.xlsx', index_col=0)
df1 = pandas.read_excel('excels/小测验2.xlsx', index_col=0)
df = pandas.concat([df, df1], axis=1)
print(df)

df.to_excel('汇总成绩.xlsx')































# import pandas

# dfs = []
# for i in range(1, 9):
#     df = pandas.read_excel(f'excels/小测验{i}.xlsx', index_col=0)
#     dfs.append(df)
# df = pandas.concat(dfs, axis=1)
# df.to_excel('汇总成绩.xlsx')

