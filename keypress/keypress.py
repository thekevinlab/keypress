import asyncio
import glob
import random
from typing import Any
from .app import path

import pynput
from playsound import playsound
from pynput.keyboard import Key

class KeyPress:
    def __init__(self):
        self.last_pressed = None
        self.modifiers = (
            Key.alt_l, Key.alt_gr, Key.cmd, Key.ctrl_l, Key.cmd_r,
            Key.ctrl_r, Key.shift, Key.shift_r, Key.backspace)

    def get_key_type(self, key):
        if key in self.modifiers:
            return "alt"

        if key == Key.space:
            return "space"

        if key == Key.enter:
            return "enter"

        else: 
            return "alpha"

    def on_press(self, key):        
        if key != self.last_pressed:
            key_type = self.get_key_type(key)

            files = glob.glob(path + '/soundpack/{0}/down/*.mp3'.format(key_type))
            playsound(random.choice(files), block=False)

            self.last_pressed = key

    def on_release(self, key) -> Any:
        key_type = self.get_key_type(key)

        files = glob.glob(path + '/soundpack/{0}/down/*.mp3'.format(key_type))
        playsound(random.choice(files), block=False)

        self.last_pressed = None

    def play_sounds(self):
        print("loading soundpack...")

        with pynput.keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()
