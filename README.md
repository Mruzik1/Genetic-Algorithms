# Genetic Algorithms
Solving Traveling Salesman Problem using Genetic Algorithms to show how it actually works. Below are some descriptions of different types of mutations and crossovers.
Also I performed a few experiments applying different crossovers, mutations and variety of parameters while solving the TSP.


## Crossover Examples
Crossover is one of the most important things in Genetic Algorithms. This part of GA itself could be considered as an "evolution performer". There are several examples of crossovers with a portion of pseudocode and the pictures illustrating the process.


### Multi-Point Crossover
One of the common crossover types is Multi-Point Crossover or N-Point Crossover. Firstly we randomly separate parents into N+1 parts with N separators. Then carry genes from the first parent's odd parts, and from even parts of the second one. <br /><br />
<img src="https://i.imgur.com/0xRD34b.png" alt="MultiPoint" width="650" />


### Single-Point Crossover
Single-Point Crossover is just a special case of the previous crossover. <br /><br />
<img src="https://i.imgur.com/796Bytg.png" alt="SinglePoint" width="650" />


### Uniform Crossover
Carrying genes by literally tossing a coin. There is also a special case of Uniform Crossover named "Parameterized Uniform Crossover" with chances for every gene to be chosen. <br /><br />
<img src="https://i.imgur.com/OHP5uMF.png" alt="Uniform" width="650" />


### Cycle Crossover
This kind of crossover makes possible to work with chromosomes consisting of ordered genes (that mustn't be repeated). Good for solving problems with graphs such as Traveling Salesman Problem, Graph Coloring Problem, Vehicle Routing Problem, etc. The working principle is illustrated below. <br /><br />
<img src="https://i.imgur.com/u9JTXwR.png" alt="Cycle" width="650" />


### Partially Mapped Crossover
Has the same purpose as the previous one, even though works different. Firstly we are taking a random slice from the parents. Then carrying this part from the first parent to the offspring. After, from the parent two, all genes that are not in the both slices have to go to the offspring, too. And the most complicated part is to find indexes for the remaining genes that are ONLY in the SECOND parent's slice. The process is demonstrated on the picture below. <br /><br />
<img src="https://i.imgur.com/quoXkWr.png" alt="PMX" width="650" />
