import pandas as pd
from ms_mint import peaklists


def test__read_peaklists():
    pass


def test__standardize_peaklist():
    peaklist = pd.DataFrame({
        'peakLabel': ['A'],
        'peakMz': [100],
        'rtmin': [1],
        'rtmax': [2],
        'peaklist': ['TEST']
    })
    
    expected = pd.DataFrame(
        {'peak_label': {0: 'A'},
         'mz_mean': {0: 100},
         'mz_width': {0: 10},
         'rt_min': {0: 1},
         'rt_max': {0: 2},
         'intensity_threshold': {0: 0},
         'peaklist_name': {0: 'unknown'}}
    )

    result = peaklists.standardize_peaklist(peaklist)
    assert result.equals(expected)

def test__check_peaklist():
    pass


def test__peak_window_from_peaklist():
    pass


def test__generate_grid_peaklist():
    peaklist = peaklists.generate_grid_peaklist(
        [115], .1, intensity_threshold=1000
    )
    assert peaklist is not None
