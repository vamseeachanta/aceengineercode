class ODAComponents:

    def __init__(self, cfg):
        self.cfg = cfg
        self.well_summary_df = None
        self.add_custom_folder()

    def add_custom_folder(self):
        import os
        if self.cfg.default['custom_folder'] is not None:
            if not os.path.exists(self.cfg.default['custom_folder']):
                os.mkdir(self.cfg.default['custom_folder'])

        if os.path.exists(self.cfg.default['custom_folder']):
            self.cfg['Analysis']['result_folder'] = self.cfg.default['custom_folder']

    def get_environments(self):
        self.environments = list(self.cfg.default['db'].keys())

    def set_up_db_connection(self, db_properties):
        from common.database import Database
        self.dbe = Database(db_properties)
        try:
            self.dbe.enable_connection_and_cursor()
            return True
        except Exception as e:
            print("Error as {}".format(e))
            print("No connection for environment: {}".format(db_properties))
            return False

    def get_well_data_for_envs(self):
        self.get_environments()
        for env_index in range(0, len(self.environments)):
            # for env_index in range(0, 1):
            self.env = self.environments[env_index]
            db_properties = self.cfg.default['db'][self.env]
            self.set_up_db_connection(db_properties)

            try:
                self.active_wells = None
                self.get_active_wells()
            except:
                print("No connection to environment {}".format(self.env))
            if self.active_wells is not None:
                self.iterate_all_wells_in_environment()

    def perform_db_analysis(self):
        self.dbe.perform_analysis(cfg_analysis=self.cfg.default['analysis']['db'].copy())

    def get_raw_data(self):
        import logging
        if self.cfg.default['input_data']['source'] == 'db':
            self.get_environments()
            for env_index in range(0, len(self.environments)):
                # for env_index in range(0, 1):
                self.env = self.environments[env_index]
                db_properties = self.cfg.default['db'][self.env]
                self.set_up_db_connection(db_properties)
                try:
                    self.get_input_data()
                except Exception as e:
                    print("Error encountered: {}".format(e))
                    logging.info(str(e))
                    print("No connection to environment {}".format(self.env))
        else:
            import sys
            print("No data source specified")
            sys.exit()

    def get_input_data(self):
        cfg_input = self.cfg.default['input_data'].copy()
        if cfg_input['source'] == 'db':
            self.dbe.get_input_data_from_db(cfg_input)
        else:
            print("No input data source defined")

    def iterate_all_wells_in_environment(self):
        import datetime
        for well_index in range(0, len(self.active_wells)):
            # for well_index in range(0, 2):
            print("Environment: {0}, well api: {1}".format(self.env, self.active_wells.UIDWell.iloc[well_index]))
            self.get_well_data(self.active_wells.iloc[well_index])
            if self.cfg.default['Analysis']['data_direct_from_nov']:
                nov_data = NOVData(self.cfg)
                end_time = datetime.datetime.now()
                start_time = end_time - datetime.timedelta(hours=-10)
                witsml_df = nov_data.read_data_from_nov_using_oxy_url(self.well_nov_uid, start_time, end_time,
                                                                      '-00:00')
                if len(witsml_df) > 100:
                    print("... NOV direct data exists")
                else:
                    print("... No NOV direct data")

                # witsml_df = nov_data.__preprocess_nov_columns(witsml_df)

            try:
                self.summarize_well_data()
            except Exception as e:
                print("Summary failed for Well with ID - {0} and API - {1}:".format(self.well_id, self.well_api))
                print(e)

    def get_active_wells(self):
        import os
        stored_procedure = 'GetWells'
        sp_args = ['Active']
        # df = self.dbe.get_df_from_stored_procedure(stored_procedure, sp_args)
        # df = self.dbe.get_df_from_stored_procedure(stored_procedure)
        filename = os.path.join('data_manager\data', 'mssql', 'definitions\\functions', 'oda_get_active_wells.sql')
        if os.path.isfile(filename):
            df = self.dbe.executeScriptsFromFile(filename, [])
            self.active_wells = df

    def get_well_data(self, well_data):
        self.well_id = well_data.WellId
        self.well_api = well_data.UIDWell
        self.well_nov_uid = well_data.NovWellId
        self.get_rig_data()
        self.get_well_plan()
        self.get_well_bha()
        self.get_witsml_data()
        self.perform_witsml_column_data_qa()
        if self.cfg.default['Analysis']['input_parameter_group_vizualizations']:
            self.prepare_witsml_data_charts()
        self.get_witsml_last_record()
        self.get_algorithm_results()

    def summarize_well_data(self):
        import pandas as pd
        if self.well_summary_df is None:
            columns = [
                'env', 'well_api', 'well_id', 'rig_name', 'planned', 'rig_time', 'hole', 'bit', 'tad', 'tad_time',
                'ilt', 'ilt_time', 'sas', 'sas_time', 'bkl', 'bkl_time', 'bbo', 'bbo_time', 'drilling_status',
                'on_bottom_data', 'last_rig_time_on_bottom', 'witsml_qa', 'bha_depth', 'bha_time'
            ]
            self.well_summary_df = pd.DataFrame(columns=columns)

        env = self.env
        well_id = self.well_id
        if self.well_api is not None:
            well_api = self.well_api
        else:
            well_api = str(well_id) + '-None'
        rig_name = self.rig_data.RigName[0]
        planned = self.well_plan.md.max()
        rig_time = self.last_witsml.RigTime[0]
        hole = self.last_witsml.HoleDepth[0]
        bit = self.last_witsml.BitDepth[0]
        tad = self.tad_results.MeasuredDepth.max()
        tad_time = self.tad_results.LastModifiedDateTime.max()
        ilt = self.ilt_results.StartConnectionDepth.max()
        if len(self.ilt_last_result) > 0:
            ilt_time = self.ilt_last_result.LastModifiedDateTime[0]
        else:
            ilt_time = None
        sas = self.sas_results.MeasuredDepth.max()
        sas_time = self.sas_results.LastModifiedDateTime.max()
        bkl = self.bkl_results.MeasuredDepth.max()
        bkl_time = self.bkl_results.LastModifiedDateTime.max()
        bbo = self.bbo_results.MeasuredDepth.max()
        bbo_time = self.bbo_results.LastModifiedDateTime.max()
        if self.last_witsml.BitOnBtm[0]:
            drilling_status = True
        else:
            drilling_status = False
        on_bottom_data = self.well_on_bottom_data
        last_rig_time_on_bottom = self.last_rig_time_on_bottom
        witsml_qa = self.witmsl_qa_array
        if len(self.well_bha) > 0:
            bha_depth = self.well_bha.MeasuredDepthAssemblyBase.max()
            bha_time = self.well_bha.DateIn.max()
        else:
            bha_depth = None
            bha_time = None
        new_row = [
            env, well_api, well_id, rig_name, planned, rig_time, hole, bit, tad, tad_time, ilt, ilt_time, sas,
            sas_time, bkl, bkl_time, bbo, bbo_time, drilling_status, on_bottom_data, last_rig_time_on_bottom,
            witsml_qa, bha_depth, bha_time
        ]
        self.well_summary_df.loc[len(self.well_summary_df)] = new_row

    def get_witsml_statistics(self):
        stored_procedure = 'GetWITSMLStatistics'
        sp_args = [int(self.well_id)]
        df = self.dbe.get_df_from_stored_procedure(stored_procedure, sp_args)
        self.witsml_statistics = df

    def get_rig_data(self):
        stored_procedure = 'GetRigInfo'
        sp_args = [self.well_id]
        df = self.dbe.get_df_from_stored_procedure(stored_procedure, sp_args)
        self.rig_data = df

    def get_well_plan(self):
        stored_procedure = 'GetPlanData'
        sp_args = [self.well_api]
        df = self.dbe.get_df_from_stored_procedure(stored_procedure, sp_args)
        self.well_plan = df

    def get_well_bha(self):
        stored_procedure = 'GetAssemblies'
        sp_args = [self.well_id]
        df = self.dbe.get_df_from_stored_procedure(stored_procedure, sp_args)
        self.well_bha = df

    def get_witsml_data(self):
        self.witmsl_qa_df_array = []
        self.witsml_number_of_rows = 10000
        query = "SELECT TOP {0} * FROM [dbo].[WITSML] WITH (SNAPSHOT) WHERE [WellID]= {1} and BitOnBtm = 1 ORDER BY DateUpdatedInserted DESC".format(
            self.witsml_number_of_rows, self.well_id)
        witsml_df = self.dbe.get_df_from_query(query)
        self.witmsl_qa_df_array.append(witsml_df)
        if len(witsml_df) > 0:
            self.last_rig_time_on_bottom = witsml_df.RigTime.iloc[0]
        if len(witsml_df) < self.witsml_number_of_rows * 0.01:
            self.well_on_bottom_data = False
        else:
            self.well_on_bottom_data = True

    def perform_witsml_column_data_qa(self):
        self.witmsl_qa_array = []

        witsml_df = self.witmsl_qa_df_array[-1]
        for column_data in self.cfg.witsml_column_for_qa:
            column_name = column_data['name']
            if 'non_null' in column_data['qa']:
                value_count = witsml_df[column_name].isnull().sum()
                if value_count > len(witsml_df) * 0.5:
                    self.witmsl_qa_array.append(column_name)
            if 'positive' in column_data['qa']:
                value_count = len(witsml_df[witsml_df[column_name] < 0])
                if value_count > len(witsml_df) * 0.5:
                    self.witmsl_qa_array.append(column_name + '_N')
            if 'unit_check' in column_data['qa']:
                if column_name == 'TdTorque':
                    value_count = witsml_df[column_name].isnull().sum()
                    if value_count < len(witsml_df) * 0.1:
                        try:
                            if witsml_df.TdTorque.max() > 5000:
                                self.witmsl_qa_array.append(column_name + ',lb-ft')
                            else:
                                self.witmsl_qa_array.append(column_name + ',klb-ft')
                        except:
                            pass

    def prepare_witsml_data_charts(self):
        from common.visualizations import Visualization
        viz = Visualization()
        witsml_df = self.witmsl_qa_df_array[-1]

        for witsml_group_index in range(0, len(self.cfg.witsml_groups)):
            try:
                plt_settings = self.cfg.plots[1].copy()
                plt_settings['y'] = self.cfg.witsml_groups[witsml_group_index]['array']
                plt_settings['label'] = plt_settings['y']
                witsml_group_name = self.cfg.witsml_groups[witsml_group_index]['name']
                plt_settings.update({
                    'file_name':
                        self.cfg['Analysis']['result_folder'] + self.cfg['Analysis']['file_name'] + '_' +
                        plt_settings['file_suffix'] + witsml_group_name + '_' + self.env + '_' + self.well_api + '.png'
                })
                plt_settings.update({'suptitle': plt_settings['suptitle'].format(witsml_group_name)})
                plt_settings.update(
                    {'title': plt_settings['title'].format(self.env, self.well_api, self.well_on_bottom_data)})
                plt_settings['ylabel'] = witsml_group_name
                viz.from_df_columns(witsml_df, plt_settings)
                viz.add_title_and_axis_labels()
                viz.add_legend()
                viz.save_and_close()
            except:
                print("Input group plot could not be saved for API - {0}".format(self.well_api))

    def get_witsml_last_record(self):
        query = "SELECT TOP 1 * FROM [dbo].[Witsml] WITH (SNAPSHOT) WHERE WellID = {0} ORDER BY DateUpdatedInserted DESC".format(
            self.well_id)
        df = self.dbe.get_df_from_query(query)
        self.last_witsml = df

    def get_algorithm_results(self):
        self.get_algorithm_info()
        self.get_tad_result()
        self.get_ilt_results()
        self.get_sas_results()
        self.get_bkl_results()
        self.get_bbo_results()

    def get_tad_result(self):
        # stored_procedure = 'GetWellAlgorithmDragVsFrictionOutput'
        # sp_args = [int(self.well_id)]
        # df = self.dbe.get_df_from_stored_procedure(stored_procedure, sp_args)
        query = "SELECT * FROM [dbo].[WellAlgorithmDragOutput] WHERE WellID = {0} AND ModelRunDateTime = (SELECT MAX(ModelRunDateTime) FROM WellAlgorithmDragOutput WHERE WellId = {0}) AND DeletedAt IS NULL".format(
            int(self.well_id))
        df = self.dbe.get_df_from_query(query)
        self.tad_results = df

    def get_ilt_results(self):
        stored_procedure = 'GetDrillingConnectionTime'
        sp_args = [int(self.well_id)]
        df = self.dbe.get_df_from_stored_procedure(stored_procedure, sp_args)
        self.ilt_results = df
        query = "SELECT TOP 1 * FROM .[dbo].[WellAlgorithmDrillingConnections] WHERE WellID = {0} ORDER BY LastModifiedDateTime DESC".format(
            int(self.well_id))
        df = self.dbe.get_df_from_query(query)
        self.ilt_last_result = df

    def get_sas_results(self):
        algorithm_code = 'SAS'
        algorithm_id = self.algorithm_data[self.algorithm_data.AlgorithmCode == algorithm_code].iloc[0].AlgorithmId
        query = "SELECT TOP 1 * FROM [dbo].[WellAlgorithmDysfunctionOutput] WHERE WellID = {0} and AlgorithmId={1} ORDER BY LastModifiedDateTime DESC".format(
            int(self.well_id), algorithm_id)
        df = self.dbe.get_df_from_query(query)
        self.sas_results = df

    def get_bkl_results(self):
        algorithm_code = 'BKL'
        algorithm_id = self.algorithm_data[self.algorithm_data.AlgorithmCode == algorithm_code].iloc[0].AlgorithmId
        query = "SELECT TOP 1 * FROM .[dbo].[WellAlgorithmDysfunctionOutput] WHERE WellID = {0} and AlgorithmId={1} ORDER BY LastModifiedDateTime DESC".format(
            int(self.well_id), algorithm_id)
        df = self.dbe.get_df_from_query(query)
        self.bkl_results = df

    def get_bbo_results(self):
        algorithm_code = 'BBO'
        algorithm_id = self.algorithm_data[self.algorithm_data.AlgorithmCode == algorithm_code].iloc[0].AlgorithmId
        query = "SELECT TOP 1 * FROM [dbo].[WellAlgorithmDysfunctionOutput] WHERE WellID = {0} and AlgorithmId={1} ORDER BY LastModifiedDateTime DESC".format(
            int(self.well_id), algorithm_id)
        df = self.dbe.get_df_from_query(query)
        self.bbo_results = df

    def get_algorithm_info(self):
        query = "EXEC [dbo].[GetAlgorithmData]"
        df = self.dbe.get_df_from_query(query)
        self.algorithm_data = df

    def save_visualizations(self):
        from common.visualizations import Visualization
        viz = Visualization()
        for row_index in range(0, len(self.well_summary_df)):
            try:
                temp_series = self.well_summary_df[['planned', 'hole', 'bit', 'tad', 'ilt', 'sas', 'bkl',
                                                    'bbo']].iloc[row_index].copy()
                df = temp_series.to_frame()
                df['label'] = df.index.to_list()
                df['depths'] = df[row_index]
                plt_settings = self.cfg.plots[0].copy()
                plt_settings.update({
                    'file_name':
                        self.cfg['Analysis']['result_folder'] + self.cfg['Analysis']['file_name'] + '_' +
                        plt_settings['file_suffix'] + '_' + self.well_summary_df['env'].iloc[row_index] + '_' +
                        self.well_summary_df['well_api'].iloc[row_index] + '.png'
                })
                plt_settings.update({
                    'title':
                        plt_settings['title'].format(self.well_summary_df['env'].iloc[row_index],
                                                     self.well_summary_df['well_api'].iloc[row_index],
                                                     self.well_summary_df['drilling_status'].iloc[row_index])
                })
                viz.from_df_columns(df, plt_settings)
                viz.add_title_and_axis_labels()
                viz.save_and_close()
            except:
                print("Plot could not be saved for API - {0}".format(self.well_summary_df['well_api'].iloc[row_index]))

    def save_results(self):
        from common.data import SaveData
        save_data = SaveData()

        file_name = self.cfg['Analysis']['result_folder'] + self.cfg['Analysis']['file_name'] + 'well_summary.csv'
        self.well_summary_df.to_csv(file_name)
        file_name = self.cfg['Analysis']['result_folder'] + self.cfg['Analysis'][
            'file_name'] + 'relative_depth_summary.csv'
        self.relative_depth_df.to_csv(file_name)
        file_name = self.cfg['Analysis']['result_folder'] + self.cfg['Analysis'][
            'file_name'] + 'well_summary_by_api.csv'
        self.well_summary_by_api_df.to_csv(file_name)

        summary_template_file_name = "C:\\Users\\achantv\\OneDrive\\OneDrive - Occidental Petroleum Corporation\\017 ODA\\Data\\Result_Availability\\template_summary.xlsx"
        summary_updated_file_name = "C:\\Users\\achantv\\OneDrive\\OneDrive - Occidental Petroleum Corporation\\017 ODA\\Data\\Result_Availability\\template_summary_copy1.xlsx"
        data = {
            'template_file_name': summary_template_file_name,
            'saved_file_name': summary_updated_file_name,
            'df': self.well_summary_by_api_df,
            'sheetname': 'app_oda_odawell_summary_api'
        }
        # save_data.df_to_sheet_in_existing_workbook(data)
        # save_data.save_sheet_to_png()

        cfg_temp = {
            'SheetNames': ['relative_depths', 'abs_depths'],
            'FileName': self.cfg['Analysis']['result_folder'] + self.cfg['Analysis']['file_name'] + '_summary.xlsx'
        }
        save_data.DataFrameArray_To_xlsx_openpyxl([self.relative_depth_df, self.well_summary_df], cfg_temp)

    def prepare_well_algorithm_alert_df(self):
        self.relative_depth_df = self.well_summary_df.copy()
        self.relative_depth_df['tad'] = self.relative_depth_df['hole'] - self.relative_depth_df['tad']
        self.relative_depth_df['ilt'] = self.relative_depth_df['hole'] - self.relative_depth_df['ilt']
        self.relative_depth_df['sas'] = self.relative_depth_df['hole'] - self.relative_depth_df['sas']
        self.relative_depth_df['bkl'] = self.relative_depth_df['hole'] - self.relative_depth_df['bkl']
        self.relative_depth_df['bbo'] = self.relative_depth_df['hole'] - self.relative_depth_df['bbo']

    def rearrange_data_by_well_api(self):
        import pandas as pd
        summary_columns = list(self.well_summary_df.columns)
        columns = ['d_' + item for item in summary_columns] + ['t_' + item for item in summary_columns] + [
            's_' + item for item in summary_columns
        ] + ['p_' + item for item in summary_columns]
        no_result_array = [None] * len(self.well_summary_df.columns)
        self.well_summary_by_api_df = pd.DataFrame(columns=columns)

        well_api_list = self.well_summary_df.well_api.unique()
        for api in well_api_list:
            well_summary_by_api_row_array = []
            for env_index in range(0, len(self.environments)):
                env = self.environments[env_index]
                df_temp = self.well_summary_df[(self.well_summary_df.well_api == api) &
                                               (self.well_summary_df.env == env)]
                if len(df_temp) != 0:
                    well_summary_by_api_row_array = well_summary_by_api_row_array + df_temp.values.tolist()[0]
                else:
                    well_summary_by_api_row_array = well_summary_by_api_row_array + no_result_array
            self.well_summary_by_api_df.loc[len(self.well_summary_by_api_df)] = well_summary_by_api_row_array
        self.well_summary_by_api_df.sort_values(by=['p_well_id'])

    def save_tad_inputs(self):
        ''' Function to be executed in-line in ODA code base'''
        import os
        well_folder_name = 'Platinum MDP1 34-3 Fed Com 24H_Phillipe/'
        filepath = os.path.join(
            'C:/Users/achantv/OneDrive/OneDrive - Occidental Petroleum Corporation/017 ODA/Data/TAD/',
            well_folder_name)

        filename = os.path.join(filepath, self.well_data_manager.well_info.well_api + '_bha_org.csv')
        self.torque_and_drag.bha_org.to_csv(filename, index=False)
        filename = os.path.join(filepath, self.well_data_manager.well_info.well_api + '_survey.csv')
        self.torque_and_drag.survey.to_csv(filename, index=False)
        filename = os.path.join(filepath, self.well_data_manager.well_info.well_api + '_hole_info_org.csv')
        self.torque_and_drag.hole_info_org.to_csv(filename, index=False)

        print(self.torque_and_drag.block_weight)
        print(self.torque_and_drag.mud_weight)

        print(self.well_data_manager.current_hole_depth)
        print(self.well_data_manager.current_bit_depth)


class NOVData:

    def __init__(self, cfg):
        self.cfg = cfg
        self.total_connection_refresh_count = 0
        self.witsml_client = None
        self.create_or_refresh_witsml_connection()

    def create_or_refresh_witsml_connection(self):
        from suds.client import Client
        self.witsml_client = Client(self.cfg.nov_witsml_server_dev.url,
                                    username=self.cfg.nov_witsml_server_dev.username,
                                    password=self.cfg.nov_witsml_server_dev.password)
        self.total_connection_refresh_count = self.total_connection_refresh_count + 1

    def get_all_surveys(self, nov_uid):
        import xmltodict
        all_surveys_qry = """<?xml version="1.0"?>
                <trajectorys xmlns:gml="http://www.opengis.net/gml/3.2" 
                        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
                        xmlns:xlink="http://www.w3.org/1999/xlink" 
                        xmlns:dc="http://purl.org/dc/terms/" 
                        version="1.3.1.1" 
                        xmlns="http://www.witsml.org/schemas/131">
                  <trajectory uidWell="{0}" uidWellbore="{0}" uid="Connect-Surveys">
                    <mdMn uom="m">0</mdMn>
                    <mdMx uom="m">100000</mdMx>
                    <trajectoryStation>
                      <dTimStn xsi:nil="true" />
                      <typeTrajStation xsi:nil="true" />
                      <md uom="m">0</md>
                      <incl uom="rad">0</incl>
                      <azi uom="rad">0</azi>                      
                      <tvd uom="ft">0</tvd>
                      <dispNs uom="ft">0</dispNs>
                      <dispEw uom="ft">0</dispEw>
                    </trajectoryStation>
                  </trajectory>
                </trajectorys>
                """

        # TODO  < vertSect uom = "ft" > 0 < / vertSect >  DID NOT work. Further investigation on going.
        # TODO The Northings and Eastings are relative. Not Abosolute. Investigation on going.

        all_surveys_qry = all_surveys_qry.format(nov_uid)
        res_all_surveys = self.witsml_client.service.WMLS_GetFromStore("trajectory", all_surveys_qry)
        all_surveys = xmltodict.parse(res_all_surveys.XMLout)
        all_surveys = all_surveys.get('trajectorys', {}).get('trajectory', {})
        all_surveys = all_surveys['trajectoryStation']

        all_surveys_dict_list = []
        for survey in all_surveys:
            survey_dict = {
                'timestamp': survey['dTimStn'],
                'srv_md': float(survey['md']['#text']),
                'srv_inc': float(survey['incl']['#text']),
                'srv_azi': float(survey['azi']['#text']),
                'srv_north': float(survey['dispNs']['#text']),
                'srv_east': float(survey['dispEw']['#text']),
                'srv_tvd': float(survey['tvd']['#text']),
                'srv_vs': None,
                'srv_code': 'srvapprv'
            }
            all_surveys_dict_list.append(survey_dict)

        import pandas as pd
        surveys_df = pd.DataFrame(all_surveys_dict_list)

        return surveys_df

    def read_data_from_nov_using_oxy_url(self, nov_uid, start_time, end_time, offset):
        # Not working
        import logging

        import pandas as pd

        nov_download_url = 'https://witsml-dev.oxy.com/api/get_witsml_data_time_based'

        if nov_uid is None:
            logging.info('NOV_UID is None, cannot load data from NOV!')
            return None
        logging.info('Reading NOV data from {}  to  {}'.format(start_time, end_time))
        df = pd.DataFrame()
        try:
            df = self.__make_web_call(
                nov_download_url, {
                    'nov_uid': nov_uid,
                    'start_time': start_time.isoformat() + offset,
                    'end_time': end_time.isoformat() + offset
                })
            logging.info('Done reading data...')
            df.sort_values('RIGTIME', inplace=True)
        except Exception as e:
            logging.error('Exception reading data from NOV: {}'.format(e))
        return df

    @staticmethod
    def __make_web_call(url, input_args={}):
        import pandas as pd
        import requests

        r = requests.post(url, verify=False, json=input_args)
        results_dict = r.json()
        final_results_df = pd.DataFrame(results_dict)
        return final_results_df
