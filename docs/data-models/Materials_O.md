# Materials - other

The 'material' node contains identity and property data for a chemical. This material node is specifically tailored for small molecules 
and inorganics. The node is fundamental identical to ['Materials - Polymers'](../Materials_P) except for the keys in the Identifiers, Properties, and Keywords sections. 


**Features:**

Same as [material node for polymer](../Materials_P)


## JSON Schema

Same as [material node for polymer](../Materials_P/#json-schema)


## Description

Same as [material node for polymer](../Materials_P/#description); except for identifiers.


### Attributes

Same as [material node for polymer](../Materials_P/#attributes); except for properties and keywords.

[see 'other material' properties section](../Materials_O/#properties)

[see 'other material' keywords section](../Materials_O/#keywords)


### Identifiers

A similar structure to [material node for polymer](../Materials_P/#identifiers); except for keys.


Key                  | Data Type      | Required    | Description
-------------        |---------       | ---------   |----
`mat_id`             | integer        | required    | id that is used to link to properties (auto-generated)
`pref_name`          | string         | required    | Preferred name 
`names`              | list[string]   | optional    | Additional names, abbreviations, short hands for the material
`chem_form`          | string         | optional    | chemical formula, Ex. benzene: "C6H6"
`smiles`             | string         | optional    | [simplified molecular-input line-entry system](https://en.wikipedia.org/wiki/Simplified_molecular-input_line-entry_system)
`cas`                | string         | optional    | [CAS number](https://www.cas.org/support/documentation/chemical-chemicals)
`pubChem_cid`        | string         | optional    | [PubChem CID](https://pubchem.ncbi.nlm.nih.gov/)
`inchi`              | string         | optional    | IUPAC International Chemical Identifier [InChI](https://iupac.org/who-we-are/divisions/division-details/inchi/)
`inchi_key`          | string         | optional    | a hashed version of the full InChI 

### Properties

A similar structure to [material node for polymer](../Materials_P/#properties); except for keys.


Key              | Method                | Range                   | Units    | Conditions                | Description
----------       |---------              |------                   |--------  |                           |---------
`conc`           | []                    | [0, 1.79e+308]          | M        |                           | concentration
`weight_p`       | []                    | [0, 1]                  | None     |                           | weight percent
`phase`          | []                    | [solid, liquid, gas]    | None     |                           | state of matter
`color`          | []                    | string                  | None     |                           | the visual appearance of the chemical 
`odor`           | []                    | string                  | None     |                           | a description of the smell of the chemical
`ref_index`      | []                    | [0, 1.79e+308]          | None     | temperature               | refractive index; a dimensionless number that describes how fast light travels through the material.
`density`        | []                    | [0, 1.79e+308]          | None     | temperature and pressure  | the amount of chemical that fit within a unit of volume.
`mw`             | ['nmr', 'ms']         | [0, 1.79e+308]          | g/mol    |                           | molecular weight 
`conc`           | []                    | [0, 1.79e+308]          | M        |                           | concentration
`bp`             | []                    | [-273.15, 1.79E308]     | degC     | pressure                  | boiling temperature
`mp`             | []                    | [-273.15, 1.79E308]     | degC     |                           | melting temperature
`flash`          | []                    | [-273.15, 1.79E308]     | degC     |                           | flash point, the temperature at a which a chemical gives off sufficient vapor to ignite
`ignite`         | []                    | [-273.15, 1.79E308]     | degC     |                           | autoignition temperature
`decomp`         | []                    | [-273.15, 1.79E308]     | degC     |                           | decomposition temperature
`vis`            | ['viscometer']        | [0, 1.79e+308]          | dl/g     | temperature               | viscosity
`ph`             | []                    | [-1.79E308, 1.79E308]   | None     |                           | potential of hydrogen
`pka`            | []                    | [-1.79E308, 1.79E308]   | None     |                           | negative base^-10^ logarithm of the acid dissociation constant
`pkb`            | []                    | [-1.79E308, 1.79E308]   | None     |                           | negative base^-10^ logarithm of the base dissociation constant
`solubility`     | []                    | [0, 1.79E308]           | mg/mL    | temperature and solvent   | the ability to dissolve
`vapor_pres`     | []                    | [0, 1.70E308]           | kPa      | temperature               | vapor pressure
`heat_vap`       | []                    | [0, 1.79E308]           | kj/mol   | temperature               | heat of vaporization
`surface_ten`    | []                    | [0, 1.79E308]           | N/m      | temperature               | surface tension
`mag_susc`       | []                    | [-1.79E308, 1.79E308]   | ml/mol   |                           | magnetic susceptibility
`dipole`         | []                    | [0, 1.79E308]           | debye    |                           | dipole moment

### Keywords

Keywords are an optional field that allow users to classify the material. Selecting multiple keywords is allowed.

Keyword         | Description  
----            | ----
** monomer types: ** |
olefin          | a chemical with one double bond and is locally surrounded by only C and H
diene           | a chemical with two or more double bonds
styrene         | a chemical with C=C-(c1ccccc1) structure
cyclic_olefin   | a chemical where at least one double bond is found in a ring (excluding aromatic rings)
acetylene       | a chemical with one or more triple bounds (C≡C)   
||
vinyl           | a chemical with C=C-R structure and the local surrounding contains elements other than C and H
vinyl_ether     | a chemical with C=C-O-R structure
vinyl_ester     | a chemical with C=C-O-(C=O)-R structure
acrylate        | a chemical with C=C-C(=O)O-R structure 
methylacrylate  | a chemical with C=C(C)-C(=O)O-R structure 
||
lactone         | (cyclic ester) a chemical with R-C(=O)O-R within a ring 
cyclic_ether    | a chemical with R-O-R within a ring 
cyclic_carbonate| a chemical with R-O-C(=O)O-R within a ring
cyclic_anhydride| a chemical with R-C(=O)-O-C(=O)-R with a ring (includes N-carboxy anhydrides)
oxazoline       | a chemical with a R-N=C(R)-O-R within a five membered ring 
||
lactam          | (cyclic amide) a chemical with R-C(=O)N(R)-R within a ring 
cyclic_amine    | a chemical with R-N(R)-R within a ring
cyclic_sulfur   | a chemical with R-S-R or R-S(=O)-R within a ring
thiophene       | a chemical with C=C1=CC=CS1 5 member ring
phosphoesters   | a chemical with R-O-P(=O)(OR)-O-R within a ring
phosphonate     | a chemical with R-O-P(=O)(C(R)(R)R)-O-R within a ring
phostone        | a chemical with R-P(=O)(R)-O-R within a ring
phosphazenes    | a chemical with R-P(R)(R)=N-R within a ring
siloxane        | a chemical with R-O-Si(R)(R)-O-R within a ring
carbosiloxane   | a chemical with R-Si(R)(R)-R within a ring
||
diol              | a chemical with two or more -OH groups
dicarboxylic_acid | a chemical with two or more -C(=O)OH groups
diamines          | a chemical with two or more -NH2 groups
diacid chloride   | a chemical with two or more -COCl groups
** other ** |
filler    | a substance that is added to resins
matrix    | a substance for binding and holding reinforcements together 



## Example

[Example](../Example/#experiment-1-anionic-polymerization-of-styrene)



