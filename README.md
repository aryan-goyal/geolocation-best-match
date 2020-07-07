# geolocation-best-match

Generates routing xml based on closest match for vechile-routing-software.

This work is initally done to provide a better method to build the ingestion file for the Vehicle Routing Open-source Optimization Machine which can be found at https://github.com/VROOM-Project/vroom.

## Alternatives include Google Colab for running from notebook

## Installation

You can find the installation documentation for the
[Jupyter platform, on ReadTheDocs](https://jupyter.readthedocs.io/en/latest/install.html).
The documentation for advanced usage of Jupyter notebook can be found
[here](https://jupyter-notebook.readthedocs.io/en/latest/).

For a local installation, make sure you have
[pip installed](https://pip.readthedocs.io/en/stable/installing/) and run:

    $ pip install notebook

## Usage - Running Jupyter notebook

### Running in a local installation

Launch with:

    $ jupyter notebook

### Running in a remote installation

You need some configuration before starting Jupyter notebook remotely. See [Running a notebook server](https://jupyter-notebook.readthedocs.io/en/stable/public_server.html).

## Requirements

Python 3+, python-pip, virtualenv

## Installation

Create a virtualenv, and activate this:

    $ virtualenv env
    $ source env/bin/activate

After, install all necessary to run:

    $ pip install -r requirements.txt

Than, run the application:

    $ python run.py

To see your application, access this url in your browser:

    http://localhost:5000
