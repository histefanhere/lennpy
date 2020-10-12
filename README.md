# lennpy ( ͡° ͜ʖ ͡°)

Python Package for accessing [Lenny faces](https://knowyourmeme.com/memes/%CD%A1-%CD%9C%CA%96-%CD%A1-lenny-face) ( ͡ᵔ ͜ʖ ͡ᵔ )

One day I woke up and decided that I needed lenny faces in my projects, but I was disappointed when I found the lack of categorized and easily accessable lenny faces in Python. So I made this.

## Installation

```
python3 -m pip install lennpy
```

## Usage

lennpy organizes lenny faces by categories, _emotions,_ which from you can get the most popular standard representation very simply and elegantly:

```py
>>> import lennpy as le
>>> le.basic
'( ͡° ͜ʖ ͡°)'
>>> le.table_flip
'(╯°□°)╯︵ ┻━┻'
>>> le.happy
'☜(⌒▽⌒)☞'
```

But don't want the same old face every time? Don't worry, lennpy has you covered! You can also call any of these emotions as if they were methods to get a randomzied lenny from a large pool of faces:

```py
>>> import lennpy as le
>>> le.basic()
'( ͡◉ ͜ʖ ͡◉)'
>>> le.basic()
'( ͡° ل͜ ͡°)'
>>> le.table_flip()
'（╯ ͡° ل͜ ͡°）╯︵ ( ͜。 ͡ʖ ͜。)'
>>> le.table_flip()
'┻━┻ ︵﻿ ¯\_( ͡° ͜ʖ ͡°)_/¯ ︵ ┻━┻'
```

And if it's needed you can also access the available emotions and retrive faces programmatically (but lets be honest here, this is boring):

```py
>>> import lennpy as le
>>> le.emotions()
['basic', 'table_flip', ...]
>>> le.get('basic')
'( ͡° ͜ʖ ͡°)'
>>> le.get('basic')
'( ͡° ͜ʖ ͡°)'
>>> le.get('basic', randomized=True)
'(͠≖ ͜ʖ͠≖)'
```


┬┴┬┴┤ ͜ʖ ͡°) ├┬┴┬┴

