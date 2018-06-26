# Purpose:
#   - linking Field and GUI (passing keyevents & imagelist)
#   - hero interacting with items on the field

from field import MapConstructor
from read_write import write_highscore


class GameLogic:
    def __init__(self, hero):
        # Vector collection for the possible movement directions (up, down, left, right)
        self.dir_vector = {1: (0, -1), 2: (1, 0), 3: (-1, 0), 4: (0, 1)}
        self.map = MapConstructor()
        self.hero = hero

    # given a direction (binded keys), checks if the move is valid, moves the hero, and checks the field
    def move(self, direction: int):
        x, y = self.map.get_hero_pos()
        vec_x, vec_y = self.dir_vector.get(direction)
        # calculating the new coordinates of the hero
        new_x, new_y = x + vec_x, y + vec_y

        if self.map.get_field(new_x, new_y).get_walkable:
            # setting the new hero position
            self.map.update_hero(new_x, new_y)
            # updating the gui
            self.update_gui()
            # checking the new field
            self.check_field()

    # for the hero's position, checks if items are collectable and switches should be triggered
    def check_field(self):
        x, y = self.map.get_hero_pos()
        field = self.map.get_field(x, y)

        pass

    def update_gui(self):
        self.map.get_all_images()

    def next_lvl(self):
        self.map.next_lvl()

    # triggered if fighting resulted in life <=0
    def gameover(self):
        pass

    def game_end(self):
        write_highscore(self.map.get_lvl())


a = GameLogic(0)
