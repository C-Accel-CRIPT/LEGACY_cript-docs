# Materials - other

The 'material' node contains identity and property data for a chemical. This material node is specifically tailored for small molecules 
and inorganics.

**Features:**

* material node points to data, and sample nodes 
* required information  
    * name
    * identity
* optional information
    * data (CRIPT nodes)
    * sample (CRIPT nodes)
    * property
    * keywords
    * source
    * lot_num
    * storage conditions
    * notes
* auto generate/update:
    * _id
    * class
    * ver_sch
    * ver_con (& all child) <-- update with version control node
  
**App features to support this node:**

* allow additional optional information in `iden`, `prop` section given that it begins with +
* units are not stored for officially supported data as all official values are converted to database standard prior to storage


## JSON Schema

```json
{
  "_id": objectId(),
  "class": "material_o",
  "ver_sch": string,
  "ver_con": {
    "_id": objectId(),
    "num": string
  },
  "date": [
    {"created": datetime},
    {"last_mod": datetime}
  ],
  "name": string,
  "iden": {"see identifiers": "for details"},
  "optional attributes"
}
```

---

## Description

Key                   |Data Type     |Required  |Description
-------------         |---------     |------    |----
`_id`                 |<span style="color:rgb(0, 72, 189)"> objectId() </span>   | <span style="color:rgb(0, 72, 189)">  auto  </span> | <span style="color:rgb(0, 72, 189)">  unique database id  </span>
`class`               |<span style="color:rgb(0, 72, 189)">  string  </span>     | <span style="color:rgb(0, 72, 189)">  auto  </span> | <span style="color:rgb(0, 72, 189)">  class of node  </span>
`ver_sch`             |<span style="color:rgb(0, 72, 189)">  string  </span>     | <span style="color:rgb(0, 72, 189)">  auto  </span> | <span style="color:rgb(0, 72, 189)">  schema version; Ex: "v0.1"  </span>
`ver_con`             |                                                          |                                                     | <span style="color:rgb(0, 72, 189)">  version control object  </span>
`ver_con/_id`         |<span style="color:rgb(0, 72, 189)">  objectId()  </span> | <span style="color:rgb(0, 72, 189)">  auto  </span> | <span style="color:rgb(0, 72, 189)">  reference id to node history  </span>
`ver_con/num`         |<span style="color:rgb(0, 72, 189)">  string  </span>     | <span style="color:rgb(0, 72, 189)">auto  </span>   | <span style="color:rgb(0, 72, 189)">  type of node ; Ex: "group"  </span>
`date`                |                                                          |                                                     | <span style="color:rgb(0, 72, 189)">  datetime object  </span>
`date/created`        |<span style="color:rgb(0, 72, 189)">  datetime  </span>   | <span style="color:rgb(0, 72, 189)">auto  </span>   | <span style="color:rgb(0, 72, 189)">  datetime created  </span>
`type/last_mod`       |<span style="color:rgb(0, 72, 189)">  datetime  </span>   | <span style="color:rgb(0, 72, 189)">auto  </span>   | <span style="color:rgb(0, 72, 189)">  last modified datetime  </span>
`name`                    | string        | required  | name of chemical
`iden`                    | list[dict]    | required  | [see identifiers section](../Materials_O/#identifiers)

### Attributes

Attributes are optional properties that can be associated with this node. The following list is the officially supported
keys. Users may define their own keys by placing a '+' in front of their custom key.

Key                | Data Type    | Units    | Description
-------------      |---------     |------    | ----
`sample`           | list[dict]   |          | [sample node](../data-models/Sample.md)
`sample/_id`       | objectId()   |          | id of data
`sample/name`      | string       |          | name of data
`data`             | list[dict]   |          | [data node](../data-models/Data.md)
`data/_id`         | objectId()   |          | id of data
`data/name`        | string       |          | name of data
`data/type`        | string       |          | type of data
`prop`             | list[dict]   |          | [see properties section](../Materials_O/#properties)
`keywords`         | list[string] |          | [see keywords section below](../Materials_O/#keywords)
`source`           | string       |          | source of material
`lot_num`          | string       |          | lot number
`store`            | dict         |          | storage conditions
`store\temp`       | double       | degC     | storage temperature
`store\time_num`   | double       | min      | storage time 
`store\notes`      | string       |          | notes related to storage  
`note`             | string       |          | free-form space to store any text



### Identifiers

Identifiers are chemical descriptors or unique ids which speaks to the chemical structure. Providing as many 
identifiers as possible great facilitate the findability of the associated data. Additionally, if sufficiently many 
identifiers are provided, the polymer ensemble can be constructed from these values.
Mixtures are supported in this section by appending to list of identifiers.

```json
[
  {
    'Key': value,
    'Key': value
  }
]
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

```json
{
  "key": string, 
  "method": string, 
  "value": double, 
  "uncer": double, 
  "unit": string,
  "data": {"_id": ObjectID, "name": string, "type": string}, 
  "note": "string"
}
```

The range bound is limited to the largest number that can be stored in 64 bits (1.79e+308).
Units are not stored for officially supported data as all official values are converted to database standard prior to storage


Key              | Method    |Range                |Units      |Description
----------       |---------              |------               |--------   |---------
`ref_index`      | []                    | [0, 1.79e+308]      | None      | a dimensionless number that describes how fast light travels through the material.
`density`        | []                    | [0, 1.79e+308]      | None      | the amount of substance that fit within a unit of volume.
`mw`             | ['nmr', 'ms']      | [0, 1.79e+308]      | g/mol     | molecular weight 
`conc`           | []                    | [0, 1.79e+308]      | M         | concentration
`bp`             | []                    | [-273.15, 1.79E308] | degC      | boiling temperature
`mp`             | []                    | [-273.15, 1.79E308] | degC      | melting temperature
`vis`            | ['viscometer']        | [0, 1.79e+308]      | dl/g      | viscosity


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

### Keywords

Keywords are an optional field that allow users to classify the experiment. Selecting multiple keywords is allowed.

* monomer
* initiator
* catalyst
* solvent
---
* olefin
* styrene  
* diene
* cyclic_olefin
 ---
* vinyl
* vinyl_ether
* vinyl_ester
* acrylate
* methylacrylate
  ---
* lactone
* cyclic_ether
* cyclic_carbonate
* cyclic_anhydride
* oxazoline
 --- 
* lactam
* cyclic_amine
* cyclic_sulfur_compound
* phosphoesters
* phosphonate
* phostone  
* siloxane
* carbosiloxane
---
* diol
* dicarboxylic acid
* diamines
* diacid chloride

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



