from .person import Person


class Passenger(Person):

    def __init__(self, name=None, last_name=None, dni=None,
                 date_of_born=None, miles_traveled=None, is_vip=False,
                 has_special_needs=False):

        Person.__init__(self, name, last_name, dni, date_of_born)

        self.miles_traveled = miles_traveled
        self.is_vip = is_vip
        self.has_special_needs = has_special_needs


