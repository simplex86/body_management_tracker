import numpy as np
import os
from datetime import datetime

# 加载统计数据，返回 日期、身高和体重 的数据列表
# 文件格式：每行 "年-月-日,身高,体重"
# 例如：2025-05-19,170,70.0
def load_datas(filename):
    dates = []
    heights = []  # 身高列表（单位：厘米）
    weights = []  # 体重列表（单位：千克）
    
    if not os.path.exists(filename):
        print(f"错误：文件 {filename} 不存在")
        return dates, heights, weights
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith('#'):  # 跳过空行和注释行
                    continue
                
                parts = line.split(',')
                if len(parts) < 3:
                    print(f"格式错误：'{line}' - 需要3个值（日期,身高,体重）")
                    continue
                
                # 解析数据
                try:
                    date_str = parts[0].strip()
                    height_val = float(parts[1].strip())  # 身高（厘米）
                    weight_val = float(parts[2].strip())   # 体重（千克）
                    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
                    
                    dates.append(date_obj)
                    heights.append(height_val)
                    weights.append(weight_val)
                except ValueError as e:
                    print(f"解析错误: {line} - {str(e)}")
    except Exception as e:
        print(f"读取文件错误: {str(e)}")
    
    return dates, heights, weights

# 加载设置数据
# 文件格式: 是否绘制身高折线图,是否绘制体重折线图,是否绘制BMI折线图,
def load_plots(filename):
    if not os.path.exists(filename):
        print(f"错误：文件 {filename} 不存在")
        return False, False, False
    
    height = True
    weight = True
    bmi = True

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith('#'):  # 跳过空行和注释行
                    continue

                parts = line.split(',')
                if len(parts) < 3:
                    print(f"格式错误：'{line}' - 需要3个值（日期,身高,体重）")
                    continue
                
                # 解析数据
                try:
                    height = (parts[0].strip() == "True")
                    weight = (parts[1].strip() == "True")
                    bmi    = (parts[1].strip() == "True")
                except ValueError as e:
                    print(f"解析错误: {line} - {str(e)}")
    except Exception as e:
        print(f"读取文件错误: {str(e)}")

    if height == False and weight == False and bmi == False:
        weight = True
    
    return height, weight, bmi

if __name__ == "__main__":
    pass