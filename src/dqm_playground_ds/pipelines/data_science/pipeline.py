from kedro.pipeline import Pipeline, node
from kedro.pipeline.modular_pipeline import pipeline

from .nodes import (
    compute_summary_statistics,
    compute_geometrical_properties,
    compute_mean_image,
    compute_rmse,
    aggregate_properties,
)


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            # computing properties
            node(
                func=compute_summary_statistics,
                inputs="preprocessed_raw_pixel_layer_1",
                outputs="summary_statistics",
                name="compute_summary_statistics_node",
            ),
            node(
                func=compute_geometrical_properties,
                inputs="preprocessed_raw_pixel_layer_1",
                outputs="geometrical_properties",
                name="compute_geometrical_properties_node",
            ),
            node(
                func=compute_mean_image,
                inputs="preprocessed_raw_pixel_layer_1",
                outputs="mean_image",
                name="compute_mean_image",
            ),
            node(
                func=compute_rmse,
                inputs=["preprocessed_raw_pixel_layer_1", "mean_image"],
                outputs="images_rmse",
                name="compute_rmse_node",
            ),
            # aggregating
            node(
                func=aggregate_properties,
                inputs=["summary_statistics", "geometrical_properties", "images_rmse"],
                outputs="aggregated_properties",
                name="aggregate_properties",
            ),
        ],
        namespace="data_science",
        inputs="preprocessed_raw_pixel_layer_1",
        outputs="aggregated_properties",
    )  # can actually be instantiated...
