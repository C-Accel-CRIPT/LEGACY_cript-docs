# Sample

The 'process' node contains ingredient and procedure information. A process can be anything from a reaction,
reation+seperation, extrusion, or sample preparation step. Typically, a process results in a change in the "identity"
portion of a material node.

**Features:**

* material and data nodes point to process nodes (multiple material and data nodes are allowed)
* process node points to material (multiple material nodes are allowed)
* required information
    * name
    * ingredient (min of one ingredient required)
    * procedure
    * references: expt, data, product(material), ingredient(material)
* optional information
    * conditions
* auto generate/update:
    * _id
    * type
    * ver_sch
    * ver_con (& all child) <-- update with version control node
    * date (& all child)
    * expt (& all child)  <-- update with expt node
    * ingr (& all child) <-- update with material nodes
    * product (& all child) <-- update with material/data node

**App features to support this node:**

* a page to fill product: experiment(materials, process, data) data
* allow additional optional information in attribute, **para** section given that it begins with +
* units are not stored and all official values are converted to database standard prior to storage

## JSON Schema

```json
{
  "_id": objectId(),
  "type": "process",
  "ver_sch": string,
  "ver_con": {
    "_id": objectId(),
    "num": string
  },
  "date": [
    {"created": datetime},
    {"last_mod": datetime}
  ],
  "notes": string,
  "expt": {"_id": objectId(), "name": string},
  "data": [{"_id": objectId(), "name": string}],
  "product": [{"_id": objectId(), "name": string}],
  "name": string,
  "ingr": ["see ingredients for details"],
  "procedure": string,
  "cond": {"see conditions": "for details"},
  "attr": {"see attributes": "for details"}
}
```

---

## Description

Key                       | Data Type     | Required        | Description
-------------             |---------      |------           |----
`_id`                     |<span style="color:rgb(0, 72, 189)"> objectId() </span>|<span style="color:rgb(0, 72, 189)">  auto  </span>|<span style="color:rgb(0, 72, 189)">  unique database id  </span>
`type`                    |<span style="color:rgb(0, 72, 189)">  string  </span> |<span style="color:rgb(0, 72, 189)">  auto  </span>|<span style="color:rgb(0, 72, 189)">  type of node ; Ex: "group"  </span>
`ver_sch`                 |<span style="color:rgb(0, 72, 189)">  string  </span>|<span style="color:rgb(0, 72, 189)">  auto  </span>|<span style="color:rgb(0, 72, 189)">  schema version; Ex: "v0.1"  </span>
`ver_con`                 |               | auto            |<span style="color:rgb(0, 72, 189)">  version control object  </span>
`ver_con/_id`             |<span style="color:rgb(0, 72, 189)">  objectId()  </span>|<span style="color:rgb(0, 72, 189)">  auto  </span>|<span style="color:rgb(0, 72, 189)">  reference id to node history  </span>
`ver_con/num`             |<span style="color:rgb(0, 72, 189)">  string  </span>|<span style="color:rgb(0, 72, 189)">auto  </span>|<span style="color:rgb(0, 72, 189)">  type of node ; Ex: "group"  </span>
`date`                    |               | auto            |<span style="color:rgb(0, 72, 189)">  datetime object  </span>
`date/created`            |<span style="color:rgb(0, 72, 189)">  datetime  </span>|<span style="color:rgb(0, 72, 189)">auto  </span>|<span style="color:rgb(0, 72, 189)">  datetime created  </span>
`type/last_mod`           |<span style="color:rgb(0, 72, 189)">  datetime  </span>|<span style="color:rgb(0, 72, 189)">auto  </span>|<span style="color:rgb(0, 72, 189)">  last modified datetime  </span>
`notes`                   |<span style="color:rgb(0, 72, 189)">  string  </span>|<span style="color:rgb(0, 72, 189)">auto  </span> |<span style="color:rgb(0, 72, 189)">  free-form space to store any text  </span>
`expt`                    |               | auto           | [experiment node](../data-models/Experiments.md)
`expt/_id`                |<span style="color:rgb(12, 145, 3)">  objectId()     </span> |<span style="color:rgb(12, 145, 3)"> auto  </span> |<span style="color:rgb(12, 145, 3)"> id of experiment </span>
`expt/name`               |<span style="color:rgb(12, 145, 3)">  string         </span> |<span style="color:rgb(12, 145, 3)"> auto  </span> |<span style="color:rgb(12, 145, 3)"> name of experiment </span>
`data`                    |               | optional       | [data node](../data-models/Data.md)
`data/_id`                |<span style="color:rgb(12, 145, 3)">  objectId()     </span> |<span style="color:rgb(12, 145, 3)"> auto  </span> |<span style="color:rgb(12, 145, 3)"> id of data </span>
`data/name`               |<span style="color:rgb(12, 145, 3)">  string         </span> |<span style="color:rgb(12, 145, 3)"> auto  </span> |<span style="color:rgb(12, 145, 3)"> name of data </span>
`product`                 |               | **required**   | <span style="color:rgb(12, 145, 3)">the product of the process node; </span> [material node](../data-models/Materials_P.md)
`product/_id`             |<span style="color:rgb(12, 145, 3)">  objectId()     </span> |<span style="color:rgb(12, 145, 3)"> auto  </span> |<span style="color:rgb(12, 145, 3)"> id of product </span>
`product/name`            |<span style="color:rgb(12, 145, 3)">  string         </span> |<span style="color:rgb(12, 145, 3)"> auto  </span> |<span style="color:rgb(12, 145, 3)"> name of product </span>
`name`                    | string        | **required**   | name of process
`ingr`                    | list          | **required**   | [see identifiers section](../Process/#ingredients)
`procedure`               | string        | **required**   | written procedure for the process
`cond`                    | dict          | optional       | conditions for the process (exposed value from written procedure)
`attr`                    | dict          | optional       | see attributes section

### Ingredients

Ingredients are originally defined as a [material node](../data-models/Materials_P.md) and linked here. A minimum of 1
quantity is required.

```json
{
  "_id": objectId(),
  "name": string,
  "chem_form": string,
  "quant": [
    {"key": string, "value": double, "uncer": double}
  ]
}
```

List of supported quantities (quant), units and valid ranges.

Key                | Units      | Range          | Description
-------------      |----------- | ----           |-----------
`mass`             | g          | [0, 1.79e+308] | mass
`vol`              | ml         | [0, 1.79e+308] | volume
`pres`             | kPa        | [0, 1.79e+308] | partial pressure
`mole`             | mmol       | [0, 1.79e+308] | mole
`equiv`            |            | [0, 1.79e+308] | equivalence
`mass_frac`        |            | [0-1]          | mass fraction
`mole_frac`        |            | [0-1]          | mole fraction
`vol_frac`         |            | [0-1]          | volume fraction

### Conditions

Conditions are any process variable that the user would like to explicitly expose. Conditions such as temperature,
pressure, or reaction times are examples. The conditions are stored in a dictionary. Units are only used for user
defined attributes which begin with a `+`.

```json
{"type": {"value": list[double], "uncer": double, "units": sting}}
```

`type`                | Units     | Description
-------------         | ----      | ----
`time`                | min       | time
`temp`                | degC      | temperature
`pres`                | kPa       | pressure (absolute)

### Attributes

Attributes are optional properties that can be associated with this node. The following list is the officially supported
keys. Users may define their own keys by placing a '+' in front of their custom key.

Key                   | Data Type   | Description
-------------         | ---------   | ---- 
`history`             | dict        | processing history (feature under construction)

### Process history

**Under construction**
The process history is a feature in development. The feature will take the `procedure` given by an user and convert it
into an expand-graph detailing intermediate steps. This feature will be powered by a NLP algorithm that is under
development.

![Experiment_network](../img/process_history.png)

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
  "notes": "",
  "expt": {"_id": "507f191e810c19729de860em", "name": "anionic polymerization of styrene"},
  "data": [{"_id": "507f191e810c19729de860em", "name": "NMR Kinetics"}],
  "product": [{"_id": "507f191e810c19729de5d0em", "name": "polystyrene"}],
  "name": "polymerization",
  "ingr": [
    { 
      "_id": "507f191e810c19729de860em",
      "name": "styrene",
      "chem_form": "C8H8",
      "quantities": [
        {"type": "mass", "value": 20.3},
        {"type": "vol", "value": 22.3},
        {"type": "mole", "value": 195},
        {"type": "equiv", "value": 50}
      ]
    },
    {
      "_id": "507f191e810c19729de560em",
      "name": "sec-bu li",
      "chem_form": "C4H9Li1",
      "quantities": [
        {"type": "vol", "value": 3},
        {"type": "mole", "value": 3.9},
        {"type": "equiv", "value": 1}
      ]
    },
    {
      "_id": "507f191e810c19729de560em",
      "name": "toluene",
      "chem_form": "C7H8",
      "quantities": [
        {"type": "mass", "value": 188},
        {"type": "vol", "value": 216},
        {"type": "mole", "value": 2039},
        {"type": "equiv", "value": 522}
      ]
    },
    {
      "_id": "507f191e810c19729de560em",
      "name": "methanol",
      "chem_form": "C1H4O1",
      "quantities": [
        {"type": "mass", "value": 2.37},
        {"type": "vol", "value": 3},
        {"type": "mole", "value": 74},
        {"type": "equiv", "value": 19}
      ]
    }
  ],
  "procedure": "In an argon filled glovebox, a round bottom flask was filled with 216 ml of dried toluene. The solution of secBuLi (3 ml, 3.9 mmol) was added next, followed by styrene (22.3 g, 176 mmol) to initiate the polymerization. The reaction mixture immediately turned orange. After 30 min, the reaction was quenched with the addition of 3 ml of methanol. The polymer was isolated by precipitation in methanol 3 times and dried under vacuum.",
  "cond": {
    "time": {"value": [60]},
    "temp": {"value": [25]}
  },
  "attr": {}
}
```

### Visualization
