"""
.. module::  libs.core.utils
   :synopsis:  Python  utilities module.

The *utils* module contains a collection of Python helper functions
and classes.

.. warning:: This module should not have any django dependencies.
            It is used during the Django application configuration phase.
"""

import time
import os
import shutil
import logging
import functools

_logger = logging.getLogger(__name__)


def dict_merge(dict1, dict2):
    """
    Return a dict combining two underlying dict instances.
    """
    combined = dict(dict1)
    combined.update(dict2)
    return combined


def class_name(cls):
    """
    Return class name given a class instance.
    """
    return cls.__name__


def instance_class_name(instance):
    """
    Return class name given an object.
    """
    return class_name(instance.__class__)


def mkdir(path):
    """
    Create a directory if it does not exist.
    """
    try:
        os.makedirs(path)
    except OSError:
        if not os.path.isdir(path):
            raise


def rmdir(path):
    """
    Remove directory.
    """
    shutil.rmtree(path, ignore_errors=True)


def touch(fname, times=None):
    """
    Touch a file.
    """
    with open(fname, 'a'):
        os.utime(fname, times)


class DictObject(object):
    """
    Python class to give dict non-keyed attribute access.
    Used to convert dictionaries to object instances.
    """
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


def timeit(method):
    """
    Time function execution.
    """
    @functools.wraps(method)
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print ('%r (%r, %r) %2.2f sec' %
               (method.__name__, args, kw, te - ts))
        return result

    return timed


class Timer(object):
    """
    Class which measures code block execution time.
    """
    msg = "%s elapsed time: %f ms"

    def __init__(self,  user_msg,  use_clock=False,
                 verbose=True, logger=None):
        self.verbose = verbose
        self.logger = logger or _logger
        self.extra_msg = user_msg
        self.timer_fn = time.clock if use_clock else time.time

    def __enter__(self):
        self.start = self.now()
        return self

    def __exit__(self, *args):
        self.end = self.now()
        self.secs = self.end - self.start
        self.msecs = self.secs * 1000  # millisecs

        if self.verbose:
            self.logger.debug(self.msg, self.extra_msg, self.msecs)

    def now(self):
        return self.timer_fn()

