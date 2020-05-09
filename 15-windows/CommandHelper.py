class CommandHelper:
    @staticmethod
    def readQSS(style):
        # 注意跨系统时会出现的编码问题
        with open(style, 'r', encoding="UTF-8") as f:
            return f.read()