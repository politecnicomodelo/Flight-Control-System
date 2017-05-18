from .person import *


class Crew(Person):
    def __init__(self, name=None, last_name=None, dni=None, date_of_born=None,
                 models_allowed_to_fly=None):
        Person.__init__(self, name, last_name, dni, date_of_born)
        self.models_allowed_to_fly = models_allowed_to_fly
