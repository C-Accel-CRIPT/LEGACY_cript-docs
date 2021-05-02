# Experiment

The 'experiment' node contains complete set of references to all the nodes of an experiment. An experiment can range from a 
synthesis, to scattering experiment, or a simulation. A single experiment is meant to capture a single, or a linear 
set of processes. For non-linear processes (like running multiple reactions for optimizations, kinetics, etc.) [collections](../data-models/Collections.md) are preferred. 

**Features:**

* experiment can reference materials, process, sample, data
* required information  
    * name
    * materials, process, sample, data nodes 
* optional information
    * references
    * notes
* auto generate/update:
    * _id
    * class
    * version_schema
    * version_control (& all child) <-- update with version control node
    * date (& all child)
  
**App features to support this node:**

* a page to fill out: experiment(materials, process, sample, data) data
* allow additional optional information in attribute section given that it begins with +


## JSON Schema

```json
{
  "_id": objectId(),
  "class": "expt",
  "version_schema": string,
  "version_control": {
    "_id": objectId(),
    "num": string
  },
  "created": datetime,
  "last_modified": datetime,
  "name": string,
  "materials": [
    {"_id": objectid(), "name": string, "role": string, "_id_proc":  objectId()}
  ],
  "process": [
    {"_id": objectid(), "name": string}
  ],
  "sample": [
    {"_id": objectid(), "name": string, "id_link": objectid()}
  ],
  "data": [
    {"_id": objectid(), "name": string, "id_link": objectid()}
  ],
  "optional attributes"
}
```

---

## Description

Key             |Data Type     |Required  |Description
-------------   |---------     |------    |----
`_id`                 |<span style="color:rgb(0, 72, 189)"> objectId() </span>   | <span style="color:rgb(0, 72, 189)">  auto  </span> | <span style="color:rgb(0, 72, 189)">  unique database id  </span>
`class`               |<span style="color:rgb(0, 72, 189)">  string  </span>     | <span style="color:rgb(0, 72, 189)">  auto  </span> | <span style="color:rgb(0, 72, 189)">  class of node  </span>
`version_schema`      |<span style="color:rgb(0, 72, 189)">  string  </span>     | <span style="color:rgb(0, 72, 189)">  auto  </span> | <span style="color:rgb(0, 72, 189)">  schema version; Ex: "v0.1"  </span>
`version_control`     |                                                          |                                                     | <span style="color:rgb(0, 72, 189)">  version control object  </span>
`version_control/_id` |<span style="color:rgb(0, 72, 189)">  objectId()  </span> | <span style="color:rgb(0, 72, 189)">  auto  </span> | <span style="color:rgb(0, 72, 189)">  reference id to node history  </span>
`version_control/num` |<span style="color:rgb(0, 72, 189)">  string  </span>     | <span style="color:rgb(0, 72, 189)">auto  </span>   | <span style="color:rgb(0, 72, 189)">  type of node ; Ex: "group"  </span>
`last_modified`       |<span style="color:rgb(0, 72, 189)">  datetime  </span>   | <span style="color:rgb(0, 72, 189)">auto  </span>   | <span style="color:rgb(0, 72, 189)">  last modified datetime  </span>
`created`             |<span style="color:rgb(0, 72, 189)">  datetime  </span>   | <span style="color:rgb(0, 72, 189)">auto  </span>   | <span style="color:rgb(0, 72, 189)">  datetime created  </span>
`name`                    | string        | required  | name of experiment
`materials`               | list[dict]    |           | [material nodes](../data-models/Materials_P.md)
`materials/_id`           | objectId()    | auto      | id of material
`materials/name`          | string        | auto      | name of material
`materials/id_proc`       | objectId()    | auto      | id of process that the material points to
`materials/id_data`       | objectId()    | auto      | id of data that the material points to
`process`                 | list[dict]    |           | [process nodes](../data-models/Process.md)
`process/_id`             | objectId()    | auto      | id of process
`process/name`            | string        | auto      | name of process
`process/id_mat`          | objectId()    | auto      | id of ingerdients the process point to 
`sample`                  | list[dict]    |           | [sample nodes](../data-models/Sample.md)
`sample/_id`              | objectId()    | auto      | id of sample
`sample/name`             | string        | auto      | name of sample
`sample/id_link`          | objectId()    | auto      | id of the material the sample points 
`data`                    | list[dict]    |           | [data nodes](../data-models/Data.md)
`data/_id`                | objectId()    | auto      | id of data
`data/name`               | string        | auto      | name of data
`data/id_link`            | objectId()    | auto      | id of the node the data points


### Attributes

Attributes are optional properties that can be associated with this node. The following list is the officially supported
keys. Users may define their own keys by placing a '+' in front of their custom key.

Key                | Data Type      | Description
-------------      |---------       |----
`reference`        | string         | reference for this experiment [DOI: digital object identifier](https://www.doi.org/)
`note`             | string         | free-form space to store any text


---

## Example

[Example](../Example/#experiment-1-anionic-polymerization-of-styrene)