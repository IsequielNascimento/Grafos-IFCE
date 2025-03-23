# Minimal-Generator-Tree
### Graphs activity that aims to exercise Kruskal's algorithm with an implementation in a problem from the Brazilian Computer Olympics.

# Copa do Mundo

Nlogonia is currently one of the fastest-growing countries in the world, and its rulers have been working hard to make the country better known and respected internationally. Nlogonia was recently chosen to host the Amateur Football World Cup, and is preparing to welcome the thousands of fans that the event attracts.

As part of the preparations for the World Cup, the government plans to overhaul the entire intercity transportation system, which is currently made up of a network of roads and railroads, each road or railroad connecting a pair of cities. With the existing roads and railroads it is already possible to travel between any pair of cities (possibly passing through other cities on the way), but the government wants to offer better transportation conditions for visitors and the population.

As there aren't enough resources to renovate all the roads and railroads, the government wants to choose a set of roads and railroads to be renovated, and has already carried out a study to establish the cost of renovating each road and railroad. The choice must comply with the following criteria:

1. At the end of the reform, it should be possible to travel between any pair of cities (possibly passing through other cities) using only reformed roads or railroads;
2. In order to prioritize public transport, among the choices that satisfy constraint 1, one must be chosen that minimizes the number of reformed roads;
3. Among the choices that satisfy constraints 1 and 2, choose one that minimizes the total cost.

You have been hired to write a program that, knowing the costs of renovating each road and railroad, determines the lowest possible cost for the renovation, given the established criteria.

## Input

The first line of the input contains three integers N, F and R, indicating the number of cities, railroads and highways respectively. Cities are identified by integers from 1 to N. Each of the following F lines describes a railroad and contains three integers A, B and C, where A and B represent cities and C represents the cost of renovating the railroad that connects A and B. Each of the following R lines describes a highway and contains three integers I, J and K, where I and J represent cities and K represents the cost of renovating the highway that connects I and J.

## Output

Your program must produce a single line, containing the lowest possible cost for the set of railroad and highway renovations, obeying the established criteria.

## Constraints

- \( 2 \leq N \leq 100 \)
- \( 1 \leq F \leq N(N-1)/2 \)
- \( 1 \leq R \leq N(N-1)/2 \)
- \( 1 \leq A < B \leq N \) and \( 1 \leq I < J \leq N \)
- \( 1 \leq C \leq 1000 \) and \( 1 \leq K \leq 1000 \)

## Score information

For a set of test cases totaling 20 points, \( 2 \leq N \leq 6 \).

## Examples

### Example 1

**Input**

3 3 2
1 2 1000
1 3 1000
2 3 900
1 3 800
2 3 700


**Output**

1900


### Example 2

**Input**

5 4 5
3 4 300
1 2 100
2 4 300
1 3 250
4 5 600
3 4 200
2 3 100
2 5 400
1 5 450


**Output**

1050


### Example 3

**Input**

5 2 3
4 5 60
2 3 60
1 2 50
1 4 50
3 4 50


**Output**

220