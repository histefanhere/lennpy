#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import random
import sys

class Lenny:
    def __init__(self):
        self.basic = "( ͡° ͜ʖ ͡°)"
        self.table_flip = "(╯°□°)╯︵ ┻━┻"
        self.sad = "( ͡° ʖ̯ ͡°)"
        self.angry = "( ͡ಠ ʖ̯ ͡ಠ)"
        self.magic = "( ͡° ͜ʖ ͡°)━☆ﾟ.*･｡ﾟ"
        self.happy = "☜(⌒▽⌒)☞"

    def __str__(self):
        return self.basic
    
    def __repr__(self):
        return self.basic

lenny = Lenny()


lennys = {
    "basic": [
        "( ͡° ͜ʖ ͡°)",
        "(☭ ͜ʖ ☭)",
        "(ᴗ ͜ʖ ᴗ)",
        "( ° ͜ʖ °)",
        "(⟃ ͜ʖ ⟄) ",
        "( ‾ ʖ̫ ‾)",
        "(͠≖ ͜ʖ͠≖)",
        "( ͡° ʖ̯ ͡°)",
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
    ]

}

class InvalidEmotion(Exception):
    def __init__(self, emotion):
        super().__init__(f"{emotion} is not a valid emotion")

def emotions():
    return list(lennys.keys())

def get(emotion: str):
    if emotion not in lennys:
        raise InvalidEmotion(emotion)
    return random.choice(lennys[emotion])

# Here we're dynamically generating the module methods from the keys of the main dict
# e.g lennpy.get_basic() will return a random basic lenny
module = sys.modules[__name__]
for key in lennys.keys():
    setattr(module, "get_" + key, lambda: get(key))