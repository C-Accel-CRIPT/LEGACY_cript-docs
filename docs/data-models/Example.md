# Example
To show how the data schema can be implemented, we will go through an example. We start by creating a user, group, and collection. 
Then we will create several real-world experiments.

## User, Group, Collection

For a new user, the first step that needs to be done is to create a 'user'. Once the 'user' is created, then
the user can either join an existing 'group' or create a new 'group'. Typically, 'groups' are created and own by a supervisor
since 'groups' maintain ownership over 'collections'/'experiments' (such as a principal investigator for an academic lab). 
In this example, we will create a new 'group' named: "CRIPT Team". With a 'user' now in a 'group', we can create a 'collection' that 
will hold the experiments. 






### User
[User node](../data-models/Users.md)

```json
{
  "_id": "607f1720633b3e6e70e529c7",
  "class": "user",
  "ver_sch": "v0.1",
  "ver_con": {
    "_id": "507f191e810c19729de860cb",
    "num": "v0.1"
  },
  "last_modified": "2021-04-20 18:07:57",
  "created": "2021-04-20 18:02:08",
  "name": "Dylan W",
  "email": "dylan@cript.edu",
  "owns_groups": [{"_id": "607f180c633b3e6e70e529c8", "name": "CRIPT Team"}],
  "in_groups": [
    {"_id": "607f180c633b3e6e70e529c8", "name": "MIT"},
    {"_id": "607f180c633b3e6e70e529c7", "name": "Olsen Lab"}
  ],
  "publication": [
    {"_id": "507f191e810c19729de860eq", "name": "Recent trends in catalytic polymerizations"},
    {"_id": "507f191e810c19729de860er", "name": "Kinetic study of living ring-opening metathesis polymerization with third-generation Grubbs catalysts"}
  ],
  "collection": [
    {"_id": "507f191e810c19729de860em", "name": "ROMP kinetic study", "date": "2021-04-20 18:02:08", "num_expt": 3}
  ],
  "orcid": "0000-0000-0000-0001",
  "organization": "Mass. Institute of Technology",
  "position": "Research Assistant"
}
```

### Group
[Group node](../data-models/Group.md)

```json
{
  "_id": "607f180c633b3e6e70e529c8",
  "class": "group",
  "version_schema": "v0.1",
  "version_control": {
    "_id": "507f191e810c19729de860eb",
    "num": "v0.1"
  },
  "last_modified": "2021-04-20 18:27:50",
  "created": "2021-04-20 18:06:04",
  "name": "CRIPT Team",
  "collection": [
      {"_id": "507f191e810c19729de860em", "name": "CRIPT Demo", "created": "2021-04-20 18:06:04"},
      {"_id": "507f191e810c19729de860em", "name": "Kinetic analysis of ROMP", "created": "2021-04-20 18:06:04"}
    ],
  "parent_group": [
      {"_id": "507f191e810c19729de860em", "name": "MIT"},
      {"_id": "507f191e810c19729de860en", "name": "Citrine"}
    ],
  "publication": [
      {"_id": "507f191e810c19729de860em", "title": "BigSMILES: A Structurally-Based Line Notation for Describing Macromolecules"},
      {"_id": "507f191e810c19729de860ey", "title": "PolyDAT: A Generic Data Schema for Polymer Characterization"}
    ],
  "website": "https://cript.mit.edu/",
  "email": "cript@mit.edu"
}
```

### Collection

[Collection node](../data-models/Collections.md)

```json
{
  "_id": "607f180c633b3e6e70e529c8",
  "class": "coll",
  "version_schema": "v0.1",
  "version_control": {
    "_id": "507f191e810c19729de860eb",
    "num": "v0.1"
  },
  "last_modified": "2021-04-20 18:27:50",
  "created": "2021-04-20 18:06:04",
  "name": "CRIPT Demo",
  "number_experiments": 2, 
  "experiment": [
    {"_id": "507f191e810c19729de860em", "name": "Anionic polymerization of styrene", "created": "2021-04-20 18:06:04"},
    {"_id": "507f191e810c19729de860en", "name": "Diblock bottlebrush synthesis and assembly", "created": "2021-04-20 18:06:04"}
  ],
    "child_collection": [
    {"_id": "507f191e810c19729de860em", "name": "Kinetic analysis of ROMP", "created": "2021-04-20 18:06:04"}
  ]
}
```


---

---

## Experiments

### Experiment 1: Anionic polymerization of styrene

### Experiment 2: Diblock bottlebrush synthesis and assembly

### Experiment 3: Kinetic analysis of ROMP

### Experiment 4: Simulation

To show how the data schema can be implemented, we will go through the anionic synthesis of a polystyrene, polybutadiene
block copolymer through sequential addition of monomers. We will describe the implementation from the perspective of the
real world experiment timeline as that is likely to be the most intuitive workflow.

The data schema begins with the definition of material nodes. These first material nodes are the ingredients for the
process node. This will be secbuLi, styrene, and toluene in our example. These materials nodes will contain information
such as name, SMILES string, CAS number, and property information (molecular weight, boiling point, etc.) The second
node to be defined will be a process node. In this case, it will be a polymerization node. The polymerization node will
contain links to those initial material nodes as well as the quantities of each material used in the polymerization. The
polymerization node will also contain details for the process in the form of a paragraph, or a list of process
parameters. For the anionic polymerization, this can be details about the order of addition of the chemicals, reaction
time, temperature, etc. In the case when data is taken about a process, a link to data node can be made. Something like
polymerization kinetics where concentration or molecular weight is monitored over time. The third node to be defined is
another material node, or product of the process. Polystyrene in this case. The process node will link to this product
material node. Any characterization data from aliquots can be added through a data node. The material node will link to
the relevant data nodes. In our example, SEC raw data or NMR spectra can be found in the data nodes, while the
calculated values like M~n~, M~w~, M~w~/M~n~, etc. would be found in the property section of the polystyrene node.

The synthesis for the second block, polybutadiene, continues with the definition of the butadiene material node. This
can be followed by the definition of a second polymerization node which will point to the product of the whole process,
polystyrene-polybutadiene block copolymer. Similar to the polystyrene characterization, the SEC and NMR data can be
placed into data nodes. With this final target material made additional material studies, like tensile testing or oxygen
barrier properties, may be done. In this case, there may be some material preparation steps such as hot pressing the
sample into a dog bone. This can be placed into a sample node. This sample node contains the material preparation steps
and any characterization data that occurred on the sample.

![Data_Model](../img/data_schema_example.svg)

We can also visualize the exact same example in the context of a direct acyclic graph.

![Data_Model](../img/data_schema_example_2.svg)

Example where they buy the polymer






## Publication
