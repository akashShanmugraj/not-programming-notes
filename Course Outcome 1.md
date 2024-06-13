
## File Processing
- organisation in a group of files
- data between files are independent
- less flexible and many limitations
- difficult maintenance
- aka Flat Files

#### Drawbacks of File Processing
- Data Redundancy and Inconsistency (many different file formats, duplication possible)
- Need a new program everytime to access a file
- No Data Isolation - multiple available file formats
- Lack of Integrity (constraints) checking
- No atomicity of updates, may be in partial update state
- uncontrolled concurrent accesses
- security problems

### Advantages of Database Approach over File Processing
- controlling redundancy in data storage 
- restrict unauthorised access to data
- can provide persistent storage for program objects
- provide storage structures for query processing
- provide backup and recovery services
- provide multiple interface to different class users
- can enforce integrity constraints
- supports triggers and procedures

Database Management System Functionality
1. Define - structures and constraints
2. Construct - initial contents of a database
3. Manipulate - retrieval, modification and accessing database
4. Processing and Sharing - serve concurrent users and application programs

### Levels of Abstraction
1. Physical Level - how a record is stored
2. Logical Level - how data is stored and related between other data in the database
3. View Level - hide details of data types for security purposes



### Database Users
1. Database Administrators - authorising access, coordinating and monitoring for database and resources, controlling its use and monitoring efficiency of operations
2. Database Designers - define content, structure, constraints, functions or transactions. need to communicate with end users
3. End Users - use data from the database, rarely update / modify the data there too

### Categories of End Users
1. Causal - occasional access to database, upon need
2. Parametric - majority, use previously well defined functions against database
3. Sophisticated - professionals who are throughly familiar with system capabilities, work with software packages
4. Standalone - personal database for ready to use packaged application 

< Data Models > 

### Schemas and Instances

- Database Schema - description of database (structure, data types and constraints)
- Schema Diagram - illustrative display of database schema
- Schema Construct - component of a schema within a schema

- Database State - data stored in a database at a particular moment in time, including collection of all data in the database - also like snapshot
- Initial Database State - database state when the database was initialised 
- Schema -> Intension
- State -> Extension


### Three Schema Architecture

1. Internal Schema - describe physical storage structures and access paths
2. Conceptual Schema - describe the structure and constraints for the whole database
3. External Schema - describe various user views


### Database System Environment

1. Storage and Access:
   - typically stored on disks, with the operating system managing disk I/O.
   - stored data manager controls access to DBMS information on disk, data transfer between disk and main storage, and managing buffers in memory.

2. Database Management Components:
   - DDL Compiler - Processes schema definitions and stores metadata
   - Interactive Query Processing - parsing, validating, optimising queries before converting them into executable code
   - Precompiler: Extracts, compiles and integrates DML Commands with the host language program

3. Runtime Database Processor:
   - Executes privileged commands, query plans, and transactions, while working with the system catalog and stored data manager.
   - Includes concurrency control and backup/recovery systems for transaction management.

4. Database Architectures:
   - Centralized DBMS: Integrates all components into a single system, processing everything at a central site.
   - Two-tier Client-Server Architecture: Specialized servers (e.g., print, file, DBMS, web, email servers) provide services to clients, which access these servers over a network.
   - Three-tier Client-Server Architecture: Common in web applications, it includes an intermediate layer (application/web server) that handles logic, processes data and enhances security

5. Specialty Databases:
   - Focus on specific fields of study and provide authoritative, accurate, and reliable information.
   - Examples include PubMed, Embase, Scopus, and CINAHL, each containing millions of records relevant to specific disciplines such as medicine and nursing.
