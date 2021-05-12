import os
import pathlib

from keypress import KeyPress

path = str(pathlib.Path(__file__).parents[0])

if __name__ == '__main__':
    app = KeyPress()
    app.play_sounds()
