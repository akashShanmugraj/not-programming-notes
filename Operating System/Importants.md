# Virtual Machines

Virtual Machines (VMs) can be categorised primarily into different types based on their implementation and usage. Here are the main types:

1. **Type 0 Hypervisor**: 
   - hardware based solutions, around for many years
   - embedded in the firmware and loads at boot time
   - divides hardware into isolated partitions
   - each partition gets dedicated resources like CPU, Memory etc
   - close to hardware performance, minimal overhead

2. **Type 1 Hypervisor** (Bare-metal):
   - run directly on hardware without software support (host operating system)
   - better performance and efficiency since no intermediate layer
   - used in enterprises, where there is a need for high performance

3. **Type 2 Hypervisor** (Hosted):
   - run on an operating system (hosted on) 
   - provides virtualisation services as an application
   - VMware Workstation, Oracle VM VirtualBox.
   - easier to setup, but have high overhead

4. **Java Virtual Machine (JVM)**:
   - programming environment virtualisation
   - allows java programs to run on any device or OS without modification
   - JVM abstracts the hardware and operating system details, providing a consistent environment for execution
   - ensure portability and platform independence for Java applications
