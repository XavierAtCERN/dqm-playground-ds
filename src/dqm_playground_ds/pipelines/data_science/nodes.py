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
    print("Running - Computing summary statistics")
    data["map"] = data["map"].apply(
        lambda x: ast.literal_eval(x)
    )  # should be done in processing...
    data["mean"] = data["map"].apply(lambda x: np.array(x).mean())
    data["std"] = data["map"].apply(lambda x: np.array(x).std())
    df_summary_statistics = data[["run", "lumi", "mean", "std"]].copy()
    print(df_summary_statistics.head())
    return df_summary_statistics


def compute_geometrical_properties(data: pd.DataFrame) -> pd.DataFrame:
    """Compute geometrical properties from data (center of mass, ...).

    Args:
        data: Dataframe containing 2D histograms.
    Returns:
        dataframe with run + lumi + geometrical properties
    """
    print("Running - Computing geometrical properties")
    data["map"] = data["map"].apply(
        lambda x: ast.literal_eval(x)
    )  # should be done in processing
    data["image"] = data["map"].apply(
        lambda x: np.reshape(x, (202, 302))[1:201, 1:301]
    )  # should be done in processing
    data["center_phi"] = data["image"].apply(
        lambda x: scipy.ndimage.measurements.center_of_mass(x)[0]
    )
    data["center_z"] = data["image"].apply(
        lambda x: scipy.ndimage.measurements.center_of_mass(x)[1]
    )
    df_geometrical_properties = data[["run", "lumi", "center_phi", "center_z"]].copy()
    print(df_geometrical_properties.head())
    return df_geometrical_properties


def compute_rmse(data: pd.DataFrame) -> pd.DataFrame:
    """Compute mean picture over a run..

    Args:
        data: Dataframe containing 2D histograms.
    Returns:
        dataframe with run + lumi + rmse
    """
    print("Running - computing RMSE")
    data["map"] = data["map"].apply(lambda x: ast.literal_eval(x))
    data["image"] = data["map"].apply(lambda x: np.reshape(x, (202, 302))[1:201, 1:301])
    tensor_image = np.array(data["image"].tolist())
    print(f"Tensor shape is {tensor_image.shape}")
    mean_image = tensor_image.mean(axis=0)
    print(f"Mean image shape is {mean_image.shape}")
    rmse = np.sqrt(np.mean(np.subtract(tensor_image, mean_image), axis=(1, 2)) ** 2)
    print(f"RMSE with broadcasting is {rmse}")
    data["rmse"] = rmse
    df_rmse = data[["run", "lumi", "rmse"]].copy()
    print(df_rmse.head())
    return df_rmse


# Aggregating properties


def aggregate_properties(
    summary_statistics: pd.DataFrame,
    geometrical_properties: pd.DataFrame,
    images_rmse: pd.DataFrame,
) -> pd.DataFrame:
    """Aggregate properties from the 2D histograms

    Args:
        summary_statistics: dataframe with run + lumi + mean + rms + ....
    Returns:
        dataframe with run + lumi + geometrical properties
    """
    print("Running - Aggregating properties")
    df_aggregated_properties = summary_statistics.merge(
        geometrical_properties, on=["run", "lumi"]
    )
    df_aggregated_properties = df_aggregated_properties.merge(
        images_rmse, on=["run", "lumi"]
    )
    print(df_aggregated_properties.head())
    return df_aggregated_properties
