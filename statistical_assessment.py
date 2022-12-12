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
            cfg_variations_array.append(statistical_assessment(application_manager.cfg))

    return cfg_variations_array


def statistical_assessment(cfg):
    import pandas as pd

    from common.data import ReadData, SaveData
    from common.visualizations import Visualization

    read_data = ReadData()
    save_data = SaveData()

    viz_data = Visualization()
    # viz_data.example_group_bar_plot1()

    df_array = []
    combine_dfs = pd.DataFrame()
    for file_index in range(0, len(cfg['files']['from_xlsx'])):
        df_array.append(read_data.from_xlsx(cfg, file_index))

        # for employee in df_array[file_index].keys():
        #     print(df_array[file_index][employee].columns)
        # combine_dfs = pd.concat(df_array[0])        # for group_by_item in cfg['Analysis']['group_by']:
        for group_by_index in range(0, len(cfg['Analysis']['group_by'])):
            group_by_item = cfg['Analysis']['group_by'][group_by_index]['columns']
            grouped = df_array[file_index].groupby(group_by_item)
            # grouped = combine_dfs.groupby(group_by_item)
            # cfg['results']['group_by'] = grouped.size()
            print(grouped.size())

    print("Grouped Successfully")
    viz_data.from_df_get_plot(df_array, cfg)

    save_data.saveDataYaml(cfg, cfg['Analysis']['result_folder'] + cfg['Analysis']['file_name'], False)
    return cfg


if __name__ == '__main__':
    application_manager = set_up_application()
    cfg_base = statistical_assessment(application_manager.cfg)
    cfg_variations_array = run_cfg_variations(application_manager)
