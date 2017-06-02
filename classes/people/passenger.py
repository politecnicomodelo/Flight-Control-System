from .person import *


class Passenger(Person):

    special_needs = []
    is_vip = None

    def charge_txt(self, l):

        """
        Creates a passenger using person class:

        is_vip: type<bool>
        special_needs: type<list>
        """

        Person.charge_txt(self, l)
        self.is_vip = l[5] == '1'  # converts the string 'is vip' to bool
        self.special_needs = l[6].split(',')
        if self.special_needs[0] == "":
            self.special_needs[0] = None
