# LogsExtracted
Simple python program to extract data from logs


To use this script you need to have Python 3.8 installed.

Also install dependencies using poetry.lock

Command: poetry install

Script runs with usage of test.log
If you need to parse other logs - place them near script and rename it to test.log

Format of logs that can be parsed:
2015-10-28T12:24:33,903 TRACE [OperImpl] entry with (addClient:97900)

Results show:
1) Name of service
2) How many times it was executed
3) Max execution time