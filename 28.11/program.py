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
    img = images.load(img_in)
    red = 0
    for row in img:
        for pixel in row:
            if pixel[0] > 150:
                red +=1
    return red

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
    img = images.load(img_in)
    count = 0
    for i, riga in enumerate(img):
        for j, pixel in enumerate(riga):
            r, g, b = pixel
            b += val
            if b > 255:
                count += 1
                b = b % 256
            img[i][j] = (r, g, b)
    images.save(img, img_out)
    return count
    

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
    img = images.load(input_pngfile)
    risultato = []
    w = (255, 255, 255)   
    for y in range(len(img)):
        found_segment = False
        for x in range(len(img[0])):
            pixel = img[y][x]
            if pixel == w:
                if not found_segment:
                    start_x = x
                    found_segment = True
                end_x = x
            else:
                if found_segment:
                    break
        if found_segment:
            risultato.append( (y, start_x, end_x) )
    return risultato

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
    img = images.load(input_file_name)
    b = (0, 0, 0)
    img_out = [[b for _ in range(len(img[0]))] for _ in range(len(img))]
    count = 0
    for y, row in enumerate(img):
        for x, pixel in enumerate(row):
            if pixel != b:
                copia = False
                if x == 0:
                    if img[y][x+1] == b:
                        copia = True
                elif x == len(img[0]) - 1:
                    if img[y][x-1] == b:
                        copia = True
                else:
                    if img[y][x-1] == b and img[y][x+1] == b:
                        copia = True 
                if copia:
                    count += 1
                    img_out[y][x] = pixel
    images.save(img_out, output_file_name)
    
    return count