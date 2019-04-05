import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
import tools as tols
from datetime import datetime
import matplotlib.pyplot as plt
# -*- coding: utf-8 -*-
from IPython.display import display
plt.style.use("fivethirtyeight")
sns.set_style({'font.sans-serif':['simhei','Arial']})
np.set_printoptions(suppress=True)
pd.set_option('display.max_columns', None)
# 检查Python版本
from sys import version_info
if version_info.major != 3:
    raise Exception('请使用Python 3 来完成此项目')
'''
# 导入假投数据

p2p_df = pd.read_excel('transaction_fake.xls')
df = p2p_df.copy()

grouped = df['money'].groupby(df['uname'])
def peak_range(group):
    return group.max()-group.min()
grouped = grouped.agg(["sum","mean","std",peak_range,"count"]).round(decimals=2)

print(grouped)
#grouped.to_excel('./data/analyse1.xls')
'''
# 导入按uname分组数据
p2p_df = pd.read_excel('./data/analyse1.xls')
df = p2p_df.copy()

#sum特征分析
data = pd.cut(df['sum'],[0,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000,5000000],
              labels=['0-10000','10000-20000','20000-30000','30000-40000','40000-50000',
                      '50000-60000','60000-70000','70000-80000','80000-90000','90000-100000','100000以上'])
df['sum_level'] = data

df.fillna({'std':0},inplace = True)
df_sum_level_count = df.groupby('sum_level')['sum'].count().to_frame().reset_index()
df_std_mean = df.groupby('sum_level')['std'].mean().to_frame().reset_index()

f, [ax1,ax2] = plt.subplots(2,1,figsize=(20,15))
sns.barplot(x='sum_level', y='sum', palette="Blues_d", data=df_sum_level_count, ax=ax1)
ax1.set_title('不同总投资金额的账户数量统计',fontsize=15)
ax1.set_xlabel('总投资金额')
ax1.set_ylabel('数量')

sns.barplot(x='sum_level', y='std', palette="Greens_d", data=df_std_mean, ax=ax2)
ax2.set_title('不同总投资金额的账户标准差均值',fontsize=15)
ax2.set_xlabel('总投资金额')
ax2.set_ylabel('标准差值')

plt.savefig('./image/image1.jpg')
plt.show()





