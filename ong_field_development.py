from common.ApplicationManager import applicationTimer, setupApplicationRuns
from common.ong_fd_components import ONGFDComponents


@setupApplicationRuns
@applicationTimer
def ong_field_development(cfg):
    import copy
    ong_fd = ONGFDComponents(cfg)
    cfg_default = copy.deepcopy(cfg)
    if cfg.default['analysis']['run_all_wells']:
        ong_fd.get_raw_data_for_field_analysis()
        all_bsee_blocks = ong_fd.get_all_bsee_blocks()
        # all_bsee_blocks = all_bsee_blocks[0:10]
        # all_bsee_blocks = ['WR627', 'GC807', 'WR508']
        for block in all_bsee_blocks:
            cfg = update_cfg_with_block_name(copy.deepcopy(cfg_default), block)
            ong_fd.assign_cfg(cfg)
            try:
                ong_fd.get_raw_data_for_field_analysis()
                ong_fd.prepare_field_api12_data()
                ong_fd.prepare_field_well_data()
                ong_fd.prepare_field_summary()
                ong_fd.save_data()
            except:
                print(f"Analysis failed for :{block}")

    elif cfg.default['analysis']['field_analysis']:
        ong_fd.get_raw_data_for_field_analysis()
        ong_fd.prepare_field_api12_data()
        ong_fd.prepare_field_well_data()
        ong_fd.prepare_field_summary()
        ong_fd.save_data()
        ong_fd.save_output_data_to_local_computer()
        ong_fd.prepare_visualizations()

    return cfg


def update_cfg_with_block_name(cfg, block):
    no_of_sets = len(cfg['default']['input_data']['sets'])
    for set_index in range(0, no_of_sets):
        try:
            cfg['default']['input_data']['sets'][set_index]['query']['arg_array'][0] = cfg['default']['input_data'][
                'sets'][set_index]['query']['arg_array'][0].replace('block_placeholder', block)
        except:
            pass

    no_of_sets = len(cfg['save_data']['sets'])
    for set_index in range(0, no_of_sets):
        cfg['save_data']['sets'][set_index]['pre_conditions']['sets'][0]['arg_array'][0] = cfg['save_data']['sets'][
            set_index]['pre_conditions']['sets'][0]['arg_array'][0].replace('block_placeholder', block)

    cfg['custom_parameters']['field_nickname'] = cfg['custom_parameters']['field_nickname'].replace(
        'block_placeholder', block)
    cfg['custom_parameters']['boem_fields'] = cfg['custom_parameters']['boem_fields'].replace(
        'block_placeholder', block)

    return cfg


if __name__ == '__main__':
    cfg_with_results = ong_field_development(cfg=None)
