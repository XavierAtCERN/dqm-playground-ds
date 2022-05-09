# Setting up the data science framework (initial setup)

### Creating a virtual environment

```
conda create -n dqm_playground_ds python=3.8
conda activate dqm_playground_ds
conda install pip
```

### Installing kedro

```
pip3 install kedro
kedro info
```

### Creating a new project

```
kedro new --starter=spaceflights
> project_name: DQM Playground DS
> repo_name: dqm-playground-ds
> python_package: dqm_playground_ds
```

### Installing dependencies

```
cd dqm-playground-ds
pip install -r src/requirements.txt
```

### Setting up the data

Copy file from eos to local data files (would be nice to use direct call to API in the future)

```
rm data/01_raw/*
cp /eos/user/x/xcoubez/SWAN_projects/ml4dqm-return/starting_data_analysis/pickles/Run_316187_ALL_clusterposition_PXLayer_* data/01_raw/.
```

Add to the catalog
```
vim conf/base/catalog.yml
```

### Modifying the pipelines

Two pipelines are provided in the starter kit:
- a data procession pipeline
- a data science pipeline

### Adding some pipelines

Two additional pipelines could be useful:
- an optional data extraction pipeline allowing to bypass the command line interface by using directly the APIs from the website
- a data visualization pipeline producing time series, correlation plots...

In order to create the new pipelines
```
kedro pipeline create data_extraction
kedro pipeline create data_visualization
```

__Starting with the data visualization pipeline__

The overall idea would be to create a new task on the website (list of runs/lumisections to develop a strategy + list of runs/lumisections to apply the strategy). The data science pipeline (aka this repository) would then allow to produce the predictions from each strategy and re-upload to the website. However, it would be good to produce few plots within the pipeline to check that the pipeline ran successfully.

### Visualising the pipelines

Visualisation can be achieved using Kedro-Viz. In order to install kedro-viz:
```bash
pip install kedro-viz
```

To run kedro-viz:
```bash
kedro viz
```

The command will run a server on http://127.0.0.1:4141. To run kedro-viz on lxplus with a no-browser option, edit .ssh/config on your personal computer with the following lines:
```
Host lxplus*
    HostName lxplus.cern.ch
    User your_username
    ForwardX11 yes
    ForwardAgent yes
    ForwardX11Trusted yes

Host *_f
    LocalForward localhost:4141 localhost:4141
    ExitOnForwardFailure yes
```

Then log to lxplus, move to the top of the kedro repository and run the command:
```bash
ssh lxplus_f

cd project

kedro viz --no-browser
```

### Adding Continuous Integration

Continuous Integration is added using Github Actions. In order to keep a catalog with full eos path and another one for ci, a new [conf folder](https://kedro.readthedocs.io/en/stable/kedro_project_setup/configuration.html#additional-configuration-environments) is created under ```conf/ci``` and used in the [CI workflow](https://github.com/XavierAtCERN/dqm-playground-ds/actions/workflows/kedro.yml):
```
kedro run --env=ci
```

### Making project into a Docker image

Instructions on how to proceed to create a Docker image can be found [here](https://github.com/kedro-org/kedro-plugins/tree/main/kedro-docker). Lxplus doesn't allow the use of docker, could be related to [this](https://www.reddit.com/r/docker/comments/7y2yp2/why_is_singularity_used_as_opposed_to_docker_in/). Two solutions are therefore available to make it into a Docker image:
- make a local copy
- [create image using Github Actions](https://event-driven.io/en/how_to_buid_and_push_docker_image_with_github_actions/)
