from unittest import TestCase
from Plane import Plane


class PlaneTests(TestCase):
    def setUp(self):
        self.plane = Plane("one", 1, 1)

    def test_position_type(self):
        self.assertEqual(type(self.plane.position), int)

    def test_position(self):
        self.assertEqual(self.plane.position, 1)

    def test_move(self):
        self.plane.move(2)
        self.assertEqual(self.plane.position, 3)

    def test_speed(self):
        self.assertEqual(self.plane.speed, 1)

    def test_accelerate(self):
        self.plane.accelerate(4)
        self.assertEqual(self.plane.speed, 5)

    def test_name_type(self):
        self.plane.rename(1)
        self.assertEqual(type(self.plane.name), str)

    def test_name(self):
        self.assertEqual(self.plane.name, 'one')

    def test_rename(self):
        self.plane.rename('two')
        self.assertEqual(self.plane.name, 'two')

