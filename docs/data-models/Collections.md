# Collections

The 'collection' node also for the grouping of experiments. Their purpose is to provide a hierarchical organization
to non-linear, but related, processes (like running multiple reactions for optimizations, kinetics, etc.). For linear
processes (like block copolymer synthesis) consider grouping it within a single experiment. 

**Features:**

* collections within collections are allowed (max depth 20)
* collection can reference experiments, collections
* required information
    * name
* optional information
    * experiments (CRIPT node)
    * child collection (CRIPT node) 
    * notes
* auto-generate/update:
    * _id
    * class
    * version_schema
    * version_control (& all child) <-- update with version control node
    * date (& all child)
    * number_experiments 


**App features to support this node:**

* a page to fill out collection details
* a tool to look up experiments, or enter _id
* a similar look up tool for users, and groups
* allow additional optional information in attribute section given that it begins with +

## JSON Schema

```json
{
  "_id": objectId(),
  "class": "coll",
  "version_schema": string,
  "version_control": {
    "_id": objectId(),
    "num": string
  },
  "date_created": datetime,
  "date_last_mod": datetime,
  "name": string,
  "number_experiments": interager,
  "optional attributes"
}
```

---

## Description

Key                   |Data Type     |Required  |Description
-------------         |---------     |------    |----
`_id`                 |<span style="color:rgb(0, 72, 189)"> objectId() </span>   | <span style="color:rgb(0, 72, 189)">  auto  </span> | <span style="color:rgb(0, 72, 189)">  unique database id  </span>
`class`               |<span style="color:rgb(0, 72, 189)">  string  </span>     | <span style="color:rgb(0, 72, 189)">  auto  </span> | <span style="color:rgb(0, 72, 189)">  class of node  </span>
`version_schema`      |<span style="color:rgb(0, 72, 189)">  string  </span>     | <span style="color:rgb(0, 72, 189)">  auto  </span> | <span style="color:rgb(0, 72, 189)">  schema version; Ex: "v0.1"  </span>
`version_control`     |                                                          |                                                     | <span style="color:rgb(0, 72, 189)">  version control object  </span>
`version_control/_id` |<span style="color:rgb(0, 72, 189)">  objectId()  </span> | <span style="color:rgb(0, 72, 189)">  auto  </span> | <span style="color:rgb(0, 72, 189)">  reference id to node history  </span>
`version_control/num` |<span style="color:rgb(0, 72, 189)">  string  </span>     | <span style="color:rgb(0, 72, 189)">auto  </span>   | <span style="color:rgb(0, 72, 189)">  type of node ; Ex: "group"  </span>
`last_modified`       |<span style="color:rgb(0, 72, 189)">  datetime  </span>   | <span style="color:rgb(0, 72, 189)">auto  </span>   | <span style="color:rgb(0, 72, 189)">  last modified datetime  </span>
`created`             |<span style="color:rgb(0, 72, 189)">  datetime  </span>   | <span style="color:rgb(0, 72, 189)">auto  </span>   | <span style="color:rgb(0, 72, 189)">  datetime created  </span>
`name`                |string       | required         | name of collection
`number_experiments`  | int         | auto-generated   | number of experiments in collection

### Attributes

Attributes are optional properties that can be associated with this node. The following list is the officially supported
keys. Users may define their own keys by placing a '+' in front of their custom key.

Key                         | Data Type      | Description
-------------               |---------       | ---- 
`experiment`                | list[dict]     | [experiment nodes](../data-models/Experiments.md)
`experiment\_id`            | objectId()     | id of experiment
`experiment\name`           | string         | name of experiment
`experiment\created`        | datetime       | date the experiment was created
`child_collection`          | list[dict]     | [collection nodes](../data-models/Collections.md)
`child_collection\_id`      | objectId()     | id of collection
`child_collection\name`     | string         | name of collection
`child_collection\created`  | datetime       | date collection created
`note`                      | string         | free-form space to store any text


---

## Example

[Collection Example](../Example/#collection)



