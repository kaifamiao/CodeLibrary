"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

from collections import defaultdict

call_time = defaultdict(int)

for record in calls:
    call_time[record[0]] += int(record[3])
    call_time[record[1]] += int(record[3])

max_call_time = 0
max_caller = ''

for caller in call_time:
    if call_time[caller] > max_call_time:
        max_call_time = call_time[caller]
        max_caller = caller

print('{} spent the longest time, {} seconds, on the phone during September, 2016.'.format(max_caller, max_call_time))