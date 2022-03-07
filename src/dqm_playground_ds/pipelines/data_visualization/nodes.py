import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
import mplhep as hep

plt.style.use([hep.style.ROOT, hep.style.firamath])
hep.rcParams.label.data = True
hep.rcParams.label.paper = False


def plot_time_series(data: pd.DataFrame) -> None:
    """Plot time serie for all variables.
    Args:
        data: aggregated dataframe
    Returns:
        None
    """
    list_of_variables = data.columns.tolist()[3:]
    print(list_of_variables)
    return None

def plot_correlations(data: pd.DataFrame) -> None:
    """Plot all pairwise correlations.
    Args:
        data: aggregated dataframe
    Returns:
        None
    """
    list_of_variables = data.columns.tolist()[3:]
    print(list_of_variables)
    return None
