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

    validate_opts(opts)

    return opts


def create_argparser():
    """Create the argparser.

    Returns
    -------
    argparse.ArgParser

    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-a',
        '--account',
        required=False,
        help='Add file to which account'
    )
    parser.add_argument(
        '-c',
        '--config',
        required=False,
        help='Custom YAML config file to use'
    )
    parser.add_argument(
        '-f',
        '--file',
        required=True,
        help='File to load'
    )

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
    args = parser.parse_args()
    config = vars(args)

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
