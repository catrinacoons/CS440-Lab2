# CS440-Lab2

Update the vacuum cleaner to use a hill-climbing strategy.

 

Assume the vacuum cleaner has a specific function to locate hard-to-reach, dirty areas. The dirt level in these locations ranges from 0 to 10. Your goal is to implement a function that identifies the dirtiest spot in the environment. To do this, the environment must be expanded to a 4x4 grid. The vacuum moves in four directions following the hill-climbing algorithm. Display a record of the path taken by the vacuum.

Environment initial setup.

0	3	2	start
0	0	0	0
0	4	6	8
7	9	0	10
 

Update the robot to use a simulated annealing function. Explain how you choose the objective function and the cooling rate. Display a log of the path taken by the vacuum cleaner.

Environment initial setup.

0	3	2	start
3	6	0	0
5	0	6	8
4	9	0	10
