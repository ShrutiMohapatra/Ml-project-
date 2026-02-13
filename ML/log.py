import pandas as pd

with open("/var/log/syslog") as file:
    logs = file.readlines()

print(logs[:10])



