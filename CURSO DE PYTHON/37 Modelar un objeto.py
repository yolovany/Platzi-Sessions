# -*- coding: utf-8 -*-
from 'class/lamp.py' import Lamp

def run():
    lamp = Lamp(is_turned_on=False)
    lamp.turn_on()
    input('')
    lamp.turn_off()
    input('')
    lamp.turn_on()
    input('')
    lamp.turn_off()
    input('')


if __name__ == '__main__':
    run()