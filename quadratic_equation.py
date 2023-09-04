# 3. Напишите программу, которая решает квадратные уравнения даже если дискриминант отрицательный.
# >* Используйте комплексные числа для извлечения квадратного корня.
def modulus(x: float):
    if x < 0:
        return x * (-1)
    else:
        return x


def root(x: float, x0: int = 10):
    out: list[float] = [modulus(x0-x)]
    tick: int = 0
    while True:
        out.append(0.5*(out[tick] + x/out[tick]))
        tick += 1
        if tick == 25:
            break
    return out[tick].__round__(4)


def calculate(coefficients: dict[str: int]) -> list[str]:
    x: list[str] = ["", ""]
    D: float = 0.0
    real: str = ""
    imag: str = ""

    D = coefficients["b"]**2 - 4 * coefficients["a"] * coefficients["c"]
    print(f"Discriminant = {D}")

    if D >= 0:
        for i in range(2):
            x[i] = ((-coefficients["b"] + (root(D)*((-1)**i))) / (2 * coefficients["a"]))
    else:
        real = "{}".format(-((coefficients["b"]) / (2 * coefficients["a"])))
        for i in range(2):
            imag = "{}i".format(((-1)**i)*((root(D))/(2*coefficients["a"])))
            x[i] = real + " + " + imag
    return x


def main():
    coefficients_name: list[str] = ["a", "b", "c"]
    x: list[str] = []
    coefficients: dict[str: int] = {"a": 0.0, "b": 0.0, "c": 0.0}

    for i in coefficients_name:
        try:
            coefficients[i] = float(input(f"Enter coefficient {i}:\n"))
        except ValueError:
            print("Error! Please enter valid numbers.")

    x = calculate(coefficients)
    for i in range(2):
        print(f"{i+1}th root is:\n{x[i]}")

    return 0


if __name__ == "__main__":
    main()
