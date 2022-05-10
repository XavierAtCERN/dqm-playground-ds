from kedro.pipeline import Pipeline, node, pipeline

from .nodes import get_run_histograms 


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=get_run_histograms,
                inputs="run_histograms",
                outputs="df_run_histograms",
                name="get_run_histograms_node",
            ),
        ],
        namespace="data_extraction",
        inputs="run_histograms",
        outputs="df_run_histograms",
    )
