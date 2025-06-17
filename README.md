{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Russian Nouns with the Suffix -\uc0\u1077 \u1088 \
\
This code processes Russian nouns ending in **-\uc0\u1077 \u1088 ** to explore whether they are inanimate and whether they have a recognizable native base.\
\
## Description\
\
- \'91opencorpora_json.py\'92 parses the \'91dict.opcorpora.xml\'92 file from OpenCorpora and extracts all inanimate nouns. It saves them to a '.json' file.\
- 'main.py' loads that JSON, reads a CSV file with nouns ending in **-\uc0\u1077 \u1088 ** (from the Russian National Corpus), checks which are inanimate, and tries to infer possible base forms.\
- The final results are saved in 'data.xlsx', with two columns: "derived word (with suffix)" and "base word".\
\
The results are preliminary. Some word pairs may match formally but are not actually related.\
\
## Files\
\
- 'dict.opcorpora.xml'\
- 'opencorpora_json.py'\
- 'main.py'\
- 'russian_nouns_er.csv'\
- 'data.xlsx'\
\
## Source\
\
This project uses the file 'russian_nouns.txt' from [Russian-Nouns](https://github.com/Harrix/Russian-Nouns) by [Harrix](https://github.com/Harrix), reused under the MIT License.\
\
\
}