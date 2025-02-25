# 从 tkinter 模块导入 Frame、Label 和 CENTER 类
from tkinter import Frame, Label, CENTER
# 导入 random 模块，用于生成随机数
import random
# 导入 logic 模块，可能包含游戏逻辑相关的函数
import logic
# 导入 constants 模块，并将其重命名为 c，用于引用游戏常量
import constants as c


# 定义一个名为 gen 的函数，用于生成一个随机整数
def gen():
    # 生成一个范围在 0 到 c.GRID_LEN - 1 之间的随机整数并返回
    return random.randint(0, c.GRID_LEN - 1)


# 定义一个名为 GameGrid 的类，继承自 Frame 类
class GameGrid(Frame):
    """
    GameGrid 类用于创建一个 2048 游戏的网格界面。
    它继承自 tkinter 的 Frame 类，用于管理游戏的图形界面和逻辑。
    """

    def __init__(self):
        """
        初始化 GameGrid 类的实例。
        此方法设置主窗口的标题，绑定键盘事件，初始化网格和游戏矩阵，
        并启动主事件循环。
        """
        # 调用父类 Frame 的构造函数
        Frame.__init__(self)

        # 将当前窗口放置在网格布局中
        self.grid()
        # 设置主窗口的标题为 '2048'
        self.master.title('2048')
        # 绑定键盘事件，当按下任意键时调用 self.key_down 方法
        self.master.bind("<Key>", self.key_down)

        # 定义一个字典，将键盘按键映射到相应的游戏逻辑函数
        self.commands = {
            c.KEY_UP: logic.up,
            c.KEY_DOWN: logic.down,
            c.KEY_LEFT: logic.left,
            c.KEY_RIGHT: logic.right,
            c.KEY_UP_ALT1: logic.up,
            c.KEY_DOWN_ALT1: logic.down,
            c.KEY_LEFT_ALT1: logic.left,
            c.KEY_RIGHT_ALT1: logic.right,
            c.KEY_UP_ALT2: logic.up,
            c.KEY_DOWN_ALT2: logic.down,
            c.KEY_LEFT_ALT2: logic.left,
            c.KEY_RIGHT_ALT2: logic.right,
        }

        # 初始化一个空列表，用于存储网格中的单元格
        self.grid_cells = []
        # 调用 init_grid 方法，初始化网格界面
        self.init_grid()
        # 调用 logic 模块的 new_game 函数，创建一个新的游戏矩阵
        self.matrix = logic.new_game(c.GRID_LEN)
        # 初始化一个空列表，用于存储游戏矩阵的历史记录
        self.history_matrixs = []
        # 调用 update_grid_cells 方法，更新网格单元格的显示
        self.update_grid_cells()

        # 启动主事件循环，处理用户输入和界面更新
        self.mainloop()

    def init_grid(self):
        """
        初始化游戏网格界面。
        此方法创建背景框架，并在其中创建网格单元格和标签。
        """
        # 创建一个背景框架，设置背景颜色和大小
        background = Frame(self, bg=c.BACKGROUND_COLOR_GAME, width=c.SIZE, height=c.SIZE)
        # 将背景框架放置在网格布局中
        background.grid()

        # 遍历网格的每一行
        for i in range(c.GRID_LEN):
            # 初始化一个空列表，用于存储当前行的单元格
            grid_row = []
            # 遍历网格的每一列
            for j in range(c.GRID_LEN):
                # 创建一个单元格框架，设置背景颜色和大小
                cell = Frame(
                    background,
                    bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                    width=c.SIZE / c.GRID_LEN,
                    height=c.SIZE / c.GRID_LEN
                )
                # 将单元格框架放置在网格布局中
                cell.grid(
                    row=i,
                    column=j,
                    padx=c.GRID_PADDING,
                    pady=c.GRID_PADDING
                )
                # 创建一个标签，用于显示单元格中的数字
                t = Label(
                    master=cell,
                    text="",
                    bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                    justify=CENTER,
                    font=c.FONT,
                    width=5,
                    height=2)
                # 将标签放置在单元格框架中
                t.grid()
                # 将标签添加到当前行的单元格列表中
                grid_row.append(t)
            # 将当前行的单元格列表添加到网格单元格列表中
            self.grid_cells.append(grid_row)

    def update_grid_cells(self):
        """
        更新网格单元格的显示。
        此方法根据游戏矩阵中的数字更新每个单元格的文本和背景颜色。
        """
        # 遍历网格的每一行
        for i in range(c.GRID_LEN):
            # 遍历网格的每一列
            for j in range(c.GRID_LEN):
                # 获取当前单元格对应的游戏矩阵中的数字
                new_number = self.matrix[i][j]
                if new_number == 0:
                    # 如果数字为 0，则清空单元格的文本并设置背景颜色为空白
                    self.grid_cells[i][j].configure(text="", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    # 如果数字不为 0，则显示数字并设置背景颜色和文本颜色
                    self.grid_cells[i][j].configure(
                        text=str(new_number),
                        bg=c.BACKGROUND_COLOR_DICT[new_number],
                        fg=c.CELL_COLOR_DICT[new_number]
                    )
        # 立即更新界面，确保所有更改都能及时显示
        self.update_idletasks()

    def key_down(self, event):
        """
        处理键盘按键事件。
        此方法根据用户按下的按键调用相应的游戏逻辑函数，
        并更新游戏矩阵和界面。
        """
        # 获取用户按下的按键名称
        key = event.keysym
        # 打印按键事件信息
        print(event)
        if key == c.KEY_QUIT:
            # 如果按下退出键，则退出游戏
            exit()
        if key == c.KEY_BACK and len(self.history_matrixs) > 1:
            # 如果按下返回键且历史记录中有多个矩阵，则恢复上一个矩阵
            self.matrix = self.history_matrixs.pop()
            # 更新网格单元格的显示
            self.update_grid_cells()
            # 打印返回操作的信息
            print('back on step total step:', len(self.history_matrixs))
        elif key in self.commands:
            # 如果按下的按键在命令字典中，则调用相应的游戏逻辑函数
            self.matrix, done = self.commands[key](self.matrix)
            if done:
                # 如果游戏逻辑函数执行成功，则在矩阵中添加一个新的数字
                self.matrix = logic.add_two(self.matrix)
                # 记录当前矩阵到历史记录中
                self.history_matrixs.append(self.matrix)
                # 更新网格单元格的显示
                self.update_grid_cells()
                if logic.game_state(self.matrix) == 'win':
                    # 如果游戏状态为胜利，则在网格中显示胜利信息
                    self.grid_cells[1][1].configure(text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="Win!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                if logic.game_state(self.matrix) == 'lose':
                    # 如果游戏状态为失败，则在网格中显示失败信息
                    self.grid_cells[1][1].configure(text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="Lose!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)

    def generate_next(self):
        # 找出所有空单元格
        empty_cells = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] == 0:
                    empty_cells.append((i, j))
        # 如果存在空单元格，随机选择一个并放置数字 2
        if empty_cells:
            index = random.choice(empty_cells)
            self.matrix[index[0]][index[1]] = 2


game_grid = GameGrid()
