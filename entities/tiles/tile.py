class Tile:
    def __init__(self, terrain, coordinates=(), neighbours=[]):
        self.terrain = terrain
        self.coordinates = coordinates
        self.neighbours = neighbours
