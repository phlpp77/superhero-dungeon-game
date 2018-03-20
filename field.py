from monsters import *
from fallen import *
from switches import *
from time import sleep

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
    # noinspection PyUnusedLocal
    def __init__(self):
        self._lvl_number, self._max_lvl = 1, len(all_level)
        self._lvl_layout, self._lvl_items = all_level[0].dungeonlayout, all_level[0].dungeonitems
        self._lvl_height, self._lvl_width = len(self._lvl_layout), len(self._lvl_layout[0])
        # splitting the
        self._lvl_switches = [[0 for x in range(self._lvl_width)] for y in range(self._lvl_height)]
        self._lvl_targets = [[0 for x in range(self._lvl_width)] for y in range(self._lvl_height)]
        for x in range(self._lvl_height):  # TODO change x for hight and y for width here?
            for y in range(self._lvl_width):
                switch = all_level[0].dungeonswitches[x][y]
                self._lvl_switches[x][y] = switch[0]
                self._lvl_targets[x][y] = switch[1]

        # creating a map with same dimensions as the level to store the objects in
        self.map = [[0 for x in range(self._lvl_width)] for y in range(self._lvl_height)]
        print(self.map)
        self._all_images = []
        # creating a fieldconstructor
        self._field_factory = FieldConstructor()

        # defining the translation dictionary for the level maps
        self._layout_dict = {0: "Wall", 1: "Floor", 254: "Entrance", 255: "Exit"}
        self._item_dict = {0: "NoItem", 101: "Dagger", 104: "Langschwert", 203: "Kettenhemd", 902: "NoItem",
                           911: "NoItem", 10101: "Ork", 10102: "Joker", 20101: "Rockfall", 30101: "Deathtrap"}
        self._switch_dict = {0: "NoSwitch", 1: "LvlEnd", 2: "GameEnd", 11: "LightSwitch", 21: "WallSwitch"}

        # setting up the first level
        self.__generate_map()
        # setting up the image list
        self.__refresh_all_images()

    # initial setup of the level map
    def __generate_map(self):
        for x in range(self._lvl_height):
            for y in range(self._lvl_width):
                obj_list = []
                layout, item, switch = self._lvl_layout[x][y], self._lvl_items[x][y], self._lvl_switches[x][y]
                switch_target = self._lvl_targets[x][y]
                obj_list.append(self._layout_dict.get(layout))
                obj_list.append(self._item_dict.get(item))
                # creating switch-target tuple
                obj_list.append((self._switch_dict.get(switch), switch_target))

                # setting the objects in the map
                self.map[x][y] = self._field_factory.generate_new(obj_list)

    # function updating each field to the next level
    def next_lvl(self):
        # setting the new level layouts
        if self._lvl_number < self._max_lvl:
            self._lvl_number, self._lvl_layout, self._lvl_items = self._lvl_number + 1, all_level[
                self._lvl_number].dungeonlayout, all_level[self._lvl_number].dungeonitems

        # updating the map to the new level layout
        self.__generate_map()
        # setting the next level for all objects
        self._field_factory.next_lvl()
        # refreshing the image list
        self.__refresh_all_images()

    # given x and y coords, returns a list of all images needed to display the single field, in order: Wall/Floor, Items
    def get_all_images_field(self, x, y):
        all_images = []
        for obj in self.map[x][y]:
            all_images.append(obj.get_image())
        # removing "None" elements returned by objects that are non-visible
        all_images = [x for x in all_images if x is not None]
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
        self._object_mem = {}
        self._objects = []
        self._all_objects = {"Wall": Wall, "Floor": Floor,
                             "Entrance": Entrance, "Exit": Exit, "NoItem": Noitem,
                             "Dagger": Dolch, "Langschwert": Langschwert, "Kettenhemd": Kettenhemd,
                             "Ork": Ork1, "Joker": Joker, "Rockfall": Steinschlagfalle, "Deathtrap": Todesfalle}
        self._all_switches = {"NoSwitch": NoSwitch, "LvlEnd": LvlEnd, "GameEnd": GameEnd, "LightSwitch": LightSwitch,
                              "WallSwitch": WallSwitch}

    # given a list of object names, the list should be in order: Wall/Floor, Items, Switches
    # returns a list containing the wanted objects
    def generate_new(self, objects):
        # resetting the old object list
        self._objects = []
        # each wanted object gets appended to the object list
        for obj in objects:
            self._objects.append(self.__obj_memorization(obj))
        return self._objects

    # using memorization pattern to minimize memory usage
    # given an object name, returns the wanted object
    # given a switch-target tuple, returns the wanted switch
    def __obj_memorization(self, obj):
        # if the wanted object is not in the memory it gets created
        if type(obj) is str and obj not in self._object_mem:
            self._object_mem[obj] = self.__factory(obj)
        elif type(obj) is tuple and obj[0] + str(obj[1]) not in self._object_mem:
            # storing the switch combined with the target for easy identification
            self._object_mem[obj[0] + str(obj[1])] = self.__factory(obj)

        if type(obj) is str:
            return self._object_mem.get(obj)
        elif type(obj) is tuple:
            return self._object_mem.get(obj[0] + str(obj[1]))

    # using factory pattern to generate wanted objects
    # given an object name, generates and returns the wanted object
    def __factory(self, obj):
        # if the wanted object is no switch it is simply returned
        if type(obj) is str:
            return self._all_objects.get(obj)(self._lvl_number)
        # if the wanted object is a switch the target parameter gets passed and the object is returned
        elif type(obj) is tuple:
            return self._all_switches.get(obj[0])(obj[1])

    def set_lvl_number(self, lvl_number):
        self._lvl_number = lvl_number

    def next_lvl(self):
        # setting each object in memory to next level
        for key in self._object_mem:
            self._object_mem[key].next_lvl()


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
print(map_constructor.get_all_images())
map_constructor.next_lvl()
print(map_constructor.get_all_images())
