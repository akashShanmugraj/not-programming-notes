# Query Processing

Different Stages:
1. Decomposition (passing and validation)
2. Optimisation
3. Code Generation
4. Execution


Scanner - identify query tokens
Parser - check query syntax
Query Tree / Graph - internal representation of query created as tree / graph data structure

### Query Decomposition
- transforms high level query into relational algebra query
- check if query is semantically and syntactically correct
- different stages in query decomposition are
	1. Analysis 
	2. Normalisation
	3. Semantic Analysis
	4. Simplification
	5. Query Restructuring 