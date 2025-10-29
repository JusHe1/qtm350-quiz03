import pandas as pd
import numpy as np

# 模拟一个小数据集
data = {
    'student': ['Alice', 'Bob', 'Charlie', 'David'],
    'quiz_score': [88, 92, 79, 85],
    'assignment_score': [90, 87, 80, 82]
}

df = pd.DataFrame(data)

# 计算平均分
df['average'] = df[['quiz_score', 'assignment_score']].mean(axis=1)

# 输出结果
print("=== Simple Student Performance Data ===")
print(df)
print("\nClass Average:", round(df['average'].mean(), 2))
