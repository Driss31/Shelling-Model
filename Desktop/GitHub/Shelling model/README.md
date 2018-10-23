*Description*

Model of racial segregation: Shelling's model.
It shows that relatively mild preference for neighbors of similar race can lead to the collapse of mixed neighborhoods,
and high levels of segregation

Script' stages:

1. We start from a perfectly mixed neighborhood
2. We disturb this perfect distribution :
    - We remove a number of citizens chosen randomly
    - We add a number of citizens (chosen randomly) in some of the empty houses
3. We define conditions of satisfaction. Depending of the number of neighbors, each citizen wants at least a certain
number of same color skin neighbors
{[number of neighbors] : number of minimum same color skin neighbors needed
{[1, 2] : 1
{[3, 4, 5] : 2
{[6, 7, 8] : 3
4. We move unsatisfied citizens to empty space where they can be satisfied


*Process*

1. We create a matrix containing 1 and -1 alternately distributed.
2. We randomly remove a number (r) of '1' and '-1'. Replace them by 0 in the matrix
3. We randomly add a number ( < r) of '1' and '-1' where we have 0 in the matrix
4. We define conditions of satisfaction
5. We look for an unsatisfied '1' or '-1'
6. We look for an empty space where it can be satisfied
7. We put an '1' or '-1' (depending or 5.) where there is a '0' (depending on 6.) and a '0' where there was that '1'
or '-1'
