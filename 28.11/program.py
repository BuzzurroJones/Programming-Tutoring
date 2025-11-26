#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# type: ignore

"""
#####################    ISTRUZIONI PER LA SIMULAZIONE.  ####################

PRIMA DI TUTTO: Assegna le variabili sottostanti con il tuo
    NOME, COGNOME, NUMERO DI MATRICOLA

Aggiungi le tue implementazioni delle funzioni descritte sotto.
Per ottenere il punteggio esegui il file grade.py contenuto nella cartella.
Per superare la simulazione e' sufficiente ottenere un punteggio maggiore o 
uguale a 18.

Per commentare/decommentare il codice velocemente usate Control + 1 !
"""

nome       = "T"
cognome    = "C"
matricola  = "1"

################################################################################
################################################################################
################################################################################

################################################################################

# %% ----------------------------------- FUNC1 ------------------------- #
""" func1: 6 punti

Define a function func1(img_in) that takes as input a string containing the path 
to a file with an image in PNG format.
The function must return the number of pixels 
in the image whose red channel has a (strictly) greater value than 150.
"""


import images


def func1(img_in) -> int:
    
    pass

# %% ----------------------------------- FUNC2 ------------------------- #
""" func2: 8 punti

Define a function that, given the name of a file (img_in)
containing an image, computes a new image in which the blue
channel is increased by a number of units val (given as a
parameter).
When the sum exceeds 255, it wraps around to 0.
For example: 240 + 100 = 85.
The resulting image is saved to the file whose name is given
as parameter (img_out).
The function returns the number of pixels whose blue channel
overflowed past 255.
To read or write the image, use the load and save commands
from the “images” module shown in class.
"""


import images


def func2(img_in: str, img_out: str, val: int) -> int:
    pass
    

# %% ----------------------------------- FUNC3 ------------------------- #
""" func3: 8 punti
Define a function func3(input_pngfile) that takes as input a
string containing the path to a PNG image file.
The image specified by input_pngfile contains only black and
white pixels.
The function must detect all horizontal white segments and
return them in a list.
On any row, there may be at most one horizontal segment.
A segment may span the full width of the image or consist of
only a single pixel.
The function returns a list in which each horizontal segment is
encoded as a tuple (y, xstart, xend).
Here, y is the row index, xstart is the first pixel of the
segment, and xend is the last pixel of the segment.
The list must be sorted in ascending order by the y coordinate.
For example, given the image:
 0 1 2 3 4 5
0 . . . . . .
1 . . . . . .
2 . . x . . .
3 . . . . . .
4 . . . . . .
5 x x x x x x
where . is black and x is white,
the function must return:
[(2, 2, 2), (5, 0, 5)]
For test cases, see the images in func5/image01.png, etc.
"""

import images


def func3(input_pngfile):
    pass

        




# %% ----------------------------------- FUNC4 ------------------------- #
''' func4: 8 punti

Define a function func4 that takes an RGB image as input.
The function counts and returns the number of non-black pixels
that are preceded and followed by black pixels.
In other words, for a pixel P, there is a black pixel before
and one after it.
If the non-black pixel is on the right edge of the image, only
the preceding pixel is considered.
If it is on the left edge, only the following pixel is considered.
The function also saves an RGB image with the same width and
height as the input, containing only the counted pixels.
For example, if B represents a black pixel and * a
non-black pixel, given the image:
BB*BBBB*
*BBB*BBB
B*BB**B*
BBBBBB*B
*BBB**BB
the function returns 8 and saves the image:
BB*BBBB*
*BBB*BBB
B*BBBBB*
BBBBBB*B
*BBBBBBB
'''

import images

def func4(input_file_name, output_file_name):
    pass