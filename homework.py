def process_array(arr):
    """
    处理数组，计算均值、最大最小值、众数和中位数。

    :param arr: 输入的数组
    :return: 包含均值、最大值、最小值、众数和中位数的字典
    """
    if not arr:
        mean = 0
        max_val = None
        min_val = None
        mode = None
        median = None
    else:
        mean = sum(arr) / len(arr)
        max_val = max(arr)
        min_val = min(arr)

        num_count = {}
        for num in arr:
            num_count[num] = num_count.get(num, 0) + 1
        max_count = max(num_count.values())
        mode = [num for num, count in num_count.items() if count == max_count]
        if len(mode) == 1:
            mode = mode[0]

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
