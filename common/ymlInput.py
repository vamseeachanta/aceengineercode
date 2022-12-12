def ymlInput(applicationYml, customYml=None):
    import yaml

    from common.update_deep import update_deep_dictionary

    with open(applicationYml, 'r') as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.Loader)

    if customYml != None:
        #  Update values file
        try:
            with open(customYml, 'r') as ymlfile:
                cfgCustomValues = yaml.load(ymlfile, Loader=yaml.Loader)

            default_yaml_file = cfgCustomValues.get('default_yaml', None)

            with open(customYml) as fp:
                custom_file_data = fp.read()
                cfgDefaultAndCustomValues = yaml.load(custom_file_data, Loader=yaml.Loader)

            if default_yaml_file is not None:
                with open(default_yaml_file) as fp:
                    default_file_data = fp.read()

                custom_and_default_yaml_data = custom_file_data + "\n" + default_file_data
                cfgDefaultAndCustomValues = yaml.load(custom_and_default_yaml_data, Loader=yaml.Loader)

            cfg = update_deep_dictionary(cfg, cfgDefaultAndCustomValues)

        except Exception as e:
            import sys
            print("Update Input file could not be loaded successfully.")
            print("Error is : {}".format(e))
            print("Stopping program")
            sys.exit()

    return cfg
