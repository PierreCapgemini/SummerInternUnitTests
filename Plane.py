class Plane:
    def __init__(self, name, position, speed):
        self.name = name
        self.position = position
        self.speed = speed

    def move(self, movement):
        self.position = self.position + movement

    def accelerate(self, acceleration):
        self.speed = self.speed + acceleration

    def rename(self, newname):
        self.name = newname

