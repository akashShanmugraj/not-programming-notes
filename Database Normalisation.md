Normalization is the process of organizing the attributes and relations of a database to minimize redundancy and dependency. The main objective is to divide large tables into smaller, manageable ones without losing data integrity. Normalization involves applying a series of rules (normal forms) to the database schema.

Here's a detailed explanation of how to normalize a given schema based on its functional dependencies (FDs):

### Steps of Normalization

1. **Identify Functional Dependencies**:
   - Functional dependencies are constraints between two sets of attributes. For example, if `A` and `B` are attributes of a relation `R`, `A -> B` means `A` functionally determines `B`.
   
2. **First Normal Form (1NF)**:
   - Ensure that the table is in 1NF. This means that each column contains atomic (indivisible) values, and each record is unique.
   - If there are repeating groups or arrays, decompose them into separate tables.

3. **Second Normal Form (2NF)**:
   - The table must be in 1NF.
   - Remove partial dependencies. This means every non-key attribute must be fully functionally dependent on the primary key.
   - If there are partial dependencies (a non-key attribute depends on part of a composite key), decompose the table to eliminate these.

4. **Third Normal Form (3NF)**:
   - The table must be in 2NF.
   - Remove transitive dependencies. This means non-key attributes must not depend on other non-key attributes.
   - Decompose tables to ensure that non-key attributes are dependent only on the primary key.

5. **Boyce-Codd Normal Form (BCNF)**:
   - The table must be in 3NF.
   - For every functional dependency `X -> Y`, `X` should be a superkey. If a table has more than one candidate key, BCNF ensures that no anomalies exist by decomposing tables further if necessary.

### Example

Consider a table `R` with attributes `A, B, C, D` and functional dependencies:
- `A -> B`
- `A -> C`
- `C -> D`

#### Step-by-Step Normalization:

**Step 1: Ensure 1NF**
- Assume the table is already in 1NF (no repeating groups and atomic values).

**Step 2: Ensure 2NF**
- Check for partial dependencies. If the primary key is `A`, `B`, `C`, or a combination:
  - `A -> B`
  - `A -> C`
  - `C -> D`
  
  Here, `C -> D` could be a partial dependency if `C` is part of a composite key. Let's assume `A` is the primary key.

**Step 3: Ensure 3NF**
- Check for transitive dependencies:
  - `A -> C` and `C -> D` implies `A -> D` (transitive dependency).
  
  To remove this, decompose into two tables:
  - Table1: `R1(A, B, C)` with FDs `A -> B` and `A -> C`.
  - Table2: `R2(C, D)` with FD `C -> D`.

**Step 4: Ensure BCNF**
- For each table, ensure every determinant is a superkey.
  - In `R1`, `A` is a superkey.
  - In `R2`, `C` is a superkey.

No further decomposition is needed if they meet BCNF.

### Resultant Tables

After normalization, we have:
- `R1(A, B, C)` where `A` is the primary key.
- `R2(C, D)` where `C` is the primary key.

This structure eliminates redundancy and maintains dependencies efficiently.

### Summary

Normalization involves:
1. **1NF**: Eliminate repeating groups, ensure atomic values.
2. **2NF**: Remove partial dependencies.
3. **3NF**: Remove transitive dependencies.
4. **BCNF**: Ensure all determinants are superkeys.

Each step involves decomposing tables to ensure that they meet the criteria of each normal form while preserving data integrity and functional dependencies.