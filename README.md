# example-codeplug

## Requirements

* linux or macOS (windows not yet supported)
* python 3.5+ (python 3.8 recommended)
* [tox](https://tox.readthedocs.io/en/latest/)
* [dzcb](https://github.com/mycodeplug/dzcb)

## Editing

Create / edit codeplug source files under [`/input`](/input).

If multiple subdirectories exist under `/input`, then multiple
codeplugs will be generated.

## Generating

### Github Actions

If you forked this repo, first click the "Actions" tab and
enable Github Actions for your fork.

Any changes pushed to this repository will trigger an
automatic rebuild of all codeplugs in `input` that have
an executable `generate.sh` file.

### Manual

```
pip install tox
tox
```
