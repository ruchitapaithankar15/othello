Documentation
Name: Ruchita Paithankar 
move :- 
A Class to stores a move, 
A state function and is a main class which implements functions of the game.
After the moves are generated, the function returns list of moves
The opposite player then makes a move
Input: -- sh run.sh human human 
Output:
         











Random:
Moves are chosen by Othello at random
Input: -- sh run.sh random random
Output: 
       
II. Minimax
Minimax algorithm uses the score function provided in the state class.
The agent constructor accepts the depth.
Input:-- sh run.sh minimax random
Output:--  

      


III.  Minimax + Alpha-beta pruning
Alpha-beta search uses the constructor to get the depth
Input:-- sh run.sh alphabeta random
Output:
  
















IV Extra credit
An output of amount of time required is received to do the search.
Input :-- sh run.sh extra random
Output :--  
 





