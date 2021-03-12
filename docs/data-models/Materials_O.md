# Materials - other

The 'material' node contains data related to a chemical. This material node is specifically tailored for small molecules 
and inorganics.

**Features:**

* material node points to process nodes (multiple process nodes are allowed)
* process, data, and sample nodes point to material nodes (multiple data nodes are allowed, single process node allowed)
* required information  
    * name
    * identity
    * references: expt, proc, data, sample (will be populated as it's linked to other nodes)
* optional information
    * property
    * source
    * lot_num
    * storage conditions
* auto generate/update:
    * _id
    * type
    * ver_sch
    * ver_con (& all child) <-- update with version control node
    * date (& all child)
    * expt (& all child)  <-- update with expt node
    * proc (& all child) <-- update with proc node
    * data (& all child) <-- update with data node

**App features to support this node:**

* a page to fill out: experiment(materials, process, data) data
* allow additional optional information in attribute, **iden, prop** section given that it begins with +
* units are not stored and all official values are converted to database standard prior to storage

## JSON Schema

```json
{
  "_id": objectId(),
  "type": "material",
  "ver_sch": string,
  "ver_con": {
    "_id": objectId(),
    "num": string
  },
  "date": [
    {"created": datetime},
    {"last_mod": datetime}
  ],
  "notes": string,
  "expt": [{"_id": objectId(), "name": string}],
  "proc": {"_id": objectId(), "name": string, "role": string},
  "data": [{"_id": objectId(), "name": string}],
  "name": string,
  "iden": {"see identifiers": "for details"},
  "prop": [{"see properties": "for details"}],
  "attr": {"see attributes": "for details"}
}
```

---

## Description

Key                       |Data Type     |Required  |Description
-------------             |---------     |------    |----
`_id`                     |<span style="color:rgb(0, 72, 189)"> objectId() </span>|<span style="color:rgb(0, 72, 189)">  auto  </span>|<span style="color:rgb(0, 72, 189)">  unique database id  </span>
`type`                    |<span style="color:rgb(0, 72, 189)">  string  </span> |<span style="color:rgb(0, 72, 189)">  auto  </span>|<span style="color:rgb(0, 72, 189)">  type of node ; Ex: "group"  </span>
`ver_sch`                 |<span style="color:rgb(0, 72, 189)">  string  </span>|<span style="color:rgb(0, 72, 189)">  auto  </span>|<span style="color:rgb(0, 72, 189)">  schema version; Ex: "v0.1"  </span>
`ver_con`                 |              |          |<span style="color:rgb(0, 72, 189)">  version control object  </span>
`ver_con/_id`             |<span style="color:rgb(0, 72, 189)">  objectId()  </span>|<span style="color:rgb(0, 72, 189)">  auto  </span>|<span style="color:rgb(0, 72, 189)">  reference id to node history  </span>
`ver_con/num`             |<span style="color:rgb(0, 72, 189)">  string  </span>|<span style="color:rgb(0, 72, 189)">auto  </span>|<span style="color:rgb(0, 72, 189)">  type of node ; Ex: "group"  </span>
`date`                    |              |          |<span style="color:rgb(0, 72, 189)">  datetime object  </span>
`date/created`            |<span style="color:rgb(0, 72, 189)">  datetime  </span>|<span style="color:rgb(0, 72, 189)">auto  </span>|<span style="color:rgb(0, 72, 189)">  datetime created  </span>
`type/last_mod`           |<span style="color:rgb(0, 72, 189)">  datetime  </span>|<span style="color:rgb(0, 72, 189)">auto  </span>|<span style="color:rgb(0, 72, 189)">  last modified datetime  </span>
`notes`                   |<span style="color:rgb(0, 72, 189)">  string  </span>|<span style="color:rgb(0, 72, 189)">auto  </span> |<span style="color:rgb(0, 72, 189)">  free-form space to store any text  </span>
`expt`                    |               |<span style="color:rgb(12, 145, 3)">  auto  </span>          | [experiment node](../data-models/Experiments.md)
`expt/_id`                |<span style="color:rgb(12, 145, 3)">  objectId()     </span> |<span style="color:rgb(12, 145, 3)"> auto  </span> |<span style="color:rgb(12, 145, 3)"> id of experiment </span>
`expt/name`               |<span style="color:rgb(12, 145, 3)">  string         </span> |<span style="color:rgb(12, 145, 3)"> auto  </span> |<span style="color:rgb(12, 145, 3)"> name of experiment </span>
`process`                 |               |         </span>  | [process nodes](../data-models/Process.md)
`process/_id`             | <span style="color:rgb(12, 145, 3)">objectId() </span>   |<span style="color:rgb(12, 145, 3)"> auto    </span>  | <span style="color:rgb(12, 145, 3)">id of process </span>
`process/name`            | <span style="color:rgb(12, 145, 3)">string      </span>  |<span style="color:rgb(12, 145, 3)"> auto     </span> | <span style="color:rgb(12, 145, 3)">name of process </span>
`process/role`            | <span style="color:rgb(12, 145, 3)">list[string] </span>  | <span style="color:rgb(12, 145, 3)">auto     </span> | <span style="color:rgb(12, 145, 3)">role of material in process [ingr, prod] </span>
`data`                    |               | optional       | [data node](../data-models/Data.md)
`data/_id`                |<span style="color:rgb(12, 145, 3)">  objectId()     </span> |<span style="color:rgb(12, 145, 3)"> auto  </span> |<span style="color:rgb(12, 145, 3)"> id of data </span>
`data/name`               |<span style="color:rgb(12, 145, 3)">  string         </span> |<span style="color:rgb(12, 145, 3)"> auto  </span> |<span style="color:rgb(12, 145, 3)"> name of data </span>
`name`                    | string        | required  | name of chemical
`iden`                    |               | required  | [see identifiers section](../Materials_P/#identifiers)
`prop`                    |               | optional  | [see properties section](../Materials_P/#properties)
`attr`                    | list          | auto      | see attributes section


### Identifiers

Identifiers are chemical descriptors or unique ids which speaks to the chemical structure. Providing as many 
identifiers as possible great facilitate the findability of the associated data. Additionally, if sufficiently many 
identifiers are provided, the polymer ensemble can be constructed from these values.
Mixtures are supported in this section by appending to list of identifiers.

The identifiers are split into two groups: Primary and Secondary. Primary identifiers are non-experimentally dertermined
values. Secondary identifiers are experimentally determined chemical descriptors. Units are only used for user
defined attributes which begin with a `+`. 'id' here is a 'double' and represents the idea of the component. 

```json
{'id':{'Key': {"value": string/double, "uncer": double, "unit": string, "method": string, "data":{"_id": ObjectID, "name": string}}}}
```

#### Primary Identifiers
Key                  | Data Type      | Required    | Description
-------------        |---------       | ---------   |----
`names`              | list[string]   | required    | Any name for the material
`cas`                | string         | optional    | [CAS number](https://www.cas.org/support/documentation/chemical-substances)
`smiles`             | string         | optional    | [simplified molecular-input line-entry system](https://en.wikipedia.org/wiki/Simplified_molecular-input_line-entry_system)
`chem_form`          | string         | optional    | chemical formula, Ex. benzene: "C6H6"



### Properties

Properties consist of the following structure:
“key”: {“method”: string, “value”: double, “uncertainty”: double, “attr”: {}}

The range bound is limited to the largest number that can be stored in 64 bits (1.79e+308).

Key              | Method                |Range                |Units      |Description
----------       |---------              |------               |--------   |---------
`ref_index`      | []                    | [0, 1.79e+308]      | None      | a dimensionless number that describes how fast light travels through the material.
`density`        | []                    | [0, 1.79e+308]      | None      | the amount of substance that fit within a unit of volume.
`mw`             | ['nmr', 'maldi']      | [0, 1.79e+308]      | g/mol     | molecular weight 
`conc`           | []                    | [0, 1.79e+308]      | M         | concentration
`bp`             | []                    | [-273.15, 1.79E308] | degC      | boiling temperature
`mp`             | []                    | [-273.15, 1.79E308] | degC      | melting temperature
`vis`            | ['viscometer']        | [0, 1.79e+308]      | dl/g      | viscosity


Key              | Description
----------       | ----
`nmr`            | Nuclear Magnetic Resonance
`sec`            | Size Exclusion Chromatography
`maldi`          | Matrix Assisted Laser Desorption Ionization
`ultra_centr`    | Ultra Centrifugation
`osmtic_pres`    | Osmotic Pressure
`ls`             | Static Light Scattering
`dls`            | Dynamic Light Scattering
`viscometer`     | Viscometer
`calorimetry`    | Calorimetry
`utm`            | Universal Testing Machine
`comp`           | Computation or Simulation

#### Attribute for Properties

Key              | Data Type     |Description
----------       |---------      |----
`ref`            |               | [publication node](../data-models/Publications.md) that was a reference for this experiment
`ref\_id`        | objectId()    | id for reference
`ref\title`      | string        | reference title
`ref\notes`      | string        | for non-publication reference enter the information here      
`data`           |               | [data](../data-models/Data.md)
`data\_id`       | objectId()    | id for data node
`data\key`       | string        | key for data
`names`          | list[string]  | additional names for property
`unit`           | string        | unit are only applicable to user defined values


### Attributes

Attributes are optional properties that can be associated with this node. The following list is the officially supported
keys. Users may define their own keys by placing a '+' in front of their custom key.

Key                | Data Type    | Units    | Description
-------------      |---------     |------    | ----
`source`           | string       |          | source of material
`lot_num`          | string       |          | lot number
`store`            |              |          | storage conditions
`store\temp`       | double       | degC     | storage temperature
`store\time_num`   | double       | min      | storage time 
`store\notes`      | string       |          | notes related to storage 

---

## Example

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

### Visualization

![Experiment_network](../img/network_material_o.svg)

