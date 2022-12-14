from random import choice


class FilmCard:
    """Формируется базовый класс фильма."""
    def __init__(self, genre: str, title: str, year: int):
        self.genre = genre
        self.title = title
        self.year = year
        # ДОБАВИТЬ: поля из класса FilmCardMaker

    def __str__(self):
        return f'Название: {self.title}' \
               f'\nГод выпуска: {self.year}' \
               f'\nЖанр: {self.genre}'


# ИСПРАВИТЬ: наследование фабрики от формируемого класса возможно, но в конечном счёте фабрика должна вернуть экземпляр именно формируемого класса, иначе смысл её существования размывается — именно это у вас и происходит: экземпляр фабрики подменяет собой экземпляр формируемого класса, а это принципиально иная объектная модель, к фабрике отношения не имеющая
class FilmCardMaker(FilmCard):
    """Дочерний класс формирует базовый класс фильма и дополняет его."""
    # ДОБАВИТЬ: аннотации параметров — внешний код будет использовать именно этот класс, поэтому аннотировать параметры здесь даже более важно, чем параметры конструктора FilmCard
    def __init__(self, genre, title, year):
        super().__init__(genre, title, year)
        # ИСПРАВИТЬ: получается, что фильм с определёнными названием, жанром и годом выхода может быть снят разными режиссёрами, с разным составом и в разных странах? разве это будут не разные фильмы? все эти поля должны быть в классе FilmCard, в то время как фабрика предоставляет только методы, с помощью которых экземпляр FilmCard формируется
        self.director = str
        self.actors = []
        # ИСПРАВИТЬ: здесь вы присваиваете в атрибут объект класса str — это не аннотация; когда необходимо создать атрибут, но работать с ним предполагается в дальнейшем, то в атрибут присваивают None — обычно это оказывается полезным для проверки атрибутов
        self.certificate = str
        self.country = str

    # ДОБАВИТЬ здесь и далее: аннотации возвращаемых значений
    # ИСПРАВИТЬ: имена идентификаторов должны быть максимально недвусмысленными — имя d можно трактовать как угодно
    def add_director(self, d: str):
        self.director = d
        # ИСПРАВИТЬ здесь и далее: разница между фабрикой и строителем порой не всегда очевидна, но возврат собственного экземпляра из метода — это несомненная прерогатива строителя
        return self

    def add_actors(self, *actors):
        self.actors += actors
        return self
    
    def add_certificate(self):
        # ИСПРАВИТЬ: явное преобразование в str избыточно — f-строка, также как и функция print(), неявно выполняет такое преобразование для каждого подставляемого выражения (есть ещё модификаторы f-строки !s и !r для явного применения вызова методов __str__() или __repr__() соответственно)
        self.certificate = f'+{str(choice([0, 12, 18]))}'
        return self
    
    def add_country(self, c: str):
        self.country = c
        return self

    def __str(self):
        return f'\nСтрана: {self.country}' \
               f'\nРежиссер: {self.director}' \
               f'\nАктеры: {self.actors}' \
               f'\nРейтинг: {self.certificate}'

    # ИСПРАВИТЬ: maker() выполняет работу метода __str__() — обычно, это не самая полезная практика, дублировать функционал встроенных методов собственными: например, здесь такой подход вынуждает вас явно использовать метод maker(), вместо передачи экземпляра FilmCardMaker в функцию print()
    def maker(self):
        return f'{self}{self.__str()}'


# СДЕЛАТЬ: если не получается просто, давайте немного усложним задачу, чтобы вы лучше прочувствовали смысл фабрики
#  - напишите дополнительный класс Actor с полями name и surname
#  - в классе FilmCard должен быть атрибут actors: list[Actor] — список экземпляров Actor
#  - в конструктор или метод фабрики должны передаваться по отдельности строки с именем и фамилией актёра
#  таким образом, фабрика должна будет в процессе инициализации экземпляра FilmCard ещё создать экземпляр(-ы) Actor


film = FilmCardMaker('драма', 'Война и Мир', 1965)
# ИСПРАВИТЬ: переменные film и factory ссылаются на один и тот же объект экземпляра FilmCardMaker — в чём причина существования двух переменных?
factory = film.add_director('Бондарчук')
factory.add_certificate()
factory.add_actors('Тихонов', 'Бондарчук')
factory.add_country('Россия')
filmcard2 = factory.maker()

film2 = FilmCardMaker('Ужасы', 'Чужой', 1979)
factory = film2.add_director('Риддли Скотт')
factory.add_certificate()
factory.add_actors('Сигурни Уивер')
factory.add_country('США')
filmcard = factory.maker()

film3 = FilmCardMaker('Ужасы', 'Нечто', 1982)
factory = film3.add_director('Джон Карпентер')
factory.add_certificate()
factory.add_actors('Курт Рассел')
factory.add_country('США')
filmcard3 = factory.maker()

print(filmcard)
print()
print(filmcard2)
print()
print(filmcard3)

# stdout:

# Название: Чужой
# Год выпуска: 1979
# Жанр: Ужасы
# Страна: США
# Режиссер: Ридли Скотт
# Актеры: ['Сигурни Уивер']
# Рейтинг: +18

# Название: Война и Мир
# Год выпуска: 1965
# Жанр: драма
# Страна: Россия
# Режиссер: Бондарчук
# Актеры: ['Тихонов', 'Бондарчук']
# Рейтинг: +0

# Название: Нечто
# Год выпуска: 1982
# Жанр: Ужасы
# Страна: США
# Режиссер: Джон Карпентер
# Актеры: ['Курт Рассел']
# Рейтинг: +12


# КОММЕНТАРИЙ: качество проработки задания у меня в намного более высоком приоритете, чем скорость сдачи задания


# ИТОГ: выполнить работу над ошибками с учётом комментариев — 2/6
