# User

The 'user' node contains data related to the user.

## JSON Schema

```json
{
  "id_": objectId(),
  "type": "user",
  "ver_sch": string,
  "ver_con": {
    "id_": objectId(),
    "num": string
  },
  "date": [
    {"created": datetime},
    {"last_mod": datetime}
  ],
  "notes": string,
  "users": [
    {"id_": objectId(), "name": string, "perm": string}
  ],
  "name": string,
  "email": string,
  "attr": {
    "see attributes": "for details"
  }
}
```

---

## Description

Key             |Data Type     |Required  |Description
-------------   |---------     |------    |----
`id_`          |<span style="color:rgb(0, 72, 189)"> objectId() </span>|<span style="color:rgb(0, 72, 189)">  auto  </span>|<span style="color:rgb(0, 72, 189)">  unique database id  </span>
`type`          |<span style="color:rgb(0, 72, 189)">  string  </span> |<span style="color:rgb(0, 72, 189)">  auto  </span>|<span style="color:rgb(0, 72, 189)">  type of node ; Ex: "group"  </span>
`ver_sch`       |<span style="color:rgb(0, 72, 189)">  string  </span>|<span style="color:rgb(0, 72, 189)">  auto  </span>|<span style="color:rgb(0, 72, 189)">  schema version; Ex: "v0.1"  </span>
`ver_con`       |              |          |<span style="color:rgb(0, 72, 189)">  version control object  </span>
`ver_con/id_`   |<span style="color:rgb(0, 72, 189)">  objectId()  </span>|<span style="color:rgb(0, 72, 189)">  auto  </span>|<span style="color:rgb(0, 72, 189)">  reference id to node history  </span>
`ver_con/num`   |<span style="color:rgb(0, 72, 189)">  string  </span>|<span style="color:rgb(0, 72, 189)">auto  </span>|<span style="color:rgb(0, 72, 189)">  type of node ; Ex: "group"  </span>
`date`          |              |          |<span style="color:rgb(0, 72, 189)">  datetime object  </span>
`date/created`  |<span style="color:rgb(0, 72, 189)">  datetime  </span>|<span style="color:rgb(0, 72, 189)">auto  </span>|<span style="color:rgb(0, 72, 189)">  datetime created  </span>
`type/last_mod` |<span style="color:rgb(0, 72, 189)">  datetime  </span>|<span style="color:rgb(0, 72, 189)">auto  </span>|<span style="color:rgb(0, 72, 189)">  last modified datetime  </span>
`notes`         |<span style="color:rgb(0, 72, 189)">  string  </span>|<span style="color:rgb(0, 72, 189)">auto  </span> |<span style="color:rgb(0, 72, 189)">  free-form space to store any text  </span>
`users`               |     |      |<span style="color:rgb(12, 145, 3)">  user permissions </span>
`users/id_`           |<span style="color:rgb(12, 145, 3)">  objectId()   </span>|<span style="color:rgb(12, 145, 3)">  auto   </span>|<span style="color:rgb(12, 145, 3)">  user id  </span>
`users/name`          |<span style="color:rgb(12, 145, 3)">  string  </span>|<span style="color:rgb(12, 145, 3)">  auto   </span>|<span style="color:rgb(12, 145, 3)">  user name  </span>
`users/perm`          |<span style="color:rgb(12, 145, 3)">  string  </span>|<span style="color:rgb(12, 145, 3)">  auto   </span>|<span style="color:rgb(12, 145, 3)">  permission level; [r: read, w: write, a: append]  </span>
`name`               |string        |auto      |name of group
`email`               |string   |required | author's email address
`attr`                 |list        |auto      |see attributes section
*username  |
*password  |

### Attributes

Attributes are optional properties that can be associated with this node. The following list is the officially supported
keys. Users may define their own keys by placing a '+' in front of their custom key.

Key                   |Data Type      |Description
-------------         |---------      |----
`phone`               |string         | phone number (###-###-####)
`web`                 |string         | website
`twitter`             |string         | twitter account
`orcid`               |string         | [ORCID number](https://orcid.org/)
`organization`        |string         | author's organization
`position`            |string         | author's position in organization
`group`               |               | [groups that the user belongs to](../data-models/Groups.md)
`group\id_`           |objectId()     | id of group
`group\name`          |string         | name of group
`pub`                 |               | [publications the user authored](../data-models/Publications.md)
`pub\id_`             |objectId()     | id of publication
`pub\title`           |string         | title of publication
`expt`                |               | [experiment nodes](../data-models/Experiments.md)
`expt\id_`            |objectId()     | id of experiments
`expt\name`           |string         | name of experiments
`expt\date`           |datetime       | date of experiments

---

## Example

```json
{
  "id_": "507f191e810c19729de860ec",
  "type": "user",
  "ver_sch": "v0.1",
  "ver_con": {
    "id_": "507f191e810c19729de860cb",
    "num": "v0.1"
  },
  "date": [
    {"created": 1612889183},
    {"last_mod": 1612889123}
  ],
  "notes": "",
  "users": [
    {"id_": "507f191e810c19729de860ec", "name": "Dylan W", "perm": "w"}
  ],
  "name": "Dylan W",
  "email": "dylan@mit.edu",
  "attr": {
    "phone": "123-456-7890",
    "orcid": "0000-0000-0000-0001",
    "organization": "MIT",
    "position": "Research Assistant",
    "group": [
      {"id_": "507f191e810c19729de860em", "name": "MIT"},
      {"id_": "507f191e810c19729de860en", "name": "CRIPT"}
    ],
    "pub": [
      {"id_": "507f191e810c19729de860eq", "name": "Recent trends in catalytic polymerizations"},
      {
        "id_": "507f191e810c19729de860er",
        "name": "Kinetic study of living ring-opening metathesis polymerization with third-generation Grubbs catalysts"
      }
    ],
    "expt": [
      {"id_": "507f191e810c19729de860em", "name": "Anionic polymerization", "date": 1612886423},
      {"id_": "507f191e810c19729de860en", "name": "ATRP of styrene with CuCl", "date": 1612886423},
      {"id_": "507f191e810c19729de860ej", "name": "ROMP catalyst kinetic study part 1", "date": 1612886423}
    ]
  }
}
```
