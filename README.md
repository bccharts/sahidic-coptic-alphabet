## Sahidic Coptic alphabet chart

Uses [PlotDevice](http://plotdevice.io).


### Installation

- Fonts used: [Antinouu](http://www.evertype.com/fonts/coptic/) and [Charis SIL](http://software.sil.org/charis/).
- Download [PyYAML](http://pyyaml.org/wiki/PyYAML) (the zipfile is fine).
- Unpack it.
- Copy the `yaml` directory (inside of `lib`) into `~/Library/Application Support/PlotDevice` or the same directory as these files (per [the manual](http://plotdevice.io/tut/Libraries)).


### Graded worksheet notes

- `generate.py` has the list of characters to use for the worksheet. (At some point this should be ported to use the YAML data.)
- To generate a new list, run `python generate.py`. This will output `graded-alphabet.list`, which `sahidic-coptic-alphabet-worksheet-graded.pv` pulls from.
