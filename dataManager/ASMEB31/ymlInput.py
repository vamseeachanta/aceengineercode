import collections
from collections import Mapping

import yaml


def ymlInput(defaultYml, updateYml):

    with open(defaultYml, 'r') as ymlfile:
        cfg = yaml.load(ymlfile)

    if updateYml != None :
    #  Update values file
        try:
            with open(updateYml, 'r') as ymlfile:
                cfgUpdateValues = yaml.load(ymlfile)
    #  Convert to logs
            # print(cfgUpdateValues)
            cfg = update_deep(cfg, cfgUpdateValues)
        except:
            print("Update Input file could not be loaded successfully. Running program default values")

    return cfg

def update_deep(d, u):
    for k, v in u.items():
        # this condition handles the problem
        if not isinstance(d, Mapping):
            d = u
        elif isinstance(v, Mapping):
            r = update_deep(d.get(k, {}), v)
            d[k] = r
        else:
            d[k] = u[k]

    return d

def compare_dictionaries():
    from pprint import pprint

    from deepdiff import DeepDiff
    t1 = {1:1, 2:2, 3:3}
    t2 = t1
    print(DeepDiff(t1, t2))