# -*- coding: utf-8 -*-
"""Main setup module."""

from finances_at_home.util.parser import parse_args
from finances_at_home.util.configs import load_configs


def setup_pipeline():
    """Setup the pipeline.

    Returns
    -------
    dict

    """
    config = get_command_line_args()
    config = load_configs(config)

    return config


def get_command_line_args():
    """Create command line argparser and parse it.

    Parameters
    ----------
    args

    Returns
    -------
    dict

    """
    opt = parse_args()

    return opt

