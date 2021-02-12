
# Overview

As part of CRIPTS mission to develop an ecosystem for polymers, there was a need to generate a standard data schema 
to share polymer data. The following documentation details with the way in which polymer data is represented and 
stored and within the CRIPT ecosystem.

---

# Philosophy
### Reporting Guidelines
Reporting guidelines refers to what information is need to be captured about an experiment.

CRIPT has been designed with minimal reporting requirements as polymer data is highly variable in 
content and completeness. However, contributors of data are encouraged to provide as much data as possible as it ensures
the polymer data has sufficient information to contextualize the data. Additionally, the more information provided will 
aid in the discoverability of the data. More specific reporting guidance can be found in the following documents. 

### Vocabulary
Vocabulary (controlled) is the set of terminology that provides unique identification and definition of datum. 

CRIPT provide an expert curated vocabulary for polymer data. Contributors are highly encouraged to stick to the official 
vocabulary as it is key to ensure data uniformity. Data uniformity is necessary for successful exchange information,
search, and data retrieval.

CRIPT recognizes that vocabulary may not cover all polymer data that contributors desire to add to the database, thus
CRIPT accepts any user-defined vocabulary such that it begins with a `+`. Contributors can petition for the addition of
new official vocabulary by emailing `cript@mit.edu` with the term, brief description, preferred units, and explanation
of why it should be added to the official vocabulary.

### Data exchange format
Data exchange format is the specification of how data is encoded to be a computer-readable and -processable format.

CRIPT structures data into to JSON files.

### Data structure
Data structure refers to the organization of data, and relationships into a schema.

CRIPT stores data into nodes. 

![Data_Schema](../img/Schema_Overview.svg)


##### Version Control
store by patchs
checksums? for data security SHA-1 hash

(group database-staging area-community database) https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F


