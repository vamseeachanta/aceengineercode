from common.ApplicationManager import applicationTimer, setupApplicationRuns


@setupApplicationRuns
@applicationTimer
def compare_tool(cfg):
    import logging

    from common.compare_tool_components import CompareTools
    compare_tools = CompareTools(cfg)
    compare_tools.get_input_data()
    compare_tools.prepare_visualizations()

    return cfg


if __name__ == '__main__':
    cfg_with_results = compare_tool(cfg=None)
