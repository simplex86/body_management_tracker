# 计算BMI指标
def get_bmis(heights:list, weights:list):
    bmis = []
    for _, (height, weight) in enumerate(zip(heights, weights)):
        bmis.append(weight / ((height / 100) ** 2))

    return bmis