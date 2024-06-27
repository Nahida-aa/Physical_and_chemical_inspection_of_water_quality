# "conda python 3.10.14"
# -*- coding: utf-8 -*-
import matplotlib
# 设置字体参数
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import re
from IPython.display import display, Markdown

def print_table(x, y, x_label, y_label, y_s, y_s0):
    # 绘制table
    df = pd.DataFrame({x_label: x, y_label: y})
    new_row1 = pd.DataFrame({x_label: ['待预测'], y_label: [y_s]}, index=['样本'])
    new_row2 = pd.DataFrame({x_label: ['-'], y_label: [y_s0]}, index=['空白'])
    df = pd.concat([df, new_row1, new_row2])
    # 打印数据框
    table_md = df.T.to_markdown().replace("|-", "|:").replace("-|", ":|")
    table_md = re.sub(r'(\d+\.\d+)', lambda x: '{:.4f}'.format(float(x.group())), table_md)
    print(table_md)
    display(Markdown(table_md))
    print(df.T)

class StandardCurve:
    def __init__(self, x, y, x_label='x', y_label='y', y_s=None):
        self.x = np.array(x)
        self.y = np.array(y)
        self.x_label = x_label
        self.y_label = y_label
        self.y_s = y_s
        self.yellow = '#ee8916'
        self.title = f'{y_label} 与 {x_label} 的标准曲线'
        self.slope, self.intercept, self.r_value, self.p_value, self.std_err = stats.linregress(self.x, self.y)

    def plot_regression(self):
        plt.figure(figsize=(10, 6))  # 设置画布大小为 10x6 英寸
        sns.regplot(x=self.x, y=self.y)
        # 添加y=0和x=0的线
        plt.axhline(0, color='black',linewidth=0.5)
        plt.axvline(0, color='black',linewidth=0.5)
        # 设置x轴的刻度
        plt.xticks(np.arange(min(self.x), max(self.x)+1, 2))
        
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.title(self.title)
        plt.scatter(self.x, self.y, label='标准系列')  # 添加标签
        # 标记每个点的纵坐标
        for i, txt in enumerate(self.y):
            plt.text(self.x[i], self.y[i], f'{txt:.4f}', ha='right')  # 保留两位小数
        
        plt.text(0.05, 0.95, self.equation(), 
             transform=plt.gca().transAxes, fontsize=14, verticalalignment='top')
        # 添加 R² 值 (决定系数)
        plt.text(0.05, 0.85, f'$R^2 = {self.r_value**2:.4f}$', transform=plt.gca().transAxes, fontsize=14, verticalalignment='top')

        if self.y_s is not None:
            x_s = self.predict_x()
            # 添加特殊的点
            plt.scatter(x_s, self.y_s, color=self.yellow, label='样本')
            # 添加虚线的垂直线
            plt.axvline(x_s, color=self.yellow, linestyle='--',linewidth=0.5)
            plt.axhline(self.y_s, color=self.yellow, linestyle='--',linewidth=0.5)
            # 标记预测的点
            plt.text(x_s, self.y_s, f'({x_s:.4f}, {self.y_s:.4f})', color=self.yellow)
            plt.figtext(0.5, 0.01, f'预测的{self.x_label}为：{x_s:.4f}', fontsize=14, horizontalalignment='center')

        plt.legend()
        plt.show()
        
    def equation(self):
        return f'$\hat{{y}} = {self.slope:.4f}x + {self.intercept:.4f}$'

    def predict_x(self):
        return (self.y_s - self.intercept) / self.slope