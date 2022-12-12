# -*- coding: utf-8 -*-
"""
Author: Vamsee Achanta
Date Updated: 2019-06-19
Objective: To prepare design calculations
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
            cfg_variations_array.append(design_calculations(application_manager.cfg))

    return cfg_variations_array


def design_calculations(cfg):
    import math

    from custom.PipeSizing import PipeSizing

    pipe_sizing = PipeSizing(cfg)
    property_dictionary = pipe_sizing.get_pipe_system_properties()

    design_code = cfg['Design'][0]['Code'][0]['Outer_Pipe']
    L = cfg['Design'][0]['length'] * 12

    factor_of_safety = cfg['DesignFactors'][design_code]['end_condition']['factor_of_safety']
    k = cfg['DesignFactors'][design_code]['end_condition']['k_design']
    EI = property_dictionary['section_properties']['pipe']['EI']
    F_theoretical = (math.pi)**2 * EI / (k * L)**2
    F_allowable = F_theoretical / factor_of_safety

    print(property_dictionary)

    return cfg


if __name__ == '__main__':
    application_manager = set_up_application()
    cfg_base = design_calculations(application_manager.cfg)
    cfg_variations_array = run_cfg_variations(application_manager)
