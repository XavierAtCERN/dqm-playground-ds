import logging
from typing import Dict, Tuple

import ast

import pandas as pd
import numpy as np
import scipy.ndimage

# Computing 2D histograms properties

def compute_summary_statistics(data: pd.DataFrame) -> pd.DataFrame:
    """Compute summary statistics from data (mean, rms).

    Args:
        data: Dataframe containing 2D histograms.
    Returns:
        dataframe with run + lumi + mean + rms + ...
    """
    print(data.head())
    data['map'] = data['map'].apply(lambda x: ast.literal_eval(x)) # should be done in processing...
    data['mean'] = data['map'].apply(lambda x: np.array(x).mean())
    data['std'] = data['map'].apply(lambda x: np.array(x).std())
    df_summary_statistics = data[['run', 'lumi', 'mean', 'std']].copy()
    print(df_summary_statistics.head())
    return df_summary_statistics

def compute_geometrical_properties(data: pd.DataFrame) -> pd.DataFrame:
    """Compute geometrical properties from data (center of mass, ...).

    Args:
        data: Dataframe containing 2D histograms.
    Returns:
        dataframe with run + lumi + geometrical properties
    """
    data['map'] = data['map'].apply(lambda x: ast.literal_eval(x)) # should be done in processing
    data['image'] = data['map'].apply(lambda x: np.reshape(x, (202, 302))[1:201, 1:301]) # should be done in processing
    data['center_phi'] = data['image'].apply(lambda x: scipy.ndimage.measurements.center_of_mass(x)[0])
    data['center_z'] = data['image'].apply(lambda x: scipy.ndimage.measurements.center_of_mass(x)[1])
    df_geometrical_properties = data[['run', 'lumi', 'center_phi', 'center_z']].copy()
    print(df_geometrical_properties.head())
    return df_geometrical_properties

# Aggregating properties

def aggregate_properties(summary_statistics: pd.DataFrame, geometrical_properties: pd.DataFrame) -> pd.DataFrame:
    """Aggregate properties from the 2D histograms

    Args:
        summary_statistics: dataframe with run + lumi + mean + rms + ....
    Returns:
        dataframe with run + lumi + geometrical properties
    """
    df_aggregated_properties = pd.merge(summary_statistics, geometrical_properties, on=['run', 'lumi'])
    print(df_aggregated_properties.head())
    return df_aggregated_properties

