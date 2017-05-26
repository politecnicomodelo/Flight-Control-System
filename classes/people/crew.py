from .person import *


class Crew(Person):
    models_allowed_to_fly = None

    def charge_txt(self, l):
        Person.charge_txt(self, l)
        self.models_allowed_to_fly = l[5]





