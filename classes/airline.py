class Airline(object):

    def __init__(self):
        self.flight_list = []
        self.people_list = []
        self.plane_list = []

    def search_plane(self, list_str):
        final_list = []
        for item in list_str:
            for model in self.plane_list:
                if model.plane_model == item:
                    final_list.append(model)
        return final_list

    def add_person(self, person):
        self.people_list.append(person)