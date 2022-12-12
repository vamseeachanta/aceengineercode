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
            cfg_variations_array.append(API579(application_manager.cfg))

    return cfg_variations_array


def API579(cfg):
    from datetime import datetime
    t_start = datetime.now()

    from common.API579_components import API579_components
    api579_components = API579_components(cfg)

    if cfg['default']['Analysis']['GML']['Circumference']:
        api579_components.gml()

    if cfg['default']['Analysis']['LML']:
        api579_components.lml()

    if cfg['default']['Analysis']['B31G']:
        api579_components.b31g()

    t_end = datetime.now()
    print("Time taken to process: {0} seconds".format((t_end - t_start).seconds))


if __name__ == '__main__':
    application_manager = set_up_application()
    cfg_base = API579(application_manager.cfg)
    cfg_variations_array = run_cfg_variations(application_manager)
