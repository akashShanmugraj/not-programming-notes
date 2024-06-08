A computer system can be divided into four components:
 - Hardware
 - Operating System
 - Application Programs
 - Users

Operating System is an intermediary program between a computer user and the computer hardware.
Goals of an OS:
    - Enable user program execution to solve problems.
    - Make the computer system user-friendly.
    - Ensure efficient utilization of computer hardware.

Simultaneous Peripheral Operation On Line (SPOOL):
- disk or RAM to temporarily store data intended for slower peripheral devices like printers
- This also introduces "Job Pool" that allows OS to choose next job to run so as to increase CPU utilisation

Timesharing:
- Multiprogramming is having multiple program in memory at the same time and rapidly switching between
- Timesharing is like Multiprogramming but a timer interrupts the program execution after a time slice.
- Interrupted program is moved to the end of the queue and the next program is moved to the head of the queue and up for execution

Notable Operating Systems (IC era):
- MULTICS
- UNIX
- Linux

A process is a program in execution. It is associated with 
- an address space 
- set of resources 
- open files 
- related processes 
- stack pointer

A process is a container that holds all information to run a program

An address space is memory used by a process. In concept, modern OS allows multiple process in memory simultaneously.

An Operating System provides an environment for execution. The set of functions that an OS provides is
1. User Interface
2. Program Execution - load a program into memory for execution
3. IO Operation - allocate IO devices if required
4. File System Manipulation
5. Communication - two processes should exchange information locally or between two computers over a network
6. Error Detection - handle CPU, Memory, IO error and take appropriate action
7. Resource Sharing - efficiently allocating resources for concurrently running processes 
8. Logging 
9. Protection - ensure than all resource access is controlled
10. Security - safeguard system against outsiders and external IO devices

System Calls are programming interface to services provided by the Operating System via a high-level API. Examples include `Win32 API`, `POSIX API`, `Java API`

There typically is a number associated with each system call, which means that the System Call Interface maintains a table with indexed system calls.

There are three ways to pass parameters along with a system call:
1. pass using registers (length restrictions present)
2. pass using memory block or table (no length restrictions present)
3. (pass using) push into stack (no length restrictions present)

![[Screenshot 2024-05-30 at 10.38.36 AM.png]]

Primarily there are 6 major classifications of system calls

- Process control: Managing processes, including creating, terminating, executing, and getting/setting attributes.
- File management: Manipulating files, including creating, deleting, opening, closing, reading, writing, and managing attributes.
- Device management: Handling devices, including requesting, releasing, reading from, writing to, and managing devices.
- Information maintenance: Maintaining system information, including getting/setting time/date, and getting/setting system data.
- Communications: Enabling communication between processes, which may involve message passing or shared memory.
- Protection: Controlling access to system resources, managing permissions, and handling user access.

Here is a more detailed listing of all system calls under the specific groups:

1. Process Control
	1. create, terminate, end, abort process
	2. load, execute process 
	3. get and set process attributes
	4. wait and signal events (semaphores)
	5. allocate and free memory 
	6. debugger and locks 
2. File Management
	1. create, open, close, delete a file
	2. read, write, reposition pointer in a file
	3. get or set file attributes
3. Device Management
	1. request, read, write, reposition, release a device
	2. get or set device attributes
	3. attach or detach devices logically
4. Information Maintenance
	1. get or set time/date
	2. get or set process, file or device attributes
5. Communications
	1. create or delete communication connection 
	2. send and receive messages 
	3. transfer status information
6. Protection 
	1. control access to resource
	2. get and set permission attributes
	3. allow and deny user access

Command-Line Interpreter (CLI) allows direct command entry for interacting with the operating system.

Graphical User Interface (GUI) provides a user-friendly desktop metaphor interface using icons, windows, and a pointing device for user interaction.

**Design and Implementation:**

- Operating system design is an iterative process, with no single solution.
- **Policy:** Defines what needs to be done.
- **Mechanism:** Determines how to implement the policy.
- Modern operating systems are often implemented using a combination of languages, with lower-level components in assembly language and higher-level components in languages like C or C++.