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
            cfg_variations_array.append(visualization(application_manager.cfg))

    return cfg_variations_array


def visualization(cfg):
    from datetime import datetime
    t_start = datetime.now()

    from common.visualization_components import VisualizationComponents
    viz_comp = VisualizationComponents(cfg)

    viz_comp.get_raw_data()
    viz_comp.save_raw_data()
    viz_comp.prepare_visualizations()

    if cfg['default']['analysis'].__contains__('run_example') and cfg['default']['analysis']['run_example']:
        viz_comp.run_example()

    t_end = datetime.now()
    print("Time taken to process: {0} seconds".format((t_end - t_start).seconds))
    return cfg


if __name__ == '__main__':
    application_manager = set_up_application()
    cfg_base = visualization(application_manager.cfg)
    cfg_variations_array = run_cfg_variations(application_manager)
