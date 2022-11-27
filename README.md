# Genetic Algorithms
Solving Traveling Salesman Problem using Genetic Algorithms to show how it actually works. Below are some descriptions of different types of mutations and crossovers.
Also I performed a few experiments applying different crossovers, mutations and variety of parameters while solving the TSP.


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
