#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pack143trial
----------------------------------

Tests for `pack143trial` module.
"""

import unittest
import cli
import pack143trial


class TestPack143trial(unittest.TestCase):

    def setUp(self):
        self.hello_message = "Hello, PyNaveen!"

    def test_prints_hello_pynaveen(self):
        output = cli.hello()
        assert(output == self.hello_message)

    def test_something(self):
        assert(pack143trial.__version__)

    def tearDown(self):
        pass
