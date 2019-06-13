#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for `util.parser`."""

import pytest

from mock import patch

from finances_at_home.util.parser import *


class TestParseArgs:
    """Testing for `parse_args`."""

    @patch('parser.create_argparser')
    @patch('parser.parse_argparser')
    @patch('parser.validate_opts')
    def test_standard_flow(self, validate, parse, create):
        """Test flow."""
        result = parse_args()

        assert isinstance(result, dict)


class TestCreateArgparser:
    """Testing for `create_argparser`."""

    def test_create_argparser(self):
        """Test flow."""
        # result = create_argparser()
        pass


class TestParseArgParser:
    """Testing for `parse_argparser`."""

    def test_create_parse_argparser(self):
        """Test flow."""
        # result = parse_argparser(mock.object)


class TestValidateOpts:
    """Testing for `validate_opts`."""

    def test_validate_opts(self):
        """Test flow."""
        validate_opts(dict())
