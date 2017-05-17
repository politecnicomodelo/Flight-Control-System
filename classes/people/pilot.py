from .person import Person


class Pilot(Person):
    def __init__(self, name=None, last_name=None, dni=None, date_of_born=None,
                 models_allowed_to_fly=None):
        """Creates a Pilot

        :param name: is the name. type<str>
        :param last_name: is the last name. type<str>
        :param dni: is the dni. type<str>
        :param date_of_born: is the day of born. type<date>
        :param models_allowed_to_fly: type<list>
        """

        Person.__init__(self, name, last_name, dni, date_of_born)

        self.models_allowed_to_fly = models_allowed_to_fly
