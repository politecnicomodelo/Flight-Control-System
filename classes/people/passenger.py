from .person import Person


class Passenger(Person):

    def __init__(self, name=None, last_name=None, dni=None,
                 date_of_born=None, miles_traveled=None, is_vip=False,
                 special_needs=False):
        """Creates a Passenger

        :param name: is the name. type<str>
        :param last_name: is the last name. type<str>
        :param dni: is the dni. type<str>
        :param date_of_born: is the date of born. type<str>
        :param miles_traveled: is the miles that the Passenger has traveled. type<int>
        :param is_vip: type<bool>
        :param special_needs: type<list>
        """
        Person.__init__(self, name, last_name, dni, date_of_born)

        self.miles_traveled = miles_traveled
        self.is_vip = is_vip
        self.special_needs = special_needs


