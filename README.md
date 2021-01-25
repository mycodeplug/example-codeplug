# example-codeplug

Generate DMR codeplugs from a variety of online sources using
[dzcb](https://github.com/mycodeplug/dzcb).

## Requirements

* linux or macOS (windows not yet supported)
* python 3.5+ (python 3.8 recommended)
* [tox](https://tox.readthedocs.io/en/latest/)
* [dzcb](https://github.com/mycodeplug/dzcb)

## Editing

Create / edit codeplug source files under [`/input`](/input).

If multiple subdirectories exist under `/input`, then multiple
codeplugs will be generated.

### See [dzcb README.md](https://github.com/mycodeplug/dzcb#dzcb) for
more information on input files and formats.

## Generating

### Github Actions

* Fork this repo
  * In the newly forked repo, click the "Actions" tab and
    enable Github Actions for your fork.
* Rename `input/kf7hvm` to `input/your-call`
* customize generate.sh and other files
  * `kf7hvm-md-uv380.json`: set your Radio ID and Radio Name
    * Copy templates from [default-tyt-md380](https://github.com/mycodeplug/dzcb/blob/main/codeplug/default-tyt-md380) for
      monoband variants.
  * `order.json`: preferred zone order, zone exclusion, preferred talkgroup order
  * `scanlists.json`: additional scanlists
* To use Repeaterbook, go to [Settings > Secrets](../../settings/secrets/actions)
  and set the following variables:
  * REPEATERBOOK_USER
  * REPEATERBOOK_PASSWD
  * `prox.csv`: customize zones
* Github [`codeplugs`](.github/workflows/codeplugs.yml) workflow
  will automatically build all codeplugs in the [`input`](./input) directory.
* When a [Release](../../releases) is published, the generated
  codeplugs will be hosted publicly with a stable URL.

### Manual

```
pip install tox
tox
```
