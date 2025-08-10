from common.ApplicationManager import applicationTimer, setupApplicationRuns


@setupApplicationRuns
@applicationTimer
def data_models(cfg):

    from common.data_models_components import DataModelsComponents
    dm = DataModelsComponents(cfg)

    if cfg.__contains__('db_tables'):
        dm.drop_dependent_tables()
        dm.create_db_tables()

    if cfg.__contains__('input_data'):
        dm.get_data_and_save_to_target()

    return cfg


if __name__ == '__main__':
    cfg_with_results = data_models(cfg=None)
