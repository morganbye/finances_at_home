# -*- coding: utf-8 -*-
"""Main file loading module."""

import os
import pandas as pd

from operator import itemgetter
from pathlib import Path


def load_file(config):
    """Load the user defined file to a pd.df.

    Parameters
    ----------
    filepath : str

    Returns
    -------
    pandas.DataFrame

    """
    ext = Path(config.get('file')).suffix

    if ext == '.csv':
        load_csv(
            config.get('file'),
            config.get('accounts')
                  .get('scotiabank')
                  .get('credit_card')
        )

    else:
        NotImplementedError('Filetype {} is not yet implemented'.format(ext))


def load_csv(filepath, account_info):
    """

    Parameters
    ----------
    filepath : str
    account_info : dict

    Returns
    -------
    pd.DataFrame

    """
    column_list = get_column_list(account_info['columns'])

    loaded_csv = pd.read_csv(
        filepath,
        column_list,
        header=account_info.get('header', 0),
        delimiter=account_info.get('delimiter', ',')
    )

    return loaded_csv


def get_column_list(column_dict):
    """Convert a column dict from the config to a list for Pandas loading.

    Parameters
    ----------
    column_dict : dict

    Returns
    -------
    list

    """
    # column_list = list()
    #
    # for key, value in column_dict:
    #     column_list.append([value['position'], key])
    #
    # column_list.sort(key=itemgetter(0))

    # column_list = sorted(column_dict.items(), key=lambda x: x['position'])
    print(str(column_list))

    return column_list
