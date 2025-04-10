import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 加载鸢尾花数据集
iris = load_iris()

# 创建DataFrame
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# 创建图形
plt.figure(figsize=(15, 10))

# 1. 箱线图
plt.subplot(2, 2, 1)
sns.boxplot(x='species', y='sepal length (cm)', data=df)
plt.title('不同种类鸢尾花的萼片长度分布')

# 2. 散点图
plt.subplot(2, 2, 2)
sns.scatterplot(data=df, x='sepal length (cm)', y='sepal width (cm)', hue='species')
plt.title('萼片长度与宽度的关系')

# 3. 小提琴图
plt.subplot(2, 2, 3)
sns.violinplot(x='species', y='petal length (cm)', data=df)
plt.title('不同种类鸢尾花的花瓣长度分布')

# 4. 相关性热力图
plt.subplot(2, 2, 4)
# 只选择数值类型的列计算相关性
numeric_columns = iris.feature_names
correlation_matrix = df[numeric_columns].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('特征相关性热力图')

# 调整子图之间的间距
plt.tight_layout()

# 保存图片
plt.savefig('iris_visualization.png')
plt.close()

print("可视化图表已保存为 'iris_visualization.png'") 