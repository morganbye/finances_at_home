# -*- coding: utf-8 -*-
"""Main argparser module."""
import argparse


def parse_args():
    """Load, parse and validate command line arguments.

    Returns
    -------
    dict

    """
    args = create_argparser()
    opts = parse_argparser(args)

    validate_opts

    return opts


def create_argparser():
    """Create the argparser.

    Returns
    -------
    argparse.ArgParser

    """
    parser = argparse.ArgumentParser()

    return parser


def parse_argparser(parser):
    """Parse the argparser.

    Parameters
    ----------
    parser : argparse.ArgumentParser

    Returns
    -------
    dict

    """
    config = vars(parser)

    return config


def validate_opts(config):
    """Perform basic error checking on inputs before proceeding.

    Parameters
    ----------
    config : dict

    Returns
    -------
    None

    """
    pass
