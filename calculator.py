class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b

    @staticmethod
    def mul(a, b):
        return a * b

    @staticmethod
    def div(a, b):
        if b == 0:
            return 0
        else:
            return a / b

if __name__ == "__main__":
    numa = 4
    numb = 2

    print(Calculator.add(numa, numb))
    print(Calculator.sub(numa, numb))
    print(Calculator.mul(numa, numb))
    print(Calculator.div(numa, numb))