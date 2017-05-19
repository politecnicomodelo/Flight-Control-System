from .crew import *


class FlightAttendant(Crew):
    languages_that_speak = None

    def charge_txt(self, l):
        Crew.charge_txt(self, l)
        self.languages_that_speak = l[6].split(',')
