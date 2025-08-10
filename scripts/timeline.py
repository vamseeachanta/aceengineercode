# -*- coding: utf-8 -*-
"""
Author: Vamsee Achanta
Date Updated: 2019-05-03
Objective: To generate vertical riser model and evaluate top tension 
Created on May 20 2019
"""


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
            cfg_variations_array.append(timeline(application_manager.cfg))

    return cfg_variations_array


def timeline(cfg):
    import logging

    import pandas as pd

    from common.visualizations import Visualization

    for file_index in range(0, len(cfg['files'])):
        file_data = cfg['files'][file_index]
        if file_data['file_type'] == 'csv':
            df = pd.read_csv(file_data['io'], parse_dates=True, index_col=0)

        for plot_index in range(0, len(cfg['plot'])):
            plt_settings = cfg['plot'][plot_index]
            plt_settings.update({
                'file_name':
                    cfg['Analysis']['result_folder'] + cfg['Analysis']['file_name'] + '_' +
                    plt_settings['file_suffix'] + '.png'
            })
            viz = Visualization()
            ax = viz.generate_time_line(df, plt_settings)

    return cfg


if __name__ == '__main__':
    application_manager = set_up_application()
    cfg_base = timeline(application_manager.cfg)
    cfg_variations_array = run_cfg_variations(application_manager)
