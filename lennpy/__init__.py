#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import random
import sys


lennys = {
    "basic": [
        "( ͡° ͜ʖ ͡°)",
        "(☭ ͜ʖ ☭)",
        "(ᴗ ͜ʖ ᴗ)",
        "( ° ͜ʖ °)",
        "(⟃ ͜ʖ ⟄) ",
        "( ‾ ʖ̫ ‾)",
        "(͠≖ ͜ʖ͠≖)",
        "ʕ ͡° ʖ̯ ͡°ʔ",
        "( ͡° ل͜ ͡°)",
        "( ͠° ͟ʖ ͡°)",
        "( ͠° ͟ʖ ͠°)",
        "( ͡~ ͜ʖ ͡°)",
        "( ͡o ͜ʖ ͡o)",
        "( ͡◉ ͜ʖ ͡◉)",
        "( ͡☉ ͜ʖ ͡☉)",
        "( ͡° ͜V ͡°)",
        "ʕ ͡° ͜ʖ ͡°ʔ",
        "( ͡ᵔ ͜ʖ ͡ᵔ )",
        "( ͡° ͜ʖ ͡ °)"
    ],
    "table_flip": [
        "(╯°□°)╯︵ ┻━┻",
        "(╯ຈل͜ຈ) ╯︵ ┻━┻",
        "(ノ͡° ͜ʖ ͡°)ノ︵┻┻",
        "(⌐▀͡ ̯ʖ▀) ╯︵ ┻─┻",
        "┬─┬ノ( ͡° ͜ʖ ͡°ノ)",
        "（╯ ͡° ▽ ͡°）╯︵ ┻━┻",
        "(/ ͡° ͜ʖ ͡°)/ ⌒ ┤",
        "(╯ ͝° ͜ʖ͡°)╯︵ ┻━┻",
        "（╯ ͡° ل͜ ͡°）╯︵ ┻━┻",
        "( ͡° ͜ʖ ͡°) ╯︵ ┻─┻",
        "┬──┬ ノ( ͡° ل͜ ͡°ノ)",
        "┬━┬ノ(▀̿̿Ĺ̯̿̿▀̿ ̿ノ)",
        "（╯ ͡°  ▽ ͡°）╯︵ ┻━┻",
        "（╯ ͡°  ل͜ ͡°）╯︵ ┻━┻",
        "（╯°□°）╯︵ ( ͜。 ͡ʖ ͜。)",
        "（╯ ͡ ͠° ͟ل͜ ͡°）╯︵ ┻━┻",
        "(▀̿̿Ĺ̯̿̿▀̿ ̿)ﾉ ︵ ┻━┻'",
        "（╯ ͡° ل͜ ͡°）╯︵ ( ͜。 ͡ʖ ͜。)",
        "┻━┻ ︵﻿ ¯\_( ͡° ͜ʖ ͡°)_/¯ ︵ ┻━┻",
        "/╲/( ͜。 ͜。 ͡ ͡ʖ ͜。 ͜。)/\╱\︵└(՞▃՞ └)",
        "!!!（╯°□°）╯ミ /╲/( ͜。 ͜。 ͡ʖ ͜。 ͜。)/\╱\""
    ],
    "sad": [
        "( ͡° ʖ̯ ͡°)"
    ],
    "angry": [
        "( ͡ಠ ʖ̯ ͡ಠ)"
    ],
    "magic": [
        "( ͡° ͜ʖ ͡°)━☆ﾟ.*･｡ﾟ"
    ],
    "happy": [
        "☜(⌒▽⌒)☞"
    ],
    "shrug": [
        "¯\_(ツ)_/¯"
    ]
}


# This class lets us make the easiest interface possible for the package
class Emotion:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        """Called when an attribute of the module is gotten
        E.G. `lennpy.basic` will return the first basic lenny via this method."""
        return lennys[self.name][0]

    def __call__(self, *args):
        """Called when an attribute of the module is called
        E.G. `lenny.basic()` will return a random basic lenny via this method."""
        return random.choice(lennys[self.name])

# And now create all the "fake" module attributes
module = sys.modules[__name__]
for emotion_name in lennys.keys():
    setattr(module, emotion_name, Emotion(emotion_name))


# Programmatic interface for getting the available emotions and a specific lenny via function calls
# A.K.A. lame and so 2015.
class InvalidEmotion(Exception):
    def __init__(self, emotion):
        super().__init__(f"{emotion} is not a valid emotion")

def emotions():
    return list(lennys.keys())

def get(emotion):
    if emotion not in lennys.keys():
        raise InvalidEmotion(emotion)
    return lennys[emotion][0]

def get_random(emotion):
    if emotion not in lennys.keys():
        raise InvalidEmotion(emotion)
    return random.choice(lennys[emotion])
