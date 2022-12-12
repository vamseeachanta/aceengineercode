def test_GetGeneralData():
    from common.orcaflex_model_components import OrcaflexModelComponents
    orcaflex_components = OrcaflexModelComponents()
    GeneralData = orcaflex_components.GetGeneral(cfg=None)
    assert GeneralData['General'].__len__() == 10


def test_GetGeneralDataWithCFG():
    from common.orcaflex_model_components import OrcaflexModelComponents
    orcaflex_components = OrcaflexModelComponents()
    cfg = {'StageDuration': [8, 120], 'TargetLogSampleInterval': 0.3, 'ImplicitConstantTimeStep': 0.02}

    GeneralData = orcaflex_components.GetGeneral(cfg)
    assert GeneralData['General'].__len__() == 10
    assert GeneralData['General']['StageDuration'] == [8, 120]
    assert GeneralData['General']['TargetLogSampleInterval'] == 0.3
    assert GeneralData['General']['ImplicitConstantTimeStep'] == 0.02
