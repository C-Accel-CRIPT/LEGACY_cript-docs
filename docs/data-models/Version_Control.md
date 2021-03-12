# Version Control

The version control implemented in CRIPT is [JSON Patch](http://jsonpatch.com/). JSON Patch is a format for describing
changes to a JSON document. Using a patch approach avoids saving the whole document when only a part of it has changed.
The file can only be created and appended to; no deletions allowed.



** how do we do branching and merging?**

## JSON Schema

```json
{
  "_id": objectId(),
  "type": "vs_###",
  "ver_sch": string,
  "date": [
    {"created": datetime},
    {"last_mod": datetime}
  ],
  "notes": string,
  "_idchild": objectId(),
  "patches": [
    {
      "_id": objectId()",
      "name_": string,
      "date": datetime,
      "notes": string,
      "ver_num": string,
      "changes": [
        {"op": string, "path": string, "value": any}
      ]
    }
  ]
}
```

---

## Description

Key                   |Data Type     |Required  |Description
-------------         |---------     |------    |----
`_id`                 |<span style="color:rgb(0, 72, 189)"> objectId() </span>|<span style="color:rgb(0, 72, 189)">  auto  </span>|<span style="color:rgb(0, 72, 189)">  unique database id  </span>
`type`                |<span style="color:rgb(0, 72, 189)">  string  </span> |<span style="color:rgb(0, 72, 189)">  auto  </span>|<span style="color:rgb(0, 72, 189)">  type of node ; Ex: "group"  </span>
`ver_sch`             |<span style="color:rgb(0, 72, 189)">  string  </span>|<span style="color:rgb(0, 72, 189)">  auto  </span>|<span style="color:rgb(0, 72, 189)">  schema version; Ex: "v0.1"  </span>
`date`                |              |          |<span style="color:rgb(0, 72, 189)">  datetime object  </span>
`date/created`        |<span style="color:rgb(0, 72, 189)">  datetime  </span>|<span style="color:rgb(0, 72, 189)">auto  </span>|<span style="color:rgb(0, 72, 189)">  datetime created  </span>
`type/last_mod`       |<span style="color:rgb(0, 72, 189)">  datetime  </span>|<span style="color:rgb(0, 72, 189)">auto  </span>|<span style="color:rgb(0, 72, 189)">  last modified datetime  </span>
`notes`               |<span style="color:rgb(0, 72, 189)">  string  </span>|<span style="color:rgb(0, 72, 189)">auto  </span> |<span style="color:rgb(0, 72, 189)">  free-form space to store any text  </span>
`_idchild`            | objectId()      | auto      | id of node that the file is storing patches for
`patches`             |                 |           | document history
`patches/_id`         | string          | auto      | id of user who made change
`patches/name`        | string          | auto      | name of user who made change
`patches/data`        | datetime        | auto      | date and time when changes were made
`patches/notes`       | string          | optional  | notes about change
`patches/ver_num`     | string          | auto      | version number of patch
`patches/changes`     | dict            | auto      | [JSON Patch](http://jsonpatch.com/)

---

## Example

```json
{
  "_id": "507f191e810c19729de861ec",
  "type": "vs_mat",
  "ver_sch": "v0.1",
  "date": [
    {"created": 1612881183},
    {"last_mod": 1612881123}
  ],
  "notes": "",
  "_idchild": "507f191e810c19729de861ec",
  "patches": [
    {
      "_id": "507f191e810c19729de860ec",
      "name_": "Dylan W",
      "date": 1612881123,
      "notes": "updating material data",
      "ver_num": "v0.2",
      "changes": [
        {"op": "replace", "path": "/proc/0/role", "value": ["prod"]},
        {"op": "add", "path": "/iden/cas", "value": "9003-53-6"},
        {"op": "remove", "path": "/prop/3"}
      ]
    },
    {
      "_iduser": "507f191e810c19729de860ec",
      "name_user": "Dylan W",
      "date": 1612881126,
      "notes": "updating material data again",
      "ver_num": "v0.3",
      "changes": [
        {"op": "replace", "path": "/prop/1/value", "value": 5200},
        {
          "op": "add", "path": "/prop", "value": {
          "key": "d", "method": "sec", "value": 1.03, "uncertainty": 0.02,
          "attr": {"data": {"_id": "507f191e810c19729de860em", "key": "sec"}}
        }
        },
        {"op": "remove", "path": "/data/2"}
      ]
    }
  ]
}
```