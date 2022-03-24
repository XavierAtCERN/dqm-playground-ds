from kedro.extras.datasets.matplotlib import MatplotlibWriter

import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
import mplhep as hep

plt.style.use([hep.style.ROOT, hep.style.firamath])
hep.rcParams.label.data = True
hep.rcParams.label.paper = False

def plot_one_time_serie(df, variable):
    print(f"Plotting time serie for variable {variable}")

    f, ax = plt.subplots()
    hep.cms.label(loc=0)
    plt.scatter(df['lumi'].tolist(), df[variable].tolist())
    plt.xlabel('lumisection')
    plt.ylabel(variable)
    plt.tight_layout()
    
    return f

def plot_one_correlation(df, variable1, variable2):
    print(f"Plotting correlation between {variable1} and {variable2}")

    f, ax = plt.subplots()
    hep.cms.label(loc=0)
    plt.scatter(df[variable1].tolist(), df[variable2].tolist())
    plt.xlabel(variable1)
    plt.ylabel(variable2)
    plt.tight_layout()

    return f

def plot_time_series(data: pd.DataFrame) -> MatplotlibWriter:
    """Plot time serie for all variables.
    Args:
        data: aggregated dataframe
    Returns:
        MatplotlibWriter creating all figures
    """

    list_of_variables = data.columns.tolist()[2:]
    print(list_of_variables)

    list_of_figures = []
    for variable in list_of_variables:
        new_figure = plot_one_time_serie(data, variable)
        list_of_figures.append(new_figure)

    return list_of_figures

def plot_correlations(data: pd.DataFrame) -> MatplotlibWriter:
    """Plot all pairwise correlations.
    Args:
        data: aggregated dataframe
    Returns:
        MatplotlibWriter creating all figures
    """
    list_of_variables = data.columns.tolist()[2:]
    print(list_of_variables)

    list_of_figures = []
    for i in range(len(list_of_variables)-1):
        new_figure = plot_one_correlation(data, list_of_variables[i], list_of_variables[i+1])
        list_of_figures.append(new_figure)

    return list_of_figures
