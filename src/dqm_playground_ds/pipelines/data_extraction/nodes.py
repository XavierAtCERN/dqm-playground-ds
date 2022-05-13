from kedro.extras.datasets.api import APIDataSet

import pandas as pd


def get_run_histograms(run_histograms: APIDataSet) -> pd.DataFrame:
    """Get run histograms using API
    Args:
        run_histograms: Full json response.
    Returns:
        Dataframe containing runs and histograms
    """
    df_run_histograms = run_histograms.text
    print(df_run_histograms)
    return df_run_histograms
