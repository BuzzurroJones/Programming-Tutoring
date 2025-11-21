#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operazioni da fare PRIMA DI TUTTO:
1) Assegnare le variabili sottostanti con il tuo
    NOME, COGNOME, NUMERO DI MATRICOLA
2) entro le 12.15 consegnare SOLO il file program.py su Classroom

Il voto finale e' la somma dei punteggi dei problemi risolti.
Si supera la simulazione se si raggiunge almeno 18.
I ragazzi/e con DSA devono raggiungere almeno 15
(e devono fami comunicare dal Servizio DSA di Sapienza che sono DSA).

Attenzione! DEBUG=True nel grade.py per visualizzare la stack trace degli errori.
"""

nome       = "T"
cognome    = "C"
matricola  = "1"

# ----------------------------------- EX.1 ----------------------------------- #

"""Func 1: 6 punti

Design a function that takes as arguments the paths of two files,
dict1 and dict2, and returns a dictionary as output.
The two files contain lines of text with words separated by spaces and tabs.
From these lines, the function must generate a dictionary considering only the lines 
that contain exactly two words:
the first word will be a dictionary key, and the second will be the value associated 
with that key.
The final dictionary to return must have:
one key for every key that is present in both dictionaries constructed from dict1 and 
dict2 following the procedure described above,
as value, the concatenation (using the character -) of the two values associated with 
the same key in the two dictionaries,
ordered alphabetically.
Example: if the two files dict1 and dict2 generate the dictionaries
{'a': 'dog', 'c': 'cat'} and
{'f': 'giraffe', 'a': 'ox'},
the function must return the dictionary {'a': 'dog-ox'}.

"""
def func1 (dict1, dict2):
    pass
    # completa il codice della funzione


#%% ----------------------------------- FUNC4 ------------------------- #
""" func2: 6 punti
Write a function func2(input_file, output_file) that takes as arguments two strings, 
input_file and output_file, which represent the paths to two files. Inside the file 
indicated by input_file a matrix is encoded, where each line of the file represents 
a row of the matrix, with values separated by commas and spaces.
For example, func2/input_1.txt contains:
1,    2, 3,            25
4, 5,      6, 17
7,   8,    9,          42
The function must read the file in input_file and write the same matrix again, 
but writing each row as a list of integers separated by a comma and a space, 
so that the following is written in output_file:
[1, 2, 3, 25]
[4, 5, 6, 17]
[7, 8, 9, 42]
and return the number of elements in the matrix.
Open func2/input_1.txt to see the input and func2/expected_1.txt to see the expected 
output.
"""

def func2(input_file, output_file):
    pass
    # completa il codice della funzione


# print(func2('func2/input_1.txt','func2/output_1.txt'))
# print(func2('func2/input_2.txt','func2/output_2.txt'))
# print(func2('func2/input_3.txt','func2/output_3.txt'))

#%% ----------------------------------- FUNC3 ------------------------- #
""" func3: 6 punti

Define a function func3(file_in, file_out, length, chars) that takes as arguments:
two strings representing the paths of two text files,
an integer length,
a string chars.
The function must return the list of all words found in the file pointed to by file_in
 that have a length at least length and contain at least one of the characters in the 
 string chars.
The list must be sorted by decreasing length and, in case of a tie, in alphabetical 
order.
In addition, the function must write the words of the list to the file pointed to by 
file_out, separated by a space.
Example:
func3('func3/in_01.txt', 'func3/out_01.txt', 5, 'asd')
must return the list ['hippopotamus', 'elephant', 'cobra', 'horse', 'panda', 'snake']
and write the string
'hippopotamus elephant cobra horse panda snake'
to func3/out_01.txt.
"""

def func3(file_in : str, file_out: str, length:int, chars:str) -> list[str]:
    pass
    # completa il codice della funzione


# print(func3('func3/in_01.txt', 'func3/out_01.txt', 5, 'asd')) # ['hippopotamus', 'elephant', 'cobra', 'horse', 'panda', 'snake']

# ---------------------------- FUNC 4 ---------------------------- #
'''
Func 4: 6 punti
Ecco la **traduzione in inglese**:

---

Define the function `func4(textfile_in, textfile_out)` which takes as arguments:

* `textfile_in`: the path of a text file to read
* `textfile_out`: the path of a text file to create

The file indicated by `textfile_in` contains numbers, either floats or integers, 
positive or negative, separated by spaces.

The function must read the numbers, sort them in decreasing order based on the number 
of numeric characters they contain, and in case of a tie, in increasing order by value.
Then it must write these sorted numbers into the file `textfile_out`, separated by a 
comma and a space.
Finally, the function returns the quantity of numbers read from `textfile_in`.

Example:
If the file `textfile_in` contains the line
`-23.5 17 -141 +322.7 -3227`
then in the file `textfile_out` the function must write the line
`-3227, +322.7, -141, -23.5, 17`
and return the value `5`.

'''

def func4(textfile_in, textfile_out):
    pass
    # completa il codice della funzione


# print(func4('func4/input_1.txt', 'func4/output_1.txt')) # 5

# ---------------------------- FUNC 5 ---------------------------- #

'''
Func 5: 6 punti
Ecco la **traduzione in inglese**:

---

Define the function `func5(filein)` which takes as argument

* `filein`: a text file containing an (N \times M) matrix of integers separated
 by spaces

and returns the matrix reflected across the secondary diagonal, that is, 
the diagonal that goes from the top-right element to the bottom-left element.
The matrix to be returned must be represented as a list of lists.
"Transposed" here means reflected with respect to that diagonal.

Example:
If the file `filein` contains the matrix

```
1 2 3 4
5 6 7 8
9 10 11 12
```

the function must return the matrix reflected across the diagonal from 4 to 9, 
as a list of lists:

```
[[12, 8, 4],
 [11, 7, 3],
 [10, 6, 2],
 [ 9, 5, 1]]
```

'''
def func5(input_filename):
    pass
    # completa il codice della funzione


# ---------------------------- EOF ---------------------------- #