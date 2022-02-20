#%%
# #!/usr/bin/env python
import sys

# [Define group level master information]
current_vin = None
make = None
year = None
curr = {}


def reset():
 # [Logic to reset master info for every new group]
    global current_vin
    global curr
    global make
    global year
    current_vin = None
    curr = {}
    make = None
    year = None

# Run for end of every group
def flush():
    # [Write the output]
    for value in curr.values():
        if value[0] == "A":
            print(f"{current_vin}\t{value[0]}\t{make}\t{year.strip()}")
            

# input comes from STDIN
# [parse the input we got from mapper and update the master info]
for linet in sys.stdin:
    line = linet.split("\t")
    vin = line[0]
    if line[1] == "I":
        make = line[2]
        year = line[3]

    # detect key changes
    if current_vin != vin:
        if current_vin is not None:
            flush()
        reset()

    # update master info after key change handling
    curr[linet]=((line[1],line[2],line[3]))
    current_vin = vin
# do not forget to output the last group if needed!
flush()

# %%
