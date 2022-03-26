# othello
Othello [https://youtu.be/xDnYEOsjZnM] is a 2-player adversarial game in which a  player places pieces into a grid and tries to align them in order to win the game: 

<img width="224" alt="game" src="https://user-images.githubusercontent.com/92649107/160254402-6313478e-b087-43fd-b9ab-1698fd862ffb.png">


The object is to have the majority of your colored disks face up on the board at the end of  the game. Every disk is white on one side and black on the other. 
Setup: Initially, we place four disks, two with white sides and two with black sides up in  the center of the board. Each player has 30 disks. One player plays as white and the other  as black. The player playing black goes first, and then turns alternate. 
Play: On your turn, you must place one disk on any empty space on the board and outflank  your opponent. Outflank means to have your disks on either side of a continuous straight  line of your opponent's disks. This line can be any number of disks long and can be  horizontal, vertical, or diagonal. When you place a disk so that you have outflanked your  opponent's disks, you then flip the outflanked disks over to your color. You are allowed to  outflank multiple lines in a single turn. 
If you cannot outflank your opponent on your turn, you are not allowed to play, and you  must skip your turn. If you can play, then you must play. Disks may only be outflanked due  to a move and must be in a direct line of the placed disk. An outflank may not skip over  your own colored disk to outflank more disks. Only the disks within the immediate  outflank are captured. 
All outflanked disks must be flipped. You may not choose only to flip some of them. If you  flip over the wrong disk and your opponent hasn't moved yet, you may fix the error. If  your opponent has already moved, then you may not fix the error. Once a disk is placed on  a square, it may never be removed, nor maybe it be moved to another square. If you run  out of disks to place, and you still have a legal move, then your opponent must give you  some of theirs to use. When it is no longer possible for either player to move, the game is  over. Disks are counted, and the player with the majority of their color showing is the  winner. 
You can also play multiple rounds and track points. The round winner receives points  equal to the difference between the number of their opponent's disks, subtracted from the  number of their disks. Once players reach a predetermined point total, the game ends, and  the player with the most points is the winner. 



The Assignment: In this assignment, we use the minimax algorithm to make an AI  agent that plays the game of Othello. You are given the code to represent the board, handle  the placement of pieces, and determine whether the game is over. Your task will be to  extend this code into a full-fledged agent that can play and win the game. The code for this assignment should runs with a shell script.


Implementation Setup 
The various parts of this assignment will require a shell script that can pass an argument  to your code—thus allowing you to use the python3 command on tux while allowing us to  be able to run your code with a consistent interface. Again, you may only use built-in  standard libraries (e.g., math, random, etc.); you may NOT use any external libraries  or packages. 
The shell script is including the  ability to accept two arguments in the general format: 
sh run.sh <argument> 
This scheme will allow you to test your code thoroughly and also allow us to test  your code using a variety of arguments. 
A sample shell script run.sh has been provided with this assignment. You should not need  to modify this script file. 
  
  

Game Implementation 
Also provided with this assignment is the Python game implementation of the game. You  can test it by running the command: 
sh run.sh human human, which should run a game where both players are humans and generate moves from the  input command line. 
You can assume for this assignment that the two players are represented by 'X' and 'O'.  Most importantly, the Othello implementation is structured as follows: 
• “OthelloMove”: this class contains stores a "move" (which player made the move  and the coordinates of the move) 
• “State”: this is the core class, which implements most of the functionality of the  game. The functions you should be aware of for implementing minimax are: 
  o “generateMoves”: this function returns the list of moves for the next player  to move. 
  o “applyMoveCloning”: this function creates a new game state that has the  result of applying move 'move'. 
• “Player”: this is an abstract class defining an agent that player Othello. Your agent  should be implemented as a class that extends this one. 
• “game”: this class uses all the above classes to play a game of Othello. 
  
Part 1: Random
For the first part of the assignment, implement an agent that plays Othello by choosing  moves at random. You can test it by running the command: 
sh run.sh random random
  
Part 2: Minimax
In this part, we are asking you to Implement an agent that playes Othello using the  standard minimax algorithm. 
For the evaluation function, just use the "score" function that is provided to you in the  State class (make sure that your bot can play both as the first or second player). Your  agent's constructor should accept the depth up to which we want to search. 
To make sure your agent works, make it play against the random agent. Your agent should  defeat it easily! We should be able to test it by running the command:  
sh run.sh minimax random <depth> 
  
Part 3: Minimax + Alpha-Beta Pruning
Implement a third agent, which uses alpha-beta search. Again, your agent's constructor  should accept the depth up to which we want to search. Compare the times that your two  agents take to search up to different depths and report it in the PDF document. 
We should be able to test it by running the command: 
sh run.sh alphabeta random <depth> 
  
Part 4: Extra Credit
Implement another agent, this agent, instead of receiving the depth at which to perform a search,  receives a certain amount of time (in milliseconds) that it can use to search. Make sure  that your bot returns a solution within this time (you can assume that at least you will  have 100 milliseconds). 
We should be able to test it by running the command: 
sh run.sh extra random <time> 
Hint: a good way to do this is by making your agent first search at depth 1. Then, if there is  still time, search at depth 2. If there is still time, go for depth 3, etc. Also, make sure that  you have a code that cancels the search if enough time has passed. 
We might collect all the agents that comply with this and play a tournament. Results will  be announced in class in the case. 



