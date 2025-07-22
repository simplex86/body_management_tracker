import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import math

dates = []
heights = {"data":[], "plot":False}
weights = {"data":None, "plot":False}
bmis = {"data":[], "plot":False}

pnum = 0
rnum = 0

# 设置日期
def set_dates(data:list):
    for v in data: 
        dates.append(v)

# 设置身高
def set_heights(data:list, plot = True):
    heights["data"] = data
    heights["plot"] = plot

    if plot: 
        global pnum
        pnum += 1

# 设置体重
def set_weights(data:list, plot = True):
    weights["data"] = data
    weights["plot"] = plot

    if plot: 
        global pnum
        pnum += 1

# 设置BMI
def set_bmis(data:list, plot = True):
    bmis["data"] = data
    bmis["plot"] = plot

    if plot: 
        global pnum
        pnum += 1

height_color = '#1f77b4'
weight_color = '#1f77b4'
bmi_color = '#ff7f0e'

# 绘制身高折线图
def plot_heights():
    if (heights["plot"] == False):
        return
    
    global rnum
    rnum += 1
    
    hdata = heights["data"]

    ax1 = plt.subplot(pnum, 1, rnum)
    ax1.plot(dates, hdata, 'p-', color=height_color, linewidth=1.5, markersize=6, label='身高')

    # 添加身高数据标签（蓝色，数据点正上方）
    for i, (date, height) in enumerate(zip(dates, hdata)):
        ax1.annotate(f"{height}", 
                    (date, height), 
                    xytext=(0, 10),
                    textcoords='offset points',
                    fontsize=11,
                    ha='center',
                    va='center',
                    color=height_color)

    minv = math.floor(min(hdata)) - 2
    maxv = math.ceil(max(hdata)) + 2

    # 设置身高图表格式 - 添加日期时间标签
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%m.%d'))
    ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7))
    ax1.set_ylabel('身高 (cm)', fontsize=13, color=height_color, labelpad=15)
    ax1.tick_params(axis='y', colors=height_color)
    ax1.set_title('身高变化趋势', fontsize=15, pad=15)
    ax1.set_ylim(minv, maxv)
    ax1.grid(True, linestyle='--', alpha=0.6)
    ax1.legend(loc='upper right')

    # 添加日期文本标签
    for i, date in enumerate(dates):
        ax1.annotate(date.strftime('%m/%d'),
                    (date, ax1.get_ylim()[0] + 0.2),
                    xytext=(0, 0),
                    textcoords='offset points',
                    fontsize=9,
                    ha='center',
                    va='bottom',
                    color='#333333')

# 绘制体重折线图
def plot_weights():
    if (weights["plot"] == False):
        return
    
    global rnum
    rnum += 1

    wdata = weights["data"]
    
    ax1 = plt.subplot(pnum, 1, rnum)
    ax1.plot(dates, wdata, 'o-', color=weight_color, linewidth=1.5, markersize=6, label='体重')

    # 添加体重数据标签（蓝色，数据点正上方）
    for i, (date, weight) in enumerate(zip(dates, wdata)):
        ax1.annotate(f"{weight}", 
                    (date, weight), 
                    xytext=(0, 10),
                    textcoords='offset points',
                    fontsize=11,
                    ha='center',
                    va='center',
                    color=weight_color)
    
    minv = math.floor(min(wdata)) - 1
    maxv = math.ceil(max(wdata)) + 1

    # 设置体重图表格式 - 添加日期时间标签
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%m.%d'))
    ax1.xaxis.set_major_locator(mdates.DayLocator(interval=7))
    ax1.set_ylabel('体重 (kg)', fontsize=13, color=weight_color, labelpad=15)
    ax1.tick_params(axis='y', colors=weight_color)
    ax1.set_title('体重变化趋势', fontsize=15, pad=15)
    ax1.set_ylim(minv, maxv)
    ax1.grid(True, linestyle='--', alpha=0.6)
    ax1.legend(loc='upper right')

    # 添加日期文本标签
    for i, date in enumerate(dates):
        ax1.annotate(date.strftime('%m/%d'),
                    (date, ax1.get_ylim()[0] + 0.2),
                    xytext=(0, 0),
                    textcoords='offset points',
                    fontsize=9,
                    ha='center',
                    va='bottom',
                    color='#333333')

# 绘制BMI折线图
def plot_bmis():
    if (bmis["plot"] == False):
        return
    
    mdata = bmis["data"]
    
    global rnum
    rnum += 1

    ax2 = plt.subplot(pnum, 1, rnum)

    # 定义健康范围（保持18.5-24.0）
    healthy_min = 18.5
    healthy_max = 24.0

    # 设置BMI坐标轴范围
    minv = min(16.5, math.floor(min(mdata)) - 1)
    maxv = max(26, math.ceil(max(mdata)) + 1)
    ax2.set_ylim(minv, maxv)

    # 绘制健康区域（18.5-24.0）
    ax2.axhspan(healthy_min, healthy_max, color='#a5d6a7', alpha=0.4)

    # 绘制不健康区域（minv-18.5和24.0-maxv）
    ax2.axhspan(minv, healthy_min, color='#ffcdd2', alpha=0.3)
    ax2.axhspan(healthy_max, maxv, color='#ffcdd2', alpha=0.3)

    # 健康边界线
    ax2.axhline(healthy_min, color='#4caf50', linestyle='--', alpha=0.7, linewidth=1.0)
    ax2.axhline(healthy_max, color='#4caf50', linestyle='--', alpha=0.7, linewidth=1.0)

    # 绘制BMI折线（橙色）
    ax2.plot(dates, mdata, 's-', color=bmi_color, linewidth=1.5, markersize=6, label='BMI')

    # 添加BMI数据标签（橙色，数据点正下方）
    c_bmi_color = bmi_color
    for i, (date, bmi) in enumerate(zip(dates, mdata)):
        if bmi > healthy_max or bmi< healthy_min:
            c_bmi_color = '#d32f2f'
        else:
            c_bmi_color = '#388e3c'

        ax2.annotate(f"{bmi:.1f}", 
                    (date, bmi), 
                    xytext=(0, 10),
                    textcoords='offset points',
                    fontsize=11,
                    ha='center',
                    va='center',
                    color=c_bmi_color)

    # 设置BMI图表格式
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%m.%d'))
    ax2.xaxis.set_major_locator(mdates.DayLocator(interval=7))
    ax2.set_ylabel('BMI 指数', fontsize=13, color=bmi_color, labelpad=15)
    ax2.tick_params(axis='y', colors=bmi_color)
    ax2.set_title('BMI变化趋势', fontsize=15, pad=15)
    ax2.grid(True, linestyle='--', alpha=0.6)
    ax2.legend(loc='upper right')

    # 添加健康状态分析
    final_bmi = bmis["data"][-1]
    if final_bmi < healthy_min:
        health_status = f"偏瘦"
        status_color = '#d32f2f'
    elif final_bmi > healthy_max:
        health_status = f"超重"
        status_color = '#d32f2f'
    else:
        health_status = f"健康"
        status_color = '#388e3c'

    ax2.annotate(health_status,
                xy=(dates[-1], bmis["data"][-1]),
                xytext=(0.99, 0.07),
                textcoords='axes fraction',
                fontsize=11,
                ha='right',
                color=status_color,
                bbox=dict(boxstyle="round,pad=0.5", fc='white', ec=status_color, alpha=0.8))

    # 添加日期文本标签到BMI图
    for i, date in enumerate(dates):
        ax2.annotate(date.strftime('%m/%d'),
                    (date, ax2.get_ylim()[0] + 0.2),
                    xytext=(0, 0),
                    textcoords='offset points',
                    fontsize=9,
                    ha='center',
                    va='bottom',
                    color='#333333')

# 绘制折线图
def plot():
    # 设置中文字体
    try:
        plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei']
        plt.rcParams['axes.unicode_minus'] = False
    except:
        pass

    plt.figure(figsize=(14, 10))

    # 绘制折线图
    plot_heights()
    plot_weights()
    plot_bmis()
    
    # 调整布局
    plt.gcf().autofmt_xdate()
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.subplots_adjust(hspace=0.3)

    # 显示窗口
    plt.show()

if __name__ == "__main__":
    pass