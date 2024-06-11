## Critical Section Problem
segment of code that CRUDs data at a shared memory. when one program modifies the critical section, no other program is allowed to modify the critical section. This is called **Mutual Exclusion**

Critical Section has three properties:
1. Process: A process has four sections, namely entry section, critical section, remaining section, exit section
2. Progress: When there are no programs inside the critical section and if two or more processes wish to enter the critical section, then the decision is made by the process those are not in the remaining section
3. Bounded Waiting: If one process has requested early to enter the critical section, then another processes gets a  limit on number of times it can request to enter the critical section, until the first process is granted critical section (assume that processes move at a nonzero speed)

### Petersons Solution

#### Process I
```
flag[i] = true
turn = j

while (flag[j] and turn == j);

// critical section code

flag[i] = false

// remainder section code

} while (true)
```

#### Process J
```
flag[j] = true
turn = i

while (flag[i] and turn == i);

// critical section code

flag[j] = false

// remainder section code

} while (true)
```

### Memory Barrier / Memory Model 
These are assurances given by the computer architecture to the operating system
- Strongly Ordered : changes made by one processor is immediately visible to others
- Weakly Ordered : changes made by one processor is immediately not visible to others

Memory Barrier - an instruction that enforces any change in memory to be visible to other processes

#### Test and Set Lock

Hardware solution to the synchronisation problem

```
boolean testandset(boolean lockvar){
	temp = lockvar
	lockvar = true
	return temp
}
```

Implementation
```
int producer(){
	while testandset(lockvar);
	// critical section
	lock = false
	
}
```

#### Compare and Swap instruction

Another hardware solution to the synchronisation problem

```
boolean compareandswap(bool target, bool expected, bool newvaule){
	temp = target
	
	if target == expected {
		target = newvalue
	}
	
	return temp
}
```

### Solution for Producer Consumer problem using Semaphores

```
int buffer[10]
int inpointer = 0
int outpointer = 0

sem_t emptysemaphore
sem_t fullsemaphore
pthread_mutex_t mutexlock


function producer()
	nextproduced = 0
	// produce next produced 

	emptysemaphore.wait()
	mutextlock.lock()

	inpointer = (inpointer + 1) % BUFFER_SIZE

	mutexthread.unlock()
	fullsemaphore.post()

function consumer()
	nextconsumed = 0

	
```