# Additional Objects

## Author

Key          |Data Type|Required|Description
-------------|---------|------   |----
`id_author`  |string   |auto     |unique database id for authors
`log`        |string   |auto     | log for version control
`date_join`  |datetime |auto     | date author joined
`name`       |string   |required | author's name
`email`      |string   |required | author's email address
`orcid_num`  |string   |optional | [ORCID number](https://orcid.org/)
`organization`|string  |optional | author's Organization
*username  |
*password  |

##### Example

``` json
{
  "id author": "################",
  "log": [
    {
      "id_version": "################",
      "id_author": "################",
      "version": "v0.1",
      "date": [2021, 2, 6, 12, 33, 45]
    }
  ],
  "date_join": [2021, 2, 6, 12, 33, 45],
  "name": "Dylan W",
  "email": "dylan@CRIPT.edu",
  "orcid_num": "0000-0000-0000-0001",
  "organization": "University of Polymers"
}
```

## Models

Key          |Data Type |Required |Description
-------------|--------- |------   |----
`id_model`   |string    |auto     |unique database id
`log`        |string    |auto     | log for version control

## Log

list of dictionaries

##### dictionary

Key           |Data Type |Required       |Description
------------- |--------- |------         |----
`id_version`  |string    |auto           |unique database id for object version
`id_author`   |string    |auto           |unique database id for authors
`version`     |string    |optional/auto  |user defined versions (Ex. v1.4 or v0.0.2)
`date`        |date      |auto           |data of change [year, month, day, hour, minute, second]

##### Version label

`version`    |version stage
-------------|---------
v0.#.# | general use
v1.#.# | staged for publication
v2.#.# | publication (and revisions)
v3.#.# | post-publication


##### Example
``` JSON
  "log": [
    {
      "id_version": "################",
      "id_author": "################",
      "version": "v0.1",
      "date": [2021, 1, 6, 12, 21, 1]
    },
    {
      "id_version": "################",
      "id_author": "################",
      "version": "v0.2",
      "date": [2021, 2, 6, 12, 33, 45]
    }
  ]
```
