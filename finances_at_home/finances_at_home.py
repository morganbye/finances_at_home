# -*- coding: utf-8 -*-
"""Main module."""
from finances_at_home.util.setup import setup_pipeline


def main():
    """Main entry point to pipeline.

    Returns
    -------
    None

    """
    config = setup_pipeline()


if __name__ == "__main__":
    main()
