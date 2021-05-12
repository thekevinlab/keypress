"""
BSD 3-Clause License

Copyright (c) 2021, Synchronous
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import glob
import random
from typing import Any

import pynput
from playsound import playsound
from pynput.keyboard import Key
import logging

log = logging.getLogger(__name__)

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

            files = glob.glob('soundpack/{0}/down/*.mp3'.format(key_type))
            playsound(random.choice(files), block=False)

            self.last_pressed = key

    def on_release(self, key) -> Any:
        key_type = self.get_key_type(key)

        files = glob.glob('soundpack/{0}/down/*.mp3'.format(key_type))
        playsound(random.choice(files), block=False)

        self.last_pressed = None

    def run(self):
        with pynput.keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

if __name__ == '__main__':
    app = KeyPress()
    app.run()
