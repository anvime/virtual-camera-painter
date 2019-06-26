import tkinter as tk
import math
from cuboid import Cuboid
from point import Point3D
from math import sin, cos
import numpy as np
from axis import Axis
from painter import Painter
from plane import Plane


class Scene(object):
    def __init__(self, master):
        self.width = 800
        self.height = 800
        self.move_step = 2
        self.zoom_step = 5
        self.rotate_step = math.pi / 18

        self.canvas = tk.Canvas(master, width=self.width, height=self.height, bg="black")
        self.canvas.pack()

        self.painter = Painter(self)

        self.camera = Point3D(0, 0, 0)
        self.d = 200

        self.shapes = []
        self.initialize()
        self.draw()

    def initialize(self):
# (wysokosc, glebokosc, wysokosc)
##popuste plasterki
        # self.shapes.append(Cuboid(Point3D(2, -5, 31), 20, 0.2, 20, "green"))
        # self.shapes.append(Cuboid(Point3D(2, -7, 31.5), 20, 0.2, 20, "blue"))
        # self.shapes.append(Cuboid(Point3D(2, -9, 32), 20, 0.2, 20, "red"))
        # self.shapes.append(Cuboid(Point3D(2, -11, 32.5), 20, 0.2, 20, "yellow"))

    #oplasterki
        self.shapes.append(Cuboid(Point3D(2, -5, 31), 20, 0.2, 20, "green"))
        self.shapes.append(Cuboid(Point3D(2, -5, 31.5), 20, 0.2, 20, "blue"))
        self.shapes.append(Cuboid(Point3D(2, -5, 32), 20, 0.2, 20, "red"))
        self.shapes.append(Cuboid(Point3D(2, -5, 32.5), 20, 0.2, 20, "yellow"))
        self.shapes.append(Cuboid(Point3D(2, -5, 33), 20, 0.2, 20, "green"))
        self.shapes.append(Cuboid(Point3D(2, -5, 33.5), 20, 0.2, 20, "blue"))
        self.shapes.append(Cuboid(Point3D(2, -5, 34), 20, 0.2, 20, "red"))
        self.shapes.append(Cuboid(Point3D(2, -5, 34.5), 20, 0.2, 20, "yellow"))

# #kostki
#         self.shapes.append(Cuboid(Point3D(2, -5, 20), 10, 10, 10, "red"))
#         self.shapes.append(Cuboid(Point3D(-12, -5, 20), 10, 10, 10, "blue"))
#         self.shapes.append(Cuboid(Point3D(2, -5, 32), 10, 10, 10, "green"))
#         self.shapes.append(Cuboid(Point3D(-12, -5, 32), 10, 10, 10, "yellow"))



    def draw(self):
        self.canvas.delete(tk.ALL)
        self.painter.draw()

    def handle_move(self, event):
        handler = {
            'w': lambda: self.move(self.move_step, Axis.Y),
            's': lambda: self.move(-self.move_step, Axis.Y),
            'a': lambda: self.move(self.move_step, Axis.X),
            'd': lambda: self.move(-self.move_step, Axis.X),
            'e': lambda: self.move(-self.move_step, Axis.Z),
            'q': lambda: self.move(self.move_step, Axis.Z)
        }.get(event.keysym)

        if handler:
            handler()
            self.draw()

    def move(self, distance, axis):
        matrix = np.array([[1, 0, 0, 0],
                           [0, 1, 0, 0],
                           [0, 0, 1, 0],
                           [0, 0, 0, 1]], dtype=float)

        matrix[axis.value, 3] = distance

        for shape in self.shapes:
            shape.transform(matrix)

    def handle_turn(self, event):
        handler = {
            'w': lambda: self.rotate(self.rotate_step, Axis.X),
            's': lambda: self.rotate(-self.rotate_step, Axis.X),
            'a': lambda: self.rotate(-self.rotate_step, Axis.Y),
            'd': lambda: self.rotate(self.rotate_step, Axis.Y),
            'e': lambda: self.rotate(-self.rotate_step, Axis.Z),
            'q': lambda: self.rotate(self.rotate_step, Axis.Z)
        }.get(event.keysym)

        if handler:
            handler()
            self.draw()

    def rotate(self, angle, axis):
        matrix = np.array([[1, 0, 0, 0],
                           [0, 1, 0, 0],
                           [0, 0, 1, 0],
                           [0, 0, 0, 1]], dtype=float)

        if axis == Axis.X:
            matrix[1:3, 1:3] = np.array([[cos(angle), -sin(angle)],
                                         [sin(angle), cos(angle)]])
        elif axis == Axis.Y:
            matrix[0:3, 0:3] = np.array([[cos(angle), 0, sin(angle)],
                                         [0, 1, 0],
                                         [-sin(angle), 0, cos(angle)]])
        elif axis == Axis.Z:
            matrix[0:2, 0:2] = np.array([[cos(angle), -sin(angle)],
                                         [sin(angle), cos(angle)]])

        for shape in self.shapes:
            shape.transform(matrix)

    def handle_zoom(self, event):
        if event.delta > 0:
            self.d += self.zoom_step
        else:
            self.d -= self.zoom_step
        self.draw()

    def reset(self, event):
        self.d = 200
        self.shapes = []
        self.initialize()

        self.draw()
