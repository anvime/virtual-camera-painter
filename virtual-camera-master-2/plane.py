from edge import Edge
from face import Face


class Plane(object):
    def __init__(self, point_0, point_1, point_2, point_3, color):
        self.color = color
        self.point_0 = point_0
        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3

        self.edge_0 = Edge(self.point_0, self.point_1)
        self.edge_1 = Edge(self.point_1, self.point_2)
        self.edge_2 = Edge(self.point_2, self.point_3)
        self.edge_3 = Edge(self.point_3, self.point_0)

        self.points = [self.point_0, self.point_1, self.point_2, self.point_3]

        self.edges = [self.edge_0, self.edge_1, self.edge_2, self.edge_3]

        self.faces = [
            Face([self.edge_0, self.edge_1, self.edge_2, self.edge_3])
        ]

    def transform(self, matrix):
        for point in self.points:
            point.transform(matrix)
        for face in self.faces:
            face.gravity_center = face.calc_gravity_center()