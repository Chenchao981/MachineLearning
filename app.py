from flask import Flask, render_template, jsonify
from sklearn.datasets import load_iris
import pandas as pd
import numpy as np

app = Flask(__name__)

# 加载鸢尾花数据集
iris = load_iris()
# 将数据转换为DataFrame格式
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
# 添加目标变量列
df['target'] = iris.target
# 将数字标签转换为物种名称
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

@app.route('/')
def index():
    return render_template('surface.html')

@app.route('/iris')
def iris_page():
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    # 准备箱线图数据
    boxplot_data = []
    for feature in iris.feature_names:
        for species in iris.target_names:
            values = df[df['species'] == species][feature].tolist()
            boxplot_data.append({
                'y': values,
                'type': 'box',
                'name': species,
                'boxpoints': 'outliers',
                'jitter': 0.3,
                'pointpos': -1.8
            })
    
    # 准备散点图数据
    scatter_data = {
        'x': df['sepal length (cm)'].tolist(),
        'y': df['sepal width (cm)'].tolist(),
        'mode': 'markers',
        'type': 'scatter',
        'marker': {
            'color': df['target'].tolist(),
            'colorscale': 'Viridis'
        },
        'text': df['species'].tolist()
    }
    
    # 准备相关性矩阵数据
    corr_matrix = df[iris.feature_names].corr()
    heatmap_data = {
        'z': corr_matrix.values.tolist(),
        'x': iris.feature_names,
        'y': iris.feature_names,
        'type': 'heatmap',
        'colorscale': 'RdBu'
    }
    
    # 准备小提琴图数据
    violin_data = []
    for species in iris.target_names:
        violin_data.append({
            'type': 'violin',
            'y': df[df['species'] == species]['petal length (cm)'].tolist(),
            'name': species,
            'box': {'visible': True},
            'meanline': {'visible': True}
        })

    return jsonify({
        'boxplot_data': boxplot_data,
        'scatter_data': scatter_data,
        'heatmap_data': heatmap_data,
        'violin_data': violin_data,
        'feature_names': iris.feature_names,
        'target_names': iris.target_names.tolist()
    })

@app.route('/api/surface-data')
def get_surface_data():
    # 创建网格点
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)
    
    # 计算二元函数值（这里使用 z = sin(sqrt(x^2 + y^2)) 作为示例）
    Z = np.sin(np.sqrt(X**2 + Y**2))
    
    return jsonify({
        'x': X.tolist(),
        'y': Y.tolist(),
        'z': Z.tolist()
    })

if __name__ == '__main__':
    app.run(debug=True) 