import json
import csv
from collections import defaultdict


"""
Load configuration from the JSON file
"""
def load_config(config_file):
    f = open(config_file)
    config = json.load(f)
    f.close()
    return config

"""
Loading the lookup_table to a dictionary
"""
def load_lookup_table(file_path):
    lookup_table = {}
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            dstport, protocol, tag = row
            lookup_table[(int(dstport), protocol.lower())] = tag.lower()

    return lookup_table

"""
Parsing the log_file by each row
"""
def process_flow_logs(log_file, lookup_table):
    tag_counts = defaultdict(int)
    port_protocol_counts = defaultdict(int)

    with open(log_file, mode='r') as file:
        for line in file:
            columns = line.split()
            if len(columns) < 5:  # checking columns as per sample input file
                continue

            dstport = int(columns[3])
            protocol = columns[4].lower()
            port_protocol_counts[(dstport, protocol)] += 1
            tag_counts[lookup_table.get((dstport, protocol), "Untagged")] += 1

    return tag_counts, port_protocol_counts

"""
Writing to the output file
"""
def write_output(tag_counts, port_protocol_counts, output_file):
    with open(output_file, mode='w') as outfile:
        outfile.write("Tag Counts:\n")
        outfile.write("Tag\tCount\n")
        for tag, count in tag_counts.items():
            outfile.write("{}\t{}\n".format(tag, count))

        outfile.write("\nPort/Protocol Combination Counts:\n")
        outfile.write("Port\tProtocol\tCount\n")
        for (port, protocol), count in port_protocol_counts.items():
            outfile.write("{}\t{}\t{}\n".format(port, protocol, count))

def main(config_file):
    config = load_config(config_file)
    lookup_table = load_lookup_table(config["lookup_file"])
    tag_counts, port_protocol_counts = process_flow_logs(config["log_file"], lookup_table)
    write_output(tag_counts, port_protocol_counts, config["output_file"])

if __name__ == "__main__":

    config_file = 'config.json'  # Path to your configuration file
    
    main(config_file)
