from kedro.pipeline import Pipeline, node
from kedro.pipeline.modular_pipeline import pipeline

from .nodes import preprocess_pixel_layer_1, preprocess_pixel_layer_2


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=preprocess_pixel_layer_1,
                inputs="raw_pixel_layer_1",
                outputs="preprocessed_raw_pixel_layer_1",
                name="preprocess_raw_pixel_layer_1_node",
            ),
            node(
                func=preprocess_pixel_layer_2,
                inputs="raw_pixel_layer_2",
                outputs="preprocessed_raw_pixel_layer_2",
                name="preprocess_raw_pixel_layer_2_node",
            ),
        ],
        namespace="data_processing",
        inputs=["raw_pixel_layer_1", "raw_pixel_layer_2"],
        outputs=["preprocessed_raw_pixel_layer_1", "preprocessed_raw_pixel_layer_2"],
    )
