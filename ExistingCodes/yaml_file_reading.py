# Example to read yaml files with  more features and flexibility

def yaml_file_reading(cfg=None):
    import sys

    from common.data import SaveData
    from common.ymlInput import ymlInput
    save_data = SaveData()
    if (sys.argv[1] != None):
        yaml_file = sys.argv[1]
    cfg = ymlInput(yaml_file)
    save_data.saveDataYaml(cfg, yaml_file + 'QA')

    print(cfg)

if __name__ == "__main__":
    print("reading yaml file to add enhancements")
    yaml_file_reading()
