class Plane(object):
    def __init__(self, plane_model=None, qty_can_fly=None, crew_required=None):
        """Creates a plane

        :param plane_model: is the model of the plane. type<str>
        :param qty_can_fly: maximum amount of passengers. type<int>
        :param crew_required: pilot + FlightAttendant required to fly. type<int>
        """
        self.plane_model = plane_model
        self.qty_can_fly = qty_can_fly
        self.crew_required = crew_required
