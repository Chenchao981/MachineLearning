import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import seaborn as sns

# 定义等差数列的首项、公差和项数
a0 = 1
# 首项

n = 10
# 项数

d = 2
# 公差

a_array = np.arange(a0, a0 + n*d, d)
print('打印等差数列')
a_array # 打印数列
print(a_array)


# # 绘制散点图
# plt.scatter(np.arange(n), a_array)

# # 添加标题和坐标轴标签
# plt.title('Arithmetic Progression')
# plt.xlabel('Index, $n$')
# plt.ylabel('Value, $a_n$')

# # 显示图形
# plt.show()

# 生成从-3到3之间的301个等间距的点，作为x1和x2的取值范围
x1_array = np.linspace(-3, 3, 301)
x2_array = np.linspace(-3, 3, 301)

# 使用meshgrid函数生成网格点矩阵
# xx1和xx2分别代表网格点的x1坐标和x2坐标
xx1, xx2 = np.meshgrid(x1_array, x2_array)

# print(xx1)
# print(xx2)

# ff = xx1**2 + xx2**2
# print(ff)

# 使用seaborn库绘制热力图
# sns.heatmap(ff, cmap='viridis', annot=True, fmt='.2f')
# plt.show()

#导入鸢尾花数据
iris_df = px.data.iris()
# 使用seaborn库中的load_dataset函数来导入鸢尾花数据集。
# load_dataset函数是seaborn库提供的一个用于加载数据集的函数，
# 它可以加载多种内置的数据集，包括鸢尾花数据集。

# 显示数据集前5行
print('打印鸢尾花数据前5行')
print(iris_df.head())

# 使用seaborn库绘制鸢尾花数据集的散点图
sns.scatterplot(data=iris_df, x='sepal_length', y='sepal_width', hue='species')
plt.show()
