# -*- coding: utf-8 -*-

class Lamp:
    _LAPS = {
        True: 'ON', 
        False: 'OFF',
    }


    def __init__(self, is_turned_on):
        self._is_turned_on = is_turned_on
        self._display_state()
    

    def turn_on(self):
        self._is_turned_on = True
        self._display_state()
    

    def turn_off(self):
        self._is_turned_on = False
        self._display_state()
    

    def _display_state(self):
        print(self._LAPS[self._is_turned_on])