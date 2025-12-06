# calc2 をテスト。
import calc2
from logger import Logger

class Calculator:
    def __init__(self, logger: Logger):
        self.result = 0 #初期値をゼロにしている
        self.logger = logger #ログをとっている

    def add(self, a):
        self.result = calc2.add(self.result, a)
        self.logger.log(f"Add({a}): result = {self.result}")

    def subtract(self, a):
        self.result = calc2.subtract(self.result, a)
        self.logger.log(f"Subtract({a}): result = {self.result}")

    def multiply(self, a):
        self.result = calc2.multiply(self.result, a)
        self.logger.log(f"Multiply({a}): result = {self.result}")

    def divide(self, a):
        try:
            self.result = calc2.divide(self.result, a)
            self.logger.log(f"Divide({a}): result = {self.result}")
        except ValueError as e:
            self.logger.log(f"Divide({a}): error = division by zero")
            raise ValueError("division error") from e

    def result(self):
        return self.result

    def reset(self):
        self.result = 0
        self.logger.log("Reset(): result = 0")