# 实验报告 - Pandas 数据操作练习

## 一、实验目的
阐述本次实验的主要目的，可参考任务目的部分。


本次实验的主要目的是通过 Pandas 和 Matplotlib 库，完成对结构化数据的读取、清洗、分析、可视化和保存的完整流程，具体目标包括：

1. **数据读取**：学习如何从 CSV 文件中读取数据，并在文件不存在时动态创建数据文件。
2. **数据基本信息查看**：掌握如何快速了解数据的基本结构，包括列名、数据类型和缺失值情况。
3. **缺失值处理**：学会识别数据中的缺失值，并根据列的数据类型选择合适的填充方法（如均值填充）。
4. **数据统计分析**：对数值列进行统计分析，计算均值、中位数和标准差，理解数据的分布特征。
5. **数据可视化**：通过直方图展示数值列的分布情况，提升对数据的直观理解。
6. **数据保存**：将处理后的数据保存为新的 CSV 文件，便于后续使用或分享。

通过本次实验，旨在提升对 Pandas 数据操作的理解，掌握数据清洗和分析的基本技能，并熟悉 Matplotlib 的可视化功能，为后续更复杂的数据分析任务打下基础。

## 二、实验步骤
详细描述你完成每个任务的步骤和方法，可结合代码进行说明。

### 任务 1: 读取数据
在代码中，我使用了 `load_data` 函数来读取数据文件。具体步骤如下：
1. 检查文件路径 `C:\Users\31025\OneDrive\桌面\t\data.csv` 是否存在。
2. 如果文件不存在，则调用 `creat_frame` 函数创建一个包含学生信息的 DataFrame，并保存为 CSV 文件。
3. 使用 `pd.read_csv` 函数读取 CSV 文件并返回 DataFrame。

代码片段：
```python
def load_data():
    file_path = r'C:\Users\31025\OneDrive\桌面\t\data.csv'
    if not os.path.exists(file_path):
        print("数据文件不存在，正在创建...")
        creat_frame()
    return pd.read_csv(file_path)
```

### 任务 2: 查看数据基本信息
通过 `show_basic_info` 函数查看数据的基本信息。使用了 Pandas 的 `info()` 方法，输出数据的列名、非空值数量、数据类型等信息。

代码片段：
```python
def show_basic_info(data):
    print("数据基本信息：")
    data.info()
```

### 任务 3: 处理缺失值
在 `handle_missing_values` 函数中，处理缺失值的步骤如下：
1. 使用 `data.isnull().any()` 找出包含缺失值的列。
2. 遍历这些列，判断其数据类型是否为数值类型。
3. 如果是数值类型，则用该列的均值填充缺失值。

代码片段：
```python
def handle_missing_values(data):
    missing_columns = data.columns[data.isnull().any()].tolist()
    for col in missing_columns:
        if pd.api.types.is_numeric_dtype(data[col]):
            data[col] = data[col].fillna(data[col].mean())
    return data
```

### 任务 4: 数据统计分析
在 `analyze_statistics` 函数中，对数值列进行统计分析。具体步骤：
1. 使用 `select_dtypes(include=['number'])` 筛选出数值列。
2. 遍历每个数值列，分别计算均值、中位数和标准差。
3. 使用 `print` 输出统计结果。

代码片段：
```python
def analyze_statistics(data):
    numeric_columns = data.select_dtypes(include=['number']).columns
    for col in numeric_columns:
        mean_value = data[col].mean()
        median_value = data[col].median()
        std_value = data[col].std()
        print(f"{col} 列的均值: {mean_value}, 中位数: {median_value}, 标准差: {std_value}")
```

### 任务 5: 数据可视化
在 `visualize_data` 函数中，绘制指定列的直方图。具体步骤：
1. 默认选择 `成绩` 列作为可视化目标。
2. 使用 Pandas 的 `plot.hist()` 方法绘制直方图。
3. 设置标题、X轴和Y轴标签，并调用 `plt.show()` 显示图表。

代码片段：
```python
def visualize_data(data, column_name='成绩'):
    data[column_name].plot.hist()
    plt.title(f"{column_name} 分布直方图")
    plt.xlabel(column_name)
    plt.ylabel("频数")
    plt.show()
```

### 任务 6: 数据保存
在 `save_processed_data` 函数中，将处理后的数据保存为新的 CSV 文件。具体步骤：
1. 指定保存路径 `C:\Users\31025\OneDrive\桌面\t\processed_data.csv`。
2. 使用 Pandas 的 `to_csv` 方法保存 DataFrame，设置 `index=False` 以避免保存索引。

代码片段：
```python
def save_processed_data(data):
    save_path = r'C:\Users\31025\OneDrive\桌面\t\processed_data.csv'
    data.to_csv(save_path, index=False)
    print(f"处理后的数据已保存到: {save_path}")
```

## 三、实验结果
展示每个任务的结果，可使用表格或图表进行呈现。

以下是每个任务的结果展示方式：

### 任务 1: 读取数据
读取的数据如下所示（前 5 行）：

| 姓名 | 年龄 | 成绩 | 城市 |
|------|------|------|------|
| 张三 | 25.0 | 85.5 | 北京 |
| 李四 | 30.0 | 90.0 | 上海 |
| 王五 | NaN  | 78.5 | 广州 |
| 赵六 | 22.0 | 88.0 | 深圳 |
| 陈七 | 28.0 | 92.0 | 上海 |

---

### 任务 2: 查看数据基本信息
运行 `data.info()` 的输出结果如下：

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 4 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   姓名      5 non-null      object 
 1   年龄      4 non-null      float64
 2   成绩      5 non-null      float64
 3   城市      5 non-null      object 
dtypes: float64(2), object(2)
memory usage: 288.0+ bytes
```

---

### 任务 3: 处理缺失值
处理缺失值后，`年龄` 列的缺失值被填充为均值（`26.25`）。处理后的数据如下：

| 姓名 | 年龄  | 成绩 | 城市 |
|------|-------|------|------|
| 张三 | 25.00 | 85.5 | 北京 |
| 李四 | 30.00 | 90.0 | 上海 |
| 王五 | 26.25 | 78.5 | 广州 |
| 赵六 | 22.00 | 88.0 | 深圳 |
| 陈七 | 28.00 | 92.0 | 上海 |

---

### 任务 4: 数据统计分析
数值列的统计分析结果如下：

| 列名 | 均值   | 中位数 | 标准差   |
|------|--------|--------|---------|
| 年龄 | 26.25  | 26.25  | 3.1125  |
| 成绩 | 86.80  | 88.00  | 5.0848  |

---

### 任务 5: 数据可视化
绘制的 `成绩` 列直方图如下：

![成绩分布直方图]![成绩分布直方图](https://github.com/user-attachments/assets/aa9904eb-498d-465c-bc2b-8b3694aaa7bc)


---

### 任务 6: 数据保存
处理后的数据已保存到路径：`C:\Users\31025\OneDrive\桌面\t\processed_data.csv`。

保存的数据内容如下：

| 姓名 | 年龄  | 成绩 | 城市 |
|------|-------|------|------|
| 张三 | 25.00 | 85.5 | 北京 |
| 李四 | 30.00 | 90.0 | 上海 |
| 王五 | 26.25 | 78.5 | 广州 |
| 赵六 | 22.00 | 88.0 | 深圳 |
| 陈七 | 28.00 | 92.0 | 上海 |



## 四、总结
总结本次实验的收获和体会，分析遇到的问题及解决方法，对 Pandas 数据操作的理解和认识。

### 实验总结

#### 收获和体会
1. **Pandas 数据操作**：
   - 熟悉了 Pandas 的基本操作，包括数据读取、缺失值处理、统计分析和数据保存。
   - 学会了使用 `select_dtypes` 筛选数值列，结合 `mean()`、`median()` 和 `std()` 进行统计分析。
   - 理解了 `isnull()` 和 `fillna()` 的用法，能够有效处理缺失值。

2. **数据可视化**：
   - 使用 Matplotlib 绘制直方图，掌握了 `plot.hist()` 的基本用法。
   - 学会了设置中文字体和解决负号显示问题，提升了图表的可读性。

3. **代码组织**：
   - 通过函数划分任务，代码结构清晰，便于维护和扩展。
   - 主函数 `main()` 将各个任务串联起来，形成完整的数据处理流程。

---

#### 遇到的问题及解决方法
1. **缺失值处理**：
   - 问题：初次处理缺失值时，未区分数值列和非数值列，导致报错。
   - 解决方法：使用 `pd.api.types.is_numeric_dtype()` 判断列的数据类型，仅对数值列填充均值。

2. **中文字体显示问题**：
   - 问题：绘制直方图时，中文标题和标签无法正常显示。
   - 解决方法：通过 `matplotlib.rcParams['font.sans-serif']` 设置中文字体为 `SimHei`，并禁用负号显示问题。

3. **文件路径问题**：
   - 问题：文件保存路径中，目录不存在时会报错。
   - 解决方法：使用 `os.makedirs()` 创建目录，并设置 `exist_ok=True` 确保目录已存在时不会报错。

---

#### 对 Pandas 数据操作的理解
- Pandas 是一个功能强大的数据分析工具，能够高效处理结构化数据。
- 数据清洗（如缺失值处理）是数据分析的重要环节，直接影响后续分析结果的准确性。
- 数据统计分析和可视化是理解数据分布和特征的关键步骤，能够为决策提供有力支持。
- 熟练掌握 Pandas 的基本操作和 Matplotlib 的可视化功能，可以显著提升数据处理效率和分析能力。

---

#### 未来改进方向
- 探索更多 Pandas 的高级功能，如分组聚合（`groupby`）和数据透视表（`pivot_table`）。
- 学习更多 Matplotlib 和 Seaborn 的可视化技巧，提升图表的美观性和信息表达能力。
- 优化代码的可复用性和鲁棒性，例如通过参数化函数增强灵活性。
    
