# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ..models.base_model_ import Model
from .. import util


class Director(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, nombre: str=None, fecha_nacimiento: datetime=None):  # noqa: E501
        """Director - a model defined in Swagger

        :param id: The id of this Director.  # noqa: E501
        :type id: str
        :param nombre: The nombre of this Director.  # noqa: E501
        :type nombre: str
        :param fecha_nacimiento: The fecha_nacimiento of this Director.  # noqa: E501
        :type fecha_nacimiento: datetime
        """
        self.swagger_types = {
            'id': str,
            'nombre': str,
            'fecha_nacimiento': datetime
        }

        self.attribute_map = {
            'id': 'id',
            'nombre': 'nombre',
            'fecha_nacimiento': 'fecha_nacimiento'
        }
        self._id = id
        self._nombre = nombre
        self._fecha_nacimiento = fecha_nacimiento

    @classmethod
    def from_dict(cls, dikt) -> 'Director':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Director of this Director.  # noqa: E501
        :rtype: Director
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Director.


        :return: The id of this Director.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Director.


        :param id: The id of this Director.
        :type id: str
        """

        self._id = id

    @property
    def nombre(self) -> str:
        """Gets the nombre of this Director.


        :return: The nombre of this Director.
        :rtype: str
        """
        return self._nombre

    @nombre.setter
    def nombre(self, nombre: str):
        """Sets the nombre of this Director.


        :param nombre: The nombre of this Director.
        :type nombre: str
        """

        self._nombre = nombre

    @property
    def fecha_nacimiento(self) -> datetime:
        """Gets the fecha_nacimiento of this Director.


        :return: The fecha_nacimiento of this Director.
        :rtype: datetime
        """
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fecha_nacimiento: datetime):
        """Sets the fecha_nacimiento of this Director.


        :param fecha_nacimiento: The fecha_nacimiento of this Director.
        :type fecha_nacimiento: datetime
        """

        self._fecha_nacimiento = fecha_nacimiento
