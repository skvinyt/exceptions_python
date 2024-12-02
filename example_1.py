import random

# Константа для достижения просветления
ENLIGHTENMENT_KARMA = 500

# Пользовательские исключения
class KillError(Exception):
    def __init__(self):
        super().__init__("KillError: You have been killed.")

class DrunkError(Exception):
    def __init__(self):
        super().__init__("DrunkError: You are drunk.")

class CarCrashError(Exception):
    def __init__(self):
        super().__init__("CarCrashError: You have been in a car crash.")

class GluttonyError(Exception):
    def __init__(self):
        super().__init__("GluttonyError: You have overeaten.")

class DepressionError(Exception):
    def __init__(self):
        super().__init__("DepressionError: You are depressed.")

# Функция для симуляции одного дня
def one_day():
    if random.randint(1, 10) == 1:
        exceptions = [KillError, DrunkError, CarCrashError, GluttonyError, DepressionError]
        raise random.choice(exceptions)()
    return random.randint(1, 7)

# Основная программа
def main():
    karma = 0
    with open('karma.log', 'w') as log_file:
        while karma < ENLIGHTENMENT_KARMA:
            try:
                daily_karma = one_day()
                karma += daily_karma
                print(f"Current karma: {karma}")
            except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as e:
                log_file.write(f"Exception occurred: {e}\n")

if __name__ == "__main__":
    main()
