# Collections

The 'collection' node also for the grouping of experiments.

**Features:**

* collections within collections are allowed
* collection can reference experiments, collections
* required information
    * name
* optional information
    * experiments (CRIPT node)
    * child collection (CRIPT node)
    * notes
* auto generate/update:
    * _id
    * class
    * ver_sch
    * ver_con (& all child) <-- update with version control node
    * date (& all child)
    * numb_expt 


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
`date_created`        |<span style="color:rgb(0, 72, 189)">  datetime  </span>   | <span style="color:rgb(0, 72, 189)">auto  </span>   | <span style="color:rgb(0, 72, 189)">  datetime created  </span>
`date_last_mod`       |<span style="color:rgb(0, 72, 189)">  datetime  </span>   | <span style="color:rgb(0, 72, 189)">auto  </span>   | <span style="color:rgb(0, 72, 189)">  last modified datetime  </span>
`name`                |string       | required  | name of collection

### Attributes

Attributes are optional properties that can be associated with this node. The following list is the officially supported
keys. Users may define their own keys by placing a '+' in front of their custom key.

Key                     | Data Type      | Description
-------------           |---------       | ----
`number_experiments`    | int            | number of experiments in collection
`experiment`            | list[dict]     | [experiment nodes](../data-models/Experiments.md)
`experiment\_id`        | objectId()     | id of experiment
`experiment\name`       | string         | name of experiment
`experiment\date`       | datetime       | date of experiment
`child_collection`      | list[dict]     | [collection nodes](../data-models/Collections.md)
`child_collection\_id`  | objectId()     | id of collection
`child_collection\name` | string         | name of collection
`child_collection\date` | datetime       | date collection created
`note`                  | string         | free-form space to store any text


---

## Example

```json
{
  "_id": "507f191e810c19729de861ec",
  "type": "coll",
  "ver_sch": "v0.1",
  "ver_con": {
    "_id": "507f191e810c19729de861cb",
    "num": "v2.1"
  },
  "date": [
    {"created": 1612881183},
    {"last_mod": 1612881123}
  ],
  "notes": "",
  "users": [
    {"_id": "507f191e810c19729de860ec", "name": "Dylan W", "perm": "w"}
  ],
  "name": "ROMP Kinetics",
  "num_expt": 3,
  "expt": [
    {"_id": "507f191e810c19729de860em", "name": "ROMP monomer order kinetic study", "date": 1612886423},
    {"_id": "507f191e810c19729de860en", "name": "ROMP pyridine order kinetic study", "date": 1612886423},
    {"_id": "507f191e810c19729de860ej", "name": "ROMP catalyst kinetic study", "date": 1612886423}
  ],
  "attr": {
    "users": [
      {"_id": "507f191e810c19729de860ec", "name": "Dylan W"}
    ],
    "group": [
      {"_id": "507f191e810c19729de860em", "name": "UIUC"}
    ]
  }
}
```



