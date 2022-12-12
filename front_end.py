from common.ApplicationManager import applicationTimer, setupApplicationRuns


@setupApplicationRuns
@applicationTimer
def front_end(cfg):
    from datetime import datetime
    t_start = datetime.now()

    from common.front_end_components import FEComponents
    fe = FEComponents(cfg)

    fe.get_raw_data()
    fe.transform_raw_data()
    fe.prepare_report_data()
    fe.prepare_web_api_data()
    fe.prepare_chart_data()
    # fe.prepare_htmls()
    fe.save_report_data_as_json()
    # fe.save_report_data_as_pkl()

    t_end = datetime.now()
    print("Time taken to process: {0} seconds".format((t_end - t_start).seconds))
    return cfg


if __name__ == '__main__':
    cfg_with_results = front_end(cfg=None)
