def test_read_excel_no_of_sheets(cfg=None):
    if cfg is None:
        cfg = {'io': 'data_manager/data/tests/sample_data.xlsx'}

    from common.excel_utilities import ReadFromExcel
    read_data = ReadFromExcel()
    data_frame = read_data.from_xlsx(cfg)

    no_of_sheets = len(data_frame.keys())
    assert no_of_sheets == 22


def test_read_excel_sheet_names(cfg=None):
    if cfg is None:
        cfg = {'io': 'data_manager/data/tests/sample_data.xlsx'}

    from common.excel_utilities import ReadFromExcel
    read_data = ReadFromExcel()
    data_frame = read_data.from_xlsx(cfg)

    sheet_names = list(data_frame.keys())
    assert sheet_names[0] == 'hosts'
    assert sheet_names[-1] == 'Ref Fatigue_Curve'
