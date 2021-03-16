# User

The 'user' node contains data related to the user. Anyone who interacts with the database can be a user.

**Features:**

* user can reference groups, collections, publications, and experiments
* required information
    * name
    * email
* optional information
    * group (CRIPT node)
    * publications (CRIPT node)
    * collections (CRIPT node)
    * experiments (CRIPT node)
    * phone
    * website
    * twitter handle
    * ORCID #
    * organization
    * notes
* auto generate/update:
    * _id
    * class
    * ver_sch
    * ver_con (& all child) <-- update with version control node
    * date (& all child)

**App features to support this node:**

* a page to fill out: name, email, etc
* a tool to look up group, or enter _id
* a similar look up tool for experiments, collections, and publications
* allow additional optional information in attribute section given that it begins with +

## JSON Schema

```json
{
  "_id": objectId(),
  "class": "user",
  "version_schema": string,
  "version_control": {
    "_id": objectId(),
    "num": string
  },
  "date_created": datetime,
  "date_last_mod": datetime,
  "name": string,
  "email": string,
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
`date_created`        |<span style="color:rgb(0, 72, 189)">  datetime  </span>   | <span style="color:rgb(0, 72, 189)">auto  </span>   | <span style="color:rgb(0, 72, 189)">  datetime created  </span>
`date_last_mod`       |<span style="color:rgb(0, 72, 189)">  datetime  </span>   | <span style="color:rgb(0, 72, 189)">auto  </span>   | <span style="color:rgb(0, 72, 189)">  last modified datetime  </span>
`name`                | string        | required      | name of user
`email`               | string        | required      | user email address


### Attributes

Attributes are optional properties that can be associated with this node. The following list is the officially supported
keys. Users may define their own keys by placing a '+' in front of their custom key.

Key                   | Data Type      | Description
-------------         |---------       |----
`group`               | list[dict]     | [groups that the user belongs to](../data-models/Groups.md)
`group\_id`           | objectId()     | id of group
`group\name`          | string         | name of group
`publication`         | list[dict]     | [publications the user authored](../data-models/Publications.md)
`publication\_id`     | objectId()     | id of publication
`publication\title`   | string         | title of publication
`experiment`          | list[dict]     | [experiment nodes](../data-models/Experiments.md)
`experiment\_id`      | objectId()     | id of experiment
`experiment\name`     | string         | name of experiment
`experiment\date`     | datetime       | date of experiment
`collection`          | list[dict]     | [collection nodes](../data-models/Collections.md)
`collection\_id`      | objectId()     | id of collection
`collection\name`     | string         | name of collection
`collection\date`     | datetime       | date of collection
`phone`               | string         | phone number (###-###-####)
`web`                 | string         | website
`twitter`             | string         | twitter handle
`orcid`               | string         | [ORCID number](https://orcid.org/)
`organization`        | string         | author's organization
`position`            | string         | author's position in organization
`note`                | string         | free-form space to store any text

---

## Example

```json
{
  "_id": "507f191e810c19729de860ec",
  "type": "user",
  "ver_sch": "v0.1",
  "ver_con": {
    "_id": "507f191e810c19729de860cb",
    "num": "v0.1"
  },
  "date": [
    {"created": 1612889183},
    {"last_mod": 1612889123}
  ],
  "notes": "",
  "users": [
    {"_id": "507f191e810c19729de860ec", "name": "Dylan W", "perm": "w"}
  ],
  "name": "Dylan W",
  "email": "dylan@cript.edu",
  "attr": {
    "phone": "123-456-7890",
    "orcid": "0000-0000-0000-0001",
    "organization": "MIT",
    "position": "Research Assistant",
    "group": [
      {"_id": "507f191e810c19729de860em", "name": "MIT"},
      {"_id": "507f191e810c19729de860en", "name": "CRIPT"}
    ],
    "pub": [
      {"_id": "507f191e810c19729de860eq", "name": "Recent trends in catalytic polymerizations"},
      {
        "_id": "507f191e810c19729de860er",
        "name": "Kinetic study of living ring-opening metathesis polymerization with third-generation Grubbs catalysts"
      }
    ],
    "expt": [
      {"_id": "507f191e810c19729de860em", "name": "Anionic polymerization", "date": 1612886423},
      {"_id": "507f191e810c19729de860en", "name": "ATRP of styrene with CuCl", "date": 1612886423},
      {"_id": "507f191e810c19729de860ej", "name": "ROMP catalyst kinetics low conc", "date": 1612886423},
      {"_id": "507f191e810c19729de860er", "name": "ROMP catalyst kinetics high conc", "date": 1612886426},
      {"_id": "507f191e810c19729de860er", "name": "ROMP monomer kinetics", "date": 1612886426}
    ]
  },
  "coll": [
    {"_id": "507f191e810c19729de860em", "name": "ROMP kinetic study", "date": 1612886423, "num_expt": 3}
  ]
}
```

