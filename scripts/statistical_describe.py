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
            cfg_variations_array.append(statistical_describe(application_manager.cfg))

    return cfg_variations_array


def statistical_describe(cfg):
    import pandas as pd

    from common.data import ReadData, SaveData
    from common.visualizations import Visualization
    read_data = ReadData()
    save_data = SaveData()
    viz_data = Visualization()

    df_array = []
    for file_index in range(0, len(cfg['files']['from_xlsx'])):
        df = read_data.from_xlsx(cfg, file_index)
        for replace_index in range(0, len(cfg['files']['from_xlsx'][file_index]['replace'])):
            to_replace = cfg['files']['from_xlsx'][file_index]['replace'][replace_index]['to_replace']
            value = cfg['files']['from_xlsx'][file_index]['replace'][replace_index]['value']
            df.replace(to_replace=to_replace, value=value, inplace=True)
        df_array.append(df)

        for to_numeric_column in cfg['files']['from_xlsx'][file_index]['to_numeric']:
            df_array[file_index][to_numeric_column] = df_array[file_index][to_numeric_column].apply(pd.to_numeric)

        for group_by_index in range(0, len(cfg['Analysis']['group_by'])):
            group_by_item = cfg['Analysis']['group_by'][group_by_index]['group_by_item']
            describe_column = cfg['Analysis']['group_by'][group_by_index]['describe']
            if describe_column is not None:
                df_describe = df_array[file_index].groupby(group_by_item)[describe_column].describe()
            else:
                df_describe = df_array[file_index].describe()

            plt_settings = cfg['Analysis']['group_by'][group_by_index]['viz']
            plt_settings.update({
                'file_name':
                    cfg['Analysis']['result_folder'] + cfg['Analysis']['file_name'] + '_' +
                    '{0}'.format(group_by_index) + '.png'
            })
            columns_to_viz = plt_settings['df_columns']
            viz_data.from_df_get_plot(df_describe[columns_to_viz], plt_settings)

    print("Finished plotting successfully")

    save_data.saveDataYaml(cfg, cfg['Analysis']['result_folder'] + cfg['Analysis']['file_name'], False)
    return cfg


if __name__ == '__main__':
    application_manager = set_up_application()
    cfg_base = statistical_describe(application_manager.cfg)
    cfg_variations_array = run_cfg_variations(application_manager)
