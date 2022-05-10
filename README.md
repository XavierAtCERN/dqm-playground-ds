# DQM Playground - Data Science Framework

[![Kedro](https://github.com/XavierAtCERN/dqm-playground-ds/actions/workflows/kedro.yml/badge.svg)](https://github.com/XavierAtCERN/dqm-playground-ds/actions/workflows/kedro.yml)
[![Docker](https://github.com/XavierAtCERN/dqm-playground-ds/actions/workflows/build-and-publish.yml/badge.svg)](https://github.com/XavierAtCERN/dqm-playground-ds/actions/workflows/build-and-publish.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Project overview

The goal of this repository is to provide a data science framework to explore various anomaly detection strategies in the context of the CMS Tracker DQM Playground effort. The code for the website hosting the data and allowing to inspect them can be found [here](https://github.com/CMSTrackerDPG/MLplayground). An optional Command Line Interface to get the data can be found [here](https://github.com/XavierAtCERN/dqm-playground-cli).

An overview of the architecture of the project highlighting the role of the data science part can be found below.

![Architecture of the project](./images/DataScience.jpeg?raw=true "Architecture of the project")

## Current structure

The current structure can be divided in three steps:
- data processing (dummy)
- data science
- data visualization (dummy)

![Current structure](./images/kedro_current_pipeline_3.png?raw=true "Current structure")

Another pipeline could be added to interface directly the website's API with the data science framework.
