# Groups

The 'group' node contains data related to the group that users are members of.

## JSON Schema

```json
{
  "id_": objectId(),
  "type": "group",
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
  "owner": {"id_": objectId(), "name": string},
  "users_num": double,
  "users_list": [
    {"id_": objectId(), "name": string}
  ],
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
`users`         |     |      |<span style="color:rgb(12, 145, 3)">  user permissions   </span>
`users/id_`           |<span style="color:rgb(12, 145, 3)">  objectId()   </span>|<span style="color:rgb(12, 145, 3)">  auto   </span>|<span style="color:rgb(12, 145, 3)">  user id  </span>
`users/name`          |<span style="color:rgb(12, 145, 3)">  string  </span>|<span style="color:rgb(12, 145, 3)">  auto   </span>|<span style="color:rgb(12, 145, 3)">  user name  </span>
`users/perm`          |<span style="color:rgb(12, 145, 3)">  string  </span>|<span style="color:rgb(12, 145, 3)">  auto   </span>|<span style="color:rgb(12, 145, 3)">  permission level; [r: read, w: write, a: append] </span>
`name`               |string        |auto      |name of group
`owner`               |string        |auto      |type of node ; Ex: "group"
`users_num`            |              |          |[number of users in the group](../data-models/Users.md)
`users_list`           |string        |auto      |list of users in the group
`users_list/id_`       |objectId()    |auto      |id of user
`users_list/name`      |string        |auto      |name of user
`attr`                 |list          |auto      |see attributes section

### Attributes

Attributes are optional properties that can be associated with this node. The following list is the officially supported
keys. Users may define their own keys by placing a '+' in front of their custom key.

Key                   |Data Type     |Description
-------------         |---------     |----
`par_group`           |              | [parent group](../data-models/Groups.md)
`par_group\id_`       |objectId()    | id of parent group
`par_group\name`      |string        | name of parent group
`chi_group`           |              | [child group](../data-models/Groups.md)
`chi_group\id_`       |objectId()    | id of child group
`chi_group\name`      |string        | name of child group
`pub`                 |              | [publication node](../data-models/Publications.md) that this experiment was a part of
`pub\id_`             |objectId()    | id for publication
`pub\title`           |string        | publication title
`web`                 |string        | website of group
`email`               |string        | group email address

---

## Example

```json
{
  "id_": "507f191e810c19729de860ea",
  "type": "group",
  "ver_sch": "v0.1",
  "ver_con": {
    "id_": "507f191e810c19729de860eb",
    "num": "v0.1"
  },
  "date": [
    {"created": 1612889182},
    {"last_mod": 1612889122}
  ],
  "notes": "CRIPT development team is funded by NSF Convergence Accelerator.",
  "users": [
    {"id_": "507f191e810c19729de860ec", "name": "Dylan W", "perm": "w"},
    {"id_": "507f191e810c19729de860ed", "name": "Eric M", "perm": "a"},
    {"id_": "507f191e810c19729de860ee", "name": "Chris B", "perm": "r"}
  ],
  "name": "CRIPT",
  "owner": {"id_": "507f191e810c19729de860ec", "name": "Dylan W"},
  "users_num": 5,
  "users_list": [
    {"id_": "507f191e810c19729de860ec", "name": "Dylan W"},
    {"id_": "507f191e810c19729de860ed", "name": "Eric M"},
    {"id_": "507f191e810c19729de860ee", "name": "Chris B"},
    {"id_": "507f191e810c19729de860ef", "name": "Tzyy-Shyang L"},
    {"id_": "507f191e810c19729de860eg", "name": "Vinay H"}
  ],
  "attr": {
    "par_group": [
      {"id_": "507f191e810c19729de860em", "name": "MIT"},
      {"id_": "507f191e810c19729de860en", "name": "Citrine"},
      {"id_": "507f191e810c19729de860eo", "name": "NIST"},
      {"id_": "507f191e810c19729de860ep", "name": "Dow"}
    ],
    "chi_group": [
      {"id_": "507f191e810c19729de860eq", "name": "chemists"},
      {"id_": "507f191e810c19729de860er", "name": "engineers"}
    ],
    "pub": [
      {"id_": "507f191e810c19729de860em", "title": "Kinetic Study of Living Ring-Opening Metathesis Polymerization"}
    ],
    "web": "https://cript.mit.edu/",
    "email": "cript@mit.edu"
  }
}
```
