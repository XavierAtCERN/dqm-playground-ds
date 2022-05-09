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

__Starting from a local copy__

Install Docker Desktop (for Mac in my case). Daemon is running by default.

Install kedro-docker:
```
pip install kedro-docker
```

Initialize the files and build the image:
```
kedro docker init
kedro docker build
```

In case an error appears during the build, try login out of Docker and back in.

[Optional] Analyse the image using Dive:
```
kedro docker dive
```

Check that the image has been created and check size of each layer - to learn more, head over to [here](https://www.thorsten-hans.com/determine-the-size-of-docker-image-layers/).
```
docker images
docker history dqm-playground-ds:latest
```

Using python buster leads to very large layers for pip install:
```
<missing>      2 hours ago   RUN /bin/sh -c pip install -r /tmp/requireme…   1.45GB    buildkit.dockerfile.v0
<missing>      2 hours ago   COPY src/requirements.txt /tmp/requirements.…   587B      buildkit.dockerfile.v0
```
Moving to slim (```kedro docker build --base-image="python:3.8-slim"```) doesn't change the situation... Dive report shows a 22MB gain from removing some files from the layers, could be done in the future but negligible with respect to the current image size.

Upload to a registry (Docker Hub for now)
```bash
docker tag dqm-playground-ds <DockerID:xavier2c>/dqm-playground-ds
docker push <DockerID:xavier2c>/dqm-playground-ds
```

### Creating an Argo workflow

Instructions on how to proceed to create an Argo workflow (with the aim of deploying to Openshift) can be found [here](https://kedro.readthedocs.io/en/stable/deployment/argo.html).

