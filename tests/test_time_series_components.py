import pytest


# @pytest.mark.skip(reason="for development")
def test_RunSimpleFFT():
    from common.time_series_components import TimeSeriesComponents
    cfg = {
        'default': {
            'analysis': {
                'fft': {
                    'flag': True,
                    'run_example': False,
                    'time_step': 0.1,
                    'window': {
                        'size': 1000,
                        'moving_average': {
                            'flag': False,
                            'window_size': 4
                        }
                    },
                    'filter': {}
                }
            }
        }
    }
    ts_components = TimeSeriesComponents(cfg)
    ts_cfg = {'seed': 1234, 'time_step': 0.02, 'peak_period': 5, 'time_range': [0, 20]}
    time_vector, signal, time_step, peak_period = ts_components.get_sample_time_series(ts_cfg=ts_cfg)
    sig_fft, filtered_signal = ts_components.run_simple_fft_example(signal, time_step)
    assert len(sig_fft) == 500


# @pytest.mark.skip(reason="for development")
def test_RunWindowFFT():
    from common.time_series_components import TimeSeriesComponents
    cfg = {
        'default': {
            'analysis': {
                'fft': {
                    'flag': True,
                    'run_example': False,
                    'time_step': 0.02,
                    'window': {
                        'size': 1000,
                        'moving_average': {
                            'flag': False,
                            'window_size': 4
                        }
                    },
                    'filter': {}
                }
            }
        }
    }
    ts_components = TimeSeriesComponents(cfg)
    ts_cfg = {'seed': 1234, 'time_step': 0.02, 'peak_period': 5, 'time_range': [0, 100]}
    time_vector, signal, time_step, peak_period = ts_components.get_sample_time_series(ts_cfg)
    average_fft_df = ts_components.fft_window_analysis(signal)


def test_WindowFFT_Peaks():
    from common.time_series_components import TimeSeriesComponents
    cfg = {
        'default': {
            'analysis': {
                'fft': {
                    'flag': True,
                    'run_example': False,
                    'time_step': 0.02,
                    'window': {
                        'size': 1000,
                        'moving_average': {
                            'flag': False,
                            'window_size': 4
                        }
                    },
                    'filter': {},
                    'peaks': {
                        'flag': True,
                        'solver': 'find_peaks',
                        'min_height_percentage': 60,
                        'min_distance_index_percentage': 50
                    }
                }
            }
        }
    }
    ts_components = TimeSeriesComponents(cfg)
    ts_cfg = {'seed': 1234, 'time_step': 0.02, 'peak_period': 5, 'time_range': [0, 100]}
    time_vector, signal, time_step, peak_period = ts_components.get_sample_time_series(ts_cfg)
    average_fft_df = ts_components.fft_window_analysis(signal)
    peak_df = average_fft_df[(average_fft_df['peak_flag'] == True) & (average_fft_df['fft_freq'] > 0)]
    fft_analysis_peak_frequency = peak_df['fft_freq'].iloc[0]
    fft_analysis_peak_period = 1 / fft_analysis_peak_frequency
    assert (peak_period == pytest.approx(fft_analysis_peak_period, rel=1e-2))


def test_RAO():
    from common.time_series_components import TimeSeriesComponents
    cfg = {
        'default': {
            'analysis': {
                'fft': {
                    'flag': True,
                    'run_example': False,
                    'time_step': 0.02,
                    'window': {
                        'size': 1000,
                        'moving_average': {
                            'flag': False,
                            'window_size': 4
                        }
                    },
                    'filter': {},
                    'peaks': {
                        'flag': True,
                        'solver': 'find_peaks',
                        'min_height_percentage': 60,
                        'min_distance_index_percentage': 50
                    }
                }
            }
        }
    }
    ts_components = TimeSeriesComponents(cfg)

    ts_cfg = {'seed': 1234, 'time_step': 0.02, 'peak_period': 5, 'time_range': [0, 100]}
    time_vector1, signal1, time_step1, peak_period1 = ts_components.get_sample_time_series(ts_cfg)

    ts_cfg2 = {'seed': 5000, 'time_step': 0.02, 'peak_period': 5, 'time_range': [0, 100]}
    time_vector2, signal2, time_step2, peak_period2 = ts_components.get_sample_time_series(ts_cfg2)

    RAO_raw, RAO_filtered = ts_components.get_RAO(signal=signal2, excitation=signal1, cfg_rao=None)
    RAO_peak_frequency_amplitude = RAO_raw[RAO_raw['frequency'] == 0.2]['amplitude'].iloc[0]
    RAO_peak_frequency_phase_radians = RAO_raw[RAO_raw['frequency'] == 0.2]['phase'].iloc[0]
    assert (0.9626 == pytest.approx(RAO_peak_frequency_amplitude, rel=1e-2))
    assert (-0.0206 == pytest.approx(RAO_peak_frequency_phase_radians, rel=1e-2))

    cfg_rao_phase_degree = {
        'phase': {
            'deg': True
        },
        'peaks': {
            'flag': True,
            'solver': 'find_peaks',
            'min_height_percentage': 60,
            'min_distance_index_percentage': 50
        }
    }
    RAO_raw, RAO_filtered = ts_components.get_RAO(signal=signal2, excitation=signal1, cfg_rao=cfg_rao_phase_degree)
    RAO_peak_frequency_amplitude = RAO_raw[RAO_raw['frequency'] == 0.2]['amplitude'].iloc[0]
    RAO_peak_frequency_phase_radians = RAO_raw[RAO_raw['frequency'] == 0.2]['phase'].iloc[0]
    assert (0.9626 == pytest.approx(RAO_peak_frequency_amplitude, rel=1e-2))
    assert (-1.1815 == pytest.approx(RAO_peak_frequency_phase_radians, rel=1e-2))


if __name__ == '__main__':
    test_RunSimpleFFT()
    test_RunWindowFFT()
    test_WindowFFT_Peaks()
    test_RAO()
