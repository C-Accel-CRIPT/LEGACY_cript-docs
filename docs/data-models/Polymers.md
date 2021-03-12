# Challenges of Polymer Data

**Under Construction**

Polymers are ensembles of molecules produced by stochastic systems of reactions, meaning that there is 
no single representation that can capture the full molecular detail of a polymer. 


Additionally, 

In practice, unless it is an aliquot of another polymer, each polymer can be effectively regarded as a unique chemical 
object. This issue makes polymer data largely disparate and presents significant challenges to curating high-quality polymer datasets.
 polymer researchers rely on a series of chemical characterizations that each reveal partial information on the distribution.
characterization data are aggregated and reported, is largely nonstandard across the polymer community


## Comparison to small molecules 
 molecule-property tuple/pair style format that relates desired properties with the structures of the molecules of 
 interest. Data in this format fits naturally into widely available and well-supported relational database technologies,
 which store data in series of data tables relating molecular properties with the corresponding chemical descriptors.
Assimilating data from different sources is straightforward as the chemical descriptors can be used unambiguously to 
 define the chemical system and provide a handle to collate and aggregate distinct instances of data for the same chemical object.
For most molecules, this information is conveniently encoded with representations that detail their chemical connectivity, 
 such as SMILES ([simplified molecular-input line-entry system](https://en.wikipedia.org/wiki/Simplified_molecular-input_line-entry_system)) strings for organic molecules, 
 nucleic acid sequences for RNA, or amino acid sequences for proteins.

## Natural Language Processing (NLP) for polymer data
Extracting polymer information with natural language processing is considerably more challenging for polymers than
small molecules because there is no uniform nomenclature (typically generic terminology used), 
figures of polymer structure are extremely high variability, and ultimately a combination of figures, raw data, generic 
terminology are all needs to be combined to define a polymer structure. Moreover, data collection methods are highly 
variable and only provided relative structure inform which requires expert knowledge to put into context. Thus, 
hindering the generation of databases from prior literature, and questioning their reliability. 


## Current Polymer Databases
Currently, for most available datasets, polymer entries are identified through names of the polymers.
Name-based identification, however, often leads to ambiguity in molecular structure specification
because polymer chemistry poorly adheres to IUPAC polymer nomenclature, making automatic translation between 
polymer names and structure difficult.

* Bicerano, J., Prediction of Polymer Properties, 3rd Edition. CRC Press: 2002, DOI: [10.1201/9780203910115](https://doi.org/10.1201/9780203910115).
* Brandrup, J.; Immergut, E. H.; Grulke, E. A.; Abe, A.; Bloch, D. R., [Polymer Handbook](https://www.wiley.com/en-us/Polymer+Handbook%2C+2+Volumes+Set%2C+4th+Edition-p-9780471479369). Wiley New York: 1999.
* Polymer Property Predictor and Database. [http://pppdb.uchicago.edu/](http://pppdb.uchicago.edu/) 
* Otsuka, S.; Kuwajima, I.; Hosoya, J.; Xu, Y.; Yamazaki, M. PoLyInfo: Polymer Database for Polymeric Materials Design. 2011, IEEE, 22– 29, DOI: [10.1109/EIDWT.2011.13](10.1109/EIDWT.2011.13).
* Mark, J. E., Physical Properties of Polymers Handbook. Springer: 2007,  DOI: [10.1007/978-0-387-69002-5](https://doi.org/10.1007/978-0-387-69002-5).
* CHEMnetBASE - Polymers: a Property Database. [http://poly.chemnetbase.com/faces/polymers/PolymerSearch.xhtml](http://poly.chemnetbase.com/faces/polymers/PolymerSearch.xhtml) 
* NanoMine. [http://materialsmine.org/nm](http://materialsmine.org/nm)


## Other Material Data Models

[PolyDAT](https://pubs.acs.org/doi/10.1021/acs.jcim.1c00028)

[GEMD](https://citrineinformatics.github.io/gemd-docs/)