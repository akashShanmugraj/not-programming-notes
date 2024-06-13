- Single Level Ordered 
	- Primary Indexes / Clustering Indexes
	- Secondary Indexes / Non Clustering Indexes
- Multi Level Ordered 
- Dynamic Multilevel Indexes using B Trees and B + Trees

### Single Level Indexes


Primary Index:
A primary index is an index on a set of fields that includes the unique primary key for a table. 
They are unique, in sorted order, and dense or sparse

Secondary Index:
A secondary index is an index that is created on a non-primary key field or fields, which may not be unique. It allows for efficient access to records based on these non-primary key attributes.
These 'secondary keys' are not unique and require additional overhead for maintenance

### Multilevel Indexes

### First-Level Index (Single-Level Index)
A first-level index is the initial index that directly maps search keys to the data blocks or records. 
Similar to Single Level indexes

### Second-Level Index
To handle larger datasets more efficiently, a second-level index is introduced. The first-level index is divided into smaller blocks, and a second-level index is created to index these blocks. This hierarchical structure reduces the number of disk accesses needed to find a record.

**Example:**
Let’s extend the example with the `student_id` index. The first-level index is divided into smaller chunks, and a second-level index is created to point to these chunks.

1. **First-Level Index:** Divided into blocks.
   ```
   Block 1: 1 - 1000
   Block 2: 1001 - 2000
   Block 3: 2001 - 3000
   ...
   Block 10: 9001 - 10000
   ```

2. **Second-Level Index:** Indexes the blocks.
   ```
   Second-Level Index:
   Start ID -> Block Pointer
   1        -> Block 1
   1001     -> Block 2
   2001     -> Block 3
   ...
   9001     -> Block 10
   ```

### Search Process Using Multilevel Indexes
1. **Using the Second-Level Index:**
   - When searching for `student_id` 2345, the DBMS first consults the second-level index to find the appropriate block.
   - The second-level index indicates that `student_id` 2345 lies within Block 3 (2001 - 3000).

2. **Using the First-Level Index:**
   - Next, the DBMS looks within Block 3 of the first-level index to find the exact location of `student_id` 2345.
   - This block provides the record pointer, leading directly to the desired record.

### Benefits of Multilevel Indexing
- **Reduced Search Space:** Each level of indexing significantly narrows down the search space, reducing the number of disk accesses required.
- **Manageability:** Smaller index blocks are easier to manage and can be more efficiently loaded into memory.
- **Scalability:** Multilevel indexes are scalable and can handle very large datasets efficiently.

### Summary
- **First-Level Index:** A direct index mapping search keys to data records. Suitable for smaller datasets but can become unwieldy if too large.
- **Second-Level Index:** An additional index on the first-level index blocks. It provides a hierarchical structure that reduces the search space and improves efficiency for large datasets.

By using a multilevel indexing approach, databases can manage large indexes more effectively, providing faster and more efficient access to data.