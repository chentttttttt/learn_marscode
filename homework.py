def process_array(arr):
    """
    处理数组，计算均值、最大最小值、众数和中位数。

    :param arr: 输入的数组
    :return: 包含均值、最大值、最小值、众数和中位数的字典
    """
    # 计算均值
    if not arr:
        mean = 0
    else:
        mean = sum(arr) / len(arr)

    # 计算最大值和最小值
    if not arr:
        max_val = None
        min_val = None
    else:
        max_val = arr[0]
        min_val = arr[0]
        for num in arr:
            if num > max_val:
                max_val = num
            if num < min_val:
                min_val = num

    # 计算众数
    if not arr:
        mode = None
    else:
        num_count = {}
        for num in arr:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1
        max_count = 0
        mode = None
        for num, count in num_count.items():
            if count > max_count:
                max_count = count
                mode = num

    # 计算中位数
    if not arr:
        median = None
    else:
        sorted_arr = sorted(arr)
        n = len(sorted_arr)
        if n % 2 == 1:
            median = sorted_arr[n // 2]
        else:
            median = (sorted_arr[n // 2 - 1] + sorted_arr[n // 2]) / 2

    return {
        'mean': mean,
        'max': max_val,
        'min': min_val,
        'mode': mode,
        'median': median
    }

# 示例使用
arr = [1, 2, 2, 3, 4, 5]
result = process_array(arr)
print(result)
