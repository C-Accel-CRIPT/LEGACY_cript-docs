# Example
To show how the data schema can be implemented, we will go through an example. We start by creating a user, group, and collection. 
Then we will create several real-world experiments.

## User, Group, Collection

For a new user, the first step that needs to be done is to create a 'user'. Once the 'user' is created, then
the user can either join an existing 'group' or create a new 'group'. Typically, 'groups' are created and own by a supervisor
since 'groups' maintain ownership over 'collections'/'experiments' (such as a principal investigator for an academic lab). 
In this example, we will create a new 'group' named: "CRIPT Team". With a 'user' now in a 'group', we can create a 'collection' that 
will hold the experiments. 



![User, Group, Collection Network](../img/V1_Example_User_Group_coll.svg)


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
  "orcid": "0000-0000-0000-0001",
  "organization": "Mass. Institute of Technology",
  "position": "Research Assistant"
}
```

![User Network](../img/V1_Example_User.SVG)

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
      {"_id": "507f191e810c19729de860em", "name": "CRIPT Demo", "created": "2021-04-20 18:06:04"}
    ],
  "parent_group": [
      {"_id": "507f191e810c19729de860em", "name": "Olsen Lab"},
      {"_id": "507f191e810c19729de860en", "name": "Citrine"}
    ],
  "publication": [
      {"_id": "507f191e810c19729de860em", "title": "Synthesis of new polymer"}
    ],
  "website": "https://cript.mit.edu/",
  "email": "cript@mit.edu"
}
```

![User Network](../img/V1_Example_group.SVG)

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

![User Network](../img/V1_Example_Coll.SVG)

---

---

## Experiments

### Experiment 1: Anionic polymerization of styrene

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

#### Experiment node

```json
{
  "_id": "507f191e810c19729de860ec",
  "class": "expt",
  "version_schema": "v0.1",
  "version_control": {
    "_id": "507f191e810c19729de860eb",
    "num": "v0.1"
  },
  "last_modified": "2021-04-20 18:27:50",
  "created": "2021-04-20 18:06:04",
  "name": "Anionic polymerization of styrene",
  "nodes": {
    "materials": [
      {"_id": "507f191e810c19729de860ec", "name": "SecBuLi"},
      {"_id": "507f191e810c19729de860ed", "name": "toluene"},
      {"_id": "507f191e810c19729de860ee", "name": "styrene"},
      {"_id": "507f191e810c19729de860eg", "name": "THF"},
      {"_id": "507f191e810c19729de860eh", "name": "butanol"},
      {"_id": "507f191e810c19729de860ei", "name": "methanol"},
      {"_id": "507f191e810c19729de860ef", "name": "polystyrene", "id_proc": "507f191e810c19729de860pe", "id_data":["507f191e810c19729de860md", "507f191e810c19729de860me"]}
    ],
    "process": [
      {
      "_id": "507f191e810c19729de860pe", 
      "name": "anionic polymerization", 
      "id_mat": [
        "507f191e810c19729de860ec",
        "507f191e810c19729de860ed",
        "507f191e810c19729de860ee",
        "507f191e810c19729de860eg",
        "507f191e810c19729de860eh",
        "507f191e810c19729de860ei"
      ]
    }
    ],
    "data": [
      {"_id": "507f191e810c19729de860md", "name": "1H NMR"},
      {"_id": "507f191e810c19729de860me", "name": "SEC"}
    ]
  },
  "attr": {
    "pub": [
      {"_id": "507f191e810c19729de860em", "title": "Kinetic Study of Living Ring-Opening Metathesis Polymerization"}
    ],
    "ref": [
      {"_id": "507f191e810c19729de860en", "title": "Kinetic Study of Anionic Living Polymerization"}
    ]
  }
}
```

#### Material node

[Material node other](../data-models/Materials_O.md)
[Material node polymers](../data-models/Materials_P.md)


```json
{
  "_id": "607f191e810c19729de860ea",
  "type": "expt",
  "ver_sch": "v0.1",
  "ver_con": {
    "_id": "607f191e810c19729de860eb",
    "num": "v0.1"
  },
  "last_modified": "2021-04-20 18:27:50",
  "created": "2021-04-20 18:06:04",
  "notes": "",
  "name": "styrene",
  "expt": [{"_id": "507f191e810c19729de860em", "name": "anionic polymerization of styrene"}],
  "proc": [{"_id": "507f191e810c19729de860em", "name": "anionic polymerization", "role": ["ingr"]}],
  "data": [],
  "iden": {
    "names": ["styrene","vinylbenzene", "phenylethylene"],
    "cas": "100-42-5",
    "smiles": "C=Cc1ccccc1",
    "chem_form": "C8H8"
  },
  "prop": [
    {
      "key": "mw", "value": 104.15, "attr": {"ref": {"notes": "sigma aldrich website"}}
    },
    {
      "key": "density", "value": 0.906
    },
    {
      "key": "bp", "value": 145, "attr": {"+vac": "1", "+vac_unit": "atm"}
    }
  ],
  "attr": {
    "store": {"temp_num": 0, "temp_unit": "degC"},
    "source": "sigma"
  }
}
```


```json
{
  "_id": "607f191e810c19729de860ea",
  "type": "expt",
  "ver_sch": "v0.1",
  "ver_con": {
    "_id": "607f191e810c19729de860eb",
    "num": "v0.1"
  },
  "date": [
    {"created": 1612889382},
    {"last_mod": 1612889322}
  ],
  "notes": "",
  "users": [
    {"_id": "507f191e810c19729de860ec", "name": "Dylan W", "perm": "w"}
  ],
  "name": "poly(styrene)",
  "expt": [
    {"_id": "507f191e810c19729de860em", "name": "anionic polymerization of styrene"}
  ],
  "iden": {
    "names": ["Poly(1-phenylethene)"],
    "cas": "9003-53-6",
    "bigsmiles": "{[$]CC(c1ccccc1)[$]}",
    "chem_repeat": "C8H8"
  },
  "prop": [
    {
      "key": "conv_mon", "method": "NMR", "value": 0.98, "uncertainty": 0.03,
      "attr": {"data": {"_id": "507f191e810c19729de860em", "key": "nmr_1h"}}
    },
    {
      "key": "m_n", "method": "nmr", "value": 5300, "uncertainty": 300,
      "attr": {"data": {"_id": "507f191e810c19729de860em", "key": "nmr_1h"}, "names": ["end group analysis"]}
    },
    {
      "key": "m_n", "method": "sec", "value": 5130, "uncertainty": 200,
      "attr": {"data": {"_id": "507f191e810c19729de860em", "key": "sec"}}
    },
    {
      "key": "d", "method": "sec", "value": 1.03, "uncertainty": 0.02,
      "attr": {"data": {"_id": "507f191e810c19729de860em", "key": "sec"}}
    }
  ],
  "proc": [
    {"_id": "507f191e810c19729de860em", "name": "anionic polymerization", "role": ["prod"]}
  ],
  "data": [
    {"_id": "507f191e810c19729de860ef", "key": "nmr_1h"},
    {"_id": "507f191e810c19729de860vm", "key": "sec"}
  ],
  "attr": {}
}
```

### Experiment 2: Diblock bottlebrush synthesis and assembly

### Experiment 3: Kinetic analysis of ROMP



{
    "materials": [
      {"_id": "507f191e810c19729de860ec", "name": "G3 Catalyst", "_idproc": "507f191e810c19729de860pe", "role": "ingr"},
      {"_id": "507f191e810c19729de860ed", "name": "dichloromethane", "_idproc": "507f191e810c19729de860pe", "role": "ingr"},
      {"_id": "507f191e810c19729de860ee", "name": "norbornene-imide", "_idproc": "507f191e810c19729de860pe", "role": "ingr"},
      {"_id": "507f191e810c19729de860ef", "name": "ethyl vinyl ether", "_idproc": "507f191e810c19729de860pe", "role": "ingr"},
      {"_id": "507f191e810c19729de860ds", "name": "poly(norborene-imide)", "_idproc": "507f191e810c19729de860pe", "role": "prod"}
    ],
    "process": [
      {"_id": "507f191e810c19729de860pe", "name": "ROMP polymerization", "_idout": "507f191e810c19729de860ds"}
    ],
    "data": [
      {"_id": "507f191e810c19729de860md", "name": "1H NMR", "_idprod": "507f191e810c19729de860ds", "_idprod": "507f191e810c19729de860ds"},
      {"_id": "507f191e810c19729de860me", "name": "SEC", "_idprod": "507f191e810c19729de860ds", "_idprod": "507f191e810c19729de860ds"}
    ]
  },
  "attr": {
    "pub": [
      {"_id": "507f191e810c19729de860em", "title": "Kinetic Study of Living Ring-Opening Metathesis Polymerization"}
    ],
    "ref": [
      {"_id": "507f191e810c19729de860en", "title": "Kinetic Study of Anionic Living Polymerization"}
    ]
  }

### Experiment 4: Simulation



## Publication

[Publications node](../data-models/Publications.md)


```json
{
  "_id": "507f191e810c19729de861ec",
  "class": "publication",
  "ver_sch": "v0.1",
  "ver_con": {
    "_id": "507f191e810c19729de861cb",
    "num": "v2.1"
  },
  "last_modified": "2021-04-20 18:27:50",
  "created": "2021-04-20 18:06:04",
  "title": "Engineering of Molecular Geometry in Bottlebrush Polymers",
  "collection": {"_id": "507f191e810c19729de860em", "name": "Bottlebrush Synthesis", "created": "2021-04-20 18:06:04"},
  "authors": ["Walsh, Dylan J.", "Dutta, Sarit", "Sing, Charles E.", "Guironnet, Damien"],
  "journal": "Macromolecules",
  "publisher": "American Chemical Society",
  "year": "2019",
  "vol": 52,
  "issue": 13,
  "page": "4847-4857",
  "doi": "10.1021/acs.macromol.9b00845",
  "issn": "0024-9297",
  "web": "http://pubs.acs.org/doi/10.1021/acs.macromol.9b00845"
}
```