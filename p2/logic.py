#
# CS1010FC --- Programming Methodology
#
# Mission N Solutions
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

import random
import constants as c

#######
# Task 1a #
#######

# [Marking Scheme]
# Points to note:
# Matrix elements must be equal but not identical
# 1 mark for creating the correct matrix

def new_game(n):
    """
    创建一个新的 2048 游戏矩阵。

    :param n: 矩阵的边长，即矩阵是 n x n 的大小。
    :return: 初始化后的游戏矩阵，其中包含两个随机位置的数字 2。
    """
    # 初始化一个 n x n 的矩阵，所有元素初始值为 0
    matrix = []
    for i in range(n):
        matrix.append([0] * n)
    # 调用 add_two 函数，在矩阵中随机一个为 0 的位置添加数字 2
    matrix = add_two(matrix)
    # 再次调用 add_two 函数，在矩阵中另一个随机为 0 的位置添加数字 2
    matrix = add_two(matrix)
    # 返回初始化完成的矩阵
    return matrix

###########
# Task 1b #
###########

# [Marking Scheme]
# Points to note:
# Must ensure that it is created on a zero entry
# 1 mark for creating the correct loop

def add_two(mat):
    """
    此函数用于在矩阵 mat 的一个随机空白位置添加数字 2。

    :param mat: 输入的 2048 游戏矩阵
    :return: 添加数字 2 后的矩阵
    """
    # 随机生成一个行索引
    a = random.randint(0, len(mat)-1)
    # 随机生成一个列索引
    b = random.randint(0, len(mat)-1)
    # 当随机位置的元素不为 0 时，继续生成新的随机位置
    while mat[a][b] != 0:
        a = random.randint(0, len(mat)-1)
        b = random.randint(0, len(mat)-1)
    # 在随机找到的空白位置添加数字 2
    mat[a][b] = 2
    # 返回添加数字 2 后的矩阵
    return mat
###########
# Task 1c #
###########

# [Marking Scheme]
# Points to note:
# Matrix elements must be equal but not identical
# 0 marks for completely wrong solutions
# 1 mark for getting only one condition correct
# 2 marks for getting two of the three conditions
# 3 marks for correct checking

def game_state(mat):
    """
    此函数用于检查 2048 游戏矩阵的当前状态，判断游戏是否胜利、失败或仍在进行中。

    :param mat: 输入的 2048 游戏矩阵
    :return: 游戏状态字符串，可能的值为 'win'（胜利）、'not over'（未结束）或 'lose'（失败）
    """
    # 检查是否有单元格的值达到 2048，如果有则游戏胜利
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 2048:
                return 'win'
    # 检查矩阵中是否存在值为 0 的单元格，如果有则游戏未结束
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                return 'not over'
    # 检查相邻单元格的值是否相等，如果有则游戏未结束
    for i in range(len(mat)-1):
        # 有意减少循环范围，用于检查右侧和下方的单元格
        # 使用异常处理会更优雅，但这里可能是常见的实现方式
        for j in range(len(mat[0])-1):
            if mat[i][j] == mat[i+1][j] or mat[i][j+1] == mat[i][j]:
                return 'not over'
    # 检查最后一行中相邻单元格的值是否相等，如果有则游戏未结束
    for k in range(len(mat)-1):
        if mat[len(mat)-1][k] == mat[len(mat)-1][k+1]:
            return 'not over'
    # 检查最后一列中相邻单元格的值是否相等，如果有则游戏未结束
    for j in range(len(mat)-1):
        if mat[j][len(mat)-1] == mat[j+1][len(mat)-1]:
            return 'not over'
    # 如果以上条件都不满足，则游戏失败
    return 'lose'

###########
# Task 2a #
###########

# [Marking Scheme]
# Points to note:
# 0 marks for completely incorrect solutions
# 1 mark for solutions that show general understanding
# 2 marks for correct solutions that work for all sizes of matrices

def reverse(mat):
    """
    此函数用于反转矩阵 mat 的每一行。

    :param mat: 输入的矩阵
    :return: 每一行都被反转后的新矩阵
    """
    # 初始化一个空列表，用于存储反转后的矩阵
    new = []
    # 遍历矩阵的每一行
    for i in range(len(mat)):
        # 为新矩阵的当前行创建一个空列表
        new.append([])
        # 遍历矩阵当前行的每一列
        for j in range(len(mat[0])):
            # 将原矩阵当前行的元素按逆序添加到新矩阵的当前行中
            new[i].append(mat[i][len(mat[0])-j-1])
    # 返回反转后的新矩阵
    return new
###########
# Task 2b #
###########

# [Marking Scheme]
# Points to note:
# 0 marks for completely incorrect solutions
# 1 mark for solutions that show general understanding
# 2 marks for correct solutions that work for all sizes of matrices

def transpose(mat):
    """
    此函数用于对输入的矩阵进行转置操作。

    :param mat: 输入的矩阵
    :return: 转置后的新矩阵
    """
    # 初始化一个空列表，用于存储转置后的矩阵
    new = []
    # 遍历原矩阵的列数
    for i in range(len(mat[0])):
        # 为新矩阵的当前行创建一个空列表
        new.append([])
        # 遍历原矩阵的行数
        for j in range(len(mat)):
            # 将原矩阵的第 j 行第 i 列元素添加到新矩阵的第 i 行第 j 列
            new[i].append(mat[j][i])
    # 返回转置后的新矩阵
    return new

##########
# Task 3 #
##########

# [Marking Scheme]
# Points to note:
# The way to do movement is compress -> merge -> compress again
# Basically if they can solve one side, and use transpose and reverse correctly they should
# be able to solve the entire thing just by flipping the matrix around
# No idea how to grade this one at the moment. I have it pegged to 8 (which gives you like,
# 2 per up/down/left/right?) But if you get one correct likely to get all correct so...
# Check the down one. Reverse/transpose if ordered wrongly will give you wrong result.

def cover_up(mat):
    """
    此函数用于将矩阵 mat 每一行的非零元素向左移动，使它们紧密排列，
    同时用零填充剩余的位置。

    :param mat: 输入的矩阵
    :return: 处理后的新矩阵和一个布尔值，表示是否有元素移动
    """
    # 初始化一个新的矩阵，所有元素初始值为 0
    new = []
    for j in range(c.GRID_LEN):
        partial_new = []
        for i in range(c.GRID_LEN):
            partial_new.append(0)
        new.append(partial_new)
    # 初始化一个布尔变量，用于记录是否有元素移动
    done = False
    # 遍历矩阵的每一行
    for i in range(c.GRID_LEN):
        # 用于记录当前行非零元素应该放置的位置
        count = 0
        # 遍历当前行的每一列
        for j in range(c.GRID_LEN):
            # 如果当前位置的元素不为 0
            if mat[i][j] != 0:
                # 将该元素移动到新矩阵当前行的 count 位置
                new[i][count] = mat[i][j]
                # 如果元素的原始位置和新位置不同，说明元素发生了移动
                if j != count:
                    done = True
                # 移动后，更新 count 位置
                count += 1
    # 返回处理后的新矩阵和元素是否移动的标志
    return new, done

def merge(mat, done):
    """
    此函数用于合并矩阵 mat 中每一行相邻且相等的非零元素。

    :param mat: 输入的矩阵
    :param done: 布尔值，表示之前的操作是否有元素移动
    :return: 合并后的矩阵和更新后的布尔值
    """
    # 遍历矩阵的每一行
    for i in range(c.GRID_LEN):
        # 遍历当前行的每一列，但不包括最后一列
        for j in range(c.GRID_LEN-1):
            # 检查当前位置的元素和其右侧相邻元素是否相等，且不为 0
            if mat[i][j] == mat[i][j+1] and mat[i][j] != 0:
                # 如果相等，则将当前位置的元素值乘以 2
                mat[i][j] *= 2
                # 将右侧相邻元素的值置为 0
                mat[i][j+1] = 0
                # 表示有元素进行了合并操作，更新标志位
                done = True
    # 返回合并后的矩阵和更新后的布尔值
    return mat, done

def up(game):
    """
    此函数用于处理 2048 游戏中向上移动的操作。

    :param game: 当前的游戏矩阵
    :return: 向上移动后的游戏矩阵和一个布尔值，表示是否有元素移动
    """
    print("up")
    # return matrix after shifting up
    # 对游戏矩阵进行转置操作，将向上移动转换为向左移动的逻辑
    game = transpose(game)
    # 调用 cover_up 函数，将矩阵每一行的非零元素向左移动，使它们紧密排列
    # 同时获取是否有元素移动的标志
    game, done = cover_up(game)
    # 调用 merge 函数，合并矩阵中每一行相邻且相等的非零元素
    # 并更新元素移动标志
    game, done = merge(game, done)
    # 再次调用 cover_up 函数，确保合并后矩阵的非零元素依然紧密排列
    game = cover_up(game)[0]
    # 对矩阵进行转置操作，将矩阵恢复到原来的方向
    game = transpose(game)
    # 返回向上移动并处理后的矩阵以及元素是否移动的标志
    return game, done

def down(game):
    """
    此函数用于处理 2048 游戏中向下移动的操作。

    :param game: 当前的游戏矩阵
    :return: 向下移动后的游戏矩阵和一个布尔值，表示是否有元素移动
    """
    print("down")
    # return matrix after shifting down
    # 先对游戏矩阵进行转置操作，再反转矩阵，将向下移动转换为向左移动的逻辑
    game = reverse(transpose(game))
    # 调用 cover_up 函数，将矩阵每一行的非零元素向左移动，使它们紧密排列
    # 同时获取是否有元素移动的标志
    game, done = cover_up(game)
    # 调用 merge 函数，合并矩阵中每一行相邻且相等的非零元素
    # 并更新元素移动标志
    game, done = merge(game, done)
    # 再次调用 cover_up 函数，确保合并后矩阵的非零元素依然紧密排列
    game = cover_up(game)[0]
    # 先对矩阵进行反转操作，再转置矩阵，将矩阵恢复到原来的方向
    game = transpose(reverse(game))
    # 返回向下移动并处理后的矩阵以及元素是否移动的标志
    return game, done

def left(game):
    """
    此函数用于处理 2048 游戏中向左移动的操作。

    :param game: 当前的游戏矩阵
    :return: 向左移动后的游戏矩阵和一个布尔值，表示是否有元素移动
    """
    print("left")
    # return matrix after shifting left
    # 调用 cover_up 函数，将矩阵每一行的非零元素向左移动，使它们紧密排列
    # 同时获取是否有元素移动的标志
    game, done = cover_up(game)
    # 调用 merge 函数，合并矩阵中每一行相邻且相等的非零元素
    # 并更新元素移动标志
    game, done = merge(game, done)
    # 再次调用 cover_up 函数，确保合并后矩阵的非零元素依然紧密排列
    game = cover_up(game)[0]
    # 返回向左移动并处理后的矩阵以及元素是否移动的标志
    return game, done

def right(game):
    """
    此函数用于处理 2048 游戏中向右移动的操作。

    :param game: 当前的游戏矩阵
    :return: 向右移动后的游戏矩阵和一个布尔值，表示是否有元素移动
    """
    print("right")
    # return matrix after shifting right
    # 对游戏矩阵进行反转操作，将向右移动转换为向左移动的逻辑
    game = reverse(game)
    # 调用 cover_up 函数，将矩阵每一行的非零元素向左移动，使它们紧密排列
    # 同时获取是否有元素移动的标志
    game, done = cover_up(game)
    # 调用 merge 函数，合并矩阵中每一行相邻且相等的非零元素
    # 并更新元素移动标志
    game, done = merge(game, done)
    # 再次调用 cover_up 函数，确保合并后矩阵的非零元素依然紧密排列
    game = cover_up(game)[0]
    # 再次对矩阵进行反转操作，将矩阵恢复到原来的方向
    game = reverse(game)
    # 返回向右移动并处理后的矩阵以及元素是否移动的标志
    return game, done