DIVISION_DEPTH = 2


class Painter(object):
    def __init__(self, scene):
        self.scene = scene

    def draw(self):
        faces = []
        for shape in self.scene.shapes:
            faces.extend(shape.faces)
        for i in range(DIVISION_DEPTH):
            faces = self.split_faces(faces)

        faces.sort(key=self.distance_from_camera, reverse=True)
        for face in faces:
            face.draw(self.scene)

    def distance_from_camera(self, face):
        return face.distance_from_camera(self.scene)

    @staticmethod
    def split_faces(faces):
        split_faces = []
        for face in faces:
            split_faces.extend(face.split())
        return split_faces
