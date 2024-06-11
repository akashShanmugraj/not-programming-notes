## Dynamic Linking and Shared Libraries

In dynamic linking, the _linking_ process is postponed till execution time. 
Without DLLs / Dynamic Linked Libraries, every program must include a copy of its language library which wastes disk space and main memory space

Therefore, using DLLs, multiple programs can point to one single library source which will be loaded into the memory during execution (delayed linking), and need not be present or linked during the build process
Also, on top of this, if changes are made to a library they are automatically reflected and changed during the delayed linking process, which otherwise would have been a tedious process to manually update all the versions of the libraries present in different program working directories.

Dynamic Linking is dependent on the operating system for assistance, for memory protection, managing access to shared memory, etc

