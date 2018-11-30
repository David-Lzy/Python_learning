#Pandas 简介
"""学习目标：
#大致了解 pandas 库的 DataFrame 和 Series 数据结构
#存取和处理 DataFrame 和 Series 中的数据
#将 CSV 数据导入 pandas 库的 DataFrame
#对 DataFrame 重建索引来随机打乱数据 """
from __future__ import print_function
import tensorflow
import pandas as pd
import matplotlib
print(pd.__version__)
california_housing_dataframe = pd.read_csv("https://download.mlcc.google.cn/mledu-datasets/california_housing_train.csv", sep=",")
#print(california_housing_dataframe.describe())
""" 上面的示例使用 DataFrame.describe 来显示关于 DataFrame 的有趣统计信息。 """
""" 另一个实用函数是 DataFrame.head，它显示 DataFrame 的前几个记录： """
#print(california_housing_dataframe.head(10))
california_housing_dataframe.plot.hist('housing_median_age')

""" pandas 的另一个强大功能是绘制图表。例如，借助 DataFrame.hist，您可以快速了解一个列中值的分布： """