# Groups

The 'group' node contains data related to a group which is a collection of users.

Example of groups are MIT, Citrine, CRIPT development team, or a research group.
They can be big organizations or small groups of only two users.

**Features:**

* groups within groups are allowed
* groups can reference groups, collections, publications
* required information  
    * name
* optional information
    * collection list (CRIPT node)
    * child group (CRIPT node)
    * Publication (CRIPT node)
    * website
    * email
    * notes
* auto generate/update:
    * _id
    * class
    * ver_sch
    * ver_con (& all child) <-- update with version control node
    * date (& all child)

  
**App features to support this node:**

* a page to fill out: name, website, email, etc.
* a tool to look up tool for groups, and publications
* allow additional optional information in attribute section given that it begins with +

## JSON Schema

```json
{
  "_id": objectId(),
  "class": "group",
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
  "coll": [
    {"_id": objectId(), "name": string}
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
`ver_sch`             |<span style="color:rgb(0, 72, 189)">  string  </span>     | <span style="color:rgb(0, 72, 189)">  auto  </span> | <span style="color:rgb(0, 72, 189)">  schema version; Ex: "v0.1"  </span>
`ver_con`             |                                                          |                                                     | <span style="color:rgb(0, 72, 189)">  version control object  </span>
`ver_con/_id`         |<span style="color:rgb(0, 72, 189)">  objectId()  </span> | <span style="color:rgb(0, 72, 189)">  auto  </span> | <span style="color:rgb(0, 72, 189)">  reference id to node history  </span>
`ver_con/num`         |<span style="color:rgb(0, 72, 189)">  string  </span>     | <span style="color:rgb(0, 72, 189)">auto  </span>   | <span style="color:rgb(0, 72, 189)">  type of node ; Ex: "group"  </span>
`date`                |                                                          |                                                     | <span style="color:rgb(0, 72, 189)">  datetime object  </span>
`date/created`        |<span style="color:rgb(0, 72, 189)">  datetime  </span>   | <span style="color:rgb(0, 72, 189)">auto  </span>   | <span style="color:rgb(0, 72, 189)">  datetime created  </span>
`type/last_mod`       |<span style="color:rgb(0, 72, 189)">  datetime  </span>   | <span style="color:rgb(0, 72, 189)">auto  </span>   | <span style="color:rgb(0, 72, 189)">  last modified datetime  </span>
`name`                | string          | required      | name of group


### Attributes

Attributes are optional properties that can be associated with this node. The following list is the officially supported
keys. Users may define their own keys by placing a '+' in front of their custom key.

Key                   | Data Type       | Description
-------------         |---------        |----
`coll`                | list[dict]      | [collection nodes](../data-models/Collections.md)
`coll\_id`            | objectId()      | id of collection
`coll\name`           | string          | name of collection
`coll\date`           | datetime        | date collection created
`chi_group`           | list[dict]      | [child group](../data-models/Groups.md)
`chi_group\_id`       | objectId()      | id of child group
`chi_group\name`      | string          | name of child group
`pub`                 | list[dict]      | [publication node](../data-models/Publications.md) that this experiment was a part of
`pub\_id`             | objectId()      | id for publication
`pub\title`           | string          | publication title
`web`                 | string          | website of group
`email`               | string          | group email address
`notes`               | string          | free-form space to store any text

---

## Example

```json
{
  "_id": "507f191e810c19729de860ea",
  "type": "group",
  "ver_sch": "v0.1",
  "ver_con": {
    "_id": "507f191e810c19729de860eb",
    "num": "v0.1"
  },
  "date": [
    {"created": 1612889182},
    {"last_mod": 1612889122}
  ],
  "notes": "CRIPT development team is funded by NSF Convergence Accelerator.",
  "name": "CRIPT",
  "owner": {"_id": "507f191e810c19729de860ec", "name": "Dylan W"},
  "users_num": 5,
  "users_list": [
    {"_id": "507f191e810c19729de860ec", "name": "Dylan W"},
    {"_id": "507f191e810c19729de860ed", "name": "Eric M"},
    {"_id": "507f191e810c19729de860ee", "name": "Chris B"},
    {"_id": "507f191e810c19729de860ef", "name": "Tzyy-Shyang L"},
    {"_id": "507f191e810c19729de860eg", "name": "Vinay H"}
  ],
  "attr": {
    "par_group": [
      {"_id": "507f191e810c19729de860em", "name": "MIT"},
      {"_id": "507f191e810c19729de860en", "name": "Citrine"}
    ],
    "pub": [
      {"_id": "507f191e810c19729de860em", "title": "CRIPT database"},
      {"_id": "507f191e810c19729de860em", "title": "bigSMILES"},
      {"_id": "507f191e810c19729de860em", "title": "PolyDat"}
    ],
    "web": "https://cript.mit.edu/",
    "email": "cript@mit.edu"
  }
}
```
