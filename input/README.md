This directory contains subdirectories that will be built into
codeplug import files by `tox`.

Each subdirectory should contain, at-minimum an executable `generate.sh`
script which will be called by `tox` to create the codeplug.

The output top-level dir may be specified by the `OUTPUT` environment
variable.
