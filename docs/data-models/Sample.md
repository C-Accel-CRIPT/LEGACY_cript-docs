# Sample

The 'sample' node contains procedure and property information. A sample can be anything from that doesn't
result in a change in the "identity".

**Features:**

* sample node points to data
* required information
    * name
    * procedure
* optional information
    * data (CRIPT node)
    * conditions
    * properties
    * note
* auto generate/update:
    * _id
    * class
    * ver_sch
    * ver_con (& all child) <-- update with version control node
    * date (& all child)


**App features to support this node:**

* allow additional optional information in `cond` section given that it begins with +
* units are not stored for officially supported data as all official values are converted to database standard prior to storage

## JSON Schema

```json
{
  "_id": objectId(),
  "class": "sample",
  "version_schema": string,
  "version_control": {
    "_id": objectId(),
    "num": string
  },
  "date_created": datetime,
  "date_last_mod": datetime,
  "name": string,
  "procedure": string,
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
`name`                    | string        | required  | name of process
`procedure`               | string        | required  | written procedure for the process


### Attributes

Attributes are optional properties that can be associated with this node. The following list is the officially supported
keys. Users may define their own keys by placing a '+' in front of their custom key.

Key                | Data Type    | Description
-------------      | ---------    | ----
`data`             | list[dict]   | [data node](../data-models/Data.md)
`data/_id`         | objectId()   | id of data
`data/name`        | string       | name of data
`data/type`        | string       | type of data
`condition`        | list[dict]   | [see condition section](../Process/#conditions)
`properties`       | list[dict]   | [see properties section](../Process/#properties)
`note`             | string       | free-form space to store any text


### Conditions

Conditions are any process variable that the user would like to explicitly expose. Conditions such as temperature,
pressure, or reaction times are examples. The conditions are stored in a dictionary. Units are only used for user
defined attributes which begin with a `+`.

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

`key`                 | Units     | Description
-------------         | ----      | ----
`time`                | min       | time
`temperature`         | degC      | temperature
`pressure`            | kPa       | pressure (absolute)


### Properties

For information on properties see [Materials node](../Materials_P/#properties)


---

## Example

```json
{
  "_id": "507f191e810c19729de860ec",
  "type": "process",
  "ver_sch": "v0.1",
  "ver_con": {
    "_id": "507f191e810c19729de860cb",
    "num": "v0.1"
  },
  "date": [
    {"created": 1612889183},
    {"last_mod": 1612889123}
  ],

}
```

