import random

terrain_types = {
    # ("terrain","unicode char","entropy")
    "water":("water", "\U0001F4A7", {"water", "coast"}),
    "coast":("coast", "\U0001F30A", {"coast", "water", "grassland"}),
    "grassland":("grassland", "\U0001F7E9", {"grassland", "coast", "forrest"}),
    "forrest":("forrest", "\U0001F332", {"forrest", "grassland"}),
    # ("coast_ne", "\U0001F30A"),
    # ("coast_e", "\U0001F30A"),
    # ("coast_se", "\U0001F30A"),
    # ("coast_s", "\U0001F30A"),
    # ("coast_sw", "\U0001F30A"),
    # ("coast_w", "\U0001F30A"),
    # ("coast_nw", "\U0001F30A"),
}



class Tile:
    # add to tile coordinates to get neighbouring tile coordinates
    relative_neighbours = [
        (-1, 1),
        (0, 1),
        (1, 1),
        (-1, 0),
        (1, 0),
        (-1, -1),
        (0, -1),
        (1, -1),
        ]
    
    # list of tuples 
    neighbours_xy = []
    entropy = 99

    def __init__(self, x,y, terrain_types):
        # dict of tuples {"water": ("water","\U0001F4A7",["water", "coast"])}
        self.terrain_types = terrain_types
        self.coordinates = (x,y)
        self.neighbours_xy = self.get_neighbours()




    def get_neighbours(self):
        """
        creates a list of tuples corresponding to the x,y coordinates of the neighbouring tiles.

        Yields:
            list: a list of tuples [(x1,y1), ... (xn,yn)]
        """ 
        for x,y in self.relative_neighbours:

            ## needs a check if coordinates are out of the map
            ## maybe set a global varianble with map size

            yield (self.coordinates[0]+x, self.coordinates[1]+y)




    def set_terrain_type(self,terrain_type):
        """
        Sets a the terrain-type of a tile: to a tuple like:\n
            ("water","\\U0001F4A7",["water", "coast"])
        
        Args:
            terrain_type (_str_): str corresponding to a terrain type e.g. "water"
        """
        self.terrain_type = terrain_types.get(terrain_type)
        self.entropy = len(self.terrain_type[2])

    def __str__(self):
        return f"x: {self.coordinates[0]}, y: {self.coordinates[1]}, terrain: {self.terrain_type}, entropy: {self.entropy}"

t = Tile(3,4,terrain_types)
# [print(x) for x in t.neighbours_xy]
# t.set_terrain_type("water")
# print(t.entropy)
# print(t)

# map max entropy
# place random tile

# create a create a list of surrounding tiles coordinates
# calculate and update entropies of the surrounding tiles
# choose tile with lowest entropy

# for surrounding tiles calculate entropy


class GameMap:

    def __init__(self, nrows, ncols):
        self.nrows = nrows
        self.ncols = ncols
        self.game_map = self.create_map(nrows, ncols)

    def create_map(self, nrows, ncols):
        """
        Creates and returns a blank map.

        Args:
            nrow (int): the number of rows
            ncol (int): the number of columns

        Returns:
            list: containing nrow of lists of size nrol
        """        
        return [
            [
                # 0  # terrain_types[random.randint(0, len(terrain_types) - 1)][1]
                Tile(row,column,terrain_types) for column in range(nrows)
            ]
            for row in range(ncols)
        ]


    def __str__(self):
        map_string = ""
        for idx_r, row in enumerate(self.game_map):
            map_string += "\n"
            for idx_c, col in enumerate(row):
                map_string += f"{col.entropy} "
        return map_string


print(GameMap(10, 10))
