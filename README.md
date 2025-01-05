# Collatz
This script was created with the intent of visualizing what the progression of numbers looks like under the Collatz Conjecture.

I took inspiration on the following video for this project: [The Simplest Math Problem No One Can Solve - Collatz Conjecture ](https://www.youtube.com/watch?v=094y1Z2wpJg)

<sub>_PS: This project is not a "solution for the unsolvable problem". It is simply a visualizer._</sub>
## Installation
```
pip -r requirements.txt
```
## Configuration
Create a file called .env and insert the following contents
```
PLT_GRAPH=1 #Creates MatplotLib window
OUT_CONSOLE=0 #Outputs result on console
OUT_JSON=1 #Outputs result on json
```
If config file is not created, the script will automatically create it for you.
## Usage
```
python main.py <value:Integer>
python main.py 3
```

## Rules
Number must be positive <sub>_(Above 0)_</sub>
If number is even, it will be divided by 2
If number is odd, it will be multiplied by 3 and have a 1 added to it, which will make it even.

| Number Type | Method |
|-------------|--------|
|     Even    |   ÷2   |
|     Odd     |  3x+1  |

This will happen in a cycle until the formula reaches the following final numbers: _4,2,1_

## Sources
Youtube: [The Simplest Math Problem No One Can Solve - Collatz Conjecture](https://www.youtube.com/watch?v=094y1Z2wpJg)

Wikipedia: [Collatz conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture)

