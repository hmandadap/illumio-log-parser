# illumio-log-parser
A program to parse flow log files and map them to tags based on a lookup table

## Features
- Reads flow log files and a lookup table in CSV format.
- Maps destination ports and protocols to tags based on the lookup table.
- Generates an output file with counts of matches for each tag and each port/protocol combination.

## Requirements
- Python 2.7
- CSV file containing the lookup table.
- Flow log file to be processed.

## Usage
1. Clone the repository:
   git clone https://github.com/hmandadap/illumio-log-parser.git
   cd illumio-log-parser
2. Replace your input log file and lookup_table as per above requirements.
3. Run the program:
   ```
    python parser.py
   ```
4. Check the output.txt file for the output.


