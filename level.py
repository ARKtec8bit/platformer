import pygame
from tiles import Tile
from settings import tile_size


class Level:
    def __init__(self, level_data, surface):

        # World Setup
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self, layout):

        self.tiles = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == "X":
                    tile = Tile((x, y), tile_size, "red")
                    self.tiles.add(tile)
                if cell == ".":
                    tile = Tile((x, y), tile_size, "cyan")
                    self.tiles.add(tile)

    def run(self):

        self.tiles.update(-1)
        self.tiles.draw(self.display_surface)
