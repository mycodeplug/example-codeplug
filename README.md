# example-codeplug

Generate DMR codeplugs from a variety of online sources using
[dzcb](https://github.com/mycodeplug/dzcb).

## Data Sources

### [PNWdigital.net](http://PNWDigital.net)

**Before using this network, please read the [quick start](http://www.pnwdigital.net/quick-start.html)**

### [SeattleDMR](https://seattledmr.org/)

**Before using these repeaters, please read the [website](https://seattledmr.org)**

### Repeaterbook Proximity

### [Local](https://github.com/mycodeplug/dzcb/blob/main/src/dzcb/data/k7abd/Digital-Repeaters__Local.csv)

Information on these Western Washington standalone DMR repeaters was
retrieved from Repeaterbook and respective websites in 2020 October.

### Simplex, GMRS, etc

Some common [Digital](https://github.com/mycodeplug/dzcb/blob/main/src/dzcb/data/k7abd/Digital-Others__Simplex.csv)
and [Analog](https://github.com/mycodeplug/dzcb/blob/main/src/dzcb/data/k7abd/Analog__Simplex.csv) simplex frequencies,
and [GMRS/FRS and MURS channels](https://github.com/mycodeplug/dzcb/blob/main/src/dzcb/data/k7abd/Analog__Unlicensed.csv) are included.

## Editing

Create / edit codeplug source files under [`/input`](/input).

If multiple subdirectories exist under `/input`, then multiple
codeplugs will be generated.

The [`default`](./input/default) directory contains the example codeplug
input files along with 2 scripts:

  * [`generate.sh`](./input/default/generate.sh) builds the codeplug with a
    standard bash shell command.
  * [`generate.py`](./input/default/generate.py) builds the same codeplug
    using python code.

Derivative codeplugs don't need to include both scripts. Use the format
that is most familiar. While the sample scripts show identical functionality,
the python code could be extended to hack at the generation process itself.

### See [dzcb README.md](https://github.com/mycodeplug/dzcb#dzcb) for more information on input files and formats.

## Generating

See [WALKTHROUGH](https://github.com/mycodeplug/dzcb/blob/main/doc/WALKTHROUGH.md#example-codeplug-walkthough)
for step-by-step instructions.

### Github Actions

* [Fork this repo](../../fork)
  * In the newly forked repo, click the ["Actions" tab](../../actions) and
    enable Github Actions for your fork.
* customize codeplug input files in [`/input/default`](./input/default)
  * [`example-md-uv380.json`](./input/default/example-md-uv380.json#L189-L193):
    set your Radio ID and Radio Name
    * Copy templates from
      [default-tyt-md380](https://github.com/mycodeplug/dzcb/blob/main/codeplug/default-tyt-md380)
      for monoband variants.
  * [`example-d878uv.conf`](./input/default/example-d878uv.conf):
    set your Radio ID and Radio Name
    * See README and templates in
      [dmrconfig](https://github.com/mycodeplug/dzcb/blob/main/src/dzcb/data/dmrconfig)
      for more information and other radio types.
  * [`k7abd`](./input/default/k7abd): manually defined zones in
    K7ABD anytone-config-builder format. See N7EKB's
    [`cps-import-builder` reference data files](https://github.com/n7ekb/cps-import-builder/tree/main/reference_data_files/N7EKB_shared_files)
    for more examples.
  * [`order.csv`](./input/default/order.csv): preferred zone, contact, channel order
  * [`exclude.csv`](./input/default/exclude.csv): zone, contact, channel exclude
  * [`replacements.csv`](./input/default/replacements.csv): object name replacements (regex)
  * [`scanlists.json`](./input/default/scanlists.json): additional scanlists
  * [`generate.py`](./input/default/generate.py): options passed to `dzcb` (whether
    to include PNWDigital, SeattleDMR, default files, etc)
* [`prox.csv`](./input/default/prox.csv): customize points of
    interest, distances, and desired bands
* Github [`codeplugs`](.github/workflows/codeplugs.yml) workflow
  will automatically build all codeplugs in the [`input`](./input) directory.
* When a [Release](../../releases) is published, the generated
  codeplugs will be hosted publicly with a stable URL.

### Manual

#### Requirements

* linux, macOS, windows
* python 3.6+ (python 3.8 recommended)
* [tox](https://tox.readthedocs.io/en/latest/)

#### Build

To output to a specific directory, set the `OUTPUT` environment variable.

```
pip install tox
tox
```

To run the `generate.sh` shell scripts

```
tox -e shell
```
