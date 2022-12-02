# Genetic Algorithms
Solving Traveling Salesman Problem using Genetic Algorithms to show how it actually works. Below are some descriptions of different types of mutations and crossovers.
Also I performed a few experiments applying different crossovers, mutations and variety of parameters while solving the TSP.

<br />


# Crossover Examples
Crossover is one of the most important things in Genetic Algorithms. This part of GA itself could be considered as an "evolution performer". There are several examples of crossovers with a portion of pseudocode and the pictures illustrating the process.


## Multi-Point Crossover

### Brief Description
One of the common crossover types is Multi-Point Crossover or N-Point Crossover. Firstly we randomly separate parents into N+1 parts with N separators. Then carry genes from the first parent's odd parts, and from even parts of the second one. <br /><br />
<img src="https://i.imgur.com/0xRD34b.png" alt="MultiPoint" width="650" />

### Pseudocode
<pre>
<b>SET</b> <i>old_separator</i> <b>TO</b> <i>0</i>
<b>SET</b> <i>offspring</i> <b>TO</b> <i>empty sequence</i>

<b>FOR</b> <i>from 0 to the separators_count-1</i>:
    <b>SET</b> <i>new_separator</i> <b>TO</b> <i>random number from old_separator+1 to parents_length-separators_count+current_separator_number</i>
    
    <b>IF</b> <i>current_separator_number is odd</i>:
        <b>CONCATENATE</b> <i>offspring</i> <b>WITH</b> <i>slice of the second parent from old_separator to new_separator-1</i>
    <b>ELSE</b>:
        <b>CONCATENATE</b> <i>offspring</i> <b>WITH</b> <i>slice of the first parent from old_separator to new_separator-1</i>
    
    <b>SET</b> <i>old_separator</i> <b>TO</b> <i>new_separator</i>
 
<b>IF</b> <i>separators_count is odd</i>:
    <b>CONCATENATE</b> <i>offspring</i> <b>WITH</b> <i>slice of the second parent from old_separator</i>
<b>ELSE</b>:
    <b>CONCATENATE</b> <i>offspring</i> <b>WITH</b> <i>slice of the first parent from old_separator</i>
</pre>


## Single-Point Crossover

### Brief Description
Single-Point Crossover is just a special case of the previous crossover. <br /><br />
<img src="https://i.imgur.com/796Bytg.png" alt="SinglePoint" width="650" />

### Pseudocode
<pre>Uses the function of Multi-Point Crossover</pre>


## Uniform Crossover

### Brief Description
Carrying genes by literally tossing a coin. There is also a special case of Uniform Crossover named "Parameterized Uniform Crossover" with chances for every gene to be chosen. <br /><br />
<img src="https://i.imgur.com/OHP5uMF.png" alt="Uniform" width="650" />

### Pseudocode
<pre>
<b>SET</b> <i>mask</i> <b>TO</b> <i>random sequence of numbers from 0 to 1 with length equals the parents length</i>
<b>SET</b> <i>offspring</i> <b>TO</b> <i>empty sequence</i>

<b>FOR</b> <i>each element of the mask</i>:
    <b>IF</b> <i>mask_element is 1</i>:
        <b>APPEND</b> <i>element of the second parent with a mask_element's index</i> <b>TO</b> <i>offspring</i>
    <b>ELSE</b>:
        <b>APPEND</b> <i>element of the second parent with a mask_element's index</i> <b>TO</b> <i>offspring</i>
</pre>


## Cycle Crossover

### Brief Description
This kind of crossover makes possible to work with chromosomes consisting of ordered genes (that mustn't be repeated). Good for solving problems with graphs such as Traveling Salesman Problem, Graph Coloring Problem, Vehicle Routing Problem, etc. The working principle is illustrated below. <br /><br />
<img src="https://i.imgur.com/u9JTXwR.png" alt="Cycle" width="650" />

### Pseudocode
<pre>
<b>SET</b> <i>used_genes</i> <b>TO</b> <i>empty sequence</i>
<b>SET</b> <i>cycles</i> <b>TO</b> <i>empty sequence</i>
<b>SET</b> <i>offspring</i> <b>TO</b> <i>empty sequence</i>

<b>FOR</b> <i>each element of the parent one</i>:
    <b>IF</b> <i>parent's element is not in the used_genes</i>:
        <b>SET</b> <i>cycle</i> <b>TO</b> <i>sequence of two elements: parent_one_element with current index, parent_two_element with current index</i>
        
        <b>WHILE</b> <i>first cycle's element is not equal to the last cycle's element</i>:
            <b>APPEND</b> <i>element of the second parent with an index of the last cycle's element in the first parent</i> <b>TO</b> <i>cycle</i>
            
        <b>SET</b> <i>cycle</i> <b>TO</b> <i>cycle without the last element</i>
        <b>APPEND</b> <i>cycle</i> <b>TO</b> <i>cycles</i>
        <b>CONCATENATE</b> <i>used_genes</i> <b>WITH</b> <i>cycle</i>
        
<b>FOR</b> <i>each element of the both parents</i>:
    <b>IF</b> <i>an element of the parent one is in an odd cycle</i>:
        <b>APPEND</b> <i>second parent's element</i> <b>TO</b> <i>offspring</i>
    <b>ELSE IF</b> <i>an element of the parent one is in an even cycle</i>:
        <b>APPEND</b> <i>first parent's element</i> <b>TO</b> <i>offspring</i>
</pre>


## Partially Mapped Crossover

### Brief Description
Has the same purpose as the previous one, even though works different. Firstly we are taking a random slice from the parents. Then carrying this part from the first parent to the offspring. After, from the parent two, all genes that are not in the both slices have to go to the offspring, too. And the most complicated part is to find indexes for the remaining genes that are ONLY in the SECOND parent's slice. The process is demonstrated on the picture below. <br /><br />
<img src="https://i.imgur.com/quoXkWr.png" alt="PMX" width="650" />

### Pseudocode
<pre>
<b>SET</b> <i>subset</i> <b>TO</b> <i>randomly chosen slice of the parents</i>
<b>SET</b> <i>offspring</i> <b>TO</b> <i>sequence (the length equals parents length) with carried subset from the first parent; remaining elements are all equal to 0's</i>

<b>FOR</b> <i>each element of the parent two</i>:
    <b>SET</b> <i>new_index</i> <b>TO</b> <i>current_index</i>
    
    <b>IF</b> <i>the second parent's element is not in the offspring</i>:
        <b>IF</b> <i>the second parent's element is in the subset</i>:
            <b>WHILE</b> <i>new_index is in the subset</i>:
                <b>SET</b> <i>new_index</i> <b>TO</b> <i>index of the element in the second parent that is equal to the same element in the first parent at new_index</i>
                
    <b>SET</b> <i>offspring's element at new_index</i> <b>TO</b> <i>current element of the parent two</i>
</pre>

<br />


# Mutation Examples
Unlike crossovers, mutations are "avoidable". In other words, theoretically a genetic algorithm can still work without them. But the results are going to be far worse. As without an entropy (that every single mutation brings) the algorithm will stuck in a local optima. Mutations usually have a low chance to be used on an offspring to keep some stability. Below are pictures illustrating the mutations I used while implementing the TSP solver (since it's pretty easy without pseudocode).

## Replacement Mutation
<img src="https://i.imgur.com/OW10fa4.png" alt="Replacement" width="650" />


## Inversion Mutation
<img src="https://i.imgur.com/zq7MDc0.png" alt="Inversion" width="650" />

<br />


# Additional Info
## What My Implementation Can Solve
The algorithm I created (genetic_algorithm.py, mutation.py and crossover.py are universal) can only solve minimization problems with ordered genes (TSP, GCP, VRP, etc).

## Parents Selection
There are different ways to select parents such as: <i>Roulette Wheel Selection, Stochastic Universal Sampling, Tournament Selection, etc</i>. In my implementation I use the first one - Roulette Wheel Selection. According to the name, it functions like a roulette wheel where a probability for every chromosome has following formula: <br />
<img src="https://latex.codecogs.com/png.image?\dpi{110}\bg{black}p_{i}&space;=&space;\frac{f_{i}^{-1}}{\sum_{j=1}^{N}f_{j}}" alt="Probability formula"/> <br />
Where N is a total population size, and <img src="https://latex.codecogs.com/png.image?\dpi{110}\bg{black}f_{i}" alt="fi"/> is a fitting score of a chromosome <img src="https://latex.codecogs.com/png.image?\dpi{110}\bg{black}c_{i}" alt="ci"/> from the whole population. And since we have a minimization problem, it's important to raise the fitting score to -1.

<br />


# How to use
## TSP module
The TSP module's main class is `NodesGenerator`. It provides a few tools for working with the problem:
- `__init__`<br />Has one required argument `count` and one optional `saved_axis`. The first one is just a nodes count (makes sense only if saved_axis is False or is not provided). And the second one is a boolean value that defines whether you already generated nodes or not. If False, it generates new nodes according to the count and saves their distances and axis to the data folder for subsequent use. If True, it uses already mentioned files.
- `get_nodes_list`<br />Just returns a list consisting of the `Node` objects (a `Node` object simply has handy methods such as finding a distance between two nodes, and so on). String representation of each node is just a number of a node.
- `total_cost`<br />Requires a list of the `Node` objects as an argument. Returns total cost of the way.
- `draw_path`<br />Requires a list of the `Node` objects as an argument. Draws a graph with connected nodes in accordance with a nodes order.

## GA module
- `CrossoverType`<br />
    Contains different types of a crossover:
    - `MULTI_POINT`
    - `SINGLE_POINT`
    - `UNIFORM`
    - `CYCLE`
    - `PMX`
- `MutationType`<br />
    Contains different types of a mutation:
    - `REPLACEMENT`
    - `INVERSION`
- `Crossover`<br />
    - `__init__`<br />Requires one argument - `crossover_type`.
    - `preform`<br />Has two required arguments: `parent1` (list), `parent2` (list), and one optional - `points` (should be provided only while performing a `MULTI_POINT` crossover). Returns an offspring from both parents.
    - `set_type`<br />Exists as a setter for a new type, requires one argument `new_type`.
- `Mutation`<br />
    - `__init__`<br />Requires two arguments: `chance` (a chance of the mutation, from 0 to 1) and `mutation_type`.
    - `preform`<br />Has one required argument `offspring` (list). Returns mutated (with some chance) `offspring`.
    - `set_type`<br />Exists as a setter for a new type, requires one argument `new_type`.
- `GeneticAlgorithm`<br />
    - `__init__`<br />Requires four arguments: `mutation_chance`, `crossover_type`, `mutation_type`, and `fitness_function` (a function that returns a score of a single chromosome, in our case it is `total_score` from `NodesGenerator`)
    - `init_population`<br />Requires two arguments: `k` (a size of the population) and `initial_chromosome` (some chromosome that will be shuffled to create different population members). Don't need to be called if you want to continue a life of the population.
    - `start`<br />Requires two arguments: `k` (time of the population's living / an amount of evolutional steps) and `selector` (how many chromosomes will die and be replaces by offsprings during the selection process). Starts an evolution, prints a process of the evolution, fills a `history`. Returns a chromosome with the best result.
    - `history`<br />A @property method that returns a history of the evolving (gotten after the `start` was successfully executed).

<br />


# Experiments
## Experiment 1
GAs with two different mutation chances (one has 100%, another has only 10%).
### Replacement
- Initial parameters<br />
<img src="https://i.imgur.com/tBnIMJN.png" width="700"/>
- An outcome<br />
<img src="https://i.imgur.com/LPO50lh.png" width="700"/>
- Conclusion<br />
The plot with 100% chance is extremely spiky, unlike the one with a mutation chance of 8% which is pretty stable. The best result from the first algorithm is 155, and from the second one is 136. I think it is obvious which GA evaluates better. Additionaly you can see some kind of "stairs" on the second plot. And, on other hand, the plot with 100% chance is like a slide.

### Inversion
- Initial parameters<br />
<img src="https://i.imgur.com/Ij1miX3.png" width="700"/>
- An outcome<br />
<img src="https://i.imgur.com/i9gZDX2.png" width="700"/>
- Conclusion<br />
An outcome gotten by using Inversion is way more smooth comparing to the replacement method. In other words Replacement brings more chaos to our data. The conclusion is similar as the previos one has.

## Experiment 2
GA with a 0% mutation chance.
- Initial parameters<br />
<img src="https://i.imgur.com/tLm4iof.png" width="700"/>
- An outcome<br />
<img src="https://i.imgur.com/jHmEZR0.png" width="700"/>
- Conclusion<br />
As you can see the blue line is descending as fast as the orange one, but suddenly starts going straight. It means that we gotten stuck in a local optima due to the lack of entropy in the population. The answer won't change anymore, respectively it won't become better.