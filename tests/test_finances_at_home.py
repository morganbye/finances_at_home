#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `finances_at_home` package."""

import pytest

from mock import patch

from finances_at_home.finances_at_home import *


class TestMain:
    """Testing for finances_at_home.main."""

    def test_main(self):
        """Test main."""
        with patch('finances_at_home.util.setup.setup_pipeline',
                   return_value=dict()):
            main()
