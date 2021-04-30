# Publications

The 'publication' node contains data related to a publication. Publications point to a collection of experiments
that no longer have write or append options. 

**Features:**

* publication can reference collections
* required information
    * title
* optional information
    * collections (CRIPT nodes)
    * title
    * authors
    * journal
    * publisher
    * year
    * vol
    * issue
    * pages
    * doi
    * issn
    * arxiv_id
    * PMID
    * website
    * notes
* auto generate/update:
    * _id
    * class
    * version_schema
    * version_control (& all child) <-- update with version control node
    * date (& all child)
  

## JSON Schema

```json
{
  "_id": objectId(),
  "class": "publication",
  "version_schema": string,
  "version_control": {
    "_id": objectId(),
    "num": string
  },
  "last_modified": datetime,
  "created": datetime,
  "title": string,
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
`last_modified`       |<span style="color:rgb(0, 72, 189)">  datetime  </span>   | <span style="color:rgb(0, 72, 189)">auto  </span>   | <span style="color:rgb(0, 72, 189)">  last modified datetime  </span>
`created`             |<span style="color:rgb(0, 72, 189)">  datetime  </span>   | <span style="color:rgb(0, 72, 189)">auto  </span>   | <span style="color:rgb(0, 72, 189)">  datetime created  </span>
`title`               | string         | required  | publication title


### Attributes

Attributes are optional properties that can be associated with this node. The following list is the officially supported
keys. Users may define their own keys by placing a '+' in front of their custom key.

Key                   | Data Type      | Description
-------------         |---------       |----
`collection`          | list[dict]     | [collection nodes](../data-models/Collections.md)
`collection\_id`      | objectId()     | id of collection
`collection\name`     | string         | name of collection
`collection\created`  | datetime       | date collection created
`authors`             | list[string]   | authors
`journal`             | string         | journal
`publisher`           | string         | publisher
`year`                | integer        | publishing year
`vol`                 | integer        | volume number
`issue`               | integer        | issue number
`pages`               | string         | page number
`doi`                 | string         | [DOI: digital object identifier](https://www.doi.org/)
`issn`                | string         | [ISSN: international standard serial number](https://www.issn.org/)
`arxiv_id`            | string         | [arXiv identifier](https://arxiv.org/)
`PMID`                | string         | [PubMed ID](https://pubmed.ncbi.nlm.nih.gov/)
`web`                 | string         | publication website
`note`                | string         | free-form space to store any text

---

## Example

[Publication Example](../Example/#publication)

