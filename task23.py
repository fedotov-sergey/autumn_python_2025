import random
import uuid
import datetime
from db import DICT_DEFENITION_WORD


class Yakubovich:
    def __init__(self):
        self.name = input("Введите имя: ")
        self.session_uuid = uuid.uuid4()

    def print_menu(self):
        print(
            """
               1. Начать игру
               2. Сохранить игру
               3. Загрузить игру
               4. Выход из игры
               5. Настройки
            """
        )

        num = int(input("Пункт меню: "))
        match num:
            case 1:
                self.key = self._generate_key()
                self.list_word = list(self.key)
                self.mask = ["#"] * len(self.key)
                self.start_game()
                # print('The UUID is: ' + str(session_uuid))
            case 2:
                pass
            case 3:
                self.load_game()
            case 4:
                self.end_game()
                print(f"Спасибо {self.name} за игру! Заходи еще! ")

    def start_game(self):
        print(DICT_DEFENITION_WORD[self.key])
        print(self.mask)
        while "#" in self.mask:
            alfa = input("Введите букву:")
            if alfa == "2":
                print("Сохранение игры!")
                self.save_game()
            cnt = 0
            for i in self.list_word:
                if alfa == i:
                    self.mask[cnt] = alfa
                    cnt += 1
                    continue
                cnt += 1
            else:
                print(self.mask)

    def save_game(self):
        f = open("save_game.csv", "at")
        dt = datetime.datetime.now()
        mask = "".join(self.mask)
        str = f"{dt}|{self.session_uuid}|{self.name}|{self.key}|{mask}\n"
        f.write(str)
        f.close()
        print("Сохранил игру!")

    def load_game(self):
        f = open("save_game.csv", "tr")
        indx = 0
        list_str = f.readlines()
        for csv_str in list_str:
            if self.name in csv_str:
                print(indx, ") ", csv_str[:-24])
            indx += 1
        indx_load = int(input("Введите номер:"))
        sg = list_str[indx_load].split("|")
        self.key = sg[3]
        self.mask = list(sg[4])
        # self.mask = self.mask[::-1]
        self.session_uuid = sg[1]
        self.start_game()

    def end_game(self):
        exit(0)

    def _generate_key(self) -> str:
        keys = list(DICT_DEFENITION_WORD.keys())
        random.shuffle(keys)
        return keys.pop()


game = Yakubovich()
game.print_menu()
