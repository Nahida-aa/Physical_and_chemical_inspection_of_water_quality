import numpy as np

# A -> B 二氧化硫含量 m (\mu g)
x_name = '二氧化硫含量 C ' + r'$(\mu g)$'
m_x_1 = np.array([0, 2, 4, 8, 12, 16])
# A -> B 吸光度 A
y_name = '吸光度 A'
A_y_1 = np.array([0.086, 0.143, 0.187, 0.211, 0.248, 0.289])
# A -> B 样品 吸光度 A
A_y_1s = 0.102
# B -> A 二氧化硫含量 m (\mu g)
m_x_2 = np.array([0, 2, 4, 8, 12, 16])
# B -> A 吸光度 A
A_y_2 = np.array([0.073, 0.106, 0.203, 0.270, 0.380, 0.485])
# B -> A 样品 吸光度 A
A_y_2s = 0.091

import pandas as pd
def print_table(x_name, x, y_name, y, y_s):
    # 绘制table
    df = pd.DataFrame({x_name: x, y_name: y})
    new_row = pd.DataFrame({x_name: ['待预测'], y_name: [y_s]}, index=['样本'])
    df = pd.concat([df, new_row])
    # 打印数据框
    # df[y_name] = df[y_name].map('{:.3f}'.format)
    # df[y_name] = df[y_name].apply(lambda x: format(x, '.3f'))
    # df[y_name] = df[y_name].apply(lambda x: '{:.3f}'.format(x))
    # df = df.applymap(lambda x: '{:.3f}'.format(x) if isinstance(x, (int, float)) else x)
    # df[y_name] = df[y_name].apply(lambda x: '{:.3f}'.format(x)).astype(float)
    print(df.T.to_markdown().replace("|-", "|:").replace("-|", ":|"))
# print_table(x_name, m_x_1, y_name, A_y_1, A_y_1s)
print_table(x_name, m_x_2, y_name, A_y_2, A_y_2s)