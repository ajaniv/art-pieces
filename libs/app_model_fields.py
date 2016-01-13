"""
.. module::  libs.app_model_fields
   :synopsis:  Django model field utilities module.

"""
from django.contrib.auth.models import User
from macaddress.fields import MACAddressField
from libs.django import fields


def annotation(**kwargs):
    """
    Return a new instance of annotation model field.
    """
    defaults = dict(
        blank=True,
        null=True,
        unique=False)
    defaults.update(kwargs)
    return fields.text(**defaults)


def description(**kwargs):
    """
    Return a new instance of description model field.
    """
    defaults = dict(
        blank=True,
        null=True,
        unique=False)
    defaults.update(kwargs)
    return fields.text(**defaults)

GEO_LOCATION_MAX_DIGITS = 9
GEO_LOCATION_DECIMAL_PLACES = 6


def geo_location(**kwargs):
    """
    Return a new instance of geo location model field.
    """
    defaults = dict(
        max_digits=GEO_LOCATION_MAX_DIGITS,
        decimal_places=GEO_LOCATION_DECIMAL_PLACES)
    defaults.update(kwargs)
    return fields.decimal(**defaults)


def mac_address(**kwargs):
    """
    Return a new instance of mac address model field.
    """
    defaults = dict(
        unique=True,
        null=False,
        blank=False)
    defaults.update(kwargs)
    return MACAddressField(**defaults)

NAME_FIELD_MAX_LENGTH = 256


def name(**kwargs):
    """
    Return a new instance of name model field.
    """
    defaults = dict(
        max_length=NAME_FIELD_MAX_LENGTH,
        unique=True,
        db_index=True,
        null=False,
        blank=False)
    defaults.update(kwargs)
    return fields.char(**defaults)


def user(**kwargs):
    """
    Return a new instance of a user model field.
    """
    return fields.foreign_key(User, **kwargs)


USER_AGENT_FIELD_MAX_LENGTH = 512


def user_agent(**kwargs):
    """
    Return a new instance of user agent model field.
    """
    defaults = dict(
        null=False,
        blank=False,
        max_length=USER_AGENT_FIELD_MAX_LENGTH)
    defaults.update(kwargs)
    return fields.char(**defaults)
