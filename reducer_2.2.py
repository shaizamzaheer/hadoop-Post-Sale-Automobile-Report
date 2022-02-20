
import sys
# [Define group level master information]
sum = 0
key_old = None

def reset():
    # [Logic to reset master info for every new group]
    sum = 0
    # Run for end of every group

def flush():
    print(f'{key_old}\t{sum}')
    # [Write the output]

    # input comes from STDIN
for line in sys.stdin:
    #    [parse the input we got from mapper and update the master info]
    linesplit = line.split('\t')
    key = linesplit[0]
    value = int(linesplit[2])
    if key_old != key:
        if (key_old != None):
            flush()
            sum = 0
    # [detect key changes]
        reset()
    sum += value
    # [update more master info after the key change handling]
    key_old = key
# do not forget to output the last group if needed!
flush()