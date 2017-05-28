from datetime import datetime


class Person(object):

    def __init__(self, name=None, last_name=None, date_of_born=None, dni=None):
        self.name = name
        self.last_name = last_name
        self.date_of_born = date_of_born
        self.dni = dni

    def charge_txt(self, l):
        self.__init__(l[1], l[2], datetime.strptime(l[3], '%d-%m-%Y').date(), l[4])
