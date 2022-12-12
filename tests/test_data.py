def test_GetData_by_download_file_from_url():
    from common.data import GetData
    get_data = GetData()
    import os
    from pathlib import Path
    cfg = {
        'url': 'https://www.data.bsee.gov/Well/Files/APIRawData.zip',
        'download_to': os.path.abspath(Path("../data_manager/data/bsee"))
    }

    get_data.download_file_from_url(cfg)
