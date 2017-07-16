!#/usr/bin/python3
"""."""


class Mine():
    """."""

    def __init__(self, num1: int, num2: int, _type: str):
        """."""
        self.type = _type
        self.num1 = num1
        self.num2 = num2
        self.result = self.parse()

    def parse(self):
        """."""
        number1 = self.num1
        number2 = self.num2
        calculate = {
            "add": lambda: number1 + number2,
            "minus": lambda: number1 - number2,
            "multiply": lambda: number1 * number2,
            "divide": lambda: number1 / number2
        }
        types = {
            "+": "add",
            "-": "minus",
            "*": "multiply",
            "/": "divide"
        }
        type_ = types.get(self.type.lower(), self.type.lower())
        result = calculate.get(type_, None)
        if isinstance(result, Exception) or not callable(result):
            raise Exception("Error: '{}' is not a valid symbol, ({})".format(
                self.type.lower(), ", ".join(x for x in [*types, *calculate])))
        return result()


print(Mine(3, "h", "-").result)
