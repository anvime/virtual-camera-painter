from point import Point3D
from edge import Edge
from face import Face


class Cuboid(object):
    def __init__(self, start_point, width, depth, height, color):
        self.color = color
        p = start_point
        self.bottom_0 = Point3D(p.x, p.y, p.z)
        self.bottom_1 = Point3D(p.x + width, p.y, p.z)
        self.bottom_2 = Point3D(p.x + width, p.y, p.z + depth)
        self.bottom_3 = Point3D(p.x, p.y, p.z + depth)

        self.top_0 = Point3D(p.x, p.y + height, p.z)
        self.top_1 = Point3D(p.x + width, p.y + height, p.z)
        self.top_2 = Point3D(p.x + width, p.y + height, p.z + depth)
        self.top_3 = Point3D(p.x, p.y + height, p.z + depth)

        self.edge_bottom_0 = Edge(self.bottom_0, self.bottom_1)
        self.edge_bottom_1 = Edge(self.bottom_1, self.bottom_2)
        self.edge_bottom_2 = Edge(self.bottom_2, self.bottom_3)
        self.edge_bottom_3 = Edge(self.bottom_3, self.bottom_0)
        self.edge_vertical_0 = Edge(self.bottom_0, self.top_0)
        self.edge_vertical_1 = Edge(self.bottom_1, self.top_1)
        self.edge_vertical_2 = Edge(self.bottom_2, self.top_2)
        self.edge_vertical_3 = Edge(self.bottom_3, self.top_3)
        self.edge_top_0 = Edge(self.top_0, self.top_1)
        self.edge_top_1 = Edge(self.top_1, self.top_2)
        self.edge_top_2 = Edge(self.top_2, self.top_3)
        self.edge_top_3 = Edge(self.top_3, self.top_0)

        self.points = [self.bottom_0, self.bottom_1, self.bottom_2, self.bottom_3,
                       self.top_0, self.top_1, self.top_2, self.top_3]

        self.edges = [
            self.edge_bottom_0,
            self.edge_bottom_1,
            self.edge_bottom_2,
            self.edge_bottom_3,
            self.edge_vertical_0,
            self.edge_vertical_1,
            self.edge_vertical_2,
            self.edge_vertical_3,
            self.edge_top_0,
            self.edge_top_1,
            self.edge_top_2,
            self.edge_top_3
        ]

        self.faces = [
            Face([self.edge_bottom_0, self.edge_bottom_1, self.edge_bottom_2, self.edge_bottom_3], color),
            Face([self.edge_top_0, self.edge_top_1, self.edge_top_2, self.edge_top_3], color),
            Face([self.edge_bottom_0, self.edge_vertical_1, self.edge_top_0.inversed(), self.edge_vertical_0.inversed()], color),
            Face([self.edge_bottom_1, self.edge_vertical_2, self.edge_top_1.inversed(), self.edge_vertical_1.inversed()], color),
            Face([self.edge_bottom_2, self.edge_vertical_3, self.edge_top_2.inversed(), self.edge_vertical_2.inversed()], color),
            Face([self.edge_bottom_3, self.edge_vertical_0, self.edge_top_3.inversed(), self.edge_vertical_3.inversed()], color)
        ]

    def transform(self, matrix):
        for point in self.points:
            point.transform(matrix)
        for face in self.faces:
            face.gravity_center = face.calc_gravity_center()






