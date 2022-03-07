from kedro.extras.datasets.pickle import PickleDataSet
import pandas as pd


def preprocess_pixel_layer_1(raw_pixel_layer_1: PickleDataSet) -> pd.DataFrame:
    """Preprocesses the data for pixel layer.

    Args:
        raw_pixel_layer_1: Raw data.
    Returns:
        Preprocessed data: raw data sorted by lumisection number (dumb preprocessing)
    """
    preprocessed_raw_pixel_layer_1 = raw_pixel_layer_1.sort_values(by=['lumi']).copy()
    return preprocessed_raw_pixel_layer_1

def preprocess_pixel_layer_2(raw_pixel_layer_2: PickleDataSet) -> pd.DataFrame:
    """Preprocesses the data for pixel layer.

    Args:
        raw_pixel_layer_2: Raw data.
    Returns:
        Preprocessed data: raw data sorted by lumisection number (dumb preprocessing)
    """
    preprocessed_raw_pixel_layer_2 = raw_pixel_layer_2.sort_values(by=['lumi']).copy()
    return preprocessed_raw_pixel_layer_2

