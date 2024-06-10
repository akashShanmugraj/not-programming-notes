## Blackbox Testing: 
1. Boundary Value Analysis
2. Equivalence Partitioning 
3. Graph Based
4. Comparison Testing
5. Orthogonal Array Testing

Errors related to interface, data structure, database initialization, termination and performance are found during Black Box testing

Boundary Value Analysis
- when input condition is bounded by a range a,b
- test cases are a, b and one value above and below a and b

Equivalence Partitioning
- divides input domain into classes of data from with test cases can be generated 
- aims to find testcase that uncovers a major class 

Comparison Testing
- when multiple values have the same implementation
- test cases from BBT are given to all these implementations and output is compared

Graph based Testing
- nodes are objects
- edges are links
- edge weights are characteristics of a link
- node weights are properties of objects
- directed links (unidirectional, bidirectional)
- parallel links


## Testing Strategies

- Constructing a program while also building it at the same time
- Integration testing focuses on design and construction of software architecture 
- BBT techniques are more prevalent but some WBT is used for better coverage

There are four types of testing strategies in incremental testing
1. Big Bang Testing
2. Incremental
	1. Top Down
	2. Bottom Up 
	3. Sandwich
3. Regression 
4. Smoke

Big Bang:
- all components are combined, entire program is tested as a whole
- chaotic results, unrelated errors

Incremental - Top Down
- modules are integrated by moving down on the control hierarchy
- DFS or BFS for subordinate modules
- Tests major control flow decisions early on 
- Stubs needed for modules that are not completed 

Incremental - Bottom Up
- integration from the most atomic modules
- no need for stubs because low level data is tested first and earler
- driver modules are need to call and test low level code

Incremental - Sandwich
- combines both Top Down and Bottom Up
- high and low level modules grouped based on control and data processing they provide for a specific feature
- has benefits of both testing, but needs control and supervision to not become another Big Bang Testing

Regression
- Series of tests over software functions to ensure that changes made has not caused any unintended behaviour
- Test all software functionalities 
- Test the module that was changed
- Test all the modules related the module that was changed

Smoke Testing
- Build and Test is done at the end of every day 
- easy to monitor and track the progress of testing 
- minimise integration risk
- Quality of Tests increase

## Unit Testing Maximum (5M)
1. Unit Testing is a testing strategy in which the code or program is decomposed to the smallest unit possible & then each unit is tested separately
2. This testing strategy can also be done before integrating various units as a whole
3. In unit testing, the local data structures are checked for their correct implementation
4. The boundary conditions of each unit are also checked to ensure that the loops are exercised with their conditions working properly 
5. The module interfaces are also checked to ensure proper integration 
6. Error handling mechanisms are also checked 
7. Unit Testing makes use of drivers and stubs

Example:
```
for (var i = 0; i < 10; i++){
	if (i == 2) OR (i == 4){
		print('2 or 4')
	}
}
```

- If unit testing is performed for the above code then boundary conditions for `for` and `if` loops are checked to see if loop works.
- The execution and display of `print` statements are checked
- (It) ensures that that the loop initiates and terminated properly

The types of common errors that can be identified through Unit Testing are:
1. Incorrect Initialisation
2. Precision Inaccuracy
3. Incorrect Representation 
4. Improper or Incorrect precedence of Arithmetic Operations
5. Invalid Data Structure