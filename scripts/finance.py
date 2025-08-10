from common.ApplicationManager import applicationTimer, setupApplicationRuns


@setupApplicationRuns
@applicationTimer
def finance(cfg):
    from datetime import datetime
    t_start = datetime.now()

    from common.finance_components import FinanceComponents
    fin_comps = FinanceComponents(cfg)

    fin_comps.get_data()
    fin_comps.prepare_time_line_plot()
    fin_comps.evaluate_returns()
    fin_comps.prepare_returns_plot()

    t_end = datetime.now()
    print("Time taken to process: {0} seconds".format((t_end - t_start).seconds))
    return cfg


if __name__ == '__main__':
    cfg_with_results = finance(cfg=None)
