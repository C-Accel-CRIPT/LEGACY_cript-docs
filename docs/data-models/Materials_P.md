# Materials - Polymer

The 'material' node contains identity and property data for a chemical. This material node is specifically tailored for polymers or
mixtures containing polymers. 

**Features:**

* material node points to data, sample and process nodes
* required information
    * name
    * identifiers
* optional information
    * data (CRIPT nodes)
    * sample (CRIPT nodes)
    * process (CRIPT node)
    * property (and child properties)
    * keywords
    * source
    * lot_num
    * storage conditions
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
`last_modified`       |<span style="color:rgb(0, 72, 189)">  datetime  </span>   | <span style="color:rgb(0, 72, 189)">auto  </span>   | <span style="color:rgb(0, 72, 189)">  last modified datetime  </span>
`created`             |<span style="color:rgb(0, 72, 189)">  datetime  </span>   | <span style="color:rgb(0, 72, 189)">auto  </span>   | <span style="color:rgb(0, 72, 189)">  datetime created  </span>
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
`process`          | dict         |          | The [process](../data-models/Process.md) that produced the material.
`process/_id`      | objectId()   |          | id of process
`process/name`     | string       |          | name of process
`properties`       | list[dict]   |          | [see properties section](../Materials_P/#properties)
`keywords`         | list[string] |          | [see keywords section below](../Materials_P/#keywords)
`source`           | string       |          | source of material
`lot_number`       | string       |          | lot number
`storage`          | dict         |          | storage conditions
`storage\temp`     | double       | degC     | storage temperature
`storage\time_num` | double       | days     | storage time
`storage\atm`      | string       |          | storage atmosphere
`storage\note`     | string       |          | notes related to storage
`hazard`           | list[string] |          | hazards
`note`             | string       |          | free-form space to store any text


### Identifiers

Identifiers are unique ids or entities that establishes the identity of the chemical. Providing as many 
identifiers as possible greatly increases the findability.
Mixtures are supported by appending to list of identifiers.

```json
[
  {
    'Key': value,
    'Key': value
  }
]
```

Key                  | Data Type      | Required          | Description
-------------        |---------       | ---------         |----
`mat_id`             | integer        | auto-generated    | id that is used to link to properties 
`pref_name`          | string         | required          | preferred name
`_id`                | objectID       | optional          | ID for material that already exists
`names`              | list[string]   | optional          | additional names, abbreviations, short hands for the material
`cas`                | string         | optional          | [CAS number](https://www.cas.org/support/documentation/chemical-substances)
`bigsmiles`          | string         | optional          | [bigSMILES Line Notation](https://olsenlabmit.github.io/BigSMILES/docs/line_notation.html#the-bigsmiles-line-notation)
`chem_repeat`        | list[string]   | optional          | chemical formula of repeating unit, Ex. polystyrene: "C8H8"
`smiles`             | string         | optional          | [simplified molecular-input line-entry system](https://en.wikipedia.org/wiki/Simplified_molecular-input_line-entry_system)
`chem_form`          | string         | optional          | chemical formula, Ex. benzene: "C6H6"
`pubChem_cid`        | string         | optional          | [PubChem CID](https://pubchem.ncbi.nlm.nih.gov/)
`inchi`              | string         | optional          | IUPAC International Chemical Identifier [InChI](https://iupac.org/who-we-are/divisions/division-details/inchi/)
`inchi_key`          | string         | optional          | a hashed version of the full InChI 

### Properties

Properties are any physical, chemical, or mechanical specification that defines or is embodied by the material.

Properties consist of the following structure:

```json
{
  "mat_id": integer,
  "component": string,
  "key": string, 
  "method": string, 
  "value": double, 
  "uncer": double, 
  "unit": string,
  "data_id": ObjectID,
  "conditions": [{"key": string, "value": double, "unit": string, "uncer": double, "_id": ObjectID, "name": string}],
  "note": "string"
}
```

 Key        | Description
----        | ----
`mat_id`    | Corresponds to the mat_id in the identifiers section and the corresponding material _id if the property if from a child (Format, materialized tree: _id(child-newest);...;_id(child-oldest);mat_id) . This identifier is useful when a mixture is characterized, and a property only corresponds to one chemical in the mixture. If the `mat_id` is "0" then the property corresponds to the mixture.
`component` | If the property speaks to a specific sub-structure. It can be specified here using [BigSMILES](https://olsenlabmit.github.io/BigSMILES/docs/line_notation.html#the-bigsmiles-line-notation).
`key`       | The property key. See tables below.
`method`    | Method used to obtain property. See table below.
`value`     | Value of property.
`uncer`     | Uncertainty of value.
`unit`      | Units associated with vale. (Units are not stored for officially supported data as all official values are converted to database standard prior to storage.)
`data`      | Link to [data node](../data-models/Data.md) associated with property. 
`conditions`| Conditions under which value was obtained.
`note`      | Free-form space to store any text.


The range bound is limited to the largest number that can be stored in 64 bits (1.79e+308).

#### Chemical

Key                  | Method                                      |Range                    |Units                | Conditions                | Description
----------           |---------                                    |------                   |--------             |---------                  |---------
`conc`               | []                                          | [0, 1.79e+308]          | M                   |                           | concentration
`weight_p`           | []                                          | [0, 1]                  | None                |                           | weight percent
`m_n`                | ['nmr', 'sec', 'maldi', 'osmtic_pres']      | [0, 1.79e+308]          | g/mol               |                           | Average molecular weight on the bases of moles or first moment of the molecular weight distribution.
`m_w`                | ['nmr', 'sec', 'maldi', 'ls']               | [0, 1.79e+308]          | g/mol               |                           | Average molecular weight on the bases of weight.
`d`                  | ['sec', 'maldi']                            | [1, 1.79e+308]          |                     |                           | Ratio of weight averaged molecular weight over number average molecular weight.
`m_z`                | ['nmr', 'sec', 'maldi', 'ultra_centr']      | [0, 1.79e+308]          | g/mol               |                           |
`m_v`                | ['viscometer']                              | [0, 1.79e+308]          | g/mol               |                           | Average molecular weight determined from viscosity
`m_p`                | ['sec', 'maldi']                            | [0, 1.79e+308]          | g/mol               |                           | Peak average molecular weight
`mw_std_dev`         | ['nmr', 'sec', 'maldi']                     | [0, 1.79e+308]          | g/mol               |                           | Standard deviation of molecular weight distribution or square root of the second moment ofthe molecular weight distribution
`mw_var`             | ['nmr', 'sec', 'maldi']                     | [0, 1.79e+308]          | g/mol               |                           | Variance of molecular weight distribution or the second moment of the molecular weight distribution
`mw_skew`            | ['nmr', 'sec', 'maldi']                     | [0, 1.79e+308]          | g/mol               |                           | Skewness of molecular weight distribution or the third moment of the molecular weight distribution
`mw_kurtosis`        | ['nmr', 'sec', 'maldi']                     | [0, 1.79e+308]          | g/mol               |                           | Kurtosis of molecular weight distribution or the fourth moment of the molecular weight distribution
`tac_Pm`             | ['nmr']                                     | [0, 1]                  |                     |                           | probability of finding meso diads (Pm)
`comp_frac`          | []                                          | [0, 1]                  |                     |                           | composition: mole fraction of component ??????
`branch`             | []                                          |                         |                     |                           | 
`tran/cis`           | []                                          |                         |                     |                           | 

#### Physical

Key                  | Method                 |Range                    |Units                | Conditions                | Description
----------           |---------               |------                   |--------             |---                        |---------
`phase`              | []                     | [solid, liquid, gas]    | None                |                           | state of matter
`color`              | []                     | string                  | None                |                           | the visual appearance of the chemical 
`odor`               | []                     | string                  | None                |                           | a description of the smell of the chemical
`solubility`         | []                     | [0, 1.79E308]           | mg/mL               | temperature and solvent   | the ability to dissolve
`heat_vap`           | []                     | [0, 1.79E308]           | kj/mol              | temperature               | heat of vaporization
`surface_ten`        | []                     | [0, 1.79E308]           | N/m                 | temperature               | surface tension
`ref_index`          | []                     | [0, 1.79e+308]          | None                |                           | A dimensionless number that describes how fast light travels through the material.
`density`            | []                     | [0, 1.79e+308]          | None                |                           | The amount of substance that fit within a unit of volume.
`t_m`                | ['dsc']                | [-273.15, 1.79e+308]    | degC                |                           | The transition temperature where crystal structures are destroyed.
`t_g`                | ['dsc']                | [-273.15, 1.79e+308]    | degC                |                           | The transition temperature where a substances turns into a glass; vitrification.
`crys_frac`          | ['dsc']                | [0, 1.2]                | None                |                           | Percent Crystallinity By Weight
`enth_crys`          | ['dsc']                | [-1.79e+308, 1.79e+308] | J/mol               |                           | Enthalpy of Crystallization, molar basis
`entr_crys`          | ['dsc']                | [-1.79e+308, 1.79e+308] | J/mol/K             |                           | Entropy of Crystallization, molar basis
`therm_cond`         | []                     | [0, 1.79e+308]          | W/m/k               |                           | Measure of a materials ability to conduct heat
`therm_expand_v`     | []                     | [-1.79e+308, 1.79e+308] | 1/K                 |                           | A change in volume in response to a change in temperature (not including phase transitions)
`therm_expand_l`     | []                     | [-1.79e+308, 1.79e+308] | 1/K                 |                           | A change in dimension in response to a change in temperature (not including phase transitions)
`c_p`                | ['calorimetry', 'dsc'] | [-1.79e+308, 1.79e+308] | J/mol/K             |                           | The amount of heat needed to be supplied to a given mole (based on repeat unit) to produce a change in temperature at constant pressure
`c_v`                | []                     | [-1.79e+308, 1.79e+308] | J/mol/K             |                           | The amount of heat needed to be supplied to a given mole (based on repeat unit) to produce a change in temperature at constant volume
`therm_diff`         | []                     | [-1.79e+308, 1.79e+308] | m^2/s               |                           | A measures the rate of transfer of heat of a material from the hot end to the cold end.
`tensile_mod`        | ['utm']                | [0, 1.79e+308]          | GPa                 |                           |
`tensile_str`        | ['utm']                | [0, 1.79e+308]          | MPa                 |                           | The maximum stress that a material can withstand while being stressed.
`yield_str`          | ['utm']                | [0, 1.79e+308]          | MPa                 |                           | Point on a stress-strain curve that indicates the limit of elastic behavior.
`frac_strain`        | ['utm']                | [1, 1.79e+308]          | None                |                           | The maximum strain that a material can withstand while being stressed.
`intr_vis`           | ['viscometer']         | [0, 1.79e+308]          | dl/g                |                           | A measure of a solute contribution to the viscosity of a solution
`mh_parameter_k`     | ['sec', 'viscometer']  | [0, 1.79e+308]          | ml/g                |                           | Mark Houwink Parameters provide a relation between intrinsic viscosity and molecular weight
`mh_parameter_a`     | ['sec', 'viscometer']  | [0, 1.79e+308]          | None                |                           | Mark Houwink Parameters provide a relation between intrinsic viscosity and molecular weight
`diff_coef`          | []                     | [0, 1.79e+308]          | cm^2/s              |                           | Proportionality constant between the molar flux due to molecular diffusion and the gradient of concentration.
`relax_time_seg`     | []                     | [0, 1.79e+308]          | s                   |                           | Time it takes a polymer segment to relax
`relax_time_long`    | []                     | [0, 1.79e+308]          | s                   |                           | Time longest time scale it takes to relax an applied stress
`iso_comp`           | []                     | [-1.79e+308, 1.79e+308] | m^2/N               |                           | A change in volume in response to a change in pressure
`char_ratio`         | []                     | [0, 1.79e+308]          | None                |                           | A measure of chain flexibility.
`khun_len`           | []                     | [0, 1.79e+308]          | angstrom            |                           | A measure of chain flexibility.
`stat_seg_len`       | []                     | [0, 1.79e+308]          | angstrom            |                           | A measure of chain flexibility.
`persis_len`         | []                     | [0, 1.79e+308]          | angstrom            |                           | A measure of the bending stiffness of a polymer.
`r_g`                | ['ls']                 | [0, 1.79e+308]          | nm                  |                           | The root-mean-square mass weighted average distance of monomers from the center of mass.
`r_h`                | ['dls']                | [0, 1.79e+308]          | nm                  |                           | The radius of an equivalent hard-sphere diffusing at the same rate as the molecule under observation
`virial_coef`        | []                     | [0, 1.79e+308]          | cm^3 * mole/gram^2  |                           |
`inter_Parm`         | []                     | [0, 1.79e+308]          | cm^3 * mole/gram^2  |                           | A measure of the interaction between molecules and the medium in which it is dissolved in.
`melt_flow`          | []                     | [0, 1.79e+308]          | g                   |                           | the mass of polymer flowing through a capillary of a specific diameter and length by a pressure of a specified time


#### Conditions

Key                   | Units     | Location   | Description
-------------         | ----      | ----       | ----
`time`                | min       | value      | time
`temperature`         | degC      | value      | temperature
`pressure`            | kPa       | value      | pressure (absolute)
`solvent`             | none      | _id, name  | solvent; material node
`standard`            | none      | _id, name  | measurement standard (ASTM, ISO)


#### Methods

Key                | Description
----------         | ----
`prescribed`       | A value that can be defined, (Ex. calculating MW from molecular formula)
`comp`             | Computation or Simulation
`nmr`              | Nuclear Magnetic Resonance
`sec`              | Size Exclusion Chromatography / Gel permeation chromatography (GPC)  
`gc`               | Gas Chromatography
`chrom`            | General Chromatography
`ms`               | General Mass Spectrometry
`maldi`            | Matrix Assisted Laser Desorption Ionization
`ultra_centr`      | Ultra Centrifugation
`osmtic_pres`      | Osmotic Pressure
`calorimetry`      | Calorimetry
`cryoscopy`        | Cryoscopy
`ebullioscopy`     | Ebullioscopy
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



### Keywords

Keywords are an optional field that allow users to classify the material. Selecting multiple keywords is allowed.

Keyword             | Description  
----                | ----
** General structure terms ** |
thermoset           | a cross-linked polymer 
thermoplastic       | a polymer that becomes pliable at elevated temperature adn solidifies upon cooling to room temperature
semicrystalline     | a polymer that does exhibit some crystalline structure
elastomer           | a cross-linked polymer with a glass transition well below room temperature
amorphous           | a polymer that does not exhibit any crystalline structure
||
homopolymer         | a polymer with a single repeating structure
copolymer           | a polymer with a two or more repeating structures
random              | a polymer with a two or more repeating structures are randomly distributed
block               | a polymer with a two or more repeating structures are distributed in groups  
alternating         | a polymer where the composition oscillates between two repeating structures
gradient            | a polymer where the composition gradually transitions from one repeating structure into another
||
isotactic           | a polymer with all substituent having the same stereoconfiguration
syndiotactic        | a polymer with substituent alternating stereoconfiguration
atactic             | a polymer with substituent having a random distribution of stereoconfiguration
||
regio_regular       | a polymer with one positional isomer; all head-to-tail or tail-to-tail and head-to-head
regio_irregular     | a polymer with more than one positional isomer; mixture of head-to-tail, tail-to-tail, and head-to-head
||
linear              | a polymer with a single line of repeat units
star                | a polymer with 3 or more arms originating from a single point
ring                | a polymer with no ends or a loop of repeat units 
comb                | a polymer with a main chain with small chains branching off the main chain
bottlebrush         | a polymer with a very high density of chains branching off the main linear chain
hyperbranch         | a polymer with a very high degree of branches and branches have more branching
network             | a polymer with a where a molecular structure percolates through the full macroscopic sample
||
polymer_blend       | a material with two or more composed of two or more polymers
composite           | a material with two or more components
||
** polymer types: ** |
polyolefins          | a polymer with [$]CC(R)[$] structure and the locally surrounding is C and H
polystyrenes         | a polymer with [$]CC(c1ccccc1)[$] structure
polyphenylenes       | a polymer with [$]c1cccc(c1)[$] structure
||
polyvinyls           | a polymer with [$]CC(R)[$] structure and the locally surrounding by elements other than C and H
polyacrylates        | a polymer with [$]CC(C(=O)O-R)[$] structure 
polymethacrylates    | a polymer with [$]CC(C)(C(=O)O-R)[$] structure
polyvinyl_ethers     | a polymer with [$]CC(OR)[$] structure 
polyvinyl_esters     | a polymer with [$]CC(OC(=O)-R)[$] structure
||
polyesters           | a polymer with R-C(=O)O-R within the backbone  
polycarbonates       | a polymer with R-O-C(=O)O-R within the backbone 
polyethers           | a polymer with R-O-R within the backbone
polyanydrides        | a polymer with R-C(=O)-O-C(=O)-R within the backbone
polyketones          | a polymer with R-C(=O)-R with the backbone
polyamines           | a polymer with R-N(R)-R within the backbone
polyurethanes        | a polymer with R-N(R)-C(=O)O-R within the backbone 
polyamides           | a polymer with R-C(=O)N(R)-R within the backbone
polyureas            | a polymer with R-N(R)-C(=O)-N(R)-R within the backbone
silicones            | a polymer with R-Si(R)(R)-R within the backbone
polysulfides         | a polymer with R-S-R within the backbone
polysulfones         | a polymer with R-S(=O)(=O)-R within the backbone
polysulfoxides       | a polymer with R-S(=O)-R within the backbone
polythiophenes       | a polymer with C=C1=CC=CS1 5 member ring within the backbone
polyphosphazenes     | a polymer with R-P(R)(R)=N-R within the backbone
conjugated_poly      | a polymer with delocalized electrons in the p orbital along the backbone
  

---

## Example


[Example](../Example/#experiment-1-anionic-polymerization-of-styrene)
