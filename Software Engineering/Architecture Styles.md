## Data Centred Architecture 
- data store resides at the centre and is accesses frequently by other components that CRUD data within the store
- client software accesses a central repository that is passive in some cases
- client software accesses data independent of any changes to the data or the actions of other client software
- the central store sends a notification to all its subscribers when data of interest changes and is this active
- this promotes integrability 

![[Pasted image 20240609171001.png]]

## Data Flow Architecture
- applied when input data are to be transformed through a series of computational or manipulative components into output data
- has a set of components called filters, connected by pipes that transmit data from one filter to another filter
- each filter works independently (upstream and downstream). they expect data in one form and output data in another form
- one filter does not require the knowledge of another filter
- if there are only one line of transforms then the architecture is called batch sequential architecture 

![[Screenshot 2024-06-09 at 5.53.04 PM.png]]

## Call and Return Architecture 
- enables system architect to build a easily modifiable and scalable system
- has two substyles: 
	1. Main-Sub Program Architecture - where main program invokes many sub programs with in turn invokes some other programs
	2. Remote Procedure Call - where components are distributed across multiple computers across the network

![[Screenshot 2024-06-09 at 6.00.23 PM.png]]
## Object Oriented Architecture
- emphasises bundling of data and methods to manipulate and access that data (Public Interface)
- Communication and Coordination is accomplished via **message passing**

![[Screenshot 2024-06-09 at 6.00.38 PM.png]]

## Layered Architecture 
- multiple layers are defined with each layer performing a set of operations
- outer most layer performs operations for user-interface and inner most layer performs operations for system-interface
- intermediate layer performs utility services and application software functions

<img width="700" alt="Screenshot 2024-06-09 at 5 20 37 PM" src="https://github.com/akashShanmugraj/programming-notes/assets/65720968/07bcde70-019f-45f8-b00a-615768b95570">

