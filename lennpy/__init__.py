#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import random
import sys

from . import faces
lennys = faces.lennys

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

def get(emotion, randomized=False):
    if emotion not in lennys.keys():
        raise InvalidEmotion(emotion)
    if randomized:
        return random.choice(lennys[emotion])
    else:
        return lennys[emotion][0]

