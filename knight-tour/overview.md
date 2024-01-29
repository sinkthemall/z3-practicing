# KNIGHT TOUR PROBLEM OVERVIEW
My opinion about this problem:
-   Knight problem has multiple solution, but some solution require a little tricks, for example, if you use backtrack to solve, remember to make the knight' move order like this:
```
   1   8
2         7
     K
3         6
   4   5
```
The reason for this is because is obey the ```Warnsdorf's rule```, helping decrease the time for finding the path. If not, it will take more time to find the solution ( I did try to shuffle the order and the result is waiting for hour to find the path)
