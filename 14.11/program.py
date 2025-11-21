#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# type: ignore

"""
#####################    ISTRUZIONI PER LA SIMULAZIONE.  ####################

PRIMA DI TUTTO: Assegna le variabili sottostanti con il tuo
    NOME, COGNOME, NUMERO DI MATRICOLA

Aggiungi le tue implementazioni delle funzioni descritte sotto.
Per ottenere il punteggio esegui il file grade.py contenuto nella cartella.
Per superare la simulazione e' sufficiente ottenere un punteggio maggiore o uguale a 18.

Per commentare/decommentare il codice velocemente usate Control + 1 !
"""

nome       = "NOME"
cognome    = "COGNOME"
matricola  = "MATRICOLA"

################################################################################
################################################################################
################################################################################

################################################################################
# %% ----------------------------------- FUNC.1 ------------------------------ #
################################################################################
'''func1: 6 punti

Define the function func1(file_in: str) -> list[str], which takes as input a string representing 
the path to a text file and returns a list of strings.
The function opens the text file and extracts all the words, converting them all to lowercase.
The function returns a list of the unique words found in the text file, sorted in alphabetical order.
Example:
if file_in points to 'txt/in_01.txt', the function returns
expected = ['bat', 'car', 'cat', 'condor', 'rat']
Note: to extract the words, consider only alphabetic characters;
examples:
the string '7od842m3m\t7gbe' becomes 4 words ['od', 'm', 'm', 'gbe']
the string 'E io a lui: "Poeta, io ti richeggio'
becomes ['e', 'io', 'a', 'lui', 'poeta', 'io', 'ti', 'richeggio']


'''

def func1(file_in : str) -> list[str]:
    # scrivi qui il tuo codice
    pass


################################################################################
# %% -------------------------------- FUNC.2 --------------------------------- #
################################################################################
''' func2: 6 punti
Define the function func2(file_in_a: str, file_in_b: str) -> 
list[str], which receives as arguments two strings pointing to two text files and returns a list of strings.
The function opens the two text files and finds all the unique characters contained in each of the two files,
except newlines, tabs, and spaces.
The function returns a list of strings where in the first part of the list are inserted the 
unique characters from the first file that do not appear in the second, sorted alphabetically; 
while in the second part are inserted the unique characters from the second file that do not appear 
in the first, also sorted alphabetically.
Example:
given as input 'txt/in_01.txt' and 'txt/in_03.txt',
the function returns
['B', 'D', 'E', 'G', 'H', 'I', 'L', 'M', 'N', 'O', 'P',
'S', 'U', 'V', 'Y', 'e', 'g', 'h', 'i', 'l', 'm', 'p', 's', 'u',
'v', 'w', 'y', '😌']
'''


def func2(file_in_a : str, file_in_b : str) -> list[str]:
    # scrivi qui il tuo codice
    pass

# print(func2('txt/in_01.txt','txt/in_03.txt')) 

################################################################################
# %% -------------------------------- FUNC.3 --------------------------------- #
################################################################################
'''func3: 6 punti
cat monkey
panda alligator
zotero zuu zoo
Implement the function func3(lists: list[list[str]], listi: list[list[int]], out: str) -> int, 
which receives as arguments:
a list of lists of strings, called lists
a list of lists of integers, called listi
a string out, which indicates the path where the function must write a text file
The function returns an integer.
For each list of words contained in lists, one line is written to the file at out.
However, the order in which the words are written on each line is specified by the corresponding 
list of integers in listi, which must be interpreted as the positions of the words to read from the 
lists in order to write them into the file.
The function returns the total number of words written to the out file.
Example if:
lists = [["monkey", "cat",], 
         ["panda", "alligator"], 
         ["zoo", 'zuu','zotero']] 
listi=  [[1, 0],	# prima la parola 1 e poi la 0
         [0, 1],	# prima la 0 e poi la 1
         [2, 1, 0]]	# prima la 2 poi la 1 poi la 0
valore di ritorno e' 7 e nel file out viene scritto:

'''

def func3(lists : list[list[str]], listi : list[list[int]], out : str) -> int:
    # scrivi qui il tuo codice
    pass

# print(func3([["monkey", "cat",], ["panda", "alligator"], ["zoo", 'zuu', 'zotero']],[[1, 0], [0, 1], [2, 1, 0]],'txt/out_01.txt'))

################################################################################
# %% ----------------------------------- FUNC.4 ------------------------------ #
################################################################################
""" func4: 6 punti

Write a function func4(input_file, output_file) that takes as input two strings, input_file and output_file, 
which represent the paths to two files.
Inside the file indicated by input_file there is a single line containing a series of words 
(made up of alphabetic characters) separated by commas, spaces, semicolons, and periods.
The function must identify all the words contained in the file indicated by input_file and write 
them into a new file specified by output_file.
The words must be written in the file on a single line ending with a newline character, 
separated by a space, and ordered as follows:
by increasing number of characters,
if equal in length, in alphabetical order, regardless of case,
if the words are identical, in lexicographical order.
The function must return the number of words written to the output file.
Example: if the content of input_file is the following
Dog,cat,dog;Cat.bird car
the call
func4('input_file', 'output_file')
must write the following line inside output_file:
car Cat cat Dog dog bird
and return the value 6.
"""


def func4(input_file : str, output_file : str) -> int:
    # scrivi qui il tuo codice
    pass

# print(func4('func4/func4_test1.txt','func4/func4_out1.txt'))

################################################################################
## %% -------------------------------- FUNC.5 --------------------------------- #
################################################################################

""" func5: 6 punti
Define a function func4(input_filename, output_filename, length) that receives as arguments 
two strings representing two filenames and an integer.
The file input_filename contains a series of strings separated by spaces, tabs, or newlines.
The function must create a new text file named output_filename containing all the strings of 
length length found in the file input_filename, organized into lines.
The lines must be in alphabetical order.
The words in each line:
have the same initial letter, ignoring case
are separated by a space
are ordered alphabetically, ignoring case. In the case of identical words, they are ordered alphabetically.
The function must return the number of strings of the required length found in the input file.
Example
If the file 'func4_test1.txt' contains the following three lines:
cat bat rat
Condor baT
Cat cAr CAR
the function
func5('func5_test1.txt', 'func5_out1.txt', 3)
must write the following 3 lines into 'func5_out1.txt':
baT bat
CAR cAr Cat cat
rat

and returns 7.
"""


def func5(input_filename : str, output_filename : str, length : int) -> int:
    # scrivi qui il tuo codice
    pass

# print(func5('func5/func5_test1.txt', 'func5/func5_out1.txt', 3))

################################################################################
################################################################################
################################################################################
