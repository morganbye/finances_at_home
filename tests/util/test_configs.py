#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for `util.config`."""

import pytest

from mock import patch

from finances_at_home.finances_at_home import *


class TestLoadConfig:
    """Tests for `load_config`."""

    def test_file_exists(self):
        """Check handling of file."""
        pass

    def test_no_file(self):
        """Check error handling of no file."""
        pass

    def test_valid_config(self):
        """Valid YAML passes."""
        pass

    def test_invalid_config(self):
        """Invalid YAML fails."""
        pass
