class Program:
    def __init__(self, name, year):
        self._name = name.title()
        self._year = year
        self._likes = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, new_year):
        self._year = new_year

    @property
    def likes(self):
        return self._likes

    def liked(self):
        self._likes += 1

    def __str__(self):
        return f'Name: {self.name} Year: {self.year} Likes: {self.likes}'

