# Модель учебных материалов
# todo: Создайте иерархию классов для представления различных типов учебных материалов.
#
# Требования: Базовый класс LearningMaterial:
# Свойства: title, author, duration_minutes
# Методы:
# display_info() - выводит основную информацию
# get_difficulty() - возвращает сложность материала (должен быть переопределен в дочерних классах)
#
# Дочерние классы:
# VideoLesson:
# Дополнительные свойства: video_quality, subtitles_available
# Сложность: "Средняя"
#
# Article:
# Дополнительные свойства: word_count, reading_level
# Сложность: рассчитывается как word_count / 1000 (легкая если <1, средняя 1-3, сложная >3)
#
# Quiz:
# Дополнительные свойства: questions_count, passing_score
# Сложность: "Высокая" если passing_score > 80, иначе "Средняя"


class LearningMaterial:
    def __init__(self, title, author, duration_minutes):
        self.title = title
        self.author = author
        self.duration_minutes = duration_minutes

    def display_info(self):
        print(f"{self.title} - {self.author} - {self.duration_minutes}")

    def get_difficulty(self):
        print(f"{self.title} - {self.author} - {self.duration_minutes}")


class VideoLesson(LearningMaterial):
    def __init__(self, title, author, duration_minutes, video_quality, subtitles_available):
        super().__init__(title, author, duration_minutes)
        self.video_quality = video_quality
        self.subtitles_available = subtitles_available

    def display_info(self):
        print(
            f"{self.title} - {self.author} - {self.duration_minutes} - {self.video_quality} - {self.subtitles_available}"
        )

    def get_difficulty(self):
        return 'Сложность - "Средняя"'


class Article(LearningMaterial):
    def __init__(self, title, author, duration_minutes, word_count, reading_level):
        super().__init__(title, author, duration_minutes)
        self.word_count = word_count
        self.reading_level = reading_level

    def display_info(self):
        print(f"{self.title} - {self.author} - {self.duration_minutes} - {self.word_count} - {self.reading_level}")

    def get_difficulty(self):
        difficulty = self.word_count / 1000
        if difficulty < 1:
            return "Легкая"
        elif difficulty > 3:
            return "Тяжелая"
        else:
            return "Средняя"


class Quiz(LearningMaterial):
    def __init__(self, title, author, duration_minutes, questions_count, passing_score):
        super().__init__(title, author, duration_minutes)
        self.questions_count = questions_count
        self.passing_score = passing_score

    def display_info(self):
        print(f"{self.title} - {self.author} - {self.duration_minutes} - {self.questions_count} - {self.passing_score}")

    def get_difficulty(self):
        if self.passing_score > 80:
            return "Сложная"
        else:
            return "Средняя"


# Этот код должен работать после реализации:
materials = [
    VideoLesson("Python ООП", "Иван Иванов", 45, "1080p", True),
    Article("Глубокое обучение", "Анна Петрова", 1200, 10000, "advanced"),
    Quiz("Проверка знаний", "Платформа", 20, 75, 10),
]

for material in materials:
    print(f"{material.title}: {material.get_difficulty()}")
