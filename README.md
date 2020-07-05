# LogsExtracted
Simple python program to extract data from logs

### Prerequisites:

- Python 3.8
- Poetry (https://python-poetry.org/)

### Installation:

    poetry install

### How to run:

    python3 main.py

Script runs with usage of `test.log`

If you need to parse other logs - place them near script and rename it to test.log

Parsable logs example:

    2015-10-28T12:24:33,903 TRACE [OperImpl] entry with (addClient:97900)

Program uses follwing GROK pattern to recognize logs:

    %{TIMESTAMP_ISO8601:ts} TRACE \[%{WORD:name}\] .* \(%{WORD:service}\:%{NUMBER:req_id}\)

Results show:

1) Name of service
2) How many times it was executed
3) Max execution time
