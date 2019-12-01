class Playlist:
    def __init__(self, name, programs):
        self._name = name.title()
        self._programs = programs

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    def __getitem__(self, item):
        return self._programs[item]

    def __len__(self):
        return self._programs
