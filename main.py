class Canvas:
    field = []

    def __init__(self):
        pass

    def set(self, _x, _y):
        x = int(_x) + 2
        y = int(_y) + 2

        self.field = [' '] * y
        for i in range(y):
            self.field[i] = [Config.chr_default] * x

        for i in range(y):  # заполнение поля базовой разметкой
            if i == 0 or i == y - 1:
                for j in range(x):
                    self.field[i][j] = '-'
            else:
                self.field[i][0] = '|'
                self.field[i][x - 1] = '|'

    def drawLines(self, x1, y1, x2, y2):
        for i in range(int(y1), int(y2) + 1):
            for j in range(int(x1), int(x2) + 1):  # рисование всех линий
                self.field[i][j] = Config.chr_line

    def drawRectangle(self, x1: int, y1: int, x2: int, y2: int):
        for i in range(y1, y2 + 1):
            for j in range(x1, x2 + 1):  # рисование всех линий
                self.field[i][j] = Config.chr_rectangle
        for i in range(y1 + 1, y2):
            for j in range(x1 + 1, x2):  # заливка центра
                self.field[i][j] = ' '

    def floodFill(self, x: int, y: int, color: str):
        if self.field[y][x] != color:
            self.__floodFillRecursion(x, y, color, old=self.field[y][x])

    def __floodFillRecursion(self, x, y, color, old):
        if x < 0 or y < 0 or x >= len(self.field[0]) or y >= len(self.field):
            return

        if self.field[y][x] == old:
            self.field[y][x] = color
        else:
            return

        self.__floodFillRecursion(x + 1, y, color, old)
        self.__floodFillRecursion(x - 1, y, color, old)
        self.__floodFillRecursion(x, y - 1, color, old)
        self.__floodFillRecursion(x, y + 1, color, old)

    def writeInFile(self, filename: str):
        f = open(filename, 'w')
        for row in self.field:  # вывод рабочего поля
            f.write(' '.join([str(elem) for elem in row]))
            f.write('\n')
        f.close()

    def execute_сommands(self, filename: str):
        file = open(filename)

        for command in file:
            com = command.split()
            if com[0] == "C":
                self.set(com[1], com[2])
            elif com[0] == "L":
                self.drawLines(com[1], com[2], com[3], com[4])
            elif com[0] == "R":
                self.drawRectangle(int(com[1]), int(com[2]), int(com[3]), int(com[4]))
            elif com[0] == "B":
                self.floodFill(int(com[1]), int(com[2]), com[3])


class Config:
    chr_default = ' '
    chr_line = 'x'
    chr_rectangle = 'x'
    input_file: str = "source/input.txt"
    output_file: str = "source/output.txt"


def main():
    canvas = Canvas()
    canvas.execute_сommands(Config.input_file)
    canvas.writeInFile(Config.output_file)


if __name__ == "__main__":
    main()
