from .person import Person


class FlightAttendant(Person):
    def __init__(self, name=None, last_name=None, dni=None, date_of_born=None,
                 languages_that_speak=None):

        Person.__init__(self, name, last_name, dni, date_of_born)

        self.languages_that_speak = languages_that_speak


