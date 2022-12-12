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
            cfg_variations_array.append(fracture_mechanics(application_manager.cfg))

    return cfg_variations_array


def fracture_mechanics(cfg):
    from datetime import datetime
    t_start = datetime.now()

    from common.fracture_mechanics_components import \
        FractureMechanicsComponents
    fracture_components = FractureMechanicsComponents(cfg)

    if cfg['default']['Analysis']['fracture_mechanics']['flaw_limits']:
        fracture_components.evaluate_FAD()
        fracture_components.critical_flaw_limits()
        fracture_components.get_flaw_growth_for_fatigue_loading()
        fracture_components.get_initial_allowable_flaw_for_life()
        fracture_components.save_result_tables()
        fracture_components.create_visualizations()

    t_end = datetime.now()
    print("Time taken to process: {0} seconds".format((t_end - t_start).seconds))
    return cfg


if __name__ == '__main__':
    application_manager = set_up_application()
    cfg_base = fracture_mechanics(application_manager.cfg)
    cfg_variations_array = run_cfg_variations(application_manager)
