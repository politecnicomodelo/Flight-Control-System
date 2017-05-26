class Plane(object):

    plane_model = None
    qty_can_fly = None
    crew_required = None

    def charge_txt(self, l):
        self.plane_model = l[0]
        self.qty_can_fly = int(l[1])
        self.crew_required = int(l[2])
