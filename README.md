# ReducedFiniteDimensionalModules

Code accompanying the paper: "Reduced submodules of finite dimensional polynomial modules".
Any object?? described or refered to here is defined and studied in the paper.

## Purpose
The purpose of this code is the aid of the study of reduced submodules of finite dimensional
polynomial modules. Let k be a field, R = k[x,y] and I be a monomial ideal of R. Consider
the module M = R/I. We wish to study the subset R(M) of M called the maximal reduced
submodule. A monomial ideal of R can be given by a Young diagram.

"main.py" provided takes as input a Young diagram and outputs generators for the
corresponding module M and for R(M). It also outputs which of the four possible types R(M)
is.

"data.py" file cycles through every possible module up to a given dimension and records the
distribution of the four types, saving the data.

The pictures.py file produces pictures of the Young diagrams associated with each of the 
modules and a picture which highlights the differences between M and R(M). This is to help
researchers consider many pictorial examples in order to gain quickly intuition.

## Usage
### main.py
Input taken as standard input as a decreasing sequence of positive integers seperated by a
space. For example:
```
Enter Young diagram in the form: * * ... *
>10 9 3 3 2 1
```
Output is given is the following form:
```
> Generators of M :  {(3, -2), (0, -6), (1, -5), (10, 0), (2, -4), (9, -1)}
> R(M) generators :  {(1, -4), (9, 0), (8, -1), (3, -2), (2, -3), (0, -5)}
> Type :  [0, 0, 1, 0]
```
Where a pair (a,-b) represents a monomial $x^ay^b$ and a 1 in the $i^{th}$ position means
type $i$ for $i = 1,...,4$.

In order to exit the programm type:
```
exit
```

### data.py
Input is given as maximum dimension to be tested. Then one eneters the name of the file
where the data will be saved. For example:
```
Enter the maximum dimension: 5   
Name file to save data under: data-test
```
In the file then is saved a file called "data-test.txt". It will have the following form:
```
Dim  T1         T2         T3         T4
2    100.0      0.0        0.0        0.0
3    66.67      33.33      0.0        0.0
4    40.0       40.0       20.0       0.0
5    28.57      28.57      42.86      0.0
~                                                                                                                                                             
                                                                                                                                                           
"data-test.txt" [noeol] 5L, 244C
```
In each collumn is the percentage share of that type of the given dimension.

### pictures.py
Input taken as standard input as a decreasing sequence of positive integers seperated by a
space. For example:
```
Enter Young diagram: 4 3 2 1
```
Ouput 
```

```

## References
[Reduced submodules of finite dimensional polynomial modules - Tilahun Abebaw, Nega Arega, Teklemichael Worku Bihonegn, Dominic Bunnett, David Ssevviiri]()
