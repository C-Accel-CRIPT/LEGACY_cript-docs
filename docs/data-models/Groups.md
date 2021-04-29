# Groups

The 'group' node contains data related to a group. Example of groups are MIT, Citrine, CRIPT development team, or a research group.


**Features:**

* groups within groups are allowed (max depth 20)
* groups can reference groups, collections, publications
* required information  
    * name
* optional information
    * collection  (CRIPT node)
    * parent group (CRIPT node)
    * publication (CRIPT node)
    * website
    * email
    * notes
* auto-generate/update:
    * _id
    * class
    * version_schema
    * version_control (& all child) <-- update with version control node
    * date (& all child)
  
## JSON Schema

```json
{
  "_id": objectId(),
  "class": "group",
  "version_schema": string,
  "version_control": {
    "_id": objectId(),
    "num": string
  },
  "last_modified": datetime,
  "created": datetime,
  "name": string,
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
`name`                | string          | required      | name of group


### Attributes

Attributes are optional properties that can be associated with this node. The following list is the officially supported
keys. Users may define their own keys by placing a '+' in front of their custom key.

Key                   | Data Type       | Description
-------------         |---------        |----
`collection`          | list[dict]      | [collection nodes](../data-models/Collections.md)
`collection\_id`      | objectId()      | id of collection
`collection\name`     | string          | name of collection
`collection\created`  | datetime        | date of collection
`parent_group`        | list[dict]      | [parent group](../data-models/Groups.md)
`parent_group\_id`    | objectId()      | id of parent group
`parent_group\name`   | string          | name of parent group
`publication`         | list[dict]      | [publications the user authored](../data-models/Publications.md)
`publication\_id`     | objectId()      | id of publication
`publication\title`   | string          | title of publication
`website`             | string          | website of group
`email`               | string          | group email address
`notes`               | string          | free-form space to store any text

---

## Example

[Groups Example](../Example/#group)


