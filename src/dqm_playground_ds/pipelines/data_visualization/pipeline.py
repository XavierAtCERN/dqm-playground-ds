"""
This is a boilerplate pipeline 'data_visualization'
generated using Kedro 0.17.7
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import plot_time_series, plot_correlations

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=plot_time_series,
                inputs="aggregated_properties",
                outputs=None,
                name="plot_time_series_node",
            ),
            node(
                func=plot_correlations,
                inputs="aggregated_properties",
                outputs=None,
                name="plot_correlations_node",
            ),
        ],
        namespace="data_visualization",
        inputs="aggregated_properties",
    )
