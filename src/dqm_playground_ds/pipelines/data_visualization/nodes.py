import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
import mplhep as hep

plt.style.use([hep.style.ROOT, hep.style.firamath])
hep.rcParams.label.data = True
hep.rcParams.label.paper = False

def plot_one_time_serie(df, variable):
    print(f"Plotting time serie for variable {variable}")
    return

def plot_one_correlation(df, variable1, variable2):
    print(f"Plotting correlation between {variable1} and {variable2}")
    return

def plot_time_series(data: pd.DataFrame) -> None:
    """Plot time serie for all variables.
    Args:
        data: aggregated dataframe
    Returns:
        None
    """
    list_of_variables = data.columns.tolist()[2:]
    print(list_of_variables)
    for variable in list_of_variables:
        plot_one_time_serie(data, variable)
    return None

def plot_correlations(data: pd.DataFrame) -> None:
    """Plot all pairwise correlations.
    Args:
        data: aggregated dataframe
    Returns:
        None
    """
    list_of_variables = data.columns.tolist()[2:]
    print(list_of_variables)
    for i in range(len(list_of_variables)-1):
        plot_one_correlation(data, list_of_variables[i], list_of_variables[i+1])
    return None
