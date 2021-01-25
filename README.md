# example-codeplug

Generate DMR codeplugs from a variety of online sources using
[dzcb](https://github.com/mycodeplug/dzcb).

## Data Sources

### [PNWdigital.net](http://PNWDigital.net)

**Before using this network, please read the [quick start](http://www.pnwdigital.net/quick-start.html)**

### [SeattleDMR](https://seattledmr.org/)

**Before using these repeaters, please read the [website](https://seattledmr.org)**

### Repeaterbook Proximity

**[Repeaterbook](http://repeaterbook.com) account is required to access this endpoint**

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

### See [dzcb README.md](https://github.com/mycodeplug/dzcb#dzcb) for more information on input files and formats.

## Generating

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
  * [`k7abd`](./input/default/k7abd): manually defined zones in
    K7ABD anytone-config-builder format. See N7EKB's
    [`cps-import-builder` reference data files](https://github.com/n7ekb/cps-import-builder/tree/main/reference_data_files/N7EKB_shared_files)
    for more examples.
  * [`order.json`](./input/default/order.json): preferred zone order,
    zone exclusion, preferred talkgroup order
  * [`scanlists.json`](./input/default/scanlists.json): additional scanlists
  * [`generate.sh`](./input/default/generate.sh): options passed to `dzcb` (whether
    to include PNWDigital, SeattleDMR, default files, etc)
* To use Repeaterbook, go to [Settings > Secrets](../../settings/secrets/actions)
  and set the following variables:
  * REPEATERBOOK_USER
  * REPEATERBOOK_PASSWD
  * [`prox.csv`](./input/default/prox.csv): customize points of
    interest, distances, and desired bands
* Github [`codeplugs`](.github/workflows/codeplugs.yml) workflow
  will automatically build all codeplugs in the [`input`](./input) directory.
* When a [Release](../../releases) is published, the generated
  codeplugs will be hosted publicly with a stable URL.

### Manual

#### Requirements

* linux or macOS (windows not yet supported)
* python 3.5+ (python 3.8 recommended)
* [tox](https://tox.readthedocs.io/en/latest/)

```
pip install tox
tox
```
