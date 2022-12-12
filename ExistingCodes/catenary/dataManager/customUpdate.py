import yaml


def customUpdate(cfg):
    cfg = updateDiameters(cfg)
    return cfg

def updateDiameters(cfg):
    if cfg['geometry']['NominalOD'] !=None:
        cfg['geometry']["NominalID"] = cfg['geometry']['NominalOD']- 2*cfg['geometry']['DesignWT']
    elif cfg['geometry']['NominalID'] !=None:
        cfg['geometry']['NominalOD'] = cfg['geometry']['NominalID'] + 2*cfg['geometry']['DesignWT']
    
    return cfg
