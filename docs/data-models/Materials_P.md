# Materials - Polymer

The 'material' node contains data related to a chemical. This material node is specifically tailored for polymers.

## JSON Schema

```json
{
  "id_": objectId(),
  "type": "material",
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
  "expt": [
    {"id_": objectId(), "name": string}
  ],
  "iden": {
    "see identifiers": "for details"
  },
  "prop": {
    "see properties": "for details"
  },
  "proc": [
    {"id_": objectId(), "name": string, "role": string}
  ],
  "data": [
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
`name`                    | string        | required  | name of chemical
`expt`                    |               |           | [experiment nodes](../data-models/Experiments.md)
`expt/id_`                | objectId()    | auto      | id of experiment
`expt/name`               | string        | auto      | name of experiment
`iden`                    |               |           | [see identifiers section](../Materials_P/#identifiers)
`prop`                    |               |           | [see properties section](../Materials_P/#properties)
`process`                 |               |           | [process nodes](../data-models/Process.md)
`process/id_`             | objectId()    | auto      | id of process
`process/name`            | string        | auto      | name of process
`process/role`            | list[string]  | auto      | role of material in process [ingr, prod]
`data`                    |               |           | [data nodes](../data-models/Data.md)
`data/id_`                | objectId()    | auto      | id of data
`data/name`               | string        | auto      | name of data
`attr`                    | list          | auto      | see attributes section

### Attributes

Attributes are optional properties that can be associated with this node. The following list is the officially supported
keys. Users may define their own keys by placing a '+' in front of their custom key.

Key                |Data Type     |Description
-------------      |---------     |----
`source`           | string       | source of material
`lot_num`          | string       | lot number
`store`            |              | storage conditions
`store\temp_num`   | double       | storage temperature 
`store\temp_unit`  | string      | storage temperature unit
`store\time_num`   | double       | storage time 
`store\time_unit`  | string      | storage time unit 
`store\notes`      | string       | notes related to storage  

### Identifiers

Identifiers are chemical descriptors or unique ids which speaks to the chemical structure, excluding parameters that
need to be measured (i.e. properties). Providing as many identifiers as possible great facilitate the findability of the
associated data.

Key                  | Data Type       | Required   | Description
-------------        |---------       | ---------   |----
`names`              | list[string]   | required    | Any name for the material
`cas`                | string         | optional    | [CAS number](https://www.cas.org/support/documentation/chemical-substances)
`bigsmiles`          | string         | optional    | [bigSMILES Line Notation](https://olsenlabmit.github.io/BigSMILES/docs/line_notation.html#the-bigsmiles-line-notation)
`chem_repeat`        | string         | optional    | chemical formula of repeating unit, Ex. polystyrene: "C8H8"
`id_`                | objectId()     | optional    | id number from CRIPT internal database

### Properties

Properties consist of the following structure:
"key": {"method": string, "value": double, "unit": string, "uncer": double, "attr": {}}

The range bound is limited to the largest number that can be stored in 64 bits (1.79e+308).

Key              | Method     |Range    |Units      |Description
----------       |---------   |------   |--------   |---------
`conc`           | []                    | [0, 1.79e+308]      | M         | concentration
`ref_index`      | []      | [0, 1.79e+308]      | None      | A dimensionless number that describes how fast light travels through the material.
`density`      | []      | [0, 1.79e+308]      | None      | The amount of substance that fit within a unit of volume.
`conv_mon`      | ['nmr', 'sec']      | [0, 1.2]      | None      | how much monomer that has reacted.
`conv_init`      | ['nmr', 'sec']      | [0, 1.2]      | None      | how much monomer that has reacted.
`init_eff`      | ['nmr', 'sec']      | [0, 1.2]      | None      | The proportion of initiators that result in an active propagating species.
`m_n`      | ['nmr', 'sec', 'maldi', 'osmtic_pres']      | [0, 1.79e+308]      | g/mol      | Average molecular weight on the bases of moles or first moment of the molecular weight distribution.
`m_w`      | ['nmr', 'sec', 'maldi', 'ls']      | [0, 1.79e+308]      | g/mol      | Average molecular weight on the bases of weight.
`d`      | ['sec', 'maldi']      | [1, 1.79e+308]      | None      | Ratio of weight averaged molecular weight over number average molecular weight.
`m_z`      | ['nmr', 'sec', 'maldi', 'ultra_centr']      | [0, 1.79e+308]      | g/mol      |
`m_v`      | ['viscometer']      | [0, 1.79e+308]      | g/mol      | Average molecular weight determined from viscosity
`mw_std_dev`      | ['nmr', 'sec', 'maldi']      | [0, 1.79e+308]      | g/mol      | Standard deviation of molecular weight distribution or square root of the second moment ofthe molecular weight distribution
`mw_var`      | ['nmr', 'sec', 'maldi']      | [0, 1.79e+308]      | g/mol      | Variance of molecular weight distribution or the second moment of the molecular weight distribution
`mw_skew`      | ['nmr', 'sec', 'maldi']      | [0, 1.79e+308]      | g/mol      | Skewness of molecular weight distribution or the third moment of the molecular weight distribution
`mw_kurtosis`      | ['nmr', 'sec', 'maldi']      | [0, 1.79e+308]      | g/mol      | Kurtosis of molecular weight distribution or the fourth moment of the molecular weight distribution
`t_m`      | ['dsc']      | [-273.15, 1.79e+308]      | degC      | The transition temperature where crystal structures are destroyed.
`t_g`      | ['dsc']      | [-273.15, 1.79e+308]      | degC      | The transition temperature where a substances turns into a glass; vitrification.
`crys_frac`      | ['dsc']      | [0, 1.2]      | None      | Percent Crystallinity By Weight
`enth_crys`      | ['dsc']      | [-1.79e+308, 1.79e+308]      | J/mol      | Enthalpy of Crystallization, molar basis
`entr_crys`      | ['dsc']      | [-1.79e+308, 1.79e+308]      | J/mol/K      | Entropy of Crystallization, molar basis
`therm_cond`      | []      | [0, 1.79e+308]      | W/m/k      | Measure of a materials ability to conduct heat
`therm_expand_v`      | []      | [-1.79e+308, 1.79e+308]      | 1/K      | A change in volume in response to a change in temperature (not including phase transitions)
`therm_expand_l`      | []      | [-1.79e+308, 1.79e+308]      | 1/K      | A change in dimension in response to a change in temperature (not including phase transitions)
`c_p`      | ['calorimetry', 'dsc']      | [-1.79e+308, 1.79e+308]      | J/mol/K      | The amount of heat needed to be supplied to a given mole (based on repeat unit) to produce a change in temperature at constant pressure
`c_v`      | []      | [-1.79e+308, 1.79e+308]      | J/mol/K      | The amount of heat needed to be supplied to a given mole (based on repeat unit) to produce a change in temperature at constant volume
`therm_diff`      | []      | [-1.79e+308, 1.79e+308]      | m^2/s      | A measures the rate of transfer of heat of a material from the hot end to the cold end.
`tensile_mod`      | ['utm']      | [0, 1.79e+308]      | GPa      |
`tensile_str`      | ['utm']      | [0, 1.79e+308]      | MPa      | The maximum stress that a material can withstand while being stressed.
`yield_str`      | ['utm']      | [0, 1.79e+308]      | MPa      | Point on a stress-strain curve that indicates the limit of elastic behavior.
`frac_strain`      | ['utm']      | [1, 1.79e+308]      | None      | The maximum strain that a material can withstand while being stressed.
`intr_vis`      | ['viscometer']      | [0, 1.79e+308]      | dl/g      | A measure of a solute contribution to the viscosity of a solution
`mh_parameter_k`      | ['sec', 'viscometer']      | [0, 1.79e+308]      | ml/g      | Mark Houwink Parameters provide a relation between intrinsic viscosity and molecular weight
`mh_parameter_a`      | ['sec', 'viscometer']      | [0, 1.79e+308]      | None      | Mark Houwink Parameters provide a relation between intrinsic viscosity and molecular weight
`diff_coef`      | []      | [0, 1.79e+308]      | cm^2/s      | Proportionality constant between the molar flux due to molecular diffusion and the gradient of concentration.
`relax_time_seg`      | []      | [0, 1.79e+308]      | s      | Time it takes a polymer segement to relax
`relax_time_long`      | []      | [0, 1.79e+308]      | s      | Time longest time scale it takes to relax an applied stress
`iso_comp`      | []      | [-1.79e+308, 1.79e+308]      | m^2/N      | A change in volume in response to a change in pressure
`char_ratio`      | []      | [0, 1.79e+308]      | None      | A measure of chain flexibility.
`khun_len`      | []      | [0, 1.79e+308]      | angstrom      | A measure of chain flexibility.
`stat_seg_len`      | []      | [0, 1.79e+308]      | angstrom      | A measure of chain flexibility.
`persis_len`      | []      | [0, 1.79e+308]      | angstrom      | A measure of the bending stiffness of a polymer.
`r_g`      | ['ls']      | [0, 1.79e+308]      | nm      | The root-mean-square mass weighted average distance of monomers from the center of mass.
`r_h`      | ['dls']      | [0, 1.79e+308]      | nm      | The radius of an equivalent hard-sphere diffusing at the same rate as the molecule under observation
`virial_coef`      | []      | [0, 1.79e+308]      | cm^3 * mole/gram^2      |
`inter_Parm`      | []      | [0, 1.79e+308]      | cm^3 * mole/gram^2      | A measure of the interaction between molecules and the medium in which it is dissolved in.

Key                |Description
----------         |----
`nmr`      | Nuclear Magnetic Resonance
`sec`      | Size Exclusion Chromatography
`maldi`      | Matrix Assisted Laser Desorption Ionization
`ultra_centr`      | Ultra Centrifugation
`osmtic_pres`      | Osmotic Pressure
`ls`      | Static Light Scattering
`dls`      | Dynamic Light Scattering
`viscometer`      | Viscometer
`calorimetry`      | Calorimetry
`utm`      | Universal Testing Machine
`comp`      |Computation or Simulation

#### Attribute for Properties

Key              | Data Type     |Description
----------       |---------      |----
`ref`            |               | [publication node](../data-models/Publications.md) that was a reference for this experiment
`ref\id_`        | objectId()    | id for reference
`ref\title`      | string        | reference title
`data`           |               | [data](../data-models/Data.md)
`data\id_`       | objectId()    | id for data node
`data\key`       | string        | key for data
`names`          | list[string]  | additional names for property

---

## Example

```json
{
  "id_": "607f191e810c19729de860ea",
  "type": "expt",
  "ver_sch": "v0.1",
  "ver_con": {
    "id_": "607f191e810c19729de860eb",
    "num": "v0.1"
  },
  "date": [
    {"created": 1612889382},
    {"last_mod": 1612889322}
  ],
  "notes": "",
  "users": [
    {"id_": "507f191e810c19729de860ec", "name": "Dylan W", "perm": "w"}
  ],
  "name": "poly(styrene)",
  "expt": [
    {"id_": "507f191e810c19729de860em", "name": "anionic polymerization of styrene"}
  ],
  "iden": {
    "names": ["Poly(1-phenylethene)"],
    "cas": "9003-53-6",
    "bigsmiles": "{[$]CC(c1ccccc1)[$]}",
    "chem_repeat": "C8H8"
  },
  "prop": [
    {
      "key": "conv_mon", "method": "NMR", "value": 0.98, "unit": null, "uncertainty": 0.03,
      "attr": {"data": {"id_": "507f191e810c19729de860em", "key": "nmr_1h"}}
    },
    {
      "key": "m_n", "method": "nmr", "value": 5300, "unit": "g/mol", "uncertainty": 300,
      "attr": {"data": {"id_": "507f191e810c19729de860em", "key": "nmr_1h"}, "names": ["end group analysis"]}
    },
    {
      "key": "m_n", "method": "sec", "value": 5130, "unit": "g/mol", "uncertainty": 200,
      "attr": {"data": {"id_": "507f191e810c19729de860em", "key": "sec"}}
    },
    {
      "key": "d", "method": "sec", "value": 1.03, "unit": null, "uncertainty": 0.02,
      "attr": {"data": {"id_": "507f191e810c19729de860em", "key": "sec"}}
    }
  ],
  "proc": [
    {"id_": "507f191e810c19729de860em", "name": "anionic polymerization", "role": ["prod"]}
  ],
  "data": [
    {"id_": "507f191e810c19729de860ef", "key": "nmr_1h"},
    {"id_": "507f191e810c19729de860vm", "key": "sec"}
  ],
  "attr": {}
}
```
