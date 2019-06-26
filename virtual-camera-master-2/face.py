from edge import Edge
from point import Point3D
from ordered_set import OrderedSet


class Face(object):
    def __init__(self, edges: [Edge], color):
        self.edges = edges
        self.gravity_center = self.calc_gravity_center()
        self.color = color

    def __repr__(self):
        points = []
        for edge in self.edges:
            points.append(edge.start_point)
        return str(points)

    def calc_gravity_center(self):
        center = Point3D(0, 0, 0)
        for point in self.unique_points():
            center = center.add_point(point)
        return center.divide_by_scalar(len(self.unique_points()))

    def unique_points(self):
        points = []
        for edge in self.edges:
            points.append(edge.start_point)
            points.append(edge.end_point)
        return list(OrderedSet(points))

    def draw(self, scene):
        if self.is_in_front_of_camera(scene):
            scene.canvas.create_polygon(self.flat_points(scene), outline="white", fill=self.color)

    def is_in_front_of_camera(self, scene):
        for edge in self.edges:
            if edge.start_point.z <= scene.camera.z or edge.end_point.z <= scene.camera.z:
                return False
        return True

    def distance_from_camera(self, scene):
        return ((self.gravity_center.x - scene.camera.x) ** 2
                + (self.gravity_center.y - scene.camera.y) ** 2
                + (self.gravity_center.z - scene.camera.z) ** 2)

    def flat_points(self, scene):
        points = []
        for point in self.unique_points():
            points.append(point.project(scene).x)
            points.append(point.project(scene).y)
        return points

    def split(self):
        faces = []
        for index, edge in enumerate(self.edges):
            previous_edge = self.edges[index-1]
            edge0 = Edge(edge.start_point, edge.get_middle_point())
            edge1 = Edge(edge.get_middle_point(),
                         Edge(edge.end_point, previous_edge.start_point).get_middle_point())
            edge2 = Edge(Edge(edge.end_point, previous_edge.start_point).get_middle_point(),
                         previous_edge.get_middle_point())
            edge3 = Edge(previous_edge.get_middle_point(), edge.start_point)

            faces.append(Face([edge0, edge1, edge2, edge3], color=self.color))

        return faces
