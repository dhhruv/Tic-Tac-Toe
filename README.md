
![Tic Tac Toe GUI Image](https://user-images.githubusercontent.com/72680045/109675782-1ad2bd80-7b9e-11eb-944e-3bac501a694c.PNG)

## Introduction
To solve games using AI, we will introduce the concept of a Game Tree followed by Minimax algorithm. This algorithm sees a few steps ahead and puts itself in the shoes of its opponent. It keeps playing ahead until it reaches a terminal arrangement of the board (terminal state) resulting in a tie, a win, or a loss. Once in a terminal state, the AI will assign an arbitrary positive score (+10) for a win, a negative score (-10) for a loss, or a neutral score (0) for a tie.

At the same time, the algorithm evaluates the moves that lead to a terminal state based on the players’ turn. It will choose the move with maximum score when it is the AI’s turn and choose the move with the minimum score when it is the human player’s turn. Using this strategy, Minimax avoids losing to the human player.

## What is Minimax?
**Minimax** (sometimes MinMax, MM or saddle point) is a decision rule used in artificial intelligence, decision theory, game theory, statistics, and philosophy for minimizing the possible loss for a worst case (maximum loss) scenario. When dealing with gains, it is referred to as **"maximin" - to maximize the minimum gain**. Originally formulated for n-player zero-sum game theory (one player wins (+10) and other player loses (-10) or both of anyone not to win (0)), covering both the cases where players take alternate moves and those where they make simultaneous moves, it has also been extended to more complex games and to general decision-making in the presence of uncertainty. 

## How does it work?
To check whether or not the current move is better than the best move we take the help of minimax function which will consider all the possible ways the game can go and returns the best value for that move, assuming the opponent also plays optimally until it finds a terminal state (win, draw or lose).

## Game Tree

### Image: 

![Game Tree Image](https://user-images.githubusercontent.com/72680045/109675821-232af880-7b9e-11eb-9062-99cc212692ee.jpg)

### Explanation:

This image depicts all the possible paths that the game can take from the root board state. It is often called the Game Tree. 
The 3 possible scenarios in the above example are : 
 
-	Left Move : If X plays [2,0]. Then O will play [2,1] and win the game. The value of this move is -10
-	Middle Move : If X plays [2,1]. Then O will play [2,2] which draws the game. The value of this move is 0
-	Right Move : If X plays [2,2]. Then he will win the game. The value of this move is +10;

**Remember, even though X has a possibility of winning if he plays the middle move, O will never let that happen and will choose to draw instead.**
Therefore the best choice for X, is to play [2,2], which will guarantee a victory for him.