# User

The 'user' node contains data related to the user. Anyone who interacts with the database can be a user.

**Features:**

* user can reference groups, collections, publications, and experiments
* required information
    * name
    * email
* optional information
    * group (CRIPT node)
    * publications (CRIPT node)
    * phone
    * website
    * twitter handle
    * ORCID #
    * organization
    * notes
* auto generate/update:
    * _id
    * class
    * version_schema
    * version_control (& all child) <-- update with version control node
    * date (& all child)

**App features to support this node:**

* a page to fill out: name, email, etc
* a tool to look up group, or enter _id
* a similar look up tool for experiments, collections, and publications
* allow additional optional information in attribute section given that it begins with +

## JSON Schema

```json
{
  "_id": objectId(),
  "class": "user",
  "version_schema": string,
  "version_control": {
    "_id": objectId(),
    "num": string
  },
  "last_modified": datetime,
  "created": datetime,
  "name": string,
  "email": string,
  "optional attributes"
}
```

---

## Description

Key             |Data Type     |Required  |Description
-------------   |---------     |------    |----
`_id`                 |<span style="color:rgb(0, 72, 189)"> objectId() </span>   | <span style="color:rgb(0, 72, 189)">  auto  </span> | <span style="color:rgb(0, 72, 189)">  unique database id  </span>
`class`               |<span style="color:rgb(0, 72, 189)">  string  </span>     | <span style="color:rgb(0, 72, 189)">  auto  </span> | <span style="color:rgb(0, 72, 189)">  class of node  </span>
`version_schema`      |<span style="color:rgb(0, 72, 189)">  string  </span>     | <span style="color:rgb(0, 72, 189)">  auto  </span> | <span style="color:rgb(0, 72, 189)">  schema version; Ex: "v0.1"  </span>
`version_control`     |                                                          |                                                     | <span style="color:rgb(0, 72, 189)">  version control object  </span>
`version_control/_id` |<span style="color:rgb(0, 72, 189)">  objectId()  </span> | <span style="color:rgb(0, 72, 189)">  auto  </span> | <span style="color:rgb(0, 72, 189)">  reference id to node history  </span>
`version_control/num` |<span style="color:rgb(0, 72, 189)">  string  </span>     | <span style="color:rgb(0, 72, 189)">auto  </span>   | <span style="color:rgb(0, 72, 189)">  type of node ; Ex: "group"  </span>
`last_modified`       |<span style="color:rgb(0, 72, 189)">  datetime  </span>   | <span style="color:rgb(0, 72, 189)">auto  </span>   | <span style="color:rgb(0, 72, 189)">  last modified datetime  </span>
`created`             |<span style="color:rgb(0, 72, 189)">  datetime  </span>   | <span style="color:rgb(0, 72, 189)">auto  </span>   | <span style="color:rgb(0, 72, 189)">  datetime created  </span>
`name`                | string        | required      | name of user
`email`               | string        | required      | user email address


### Attributes

Attributes are optional properties that can be associated with this node. The following list is the officially supported
keys. Users may define their own keys by placing a '+' in front of their custom key.

Key                   | Data Type      | Description
-------------         |---------       |----
`owns_groups`         | list[dict]     | [groups that the user owns](../data-models/Groups.md)
`owns_groups\_id`     | objectId()     | id of group
`owns_groups\name`    | string         | name of group
`in_groups`           | list[dict]     | [groups that the user belongs to](../data-models/Groups.md)
`in_groups\_id`       | objectId()     | id of group
`in_groups\name`      | string         | name of group
`publication`         | list[dict]     | [publications the user authored](../data-models/Publications.md)
`publication\_id`     | objectId()     | id of publication
`publication\title`   | string         | title of publication
`phone`               | string         | phone number (###-###-####)
`web`                 | string         | website
`twitter`             | string         | twitter handle
`orcid`               | string         | [ORCID number](https://orcid.org/)
`organization`        | string         | author's organization
`position`            | string         | author's position in organization
`note`                | string         | free-form space to store any text

---

## Example

[User Example](../Example/#user)

