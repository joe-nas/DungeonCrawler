import random


class Tile:
    def __init__(self, coordinates, entropy):
        self.terrain = ""
        self.coordinates = coordinates
        self.neighbours = []
        self.entropy = entropy

    def get_neighbours(self):
        neighbours = [
            (-1, 1),
            (0, 1),
            (1, 1),
            (-1, 0),
            (1, 0),
            (-1, -1),
            (0, -1),
            (1, -1),
        ]

    def __str__(self):
        return self.coordinates


# map max entropy
# place random tile

# create a create a list of surrounding tiles coordinates
# calculate and update entropies of the surrounding tiles
# choose tile with lowest entropy

# for surrounding tiles calculate entropy


terrain_types = [
    # ("terrain","unicode char","entropy")
    ("water", "\U0001F4A7", ["water", "coast_n"]),
    ("coast_n", "\U0001F30A", ["coast_n", "water", "grassland"]),
    ("grassland", "\U0001F7E9", ["grassland", "coast_n", "forrest"]),
    ("forrest", "\U0001F332", ["forrest", "grassland"]),
    # ("coast_ne", "\U0001F30A"),
    # ("coast_e", "\U0001F30A"),
    # ("coast_se", "\U0001F30A"),
    # ("coast_s", "\U0001F30A"),
    # ("coast_sw", "\U0001F30A"),
    # ("coast_w", "\U0001F30A"),
    # ("coast_nw", "\U0001F30A"),
]


class GameMap:

    def __init__(self, nrow, ncol):
        self.nrow = nrow
        self.ncol = ncol
        self.game_map = self.create_map(nrow, ncol)

    def create_map(self, nrow, ncol):
        return [
            [
                0  # terrain_types[random.randint(0, len(terrain_types) - 1)][1]
                for x in range(nrow)
            ]
            for i in range(ncol)
        ]

    def __str__(self):
        map_string = ""
        for idx, row in enumerate(self.game_map):
            map_string += f"{row}\n"
            if idx == self.nrow - 1:
                map_string += f"{row}"
        return map_string


print(GameMap(10, 10))
