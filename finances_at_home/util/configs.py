# -*- coding: utf-8 -*-
"""Main config locating and loading module."""
import os
import yaml


def load_configs(config):
    """Load options from config file.

    Parameters
    ----------
    config : dict

    Returns
    -------
    dict

    """
    config['accounts'] = load_yaml_from_config_dir('accounts')
    config['categories'] = load_yaml_from_config_dir('categories')

    return config


def load_yaml_from_config_dir(filename):
    """Load `configuration/<filename>.yaml`."""

    abs_path = os.path.join(
        get_config_dir(),
        filename + '.yaml'
    )

    loaded_config = load_yaml(abs_path)

    return loaded_config


def get_config_dir():
    """Find the path to the configuration directory.

    Returns
    -------
    str
        path to config directory

    """
    this_file = os.path.realpath(__file__)
    config_dir = os.path.join(
        os.path.dirname(this_file),
        '..',
        '..',
        'configuration'
    )

    return config_dir


def load_yaml(path):
    """Load a YAML file.

    Parameters
    ----------
    path : str

    Returns
    -------
    dict

    Raises
    ------
    IOError

    """

    with open(path, 'r') as stream:
        try:
            loaded_yaml = yaml.load(stream)
        except yaml.YAMLError:
            raise IOError('Invalid YAML file')

    return loaded_yaml

