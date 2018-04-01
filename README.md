# prep


# Coding Problems: https://github.com/donnemartin/interactive-coding-challenges  

1. Knapsack: https://www.geeksforgeeks.org/knapsack-problem/  

2. Longest common subsequence: http://nbviewer.jupyter.org/github/donnemartin/interactive-coding-challenges/blob/master/recursion_dynamic/longest_common_subsequence/longest_common_subseq_solution.ipynb



# The Web:  

TCP: Data arrives in packets, in order  

UDP: Streaming data, may not arrive in order, use when you need low latency  

REST: Client acts on a state of information in the backend. All communication is stateless.  

Sample REST calls:  

GET /someresources/anId  

PUT /someresources/anId {"anotherdata": "another value"}  

Problems with REST: Sometimes data could require multiple calls to display a webpage (Facebook, etc). Requires a certain hierarchy.  



# Databases:
NoSQL: NoSQL is a collection of data items represented in a key-value store, document-store, wide column store, or a graph database.  

SQL: Structured data, strict schema (how tables are configured), transactions, complex joins




# JavaScript:

1. Closures: http://javascriptissexy.com/understand-javascript-closures-with-ease/
Inner function has access to everything in the outer function and any global variables

```	
function showName (firstName, lastName) { 
		var nameIntro = "Your name is ";
	 	// this inner function has access to the outer function's variables, including the parameter​
		function makeFullName () { 
			return nameIntro + firstName + " " + lastName;
		 }

		return makeFullName (); 
	}
 ```



Problems with closures:
```
// This example is explained in detail below (just after this code box).​
	​function celebrityIDCreator (theCelebrities) {
	    var i;
	    var uniqueID = 100;
	    for (i = 0; i < theCelebrities.length; i++) {
	      theCelebrities[i]["id"] = function ()  {
	        return uniqueID + i;
	      }
	    }
	    
	    return theCelebrities;
	}
	
	var actionCelebs = [{name:"Stallone", id:0}, {name:"Cruise", id:0}, {name:"Willis", id:0}];
	
	var createIdForActionCelebs = celebrityIDCreator (actionCelebs);
	
	var stalloneID = createIdForActionCelebs [0]; console.log(stalloneID.id()); // 103
```



In the preceding example, by the time the anonymous functions are called, the value of i is 3 (the length of the array and then it increments). The number 3 was added to the uniqueID to create 103 for ALL the celebritiesID. So every position in the returned array get id = 103, instead of the intended 100, 101, 102.


When a function accesses a variable outside its scope, it accesses that variable, not a frozen copy. So when the value held by the variable changes, the function gets that new value. By the time the user starts pressing buttons, our loop will have already completed and btnNum will be 3, so this is what each of our anonymous functions will get for num!


The reason this happened was because, as we have discussed in the previous example, the closure (the anonymous function in this example) has access to the outer function’s variables by reference, not by value. So just as the previous example showed that we can access the updated variable with the closure, this example similarly accessed the i variable when it was changed, since the outer function runs the entire for loop and returns the last value of i, which is 103.


