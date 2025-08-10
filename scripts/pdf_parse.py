# -*- coding: utf-8 -*-
'''
Author: Vamsee Achanta
Objective: To help get statistics from tabular data
'''


def set_up_application():
    import logging
    import os

    from common.ApplicationManager import configureApplicationInputs
    from common.set_logging import set_logging

    basename = os.path.basename(__file__).split('.')[0]
    application_manager = configureApplicationInputs(basename)
    application_manager.configure()

    set_logging(application_manager.cfg)
    logging.info(application_manager.cfg)

    return application_manager


def run_cfg_variations(application_manager):
    application_manager.cfg_variation_type = 'pre_analysis'
    run_cfg_variations_by_type(application_manager)
    application_manager.cfg_variation_type = 'post_analysis'
    cfg_variations_array = run_cfg_variations_by_type(application_manager)
    return cfg_variations_array


def run_cfg_variations_by_type(application_manager):
    cfg_variations_array = []
    if application_manager.cfg['cfg_variations'][application_manager.cfg_variation_type] is not None:
        for run_number in range(
                0, len(application_manager.cfg['cfg_variations'][application_manager.cfg_variation_type])):
            application_manager.update_cfg_with_variation(run_number)
            cfg_variations_array.append(pdf_parse(application_manager.cfg))

    return cfg_variations_array


def pdf_parse(cfg):
    import pandas as pd

    from common.data import ReadData, SaveData
    read_data = ReadData()
    save_data = SaveData()

    df_array = []
    for file_index in range(0, len(cfg['files']['from_pdf'])):
        df_array.append(read_data.from_pdf(cfg, file_index))

        for df_index in range(0, len(df_array[file_index])):
            print(df_array[file_index][df_index].columns)
            print(df_array[file_index][df_index].head(3))
            if cfg.files['from_pdf'][file_index]['save']:
                file_name = cfg['Analysis']['result_folder'] + cfg['Analysis'][
                    'file_name'] + 'file_{0}_df_index_{1}.csv'.format(file_index, df_index)
                df_array[file_index][df_index].to_csv(file_name)

    # TODO Add filter options to only get the required data

    save_data.saveDataYaml(cfg, cfg['Analysis']['result_folder'] + cfg['Analysis']['file_name'], False)
    return cfg


if __name__ == '__main__':
    application_manager = set_up_application()
    cfg_base = pdf_parse(application_manager.cfg)
    cfg_variations_array = run_cfg_variations(application_manager)
