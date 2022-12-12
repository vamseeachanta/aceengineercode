# Data preparation
def set_up_application():
    import logging
    import os

    from common.ApplicationManager import configureApplicationInputs
    from common.set_logging import set_logging

    basename = os.path.basename(__file__).split('.')[0]
    application_manager = configureApplicationInputs(basename)
    application_manager.configure()

    # Set logging
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
            cfg_variations_array.append(oda(application_manager.cfg))

    return cfg_variations_array


def oda(cfg):
    from datetime import datetime
    t_start = datetime.now()

    from common.oda_components import ODAComponents
    oda = ODAComponents(cfg)

    if cfg.default.__contains__('input_data'):
        oda.get_raw_data()

    # oda.perform_db_analysis()

    if cfg.default['Analysis']['depth_analysis']:
        oda.get_well_data_for_envs()
        oda.prepare_well_algorithm_alert_df()
        oda.rearrange_data_by_well_api()
    if cfg.default['Analysis']['depth_vizualizations']:
        oda.save_visualizations()
    oda.save_results()

    t_end = datetime.now()
    print("Time taken to process: {0} seconds".format((t_end - t_start).seconds))
    return cfg


if __name__ == '__main__':
    application_manager = set_up_application()
    cfg_base = oda(application_manager.cfg)
    cfg_variations_array = run_cfg_variations(application_manager)
