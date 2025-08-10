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
            cfg_variations_array.append(log_file_analysis(application_manager.cfg))

    return cfg_variations_array


def log_file_analysis(cfg):
    from common.log_file_analysis_components import LogFileAnalysisComponents
    log_file_analysis_components = LogFileAnalysisComponents(cfg)

    log_file_analysis_components.get_file_list()

    if cfg.default['analysis']['file_count']:
        log_file_analysis_components.get_detailed_file_information()
        log_file_analysis_components.get_file_information_statistics()

    if cfg.default['analysis']['line_contents']:
        log_file_analysis_components.get_last_2_lines()

    return cfg


if __name__ == '__main__':
    application_manager = set_up_application()
    cfg_base = log_file_analysis(application_manager.cfg)
    cfg_variations_array = run_cfg_variations(application_manager)
