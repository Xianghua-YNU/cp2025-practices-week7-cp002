import pandas as pd
import matplotlib.pyplot as plt
import os
import matplotlib

# 设置 Matplotlib 中文字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为 SimHei
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
matplotlib.use('TkAgg')  # 使用 TkAgg 后端


def creat_frame():
    """
    创建一个包含学生信息的DataFrame并保存为CSV文件。
    """
    data = {
        '姓名': ['张三', '李四', '王五', '赵六', '陈七'],
        '年龄': [25, 30, None, 22, 28],
        '成绩': [85.5, 90.0, 78.5, 88.0, 92.0],
        '城市': ['北京', '上海', '广州', '深圳', '上海']
    }
    df = pd.DataFrame(data)
    save_path = r'C:\Users\31025\OneDrive\桌面\t\data.csv'
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    df.to_csv(save_path, index=False, encoding='utf-8')
    print(f"数据已保存到: {save_path}")


def load_data():
    """任务1: 读取数据文件"""
    file_path = r'C:\Users\31025\OneDrive\桌面\t\data.csv'
    if not os.path.exists(file_path):
        print("数据文件不存在，正在创建...")
        creat_frame()
    return pd.read_csv(file_path)


def show_basic_info(data):
    """任务2: 显示数据基本信息"""
    print("数据基本信息：")
    data.info()


def handle_missing_values(data):
    """任务3: 处理缺失值"""
    missing_columns = data.columns[data.isnull().any()].tolist()
    for col in missing_columns:
        if pd.api.types.is_numeric_dtype(data[col]):
            data[col] = data[col].fillna(data[col].mean())
    return data


def analyze_statistics(data):
    """任务4: 统计分析数值列"""
    numeric_columns = data.select_dtypes(include=['number']).columns
    for col in numeric_columns:
        mean_value = data[col].mean()
        median_value = data[col].median()
        std_value = data[col].std()
        print(f"{col} 列的均值: {mean_value}, 中位数: {median_value}, 标准差: {std_value}")


def visualize_data(data, column_name='成绩'):
    """任务5: 数据可视化"""
    # 绘制直方图
    ax = data[column_name].plot.hist()
    plt.title(f"{column_name} 分布直方图")
    plt.xlabel(column_name)
    plt.ylabel("频数")

    # 保存图像到指定路径
    save_path = r'C:\Users\31025\OneDrive\桌面\t\成绩分布直方图.png'
    os.makedirs(os.path.dirname(save_path), exist_ok=True)  # 确保目录存在
    plt.savefig(save_path, dpi=300, bbox_inches='tight')  # 保存图像
    print(f"图像已保存到: {save_path}")
    plt.close()  # 关闭图像，释放资源


def save_processed_data(data):
    """任务6: 保存处理后的数据"""
    save_path = r'C:\Users\31025\OneDrive\桌面\t\processed_data.csv'
    data.to_csv(save_path, index=False)
    print(f"处理后的数据已保存到: {save_path}")


def main():
    """主函数，执行所有数据处理流程"""
    data = load_data()
    show_basic_info(data)
    processed_data = handle_missing_values(data.copy())
    analyze_statistics(processed_data)
    visualize_data(processed_data)
    save_processed_data(processed_data)


if __name__ == "__main__":
    main()
