# ethnic-residential-dynamics
[![CircleCI](https://circleci.com/gh/Driss31/nlp-negative-sampling.svg?style=svg)](https://circleci.com/gh/Driss31/nlp-negative-sampling)
[![Python: 3.8.2](https://img.shields.io/badge/python-3.8.2-blue.svg)](https://www.python.org/downloads/release/python-381/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

I implemented the [Schelling Model of Ethnic Residential Dynamics.](http://jasss.soc.surrey.ac.uk/15/1/6.html)

The model was introduced by Thomas Schelling to illustrate how individual incentives and individual perceptions of difference can lead collectively to segregation.


### _*Description*_

Model of racial segregation: Shelling's model.
It shows that relatively **mild preference** for neighbors of similar race can lead to the collapse of mixed neighborhoods,
and high levels of segregation

### **Script' stages:**

1. Start from a perfectly mixed neighborhood
2. Disturb this perfect distribution :
    - Remove a number of citizens chosen randomly
    - Add a number of citizens (chosen randomly) in some of the empty houses
3. Define conditions of satisfaction. Depending of the number of neighbors, each citizen wants at least a certain
number of same color skin neighbors
```
{[number of neighbors] : number of minimum same color skin neighbors needed
{[1, 2] : 1
{[3, 4, 5] : 2
{[6, 7, 8] : 3
```
4. Move unsatisfied citizens to empty space where they can be satisfied


### **Process**

1. Create a matrix containing 1 and -1 alternately distributed.
2. Randomly remove a number (r) of '1' and '-1'. Replace them by 0 in the matrix
3. Randomly add a number ( < r) of '1' and '-1' where we have 0 in the matrix
4. Define conditions of satisfaction
5. Look for an unsatisfied '1' or '-1'
6. Look for an empty space where it can be satisfied
7. Put a '1' or '-1' (depending or 5.) where there is a '0' (depending on 6.) and a '0' where there was that '1'
or '-1'
