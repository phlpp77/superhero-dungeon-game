import unittest
from field import *


class MapConstructorTest(unittest.TestCase):
    """Testing class for the methods of class MapConstructor"""

    def __init__(self, *args, **kwargs):
        super(MapConstructorTest, self).__init__(*args, **kwargs)
        self.map_obj = MapConstructor()


class FieldConstructorTest(unittest.TestCase):
    """Testing class for the methods of class FieldConstructor"""

    def __init__(self, *args, **kwargs):
        super(FieldConstructorTest, self).__init__(*args, **kwargs)
        self.field_obj = FieldConstructor()
        self.all_fields = ["Wall", "Floor", "Entrance", "Exit"]
        self.all_items = ["NoItem", "Dagger", "Langschwert", "Kettenhemd", "Ork", "Joker", "Rockfall", "Deathtrap"]
        self.all_switches = [("NoSwitch", (0, [])), ("LvlEnd", (0, [])), ("GameEnd", (0, [])), ("LightSwitch", (0, [])),
                             ("WallSwitch", (0, []))]
        # noinspection PyTypeChecker
        self.all_obj = self.all_fields + self.all_items + self.all_switches

    def test_all_objects(self):
        """
        Test testing if all objects are being created correctly
        """
        all_obj = self.field_obj.generate_new(self.all_obj)
        expected_obj = [Wall, Floor, Entrance, Exit, Noitem, Dolch, Langschwert, Kettenhemd, Ork1, Joker,
                        Steinschlagfalle, Todesfalle, NoSwitch, LvlEnd, GameEnd, LightSwitch, WallSwitch]
        self.assertEqual([type(ii) for ii in all_obj], expected_obj)

    def test_init_level_num(self):
        """
        Test testing if the initial level number of all field obejcts is correct ( equal to 1)
        """
        all_obj = self.field_obj.generate_new(self.all_fields)
        all_lvl = [ii.get_lvl() for ii in all_obj]
        self.assertEqual(all_lvl.count(all_lvl[0]), len(all_lvl))

    def test_next_level_num(self):
        """
        Test testing if the next_lvl method is setting the level correctly
        """
        all_obj = self.field_obj.generate_new(self.all_fields)
        all_lvl_init_plus_1 = [ii.get_lvl() + 1 for ii in all_obj]
        self.field_obj.next_lvl()
        all_lvl_next = [ii.get_lvl() for ii in all_obj]
        self.assertEqual(all_lvl_init_plus_1, all_lvl_next)


if __name__ == "__main__":
    unittest.main()
