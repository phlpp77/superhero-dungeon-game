from monsters import *
from fallen import *

# noinspection PyUnresolvedReferences
from level.dungeonlevels import *

all_level = [DungeonLevel01, DungeonLevel02(), DungeonLevel03(), DungeonLevel04(), DungeonLevel05(), DungeonLevel06()]


# MapConstructor -> List of Fields -> List of Lists of Objects on field
# Field -> List of objects on Field

# Usage:    MapConstructor()                    -> initial setup of first level
#           MapConstructor().next_lvl()         -> setting up the next level
#           MapConstructor().get_all_images()   -> getting a list of all images needed to display the level
#                                                  in format: [[[Layout, Item], [Layout, Item]], [[Layout, Item]]]

class MapConstructor:
    def __init__(self):
        self._lvl_number, self._max_lvl = 1, len(all_level)
        self._lvl_layout, self._lvl_items, = all_level[0].dungeonlayout, all_level[0].dungeonitems
        self._lvl_height, self._lvl_width = len(self._lvl_layout), len(self._lvl_layout[0])
        # creating a list with same dimensions
        self.map = self._lvl_layout
        self._all_images = []
        # creating a fieldconstructor
        self._field_factory = FieldConstructor()

        # defining the translation dictionary for the level maps
        self._layout_dict = {0: "Wall", 1: "Floor", 254: "Entrance", 255: "Exit"}
        self._item_dict = {0: "NoItem", 101: "Dagger", 104: "Landgschwert", 203: "Kettenhemd", 902: "Teleport",
                           911: "Stairs", 10101: "Ork", 10102: "Joker", 20101: "Rockfall", 30101: "Deathtrap"}
        # self._switch_dict = {0: "NoSwitch", 1: "LvlEnd", 2: "GameEnd", 11: "LightSwitch", 21: "WallSwitch"}

        # setting up the first level
        self.generatemap()

    # initial setup of the level map
    def generatemap(self):
        for x in range(self._lvl_height):
            for y in range(self._lvl_width):
                obj_list = []
                layout, item = self._lvl_layout[x][y], self._lvl_items[x][y]
                obj_list.append(self._layout_dict.get(layout))
                obj_list.append(self._item_dict.get(item))
                # setting the objects in the map
                self.map[x][y] = self._field_factory.generate_new(obj_list)
        # setting up the image list
        self.__refresh_all_images()

    # function updating each field to the next level
    def next_lvl(self):
        # setting the new level layouts
        if self._lvl_number < self._max_lvl:
            self._lvl_number, self._lvl_layout, self._lvl_items = self._lvl_number + 1, all_level[
                self._lvl_number].dungeonlayout, all_level[self._lvl_number].dungeonitems

        # updating the map to the new level layout
        for x in range(self._lvl_height):
            for y in range(self._lvl_width):
                obj_list = []
                layout, item = self._lvl_layout[x][y], self._lvl_items[x][y]
                obj_list.append(self._layout_dict.get(layout))
                obj_list.append(self._item_dict.get(item))
                # replacing the objects in the map
                self.map[x][y] = self._field_factory.generate_new(obj_list)
        # setting the next level for all objects
        self._field_factory.next_lvl()
        # refreshing the image list
        self.__refresh_all_images()

    # returns a list of all images needed to display the single field, in order: Wall/Floor, Items
    def get_all_images_field(self, x, y):
        all_images = []
        for obj in self.map[x][y]:
            all_images.append(obj.get_image())
        return all_images

    # sets a list of lists containing all images needed to display the level, in order: Wall/Floor, Items
    def __refresh_all_images(self):
        self._all_images = self.map
        for x in range(self._lvl_height):
            for y in range(self._lvl_width):
                self._all_images[x][y] = self.get_all_images_field(x, y)

        # returns all images needed to display the level

    def get_all_images(self):
        return self._all_images


# Class to generate new fields efficiently, using generate_new()
class FieldConstructor:
    def __init__(self):
        self._lvl_number = 1
        self.object_mem = {}
        self._objects = []
        self._all_objects = {"Wall": Wall(self._lvl_number), "Floor": Floor(self._lvl_number),
                             "Entrance": Entrance(self._lvl_number), "Exit": Exit(self._lvl_number), "NoItem": Noitem(),
                             "Dagger": Dolch(), "Landgschwert": Langschwert(), "Kettenhemd": Kettenhemd(),
                             "Ork": Ork1(), "Joker": Joker(), "Rockfall": Steinschlagfalle(), "Deathtrap": Todesfalle()}

    # given a list of object names, the list should be in order: Wall/Floor, Items
    # returns a list containing the wanted objects
    def generate_new(self, objects):
        # resetting the old object list
        self._objects = []
        for obj in objects:
            self._objects.append(self.obj_memorization(obj))
        return self._objects

    # using memorization pattern to limit memory usage
    # given an object name, returns the wanted object
    def obj_memorization(self, obj):
        if obj not in self.object_mem:
            self.object_mem[obj] = self.factory(obj)
        return self.object_mem.get(obj)

    # using factory pattern to generate wanted objects
    # given an object name, generates and returns the wanted object
    def factory(self, obj):
        return self._all_objects.get(obj)

    def set_lvl_number(self, lvl_number):
        self._lvl_number = lvl_number

    def next_lvl(self):
        # self.set_lvl_number(self._lvl_number + 1)
        # for obj in self._all_objects:
        #     obj.next_lvl()
        # return self.get_all_images()

        # setting each object in memory to next level
        for key in self.object_mem:
            self.object_mem[key].next_lvl()


class Field:
    def __init__(self, lvl_number):
        self._lvl_number, self._image, self._image_name = lvl_number, "", ""
        self._walkable = True
        self.set_image()

    # function to manually set the level number
    def set_lvl_number(self, lvl_number):
        self._lvl_number = lvl_number
        self.set_image()

    # function to automatically get the next level image
    def next_lvl(self):
        self.set_lvl_number(self._lvl_number + 1)

    def set_image(self):
        self._image = "gfxlvl%d/%s" % (self._lvl_number, self._image_name)

    def get_image(self):
        return self._image

    def get_walkable(self):
        return self._walkable


class Wall(Field):
    def __init__(self, lvl_number):
        Field.__init__(self, lvl_number)
        self._walkable = False
        self._image_name = "wand.gif"
        self.set_image()


class Floor(Field):
    def __init__(self, lvl_number):
        Field.__init__(self, lvl_number)
        self._image_name = "boden.gif"
        self.set_image()


class Entrance(Field):
    def __init__(self, lvl_number):
        Field.__init__(self, lvl_number)
        self._image_name = "teleportschatten.gif"
        self.set_image()


class Exit(Field):
    def __init__(self, lvl_number):
        Field.__init__(self, lvl_number)
        self._image_name = "treppe.gif"


# creating a map constructor starting with level one
map_constructor = MapConstructor()
