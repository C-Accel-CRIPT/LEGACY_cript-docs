# Materials - Polymer

The 'material' node contains identity and property data for a chemical. This material node is specifically tailored for polymers or
mixtures containing polymers. The major changes when compared to `Materials - Other` are in the Identifier, Properties, and Keywords sections. 
The fundamental structure of the node is identical.

**Features:**

* material node points to data, and sample nodes
* required information
    * name
    * identity
* optional information
    * data (CRIPT nodes)
    * sample (CRIPT nodes)
    * property
    * keywords
    * source
    * lot_num
    * storage conditions
    * notes
* auto generate/update:
    * _id
    * class
    * version_schema
    * version_control (& all child) <-- update with version control node
    * **sample properties**

**App features to support this node:**

* allow additional optional information in `iden`, `prop` section given that it begins with +
* units are not stored for officially supported data as all official values are converted to database standard prior to storage

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
  "date_created": datetime,
  "date_last_mod": datetime,
  "identifiers": {"see identifiers": "for details"},
  "optional attributes"
}
```

---

## Description

Key                   |Data Type     |Required  |Description
-------------         |---------     |------    |----
`_id`                 |<span style="color:rgb(0, 72, 189)"> objectId() </span>   | <span style="color:rgb(0, 72, 189)">  auto  </span> | <span style="color:rgb(0, 72, 189)">  unique database id  </span>
`class`               |<span style="color:rgb(0, 72, 189)">  string  </span>     | <span style="color:rgb(0, 72, 189)">  auto  </span> | <span style="color:rgb(0, 72, 189)">  class of node; "material_p"  </span>
`version_schema`      |<span style="color:rgb(0, 72, 189)">  string  </span>     | <span style="color:rgb(0, 72, 189)">  auto  </span> | <span style="color:rgb(0, 72, 189)">  schema version; Ex: "v0.1"  </span>
`version_control`     |                                                          |                                                     | <span style="color:rgb(0, 72, 189)">  version control object  </span>
`version_control/_id` |<span style="color:rgb(0, 72, 189)">  objectId()  </span> | <span style="color:rgb(0, 72, 189)">  auto  </span> | <span style="color:rgb(0, 72, 189)">  reference id to node history  </span>
`version_control/num` |<span style="color:rgb(0, 72, 189)">  string  </span>     | <span style="color:rgb(0, 72, 189)">auto  </span>   | <span style="color:rgb(0, 72, 189)">  type of node ; Ex: "group"  </span>
`date_created`        |<span style="color:rgb(0, 72, 189)">  datetime  </span>   | <span style="color:rgb(0, 72, 189)">auto  </span>   | <span style="color:rgb(0, 72, 189)">  datetime created  </span>
`date_last_mod`       |<span style="color:rgb(0, 72, 189)">  datetime  </span>   | <span style="color:rgb(0, 72, 189)">auto  </span>   | <span style="color:rgb(0, 72, 189)">  last modified datetime  </span>
`name`                | string        | required  | name of chemical
`identifiers`         | list[dict]    | required  | [see identifiers section](../Materials_P/#identifiers)

### Attributes

Attributes are optional properties that can be associated with this node. The following list is the officially supported
keys. Users may define their own keys by placing a '+' in front of their custom key.

Key                | Data Type    | Units    | Description
-------------      |---------     |------    | ----
`sample`           | list[dict]   |          | [sample node](../data-models/Sample.md)
`sample/_id`       | objectId()   |          | id of sample
`sample/name`      | string       |          | name of sample
`sample/prop`      | list[dict]   |          | properties of sample 
`data`             | list[dict]   |          | [data node](../data-models/Data.md)
`data/_id`         | objectId()   |          | id of data
`data/name`        | string       |          | name of data
`data/type`        | string       |          | type of data
`properties`       | list[dict]   |          | [see properties section](../Materials_P/#properties)
`keywords`         | list[string] |          | [see keywords section below](../Materials_P/#keywords)
`source`           | string       |          | source of material
`lot_number`       | string       |          | lot number
`store`            | dict         |          | storage conditions
`store\temp`       | double       | degC     | storage temperature
`store\time_num`   | double       | min      | storage time
`store\note`       | string       |          | notes related to storage
`note`             | string       |          | free-form space to store any text


### Identifiers

Identifiers are chemical descriptors or unique ids which speaks to the chemical structure. Providing as many identifiers
as possible great facilitate the findability of the associated data. 

```json
[
  {
    'Key': value,
    'Key': value
  }
]
```

Key                  | Data Type      | Required    | Description
-------------        |---------       | ---------   |----
`mat_id`             | objectId()     | required    | id that is used to link to properties
`names`              | list[string]   | required    | Any name for the material
`cas`                | string         | optional    | [CAS number](https://www.cas.org/support/documentation/chemical-substances)
`bigsmiles`          | string         | optional    | [bigSMILES Line Notation](https://olsenlabmit.github.io/BigSMILES/docs/line_notation.html#the-bigsmiles-line-notation)
`chem_repeat`        | list[string]   | optional    | chemical formula of repeating unit, Ex. polystyrene: "C8H8"
`smiles`             | string         | optional    | [simplified molecular-input line-entry system](https://en.wikipedia.org/wiki/Simplified_molecular-input_line-entry_system)
`chem_form`          | string         | optional    | chemical formula, Ex. benzene: "C6H6"
`pubChem_id`         | string         | optional    | [PubChem ID](https://pubchem.ncbi.nlm.nih.gov/)
`inchi`              | string         | optional    | IUPAC International Chemical Identifier [InChI](https://iupac.org/who-we-are/divisions/division-details/inchi/)
`inchi_key`          | string         | optional    | a hashed version of the full InChI 

### Properties

Properties consist of the following structure:

```json
{
  "mat_id": objectID,
  "key": string, 
  "method": string, 
  "value": double, 
  "uncer": double, 
  "unit": string,
  "data": {"_id": ObjectID, "name": string, "type": string}, 
  "note": "string"
}
```
`mat_id` is the id that corresponds to the id in the identifier. This identifier is useful when a mixture is charaterizaed, and a property only corresponds to one component.
If the `mat_id` is not present then the property corresponds to the mixture.
The range bound is limited to the largest number that can be stored in 64 bits (1.79e+308).
Units are not stored for officially supported data as all official values are converted to database standard prior to storage

#### Chemical

Key              | Method                                      |Range                |Units       |Description
----------       |---------                                    |------               |--------    |---------
`m_n`            | ['nmr', 'sec', 'maldi', 'osmtic_pres']      | [0, 1.79e+308]      | g/mol      | Average molecular weight on the bases of moles or first moment of the molecular weight distribution.
`m_w`            | ['nmr', 'sec', 'maldi', 'ls']               | [0, 1.79e+308]      | g/mol      | Average molecular weight on the bases of weight.
`d`              | ['sec', 'maldi']                            | [1, 1.79e+308]      |            | Ratio of weight averaged molecular weight over number average molecular weight.
`m_z`            | ['nmr', 'sec', 'maldi', 'ultra_centr']      | [0, 1.79e+308]      | g/mol      |
`m_v`            | ['viscometer']                              | [0, 1.79e+308]      | g/mol      | Average molecular weight determined from viscosity
`mw_std_dev`     | ['nmr', 'sec', 'maldi']                     | [0, 1.79e+308]      | g/mol      | Standard deviation of molecular weight distribution or square root of the second moment ofthe molecular weight distribution
`mw_var`         | ['nmr', 'sec', 'maldi']                     | [0, 1.79e+308]      | g/mol      | Variance of molecular weight distribution or the second moment of the molecular weight distribution
`mw_skew`        | ['nmr', 'sec', 'maldi']                     | [0, 1.79e+308]      | g/mol      | Skewness of molecular weight distribution or the third moment of the molecular weight distribution
`mw_kurtosis`    | ['nmr', 'sec', 'maldi']                     | [0, 1.79e+308]      | g/mol      | Kurtosis of molecular weight distribution or the fourth moment of the molecular weight distribution
`tac_Pm`         | ['nmr']                                     | [0, 1]              |            | probability of finding meso diads (Pm)
`comp_frac`      | []                                          | [0, 1]              |            | composition: mole fraction of component ??????
`branch`

#### Physical

Key              | Method     |Range    |Units      |Description
----------       |---------   |------   |--------   |---------
`ref_index`      | []      | [0, 1.79e+308]      | None      | A dimensionless number that describes how fast light travels through the material.
`density`        | []      | [0, 1.79e+308]      | None      | The amount of substance that fit within a unit of volume.
`t_m`            | ['dsc']      | [-273.15, 1.79e+308]      | degC      | The transition temperature where crystal structures are destroyed.
`t_g`            | ['dsc']      | [-273.15, 1.79e+308]      | degC      | The transition temperature where a substances turns into a glass; vitrification.
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
`r_h`              | ['dls']      | [0, 1.79e+308]      | nm      | The radius of an equivalent hard-sphere diffusing at the same rate as the molecule under observation
`virial_coef`      | []      | [0, 1.79e+308]      | cm^3 * mole/gram^2      |
`inter_Parm`      | []      | [0, 1.79e+308]      | cm^3 * mole/gram^2      | A measure of the interaction between molecules and the medium in which it is dissolved in.

#### Methods

Key                | Description
----------         | ----
`nmr`              | Nuclear Magnetic Resonance
`sec`              | Size Exclusion Chromatography
`gc`               | Gas Chromatography
`chrom`            | General Chromatography
`ms`               | General Mass Spectrometry
`maldi`            | Matrix Assisted Laser Desorption Ionization
`ultra_centr`      | Ultra Centrifugation
`osmtic_pres`      | Osmotic Pressure
`calorimetry`      | Calorimetry

`viscometer`       | Viscometer
`utm`              | Universal Testing Machine
`dma`              | Dynamic Mechanical Analysis

`dsc`              | Differential Scanning Calorimetry
`tga`              | Thermogravimetric Analysis

`raman`            | Raman spectroscopy
`ir`               | Infrared spectroscopy
`uv_vis`           | Ultraviolet–visible spectroscopy
`x_ray`            | X_ray spectroscopy

`saxs`             | Small-angle x-ray scattering
`waxs`             | Wide-angle x-ray scattering
`neutron`          | Neutron scattering
`ls`               | Static Light Scattering
`dls`              | Dynamic Light Scattering

`confocal`         | Confocal microscopy
`afm`              | Atomic force microscopy
`tem`              | Transmission electron microscopy
`sem`              | Scanning electron microscopy

`comp`             | Computation or Simulation

### Keywords

Keywords are an optional field that allow users to classify the material. Selecting multiple keywords is allowed.

* thermoset
* thermoplasti
* semicrystalline
* elstomer
---
* polyolefin
  polyvinyl
* polyester
* polyurethane
* polyamide
* polycarbonate
* silicone
* polyacylate
* conjugated_polymer
---  
* homopolymer
* copolymer
* random  
* block
* alternating
* gradient
---
* isotactic
* syndiotactic
* atactic
---
* regio_regualr
* regio_irregular
---
* linear
* star
* ring
* comb
* bottlebrush
* hyperbranch
* network
---
* polymer_blend
* composite







---

## Example

```json
{
  "_id": "607f191e810c19729de860ea",
  "type": "expt",
  "ver_sch": "v0.1",
  "ver_con": {
    "_id": "607f191e810c19729de860eb",
    "num": "v0.1"
  },
  "date": [
    {"created": 1612889382},
    {"last_mod": 1612889322}
  ],
  "notes": "",
  "users": [
    {"_id": "507f191e810c19729de860ec", "name": "Dylan W", "perm": "w"}
  ],
  "name": "poly(styrene)",
  "expt": [
    {"_id": "507f191e810c19729de860em", "name": "anionic polymerization of styrene"}
  ],
  "iden": {
    "names": ["Poly(1-phenylethene)"],
    "cas": "9003-53-6",
    "bigsmiles": "{[$]CC(c1ccccc1)[$]}",
    "chem_repeat": "C8H8"
  },
  "prop": [
    {
      "key": "conv_mon", "method": "NMR", "value": 0.98, "uncertainty": 0.03,
      "attr": {"data": {"_id": "507f191e810c19729de860em", "key": "nmr_1h"}}
    },
    {
      "key": "m_n", "method": "nmr", "value": 5300, "uncertainty": 300,
      "attr": {"data": {"_id": "507f191e810c19729de860em", "key": "nmr_1h"}, "names": ["end group analysis"]}
    },
    {
      "key": "m_n", "method": "sec", "value": 5130, "uncertainty": 200,
      "attr": {"data": {"_id": "507f191e810c19729de860em", "key": "sec"}}
    },
    {
      "key": "d", "method": "sec", "value": 1.03, "uncertainty": 0.02,
      "attr": {"data": {"_id": "507f191e810c19729de860em", "key": "sec"}}
    }
  ],
  "proc": [
    {"_id": "507f191e810c19729de860em", "name": "anionic polymerization", "role": ["prod"]}
  ],
  "data": [
    {"_id": "507f191e810c19729de860ef", "key": "nmr_1h"},
    {"_id": "507f191e810c19729de860vm", "key": "sec"}
  ],
  "attr": {}
}
```

