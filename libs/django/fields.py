"""
.. module::  libs.django.fields
   :synopsis:  Django model fields utilities module.

The *fields* module is a collection of Django model fields utilities
designed to foster common field usage and facilitate configuration changes.
"""

import inflection
from django.db import models
from libs.core.utils import class_name


def auto(**kwargs):
    """
    Return a new instance of auto increment model field.
    """
    defaults = dict(
        primary_key=True,
        unique=True)
    defaults.update(kwargs)
    return models.AutoField(**defaults)


def boolean(**kwargs):
    """
    Return a new instance of boolean model field.
    """
    defaults = dict(
        blank=True,
        null=False,
        default=False)
    defaults.update(kwargs)
    return models.BooleanField(**defaults)


def file_field(upload_to, **kwargs):
    """
    Return a new instance of file model field.
    """
    return models.FileField(upload_to=upload_to, **kwargs)

CHAR_FIELD_MAX_LENGTH = 16


def char(**kwargs):
    """
    Return a new instance of char model field.
    """
    defaults = dict(
        max_length=CHAR_FIELD_MAX_LENGTH,
        blank=False,
        null=False,
        unique=False)
    defaults.update(kwargs)
    return models.CharField(**defaults)


def date(**kwargs):
    """
    Return a new instance of date model field.
    """
    defaults = dict(auto_now=False,
                    auto_now_add=False,
                    blank=False,
                    null=False)
    defaults.update(kwargs)
    return models.DateField(**defaults)


def datetime(**kwargs):
    """
    Return a new instance of datetime model field.
    """
    defaults = dict(auto_now=False,
                    auto_now_add=False,
                    blank=False,
                    null=False)
    defaults.update(kwargs)
    return models.DateTimeField(**defaults)


def decimal(max_digits, decimal_places, **kwargs):
    """
    Return a new instance of decimal model field.
    """
    defaults = dict(
        decimal_places=decimal_places,
        max_digits=max_digits,
        default=0,
        blank=False, null=False)
    defaults.update(kwargs)
    return models.DecimalField(**defaults)


def floating_point(**kwargs):
    """
    Return a new instance of floating point model field.
    """
    defaults = dict(
        blank=False,
        null=False,
        default=0.0)
    defaults.update(kwargs)
    return models.FloatField(**defaults)


def foreign_key(to, **kwargs):
    """
    Return a new instance of foreign key model field.
    """
    defaults = dict(
        blank=False,
        db_constraint=True,
        null=False,
        on_delete=models.PROTECT)

    defaults.update(kwargs)
    return models.ForeignKey(to, **defaults)


def image(**kwargs):
    """
    Return a new instance of image model field.
    """
    return models.ImageField(**kwargs)


def integer(**kwargs):
    """
    Return a new instance of integer model field.
    """
    defaults = dict(
        default=0,
        blank=False, null=False)
    defaults.update(kwargs)
    return models.IntegerField(**defaults)


def ip_address(**kwargs):
    """
    Return a new instance of ip address model field.
    """
    defaults = dict(
        null=False,
        blank=False)
    defaults.update(kwargs)
    return models.GenericIPAddressField(**defaults)


def many_to_many(to, db_table, **kwargs):
    """
    Return a new instance of many to many model field.
    """
    defaults = dict(
        db_constraint=True,
        null=True,
        blank=True)

    related_name = kwargs.pop('related_name', None)
    defaults.update(kwargs)

    related_name = (
        related_name or
        '{}_set'.format(inflection.camelize(class_name(to))))

    return models.ManyToManyField(
        to,
        db_table=db_table,
        related_name=related_name,
        **defaults)


def one_to_one(to, **kwargs):
    """
    Return a new instance of one-to-one model field.
    """
    defaults = dict(
        blank=False,
        db_constraint=True,
        null=False,
        on_delete=models.PROTECT)

    defaults.update(kwargs)
    return models.OneToOneField(to, **defaults)


def small_integer(**kwargs):
    """
    Return a new instance of small integer model field.
    """
    defaults = dict(
        default=0,
        blank=False, null=False)
    defaults.update(kwargs)
    return models.SmallIntegerField(**defaults)


def text(**kwargs):
    """
    Return a new instance of text model field.
    """
    defaults = dict(
        blank=True,
        null=True,
        unique=False)
    defaults.update(kwargs)
    return models.TextField(**defaults)

URL_FIELD_MAX_LENGTH = 200


def url(**kwargs):
    """
    Return a new instance of url model field.
    """
    defaults = dict(
        max_length=URL_FIELD_MAX_LENGTH,
        null=False,
        blank=False)
    defaults.update(kwargs)
    return models.URLField(**defaults)


def uuid(**kwargs):
    """
    Return a new instance of uuid model field.
    """
    defaults = dict(
        unique=True,
        auto=True,
        db_index=True)
    defaults.update(kwargs)
    return models.UUIDField(**defaults)
