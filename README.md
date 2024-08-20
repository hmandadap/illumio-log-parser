# illumio-log-parser
A program to parse flow log files and map them to tags based on a lookup table

## Features  
- Reads a lookup table in CSV format with columns for destination port, protocol, and tag.
- Processes flow logs, matching each entry against the lookup table to determine the appropriate tag.
- The program handles case insensitivity by converting the protocol field to lowercase before performing lookups.
- Generates an output file with counts of matches for each tag and each port/protocol combination.

## Requirements
- Python 2.7
- 1. **lookup_table.csv**: A CSV file containing the mapping of destination ports and protocols to tags. The format should be:

      dstport,protocol,tag
      25,tcp,sv_P1
      68,udp,sv_P2
      23,tcp,sv_P1
      31,udp,SV_P3
      443,tcp,sv_P2

   **Headers:**
   - `dstport`: The destination port number (e.g., 25, 443).
   - `protocol`: The protocol used (e.g., `tcp`, `udp`).
   - `tag`: The tag associated with this port and protocol combination.

2. **logs.txt**: A text file containing flow log entries. Each line should have the following format:
    Sample input line:
    2 10.0.0.1 10.0.0.2 443 tcp 1234 ACCEPT OK
   Format:
      ```plaintext
      <field_1> <field_2> <field_3> <dstport> <protocol> <field_6> <field_7>
  **Headers:**
   - `dstport`: The destination port (e.g., 443, 80), found in the 4th field.
   - `protocol`: The protocol (e.g., tcp, udp), found in the 5th field.
   - `tag`: The tag associated with this port and protocol combination.

## Usage
1. Clone the repository:
   ```
   git clone https://github.com/hmandadap/illumio-log-parser.git
   cd illumio-log-parser
   ```
2. Replace your input log file and lookup_table as per above requirements or run the program with existing files in the folder.
3. Run the program:
   ```
    python parser.py
   ```
4. Check the output.txt file for the output.
   sample output:
      Tag Counts:
      Tag     Count
      Untagged        1
      sv_p3   1
      sv_p2   2
      sv_p1   2
      
      Port/Protocol Combination Counts:
      Port    Protocol        Count
      80      tcp     1
      23      tcp     1
      25      tcp     1
      31      udp     1
      443     tcp     2


