import logging
import os
import shutil
import sys
import unittest

import fiona

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

from .test_collection import ReadingTest

class FileReadingTest(ReadingTest):
    
    def setUp(self):
        self.c = fiona.open("docs/data/test_uk.shp", "r", layer="test_uk")
    
    def tearDown(self):
        self.c.close()

class DirReadingTest(ReadingTest):
    
    def setUp(self):
        self.c = fiona.open("docs/data", "r", layer="test_uk")
    
    def tearDown(self):
        self.c.close()

    def test_open_repr(self):
        self.failUnlessEqual(
            repr(self.c),
            ("<open Collection 'docs/data:test_uk', mode 'r' "
            "at %s>" % hex(id(self.c))))

    def test_closed_repr(self):
        self.c.close()
        self.failUnlessEqual(
            repr(self.c),
            ("<closed Collection 'docs/data:test_uk', mode 'r' "
            "at %s>" % hex(id(self.c))))

    def test_path(self):
        self.failUnlessEqual(self.c.path, "docs/data")

class InvalidLayerTest(unittest.TestCase):

    def test_invalid(self):
        self.assertRaises(ValueError, fiona.open, ("docs/data/test_uk.shp"), layer="foo")
