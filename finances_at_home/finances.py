# -*- coding: utf-8 -*-
"""Main module."""
from finances_at_home.util.setup import setup_pipeline
from finances_at_home.util.io import load_file
# from categorization import


def main():
    """Main entry point to pipeline.

    Returns
    -------
    None

    """
    config = setup_pipeline()
    loaded_file = load_file(config)


if __name__ == "__main__":
    main()
