Documentation
Name: Ruchita Paithankar 


move :- 
A Class to stores a move, 
A state function and is a main class which implements functions of the game.
After the moves are generated, the function returns list of moves
The opposite player then makes a move
Input: -- sh run.sh human human 
Output:
         


<img width="559" alt="output" src="https://user-images.githubusercontent.com/92649107/160254673-9f769c2c-4e75-41e6-86ff-5810a493e80e.png">









Random:
Moves are chosen by Othello at random
Input: -- sh run.sh random random
Output: 
<img width="578" alt="random" src="https://user-images.githubusercontent.com/92649107/160254683-ff958a84-9eee-4358-aec1-79b8bd5e6a9b.png">

       
II. Minimax
Minimax algorithm uses the score function provided in the state class.
The agent constructor accepts the depth.
Input:-- sh run.sh minimax random
Output:--  

      
<img width="552" alt="minimax" src="https://user-images.githubusercontent.com/92649107/160254689-5ff41b55-c9a9-4416-85d7-a44500d98eb0.png">


III.  Minimax + Alpha-beta pruning
Alpha-beta search uses the constructor to get the depth
Input:-- sh run.sh alphabeta random
Output:
  


<img width="549" alt="minimax+alpha beta" src="https://user-images.githubusercontent.com/92649107/160254700-4b1d8c9b-35a1-4ac4-8972-8248ff6d0665.png">


IV Extra credit
An output of amount of time required is received to do the search.
Input :-- sh run.sh extra random
Output :--  
<img width="528" alt="extra credit" src="https://user-images.githubusercontent.com/92649107/160254704-422bf03b-bf56-464f-9c3f-cd18f03baf8c.png">

 





