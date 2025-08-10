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
            cfg_variations_array.append(ETL(application_manager.cfg))

    return cfg_variations_array


def ETL(cfg):
    from datetime import datetime

    from common.ETL_components import ETL_components
    t_start = datetime.now()
    etl = ETL_components(cfg)

    # Extract
    if cfg.default['extract'] is not None:
        print("Data extraction ... ")
        etl.extract_data()
        print("Data extraction ... COMPLETE")

    # Transformations
    if cfg['default']['transform']['from_xlsx_to_yaml_file']:
        etl.from_xlsx_to_yaml_file()

    if cfg['default']['transform']['repeat_patterns']:
        etl.write_repeat_pattern_files()

    if cfg['default']['transform']['replace']:
        etl.write_replace_files()

    if cfg.default['transform'].__contains__('viv_current_reformat_1'):
        if cfg.default['transform']['viv_current_reformat_1']['flag']:
            print("Data transformation ... ")
            etl.transform_viv_current_reformat_1()
            print("Data transformation ... ")

    if cfg.default.__contains__('save'):
        if cfg.default['save']['excel']:
            etl.save()

    t_end = datetime.now()
    print("Time taken to process: {0} seconds".format((t_end - t_start).seconds))
    return cfg


if __name__ == '__main__':
    application_manager = set_up_application()
    cfg_base = ETL(application_manager.cfg)
    cfg_variations_array = run_cfg_variations(application_manager)
