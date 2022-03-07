"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline

from dqm_playground_ds.pipelines import data_processing as dp
from dqm_playground_ds.pipelines import data_science as ds
from dqm_playground_ds.pipelines import data_visualization as dv

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.

    """
    data_processing_pipeline = dp.create_pipeline()
    data_science_pipeline = ds.create_pipeline()
    data_visualization_pipeline = dv.create_pipeline()

    return {
        "__default__": data_processing_pipeline + data_science_pipeline + data_visualization_pipeline,
        "dp": data_processing_pipeline,
        "ds": data_science_pipeline,
        "dv": data_visualization_pipeline,
    }
