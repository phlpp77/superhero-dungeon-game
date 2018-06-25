import unittest
from field import *


class FieldConstructorTest(unittest.TestCase):
    """
    Testing class for the methods of class FieldConstructor
    """
    def __init__(self, *args, **kwargs):
        super(FieldConstructorTest, self).__init__(*args, **kwargs)
        self.field_obj = FieldConstructor()
        self.all_fields = ["Wall", "Floor", "Entrance", "Exit"]
        self.all_items = ["NoItem", "Dagger", "Langschwert", "Kettenhemd", "Ork", "Joker", "Rockfall", "Deathtrap"]
        self.all_switches = ["Wall", "Floor", "Entrance", "Exit", "NoItem", "Dagger", "Langschwert", "Kettenhemd",
                             "Ork", "Joker", "Rockfall", "Deathtrap"]
        self.all_obj = self.all_fields + self.all_items

    def test_all_objects(self):
        """
        Test testing if all objects are being created correctly
        """
        all_obj = self.field_obj.generate_new(self.all_obj)
        expected_obj = [Wall, Floor, Entrance, Exit, Noitem, Dolch, Langschwert, Kettenhemd, Ork1, Joker,
                        Steinschlagfalle, Todesfalle]
        self.assertEqual([type(i) for i in all_obj], expected_obj)

    def test_all_switches(self):
        """
        Test testing if all switches are being created correctly
        """
        all_switches = self.field_obj.generate_new(self.all_switches)
        expected_switches = [NoSwitch, LvlEnd, GameEnd, LightSwitch, WallSwitch]
        self.assertEqual([type(i) for i in all_switches], expected_switches)

    def test_init_level_num(self):
        """
        Test testing if the initial level number of all field obejcts is correct ( equal to 1)
        """
        all_obj = self.field_obj.generate_new(self.all_fields)
        all_lvl = [i.get_lvl() for i in all_obj]
        self.assertEqual(all_lvl.count(all_lvl[0]), len(all_lvl))

    def test_next_level_num(self):
        """
        Test testing if the next_lvl method is setting the level correctly
        """
        all_obj = self.field_obj.generate_new(self.all_fields)
        all_lvl_init_plus_1 = [i.get_lvl()+1 for i in all_obj]
        self.field_obj.next_lvl()
        all_lvl_next = [i.get_lvl() for i in all_obj]
        self.assertEqual(all_lvl_init_plus_1, all_lvl_next)


if __name__ == "__main__":
    unittest.main()
