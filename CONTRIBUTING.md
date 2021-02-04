# Contributing guidelines

- Use `kebab-case` file names, as they are used when forming the documentation URLs
  * Lower case with a `-` to separate words
- Place no more than one sentence per source line whenever allowed by markdown syntax
  * Table rows have to be crammed into a single line
  * One sentence can be spread over multiple source lines if it is long


## Pull requests

Please direct all pull requests to the `develop` branch.
Add one of the maintainers as a reviewer to get your contributions reviewed and
merged into the documentation.


## Building the docs Locally

The documentation is built with [mkdocs](https://www.mkdocs.org/#mkdocs).

You'll need a working python environment to get started.
If you are within a `conda` environment, do:

```
conda install mkdocs-material-extensions
```

Alternatively, you can use `pip`:
```
pip install mkdocs-material-extensions
```

To build the static site in `./site`:
```
mkdocs build
```

To serve the site, with live reloading:
```
mkdocs serve
```
This will be served at `localhost:8000` by default.
