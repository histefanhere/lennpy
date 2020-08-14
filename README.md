# lennpy

Python Package for accessing [Lenny faces](https://knowyourmeme.com/memes/%CD%A1-%CD%9C%CA%96-%CD%A1-lenny-face)

One day I woke up and decided that I needed lenny faces in my projects, but I was disappointed when I found the lack of categorized and easily accessable lenny faces in Python. So I made this.

## Installation

```
python3 -m pip install lennpy
```

## Usage

If you just want the standard lenny faces, lennpy provides `lennpy.lenny` which holds the popular lenny face, among others:

```py
>>> import lennpy as le
>>> le.lenny
'( ͡° ͜ʖ ͡°)'
>>> le.lenny.table_flip
'(╯°□°)╯︵ ┻━┻'
```

But lennpy also organizes lenny faces by categories, _emotions,_ from which you can get a random face in various ways:

```py
>>> import lennpy as le
>>> le.get_basic()
'( ͡° ͜ʖ ͡°)'
>>> le.emotions()
['basic', 'table_flip', ...]
>>> le.get('basic')
'( ͡ᵔ ͜ʖ ͡ᵔ )'
```