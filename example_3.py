import random
import os

class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def delete_file(self):
        try:
            os.remove(self.filename)
        except FileNotFoundError:
            pass

    def append_to_file(self, data):
        with open(self.filename, 'a') as file:
            file.write(f"{data}\n")

    def read_file(self):
        try:
            with open(self.filename, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return ""

def random_exception():
    if random.randint(1, 13) == 1:
        raise Exception("Вас постигла неудача!")

def main():
    filename = 'out_file.txt'
    file_manager = FileManager(filename)
    file_manager.delete_file()

    total_sum = 0

    while total_sum < 777:
        try:
            number = int(input("Введите число: "))
            random_exception()
            total_sum += number
            file_manager.append_to_file(number)
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")
        except Exception as e:
            print(e)
            break

    if total_sum >= 777:
        print("Вы успешно выполнили условие для выхода из порочного цикла!")

    print("Содержимое файла out_file.txt:")
    print(file_manager.read_file())

if __name__ == "__main__":
    main()
