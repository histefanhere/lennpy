#!/usr/bin/env python
# -*- coding: UTF-8 -*-

lennys = {}

def get_lennys_from_emotion(emotion):
    return lennys[emotion]

def generate_faces(mouths, eyes, ears):
    output_lennys = []
    for mouth in mouths:
        for eye in eyes:
            if isinstance(eye, tuple):
                left_eye, right_eye = eye
            else:
                left_eye = right_eye = eye
            for ear in ears:
                if isinstance(ear, tuple):
                    left_ear, right_ear = ear
                else:
                    left_ear = right_ear = ear
                
                lenny = left_ear + left_eye + mouth + right_eye + right_ear
                if not lenny in output_lennys:
                    output_lennys.append(lenny)
    return output_lennys


lennys['basic'] = ['( ͡° ͜ʖ ͡°)'] + generate_faces(
    mouths = [
        ' ͜ʖ',
        ' ل͜',
        '╭͜ʖ╮'
    ],
    eyes = [
        ' ͡°',
        ' °',
        ' ᴗ',
        ' ͡☉',
        ' ͡◉',
        '๏',
        'ᵔ',
        (' ͠°', '°')
    ],
    ears = [
        ('(', ')'),
        ('ʕ', 'ʔ')
    ]
)


lennys['table_flip'] = ['(╯°□°)╯︵ ┻━┻'] + generate_faces(
    mouths = [
        ' ▽ ',
        ' _ ',
        '□',
        ' ͜ʖ',
        ' ل͜',
        'Д'
    ],
    eyes = [
        ' ͡°',
        ' °',
        '๏',
        'ᵔ'
    ],
    ears = [
        ('(╯', ')╯︵/(.□ . \)'),
        ('(ノ', ')ノ彡┻━┻'),
        ('┻━┻ ︵﻿ ¯\_(', ')_/¯ ︵ ┻━┻'),
        ('(╯', ')╯︵ ┻━┻')
    ]
)


lennys['happy'] = ['☜(⌒▽⌒)☞'] + generate_faces(
    mouths = [
        '▽',
        'ヮ',
        '‿',
        'ᗜ'
    ],
    eyes = [
        ' ͡^',
        '⌒',
        '∩',
        '^',
        ('´', '`')
    ],
    ears = [
        ('(', ')'),
        ('☜(', ')☞'),
        ('(✿', ')'),
        ('(づ ', ' )づ'),
        ('\( ', ' )/')
    ]
)