Source codes are compiled into objected files that are designed to be loaded into any physical memory location

- Linker: Combines compiled code and libraries associated to a single binary executable, BIN EXEC at secondary storage
- Loader: Brings / Loads binary executables into primary memory for execution
- Relocation: Assigns final address to programs
- DLL: Dynamically Linked Libraries
- avoids redundant '_linking libraries to executables_'

![[Screenshot 2024-05-30 at 11.25.37 AM.png]]

Generally, each operating system provides its own unique system calls. That is the reason why applications complied on one system usually is not supported / executable on other operating systems

Sometimes applications can be supported across multiple operating system when they are written in an interpreted language, etc

An Application Binary Interface (ABI) is a set of rules and standards that define how different pieces of binary code, such as compiled programs and libraries, interact at the machine level.

## Process Management
Process is a program in sequential execution. It contains multiple parts such as
- Program Code
- Program Counter
- Stack (with temporary data)
- Data section (with global variables)
- Heap 

Program (passive entity) becomes a Process (active entity) when it is loaded into the memory. One program can be associated with several processes but one process can be associated with only one program.

A process can be created by:
- System Initialisation 
- System Call by the user
- System Call by another running process

Conditions when a process gets terminated are:
- Normal, voluntary
- Error Exit, voluntary
- Fatal Error, involuntary
- Killed by another process, involuntary

Process States
- CREATED
- READY
- RUNNING
- BLOCKED
- EXIT

![[Screenshot 2024-05-30 at 5.45.32 PM.png]]

<Interrupt: Process Perspective - L03.19>
<Process Representation in Linux - L03.22

## CPU Scheduling

- Preemptive vs Non-Preemptive
- First Come First Serve (FCFS)
- Shortest Job First (SJF)
- Shortest Remainingtime First (SRF) (Optional)
- Round Robin (RR)
- Priority Scheduling
- Priority Scheduling with Round Robin
- Multilevel Feedback Queue (Optional)


To calculate Turnaround and Waiting Time:
- Turnaround Time = End Time - Arrival Time
- Waiting Time = Turnaround Time - Burst Time

## Threads
Threads are single sequence of programmed instructions that can be managed independently by a scheduler. It comprises a thread ID, program counter, register set, a stack.

Threads are essentially a light weight unit of execution within a process / application.

Multiple tasks with the application can be implemented by separate, independent threads
- Update display
- Fetch data
- Spell Checking
- Answer a network request

Threads can potentially improve responsiveness, resource sharing, process creation and scalability.

Cardinality in Multithreading Models
1. Many to One
	1. many user level threads mapped to one kernel thread
	2. one thread blocking causes all other threads to stop
2. One to One
	1. each user level thread maps to one kernel level thread
	2. more concurrency
3. Many to Many
	1. many user level threads are mapped to one many kernel level threads
	2. the operating system create sufficient number of threads
4. Two Level
	1. combines many to many and one to one
	2. a user thread can be either mapped to several kernel threads or it can just be mapped to one kernel thread.

`pthread` is a POSIX standard API for creating a thread programmatically, commonly found in UNIX based Operating Systems

Threading Issues

- Fork and Exec Semantics
- Signal Handling
- Thread Cancellation
- Thread-Local Storage (TLS)
- Scheduler Activations

(need elaboration)

Both M:M and Two Level models require proper communication to maintain the appropriate number of kernel threads allocated to the application. Therefore a light weight process (LWP) is attached to the kernel thread

Thread Scheduling
- **User-Level vs. Kernel-Level Scheduling**: Differentiates between how threads are scheduled in different models.
- **Pthread Scheduling**: API allows specifying process-contention scope (PCS) or system-contention scope (SCS) scheduling.

(need elaboration)

## Inter Process Communication

A process can be independent or cooperative. A cooperative process can affect or be affected by other processes. 

There are two models of IPCs:
- Shared Memory
- Message Passing

### Shared Memory

Under shared memory there are two variations:
1. Unbounded Buffer
	- no limit on size
	- producer never waits
	- consumer waits during empty buffer
2. Bounded Buffer
	- limited size
	- both producer and consumer wait (full and empty buffers respectively)

Here is an example of producer and consumer processes in a a bounded buffer:

Producer Process:
```
item next_produced;
while (true) {
	// produce an item
	while ((in + 1) % BUFFER_SIZE == out);

	buffer[in] = next_produced;
	in = (in + 1) % BUFFER_SIZE;
}
```

Consumer Process:
```
item next_consumed;
while (true) {
	while (in == out);

	next_consumed = buffer[out];
	out = (out+1) % BUFFER_SIZE;
}
```

Alternatively the above two processes can also be implemented by using a counter variable against the `BUFFER_SIZE`.

Now, if we do use a counter variable, we would ideally increment it when an item is added to the buffer, and decrement it when an item is removed from the buffer. (i.e., `counter++` and `counter--` operations respectively)

When production and consumption happens simultaneously there arises a possibility of race condition / lost update.

Consider the below `counter++` and `counter--` implementation:

```
register1 = counter;
register1 = register1 + 1;
counter = register1;
```

```
register2 = counter;
register2 = register2 - 1;
counter = register2
```

Assume they both were called at the same time and notice the below sequence of execution of commands
S0: producer execute register1 = counter                                 {register1 = 5}
S1: producer execute register1 = register1 + 1                          {register1 = 6}
S2: consumer execute register2 = counter                               {register2 = 5}
S3: consumer execute register2 = register2 – 1                       {register2 = 4}
S4: producer execute counter = register1                                 {counter  =  6}
S5: consumer execute counter = register2                               {counter  =  4}

The update to the counter variable in S1 is lost / not written. This is the race condition.

### Message Passing

Processes communicate with each other without using shared memory / sharing same address space.

### Direct Communication
Two (or more) processes need to establish a communication link first, before exchanging messages.
These communication links can either be Physical (Hardware Bus, Network) or Logical (Direct/Indirect, Synchronous/Asynchronous, Automatic/Explicit Buffering)

Two main operations involved:
1. `send(receiver, message)`
2. `receive(sender, message)`

Properties of **direct** communication link:
- Established automatically
- associated with only one pair of communicating processes
- maybe unidirectional, but usually is bidirectional

### Indirect Communication

Messages are directed and received from mailboxes / PORTS
Each mailbox has a unique ID and communication is only possible only if they share a mailbox

Two main operations involved:
1. `send(mailbox, message)`
2. `receive(mailbox, message)`

Properties of **indirect** communication link:
- Link can only be established if processes share a common mailbox
- One link maybe associated with many processes
- Each pair of process may share several communication links
- Maybe unidirectional or bidirectional

The message passing process can be either Blocking (synchronous) or Non-blocking (asynchronous).
Under blocking,
- Blocking Send - sender is blocked until the message is received
- Blocking Receive - receiver is blocked until the message is avaiable

Under non-blocking,
- Non-blocking Send - sender sends a message and continues 
- Non-blocking Receive - receiver either gets a valid message or null message

If both the send and receive are blocking then we have a `rendezvous`.

Message Passing process - Producer
```
message nextproduced;
while (true) {
	// produce next message
	send (nextproduced)
}
```

Message Passing process - Consumer
```
message nextconsumed;
while (true) {
	receive(nextconsumed);
}
```

Buffering here is a queue of messages attacked to a communication link. Three ways:
1. Zero Capacity - no messages are queued, sender waits for receiver (rendezvous)
2. Bounded - finite size, sender waits if buffer is full
3. Unbounded - no finite size, sender never waits
### Pipes 
Pipes are temporary channels of communication for IPC systems. There are two types of pipes, namely Ordinary Pipe and Named Pipes.

Ordinary Pipes,
- producer writes to the `write` end of the pipe and consumer consumes from the `read` end of the pipe (producer-consumer style)
- therefore are unidirectional and requires a parent child relationship
- cannot be accessed outside the relationship

Names Pipes,
- have bidirectional communication
- parent child relationship is not required 
- several processes can use the named pipe for communication