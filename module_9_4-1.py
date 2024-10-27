
first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: x == y, first, second))
print(result)  # [False, True, True, False, False, False, False, False, True, False, False, False, False, False]


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for data in data_set:
                file.write(f"{data}\n")
    return write_everything


writer = get_advanced_writer('output.txt')
writer('Привет, мир!', 42, [1, 2, 3])


from random import choice

class MysticBall:
    def __init__(self, words):
        self.words = words

    def __call__(self):
        return choice(self.words)


ball = MysticBall(['Да', 'Нет', 'Наверное'])
print(ball())