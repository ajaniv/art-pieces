"""
.. module::  inventory.models
   :synopsis:  Inventory models module.

Inventory models module.
"""

from core import models
from core import fields

_app_label = 'inventory'

# @TODO: how to capture biography, formated
# @TODO: model art piece images


@models.meta(models.BusinessObject.Meta, _app_label)
class Artist(models.BusinessObject):
    """
    An abstraction of a person engaged in a wide spectrum
    of activities related to creating art.
    """
    dob = fields.date_field()


class ArtPiece(models.NamedObject):
    """
    An abstraction of a work of art including paintings, sculptures,
    jewelry, film and more.
    """
    class Meta(object):
        abstract = True

    artist = fields.foreign_key_field(
        Artist,
        related_name="%(app_label)s_%(class)s_related_artist")


@models.meta(models.BusinessObject.Meta, _app_label)
class Painting(ArtPiece):
    """
    An abstraction of a work of art made by the application of  paint, pigment,
    color or other medium to a surface such as walls, paper, canvas, wood,
    glass, lacquer, clay, leaf, copper and concrete.
    Brush, knives, sponges, air brushes and other tools can be used to apply
    the paint to the surface.
    """
    pass


@models.meta(models.BusinessObject.Meta, _app_label)
class Sculpture(ArtPiece):
    """
    A abstraction of a work of art that is made by carving or molding clay,
    stone, metal, and other materials.
    """
    pass


@models.meta(models.BusinessObject.Meta, _app_label)
class Photograph(ArtPiece):
    """
    An abstraction of a work of art where an image is created
    by light falling on a light-sensitive surface such as  photographic film.
    """
    pass


@models.meta(models.BusinessObject.Meta, _app_label)
class Lithograph(ArtPiece):
    """
    An abstraction of a work of art where
    a print is produced by a lithographic process.
    """


@models.meta(models.BusinessObject.Meta, _app_label)
class GenericArtPeice(ArtPiece):
    """
    An abstraction of a generic work of art whose custom
    details are not yet modeled.
    """
