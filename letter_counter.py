# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.
import logging
import argparse

log_file = "letter_log.txt"
logging.basicConfig(filename=log_file, filemode='w', level=logging.WARNING, style='{',
                    format="{levelname:<8} - {asctime}.\nError message is: \n{msg}")
logger = logging.getLogger("Logger")


def counter(filename: str):
    text_raw: list = []
    count: int = 0
    try:
        with open(filename, '+r') as f:
            for i in list(f):
                str(i).strip(",.")
                text_raw += (str(i).split())

            for i in range(len(text_raw)):
                d = {x: text_raw.count(x) for x in text_raw}

                for k, v in d.items():
                    if v > 10:
                        count += 1
                        print(f"Word ={k}= is used {v} times.")
                        if count == 10:
                            break
                break
    except FileNotFoundError:
        logger.warning(f"File {filename} does not exist or path is wrong.")
    except OSError:
        logger.warning(f"File {filename} is wrong.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Simple word counter for txt files.',
                                     description='Counts all the words used in a txt file.',
                                     epilog=f'Please enter the correct file name. All logs are saved at {log_file}', )
    parser.add_argument('filename', type=str, nargs=1, help=f'Enter the correct path and a file name. All logs are '
                                                            f'kept at {log_file}')
    args = parser.parse_args()
    counter(args.filename[0])
