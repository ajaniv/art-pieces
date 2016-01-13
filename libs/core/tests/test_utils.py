"""
.. module::  libs.core.tests.test_utils
   :synopsis: libs.core.utils unit test module.

The *test_utils* is libs.core.utils  unit test module.

"""
import os
import json
import unittest

from .. import utils


class UtilsTestCase(unittest.TestCase):
    """
    Utils unit test base class
    """
    current_dir = os.path.dirname(__file__)


class TestFile(UtilsTestCase):
    """
    File related test cases
    """
    def setUp(self):
        self.new_dir = os.path.join(self.current_dir, 'test_dir')

    def tearDown(self):
        utils.rmdir(self.new_dir)

    def test_mkdir(self):
        new_dir = self.new_dir
        self.assertFalse(os.path.isdir(new_dir))
        utils.mkdir(new_dir)
        self.assertTrue(os.path.isdir(new_dir))
        utils.rmdir(new_dir)
        self.assertFalse(os.path.isdir(new_dir))


class TestJson(UtilsTestCase):
    '''
    Test json
    '''
    def test_json_encoding(self):
        data = {u'spam': u'eggs'}
        json_data = json.dumps(data)
        self.assertEqual(json_data, '{"spam": "eggs"}')


class TimerTestcase(UtilsTestCase):
    '''
    Timer  unit test class.
    '''
    def test_timer(self):
        with utils.Timer('my timer', verbose=True) as timer:
            self.assertTrue(timer.start)
        self.assertTrue(timer.end > timer.start)

    def test_timeit(self):
        @utils.timeit
        def timed_function(count, **kwargs):
            total = 0
            for index in range(0, count):
                total += index * kwargs['value']
            return total

        timed_function(count=1000000, value=1000)
