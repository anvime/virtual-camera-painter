from point import Point3D

class Edge(object):
    def __init__(self, start_point : Point3D, end_point : Point3D):
        self.start_point = start_point
        self.end_point = end_point

    def get_middle_point(self):
        return self.start_point.add_point(self.end_point).divide_by_scalar(2)

    def inversed(self):
        return Edge(start_point=self.end_point, end_point=self.start_point)

    def __repr__(self):
        return str(self.start_point) + " " + str(self.end_point)

