# Just for fun project

SLS document must be
 - has location information on the first page
 - has respondent list information on the second page and so on

## Installation

install tesseract-ocr, you can download from [here]([https://](https://github.com/UB-Mannheim/tesseract/wiki#tesseract-installer-for-windows)).

install python dependencies by using this command

```bash
pip install -r requirements.txt
```

## Running

put your SLS data on data folder (only pdf files), then main script.

```bash
python main.py
```

or (linux)

```bash
python3 main.py
```

you can see the result on [result.csv](./result.csv) with filename and total respondent data for each SLS.