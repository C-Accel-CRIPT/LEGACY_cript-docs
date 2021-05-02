# Simulation

** Under Construction **

The 'simulation' node contains ....



**Features:**

* required information
    * name
* optional information

    * notes
* auto generate:
    * _id
    * class
    * version_schema
    * version_control (& all child) <-- update with version control node
  

## JSON Schema


```json
{
  "_id": objectId(),
  "class": "material_p",
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


## Description

Key                   |Data Type     |Required  |Description
-------------         |---------     |------    |----
`_id`                 |<span style="color:rgb(0, 72, 189)"> objectId() </span>   | <span style="color:rgb(0, 72, 189)">  auto  </span> | <span style="color:rgb(0, 72, 189)">  unique database id  </span>
`class`               |<span style="color:rgb(0, 72, 189)">  string  </span>     | <span style="color:rgb(0, 72, 189)">  auto  </span> | <span style="color:rgb(0, 72, 189)">  class of node; "material_p"  </span>
`version_schema`      |<span style="color:rgb(0, 72, 189)">  string  </span>     | <span style="color:rgb(0, 72, 189)">  auto  </span> | <span style="color:rgb(0, 72, 189)">  schema version; Ex: "v0.1"  </span>
`version_control`     |                                                          |                                                     | <span style="color:rgb(0, 72, 189)">  version control object  </span>
`version_control/_id` |<span style="color:rgb(0, 72, 189)">  objectId()  </span> | <span style="color:rgb(0, 72, 189)">  auto  </span> | <span style="color:rgb(0, 72, 189)">  reference id to node history  </span>
`version_control/num` |<span style="color:rgb(0, 72, 189)">  string  </span>     | <span style="color:rgb(0, 72, 189)">auto  </span>   | <span style="color:rgb(0, 72, 189)">  type of node ; Ex: "group"  </span>
`last_modified`       |<span style="color:rgb(0, 72, 189)">  datetime  </span>   | <span style="color:rgb(0, 72, 189)">auto  </span>   | <span style="color:rgb(0, 72, 189)">  last modified datetime  </span>
`created`             |<span style="color:rgb(0, 72, 189)">  datetime  </span>   | <span style="color:rgb(0, 72, 189)">auto  </span>   | <span style="color:rgb(0, 72, 189)">  datetime created  </span>
`name`                | string        | required  | name of chemical


### Attributes

Attributes are optional properties that can be associated with this node. The following list is the officially supported
keys. Users may define their own keys by placing a '+' in front of their custom key.

Key                | Data Type    | Units    | Description
-------------      |---------     |------    | ----
`keywords`         | list[string] |          | [see keywords section below](../Simulation/#keywords)



### Keywords

Keywords are an optional field that allow users to classify the material. Selecting multiple keywords is allowed.

Keyword             | Description  
----                | ----



---

## Example

