class Switch:
    def __init__(self, switch_type):
        self._schaltertyp = switch_type

    def get_switch_type(self):
        return self._schaltertyp


class NoSwitch(Switch):
    def __init__(self):
        Switch.__init__(0)