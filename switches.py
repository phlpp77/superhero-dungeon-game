class Switch:
    def __init__(self, switch_type, target_coords):
        self._schaltertyp = switch_type
        self._target_coords = target_coords

    def get_switch_type(self):
        return self._schaltertyp

    def get_target_coords(self):
        return self._target_coords

    def next_lvl(self):
        pass

    def get_image(self):
        pass


class NoSwitch(Switch):
    def __init__(self, target_coords):
        Switch.__init__(self, 0, target_coords)


class LvlEnd(Switch):
    def __init__(self, target_coords):
        Switch.__init__(self, 1, target_coords)


class GameEnd(Switch):
    def __init__(self, target_coords):
        Switch.__init__(self, 2, target_coords)


class LightSwitch(Switch):
    def __init__(self, target_coords):
        Switch.__init__(self, 3, target_coords)


class WallSwitch(Switch):
    def __init__(self, target_coords):
        Switch.__init__(self, 4, target_coords)
