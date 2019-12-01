from Program import Program


class Series(Program):
    def __init__(self, name, year, season):
        super().__init__(name, year)
        self._season = season

    @property
    def season(self):
        return self._season

    @season.setter
    def season(self, new_season):
        self._season = new_season

    def __str__(self):
        return f'Name: {self.name} Season: {self.season} Year: {self.year} Likes: {self.likes}'
