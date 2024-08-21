sample_line = "2 10.0.0.1 10.0.0.2 443 tcp 1234 ACCEPT OK\n" # 43 bytes size
num_of_lines = 244000 # for 10mb of data as each line is 43 bytes
num_of_mappings = 10000

with open("logs_10mb.txt", "w") as f:
    for _ in range(num_of_lines):
        f.write(sample_line)

with open("lookup_table_10000.csv", "w") as f:
    f.write("dstport,protocol,tag\n")
    for i in range(num_of_mappings):
        f.write("{},tcp,sv_p{}\n".format(i+1, i+1))

