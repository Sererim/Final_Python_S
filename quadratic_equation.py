# 3. Напишите программу, которая решает квадратные уравнения даже если дискриминант отрицательный.
# >* Используйте комплексные числа для извлечения квадратного корня.
import logging
import argparse


log_file: str = "quadratic_log.txt"
logging.basicConfig(filename=log_file, filemode='a', level=logging.NOTSET, style='{',
                    format="{levelname:<8} - {asctime}.\nLog message is: \n{msg}")
logger = logging.getLogger("Quadratic logger")


def modulus(x: float):
    if x < 0:
        return x * (-1)
    else:
        return x


def root(x: float, x0: int = 10):
    out: list[float] = [modulus(x0 - x)]
    tick: int = 0
    while True:
        out.append(0.5 * (out[tick] + x / out[tick]))
        tick += 1
        if tick == 25:
            break
    return out[tick].__round__(4)


def calculate(coefficients: dict[str: int]) -> str:
    x: list[str] = ["", ""]
    d: float = 0.0
    real: str = ""
    image: str = ""

    d = coefficients["b"] ** 2 - 4 * coefficients["a"] * coefficients["c"]
    print(f"Discriminant = {d}")

    if d >= 0:
        for i in range(2):
            x[i] = ((-coefficients["b"] + (root(d) * ((-1) ** i))) / (2 * coefficients["a"]))
    else:
        real = "{}".format(-((coefficients["b"]) / (2 * coefficients["a"])))
        for i in range(2):
            image = "{}i".format(((-1) ** i) * ((root(d)) / (2 * coefficients["a"])))
            x[i] = real + " + " + image

    logger.info("Program finished working:\n"
                f"Equation is:\n"
                f"{coefficients['b']}*x^2 + {coefficients['a']}*x + {coefficients['c']} = 0\n"
                f"First root is: {x[0]}\n"
                f"Second root is: {x[1]}\n"
                )

    return f"Equation is:\n" \
           f"{coefficients['b']}*x^2 + {coefficients['a']}*x + {coefficients['c']} = 0\n" \
           f"First root is: {x[0]}\n" \
           f"Second root is: {x[1]}\n"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="Program that calculates the roots of quadratic equation.",
                                     epilog="Enter any int or float numbers.")
    parser.add_argument('-a', metavar='a', type=float, help="Enter the first coefficient for a quadratic equation.",
                        default=1)
    parser.add_argument('-b', metavar='b', type=float, help="Enter the second coefficient for a quadratic equation.",
                        default=0)
    parser.add_argument('-c', metavar='c', type=float, help="Enter the third coefficient for a quadratic equation.",
                        default=0)
    args = parser.parse_args()
    print(calculate({"a": args.a, "b": args.b, "c": args.c}))
