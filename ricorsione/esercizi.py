"""
Ex1: 6 punti

Definire la funzione ex1(stringa, l), ricorsiva o che utilizza funzioni o metodi ricorsivi,
che prende in ingresso una stringa e un intero l e restituisce
l'insieme di tutti i possibili anagrammi di lunghezza l senza alcun carattere
doppio che possono essere costruiti con i caratteri della stringa.
Se l è maggiore della lunghezza della stringa, l'insieme restituito è vuoto.

Esempio:
    ex1('aabca', 4) should return the set
    {'acba', 'caba', 'acab', 'abac', 'abca', 'baca'}

"""
import os

def ex1(string, l):
    ## Scrivi qui il tuo codice
    pass

# print(ex1('aabca', 4)) # {'acba', 'caba', 'acab', 'abac', 'abca', 'baca'}
# print(ex1('aabca', 5)) # {'abaca', 'acaba'}

"""
Ex1: 6 points
Definire la funzione ex1(chars, l), ricorsiva o che utilizza funzioni o
metodi ricorsivi, che prende in input un insieme di caratteri (ovvero 
stringhe di lunghezza uno) e un int l e restituisce l'insieme di tutte
le possibili stringhe palindrome di lunghezza l composte da caratteri
presi da chars.

Esempio:
    ex1({'a', 'b', 'c'}, 3) deve ritornare il set
    {'aaa', 'bab', 'cac', 'aba', 'bbb', 'cbc', 'aca', 'bcb', 'ccc'}

"""
def ex1(chars, l):
    ## Scrivi qui il tuo codice
    pass

'''
Ex2: 8 punti
Si scriva una funzione ricorsiva ex2(nums, ops), oppure una che usi
altre funzioni ricorsive, che prende in ingresso un set di numeri
interi positivi 'nums' e una lista di stringhe 'ops' che indicano
delle operazioni sui numeri. La funzione deve generare ricorsivamente
tutte le possibili espressioni aritmetiche, dove ciascuna espressione
e' una stringa. Le espressioni derivano dalla unione di due
o più numeri presi da 'nums' mediante operazioni del set 'ops', usando
le regole seguenti:

1. una volta che un numero e' usato nell'espressione, non puo' piu' essere usato
   Esempio:
     se nums={5,8,0} e ops=['+','*']
     '8+5+0' e' un'espressione valida ma '8+5+8' non lo e'.

2. le operazioni possono essere riutilizzate a piacimento quante volte si vuole.
   Nell'esempio precedente '8+5+0', infatti, il '+' e' stato usato 2 volte.

La funzione torna un set con tutte le espressioni generate.

Esempio: nums={5,8,0} e ops=['+','*'] la funzione deve generare il set:
{'8*5*0', '5+0+8', '5+0*8', '0+5+8', '0+8+5', '8+5*0', '0+5*8',
'0*8*5', '0*8+5', '8+5+0', '5*0*8', '8+0*5', '5*8+0', '5*0+8',
'5+8+0', '8*0+5', '0*5*8', '0+8*5', '8*5+0', '8*0*5', '5*8*0',
'5+8*0', '0*5+8', '8+0+5'}

NOTA: NON  definite la funzione ricorsiva interamente a ex2() altrimenti
non passate il test ricorsivo.
NOTA: consigliamo fortemente di dividere l'esercizio in sottoproblemi
dividendo in funzioni per ogni sottoproblema.
'''


def ex2(nums, ops):
    # scrivi qui il tuo codice
    pass

"""
Ex1: 6 punti
Si scriva una funzione ricorsiva ex1(root), o che al suo interno usi
una funzione ricorsiva, che prende in ingresso una stringa che punta ad una
directory e ricorsivamente esplori l'albero delle directory e restituisca un
dizionario. La chiave del dizionario e' il percorso assoluto a partire
dalla 'root', sottoforma di stringa.  Il valore corrisponde ad una
stringa così fatta: considerando una directory trovata, si prendano
soltanto i file in QUELLA directory con estensione ".txt", ordinati
in maniera alfabetica.  I file .txt sono file testuali dove su ogni
riga vi e' una serie di numeri interi seguiti solo da uno spazio. A
esempio 'ex1_A/XYCwdkCokL.txt' contiene:

75 84 84 73 83
76 74 76

Si legga sequenzialmente all'alto al basso, da sinistra a destra,
ciascun numero, lo si interpreti come valore Unicode, convertendolo
in un carattere e lo si concateni con il carattere successivo.

Ad esempio la sequenza suddetta e' convertita nella stringa "KTTISLJL".

Il valore nel dizionario e' la stringa che si ottiene
concatenando le stringhe generate per ogni file testuale per quella
directory, secondo l'ordine alfabetico dei file.txt.

Se la directory non contiene nessun file .txt allora quella directory
non appare nel dizionario.

Se la funzione e' chiamata su 'ex1_A', ritorna:

{'ex1_A/bkLbD': 'A\x9eŻĂĳŜǖ', 'ex1_A': 'KTTISLJL'}

NOTA: e' proibito usare la funzione os.walk. Si possono usare:
os.listdir, os.path.isfile, os.path.exists, etc.
Per concatenare i path, si usi l'operazione di concatenazione con il carattere '/'

NOTA: consigliamo fortemente di dividere l'esercizio in sottoproblemi
dividendo in funzioni per ogni sottoproblema.
"""

import os


def ex1(root):
    # scrivi qui il tuo codice
    pass