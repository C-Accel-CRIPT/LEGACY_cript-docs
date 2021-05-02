
^^Are mixtures supported?^^

* Yes, in the [Materials node](../data-models/Materials_P.md) the identifiers section is a list, which means multiple identifiers from each of the 
  mixtures components can be added.



^^What format should units be in?^^

* We use [Pint](https://pint.readthedocs.io/en/stable/) to convert units, so check with their documentation for [officially supported units](https://github.com/hgrecco/pint/blob/master/pint/default_en.txt).



^^Are user defined properties or material identifiers allowed?^^

* Yes, CRIPT accepts any user-defined vocabulary such that it begins with a `+`, but would encourage users to stick to 
  official vocabulary whenever possible as that increases the findablity of your data.



^^Can I link to data in a different database?^^ 

* Yes, the [data node](../Data/#attributes) allows you to link to outside data with `web_link`.


