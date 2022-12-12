import math

import yaml

with open("dataManager\\API_RP_2RD\\APIRP2RD.yml", 'r') as ymlfile:
    config = yaml.load(ymlfile)
  
for section in config:
    print(section)

print(config)