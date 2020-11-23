# Composing Mozart Variations with Dice Code
### Eva Burns

## Description
There are three different python codes to simulate results for creating a piece of music using Mozart's dice game.

#### [brute_force.py](../main/brute_force.py)

Calculates the total number of ways to create a piece of music of n bars using a brute force method.  The program will ask you how many bars you would like to use.  Note: when n >= 10, the run time will be slow, so the program will prompt you if you would like to proceed with the program.

#### [algorithm.py](../main/algorithm.py)

Calculates the total number of ways to create a piece of music of n bars using the algorithm I calculated.  The program will ask you how many bars you would like to use.

#### [prob.py](../main/prob.py)
Creates a graph called plot.png that will show the distribution of dice rolls and the probability that a number x will be rolled by two dice.

## How to Run
First make sure that python (and pip) is installed.  Then, open a terminal.
1. Install requirements: 
``` console
pip install -r requirements.txt
```
or 
``` console
pip3 install -r requirements.txt
```
if you have python 3.

2. Run the code:
``` console
python brute_force.py
python algorithm.py
python prob.py
```
or
``` console
python3 brute_force.py
python3 algorithm.py
python3 prob.py
```
