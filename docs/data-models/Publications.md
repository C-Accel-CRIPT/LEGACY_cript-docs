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


**App features to support this node:**

* a page to fill out publication details
* a tool to look up collections, or enter _id
* allow additional optional information in attribute section given that it begins with +

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
  "date_created": datetime,
  "date_last_mod": datetime,
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
`ver_sch`             |<span style="color:rgb(0, 72, 189)">  string  </span>     | <span style="color:rgb(0, 72, 189)">  auto  </span> | <span style="color:rgb(0, 72, 189)">  schema version; Ex: "v0.1"  </span>
`ver_con`             |                                                          |                                                     | <span style="color:rgb(0, 72, 189)">  version control object  </span>
`ver_con/_id`         |<span style="color:rgb(0, 72, 189)">  objectId()  </span> | <span style="color:rgb(0, 72, 189)">  auto  </span> | <span style="color:rgb(0, 72, 189)">  reference id to node history  </span>
`ver_con/num`         |<span style="color:rgb(0, 72, 189)">  string  </span>     | <span style="color:rgb(0, 72, 189)">auto  </span>   | <span style="color:rgb(0, 72, 189)">  type of node ; Ex: "group"  </span>
`date`                |                                                          |                                                     | <span style="color:rgb(0, 72, 189)">  datetime object  </span>
`date/created`        |<span style="color:rgb(0, 72, 189)">  datetime  </span>   | <span style="color:rgb(0, 72, 189)">auto  </span>   | <span style="color:rgb(0, 72, 189)">  datetime created  </span>
`type/last_mod`       |<span style="color:rgb(0, 72, 189)">  datetime  </span>   | <span style="color:rgb(0, 72, 189)">auto  </span>   | <span style="color:rgb(0, 72, 189)">  last modified datetime  </span>
`title`               | string         | required  | publication title


### Attributes

Attributes are optional properties that can be associated with this node. The following list is the officially supported
keys. Users may define their own keys by placing a '+' in front of their custom key.

Key                   | Data Type      | Description
-------------         |---------       |----
`coll`                |                | [collection nodes](../data-models/Collections.md)
`coll\_id`            | objectId()     | id of collection
`coll\name`           | string         | name of collection
`coll\date`           | datetime       | date collection created
`authors`             | list[string]   | authors
`author`              | list[dict]     | authors details 
`author\orcid`        | objectId()     | author [ORCID number](https://orcid.org/)
`author\name`         | string         | author name
`journal`             | string         | journal
`publisher`           | string         | publisher
`year`                | int            | publishing year
`vol`                 | int            | volume number
`issue`               | int            | issue number
`pages`               | string         | page number
`doi`                 | string         | [DOI: digital object identifier](https://www.doi.org/)
`issn`                | string         | [ISSN: international standard serial number](https://www.issn.org/)
`arxiv_id`            | string         | [arXiv identifier](https://arxiv.org/)
`PMID`                | string         | [PubMed ID](https://pubmed.ncbi.nlm.nih.gov/)
`web`                 | string         | publication website
`note`                | string         | free-form space to store any text

---

## Example

```json
{
  "_id": "507f191e810c19729de861ec",
  "class": "pub",
  "ver_sch": "v0.1",
  "ver_con": {
    "_id": "507f191e810c19729de861cb",
    "num": "v2.1"
  },
  "date": [
    {"created": 1612881183},
    {"last_mod": 1612881123}
  ],
  "notes": "",
  "users": [
    {"_id": "507f191e810c19729de860ec", "name": "Dylan W", "perm": "w"}
  ],
  "expt": [
    {"_id": "507f191e810c19729de860em", "name": "ROMP monomer order kinetic study", "date": 1612886423},
    {"_id": "507f191e810c19729de860en", "name": "PLA bottlebrush synthesis", "date": 1612886423},
    {"_id": "507f191e810c19729de860ej", "name": "ROP of lactide kinetics", "date": 1612886423}
  ],
  "attr": {
    "title": "Engineering of Molecular Geometry in Bottlebrush Polymers",
    "authors": ["Walsh, Dylan J.", "Dutta, Sarit", "Sing, Charles E.", "Guironnet, Damien"],
    "author": [
      {"_id": "507f191e810c19729de860ec", "name": "Dylan W"}
    ],
    "journal": "Macromolecules",
    "publisher": "American Chemical Society",
    "year": "2019",
    "vol": 52,
    "issue": 13,
    "page": "4847-4857",
    "doi": "10.1021/acs.macromol.9b00845",
    "issn": "0024-9297",
    "web": "http://pubs.acs.org/doi/10.1021/acs.macromol.9b00845",
    "group": [
      {"_id": "507f191e810c19729de860em", "name": "UIUC"}
    ]
  }
}
```

