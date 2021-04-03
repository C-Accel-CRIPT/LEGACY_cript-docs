# Data

The 'data' node contains data related to raw or processed data. This can be an NMR fid, SEC trace, 
molecular weight distribution, or stress-strain curve.

**Features:**

* data nodes points only to raw data files
* required information
    * name
    * type
    * source
* optional information
    * file
    * file type
    * sample preparation  
    * instrument details
    * calibration
    * data
    * history
    * note 
* auto generate/update:
    * _id
    * class
    * version_schema
    * version_control (& all child) <-- update with version control node
    * date (& all child)
  

**App features to support this node:**

* a page to plot, analyze data (csv or `data`)
* allow additional optional information in attribute section given that it begins with +
* units are not stored and all official values are converted to database standard prior to storage


## JSON Schema

```json
{
  "_id": objectId(),
  "class": "data",
  "version_schema": string,
  "version_control": {
    "_id": objectId(),
    "num": string
  },
  "date_created": datetime,
  "date_last_mod": datetime,
  "name": string,
  "type": string,
  "source": string,
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
`name`                | string        | required  | name of data
`type`                | string        | required  | type of data, [see options below](../Data/#type)
`source`              | string         | required  | source of data [expt, proc, comp] experiment, processed data, computed data



### Attributes

Attributes are optional properties that can be associated with this node. The following list is the officially supported
keys. Users may define their own keys by placing a '+' in front of their custom key.

Data can either be linked through `file` or placed directly in the document with `data`. `data` is restricted to #### total data points.
total data points = row * col

Key                     | Data Type       | Description
-------------           | ---------       | ----------
`file`                  | list[dict]      | link to raw file
`file/_id`              | objectId()      | id for file
`file/type`             | string          | file type (ex. csv, txt, xlsm)
`file/dis`              | string          | description
`web_link`              | string          | raw data may be store on another website and can be linked here
`sample_preparation`    | string          | description of sample preparation
`equipment`             | list[dict]      | equipment or instrument details/configuration
`equipment/_id`         | objectId()      | id for file
`equipment/type`        | string          | file type (ex. csv, txt, xlsm)
`equipment/description` | string          | description
`calibration`           | list[dict]      | calibration details
`calibration/_id`       | objectId()      | id for file
`calibration/type`      | string          | file type (ex. csv, txt, xlsm)
`calibration/dis`       | string          | description
`data`                  | dict            | data information
`data/col_head`         | list            | labels for columns (order should match data)
`data/row_head`         | list            | labels for rows (order should match data)
`data/col_unit`         | list            | units for columns (order should match data)
`data/row_unit`         | list            | units for rows (order should match data)
`history`               | dict            | data history (feature under construction)
`note`                  | string          | free-form space to store any text


### Type

#### 1D data

`type`         | x-axis            | x-axis unit   | y-axis           | y-axis unit | Description
------         |-------            | ---------     | -------          |---------    | --------
rxn_conv       | time              | min           | conversion       |             | reaction conversion vs time
mn_conv        | conversion        |               | m_n              | g/mol       | M_n vs monomer conversion
mwd            | molecular weight  | g/mol         | population       | mol frac    | molecular weight distribution (by mole)
mwd_wt         | molecular weight  | g/mol         | population       | wt frac     | molecular weight distribution (by weight)
sec_trace      | retention time    | min           | signal           |             | SEC trace (by retention time)
sec_trace_vol  | elution vol.      | ml            | signal           |             | SEC trace (by elution volume)
nmr            | time              | us            | voltage          | V           | Free induction decay
nmr_h1         | chemical shift    | ppm           | signal           |             | proton NMR (H1 NMR)
nmr_c13        | chemical shift    | ppm           | signal           |             | carbon NMR (C13 NMR)
nmr_n15        | chemical shift    | ppm           | signal           |             | nitrogen NMR (N15 NMR)
nmr_o17        | chemical shift    | ppm           | signal           |             | oxygen NMR (O17 NMR)
nmr_f19        | chemical shift    | ppm           | signal           |             | fluorine NMR (F19 NMR)
nmr_si29       | chemical shift    | ppm           | signal           |             | silicon NMR (Si29 NMR)
nmr_p31        | chemical shift    | ppm           | signal           |             | phosphorous NMR (P31 NMR)
nmr_noe        | chemical shift    | ppm           | signal           |             | nuclear Overhauser effect NMR
nmr_tocsy      | chemical shift    | ppm           | signal           |             | total correlation spectroscopy NMR
ir             | wavenumber        | cm**-1        | signal           |             | infrared spectroscopy
stess_st       | stess             | kPa           | strain           |             | stress strain curve
waxs           | q                 | angstrom**-1  | intensity        |             | wide angle light scattering
saxs           | q                 | angstrom**-1  | intensity        |             | small angle light scattering
g_prime        | frequency         | rad/s         | stress           | Pa          | storage modulus
g_doub_prime   | frequency         | rad/s         | stress           | Pa          | loss modulus

#### 2D data

`type`         | x-axis            | x-axis unit   | y-axis           | y-axis unit | Description
------         |-------            | ---------     | -------          |---------    | --------
nmr_cosy       | chemical shift    | ppm           | chemical shift   | ppm         | correlation spectroscopy NMR (H - H)
nmr_hsqc       | chemical shift    | ppm           | chemical shift   | ppm         | heteronuclear single-quantum correlation spectroscopy NMR (H - C)
nmr_hmbc       | chemical shift    | ppm           | chemical shift   | ppm         | heteronuclear multiple-bond correlation spectroscopy NMR (H - C)
nmr_dosy       | chemical shift    | ppm           | diffusion coeff. | m**2/s      | Diffusion NMR 
waxs_i         | distance          | nm**-1        | distance         | nm**-1      | wide angle light scattering image
saxs_i         | distance          | nm**-1        | distance         | nm**-1      | small angle light scattering image

#### n-D data

`type`         | x-axis            | x-axis unit   | y-axis           | y-axis unit | Description
------         |-------            | ---------     | -------          |---------    | --------


## Data history
**Under construction**

![Data_network](../img/data_history.png)

---

## Example

```json
{
  "_id": "507f191e810c19729de860ec",
  "type": "data",
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
  "name": "sec",
  "source": "expt",
  "expt": [
    {"_id": "507f191e810c19729de860em", "name": "Anionic polymerization", "date": 1612886423}
  ],
  "mat": [
    {"_id": "507f191e810c19729de860ed", "name": "poly(styrene)", "prop": "m_n", "value": 5300},
    {"_id": "507f191e810c19729de860ed", "name": "poly(styrene)", "prop": "d", "value": 1.03}
  ],
  "attr": {
    "file": "507f191e810c19729de860ed",
    "file_type": "csv"
  }
}
```

