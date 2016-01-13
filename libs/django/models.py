"""
.. module::  libs.django.models
   :synopsis:  Shared Django models module.

"""
from django.db import models
from django.contrib.sites.models import Site
from libs.django import fields
from libs import app_model_fields


class BusinessObjectManager(models.Manager):
    """
    Business object manager class.
    """

    def get_or_none(self, *args, **kwargs):
        """
        Return an object instance or none.

        :param args: Positional argument list.
        :type args: list.
        :param kwargs: Key words arguments.
        :type kwargs: dict.
        :returns:  An instance of Model or None.
        """
        try:
            return self.get(*args, **kwargs)
        except self.model.DoesNotExist:
            return None


class BusinessObject(models.Model):
    """
    An abstract base class for application business objects.
    """
    class Meta(object):
        abstract = True
        get_latest_by = 'update_time'

    objects = BusinessObjectManager()
    id = fields.auto()
    uuid = fields.uuid()
    version = fields.integer()
    enabled = fields.boolean(default=True)
    deleted = fields.boolean(default=False)
    creation_time = fields.datetime(auto_now_add=True)
    update_time = fields.datetime(auto_now=True)

    creation_user = app_model_fields.user(
        related_name="%(app_label)s_%(class)s_related_creation_user")

    update_user = app_model_fields.user(
        related_name="%(app_label)s_%(class)s_related_update_user")

    site = fields.foreign_key(
        Site,
        related_name="%(app_label)s_%(class)s_related_site")

    def __init__(self, *args, **kwargs):
        super(BusinessObject, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        """
        Save an instance
        """
        self.version += 1
        update_user = kwargs.pop('update_user', None)
        if update_user is not None:
            self.update_user = update_user
        super(BusinessObject, self).save(*args, **kwargs)
