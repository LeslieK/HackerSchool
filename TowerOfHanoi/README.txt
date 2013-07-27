Tower of Hanoi is the sample facebook puzzle. I solved it in June 2012, when I was just a python beginner.
1 year later, after taking an Algorithms course, I wanted to solve it by transforming the problem into a graph and applying breadth first search. The code I wrote 1 year ago was very hard for me to follow today. This code seems so much simpler.

Solution: 
>> run Hanoi.py   		(dependencies: GraphLib.py, BreadthFirstSearch.py)

Input is from StdIn:

>>> N K: 2 3			2 discs, 3 pegs (N = number discs, K = number of pegs)
>> initial: 1 1			disc 1: peg 1  disc 2: peg 1  (each position represents a disc; values represent peg)
>> final: 2 2 			disc 1: peg 2  disc 2: peg 2

Output:

>> 3  (minimum number of moves)
>> 1 3  				move from peg 1 to 3
>> 1 2 					move from peg 1 to 2
>> 3 2 					move from peg 3 to 2