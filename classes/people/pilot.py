from .crew import *


class Pilot(Crew):
    def __init__(self, name=None, last_name=None, dni=None, date_of_born=None,
                 models_allowed_to_fly=None):
        """Creates a Pilot

        :param name: is the name. type<str>
        :param last_name: is the last name. type<str>
        :param dni: is the dni. type<str>
        :param date_of_born: is the day of born. type<date>
        :param models_allowed_to_fly: type<list>
        """

        Crew.__init__(self, name, last_name, dni, date_of_born, models_allowed_to_fly)

    def charge_txt(self, l):
        Crew.charge_txt(self, l)
        self.models_allowed_to_fly = l[5].split(',')
