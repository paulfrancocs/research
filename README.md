This code processes Russian nouns ending in -ер to explore whether they are inanimate and whether they have a recognizable native base.

## Description

- `opencorpora_json.py` parses the `dict.opcorpora.xml` file from OpenCorpora and extracts all inanimate nouns. It saves them to a `.json` file.
- `main.py` loads that JSON, reads a CSV file with nouns ending in -ер (from the Russian National Corpus), checks which are inanimate, and tries to infer base forms.
- The final results are saved in `data.xlsx`, with two columns, derived word (with suffix) and base word.

The results are preliminary. Some word pairs may match formally but are not actually related.

## Files

- dict.opcorpora.xml
- opencorpora_json.py
- main.py
- russian_nouns_er.csv
- data.xlsx

## Source

This project uses the file `russian_nouns.txt` from [Russian-Nouns](https://github.com/Harrix/Russian-Nouns) by [Harrix](https://github.com/Harrix), reused under the MIT License.
