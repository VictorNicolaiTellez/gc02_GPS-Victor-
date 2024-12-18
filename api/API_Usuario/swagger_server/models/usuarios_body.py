# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from api.API_Usuario.swagger_server.models.base_model_ import Model
from api.API_Usuario.swagger_server import util


class UsuariosBody(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, nombre: str=None, apellidos: str=None, correo: str=None, contrasea: str=None, imagen_perfil: str=None, metodo_pago: str=None, idioma: str=None, genero_favorito: str=None):  # noqa: E501
        """UsuariosBody - a model defined in Swagger

        :param nombre: The nombre of this UsuariosBody.  # noqa: E501
        :type nombre: str
        :param apellidos: The apellidos of this UsuariosBody.  # noqa: E501
        :type apellidos: str
        :param correo: The correo of this UsuariosBody.  # noqa: E501
        :type correo: str
        :param contrasea: The contrasea of this UsuariosBody.  # noqa: E501
        :type contrasea: str
        :param imagen_perfil: The imagen_perfil of this UsuariosBody.  # noqa: E501
        :type imagen_perfil: str
        :param metodo_pago: The metodo_pago of this UsuariosBody.  # noqa: E501
        :type metodo_pago: str
        :param idioma: The idioma of this UsuariosBody.  # noqa: E501
        :type idioma: str
        :param genero_favorito: The genero_favorito of this UsuariosBody.  # noqa: E501
        :type genero_favorito: str
        """
        self.swagger_types = {
            'nombre': str,
            'apellidos': str,
            'correo': str,
            'contrasea': str,
            'imagen_perfil': str,
            'metodo_pago': str,
            'idioma': str,
            'genero_favorito': str
        }

        self.attribute_map = {
            'nombre': 'nombre',
            'apellidos': 'apellidos',
            'correo': 'correo',
            'contrasea': 'contraseña',
            'imagen_perfil': 'imagen_perfil',
            'metodo_pago': 'metodo_pago',
            'idioma': 'idioma',
            'genero_favorito': 'genero_favorito'
        }
        self._nombre = nombre
        self._apellidos = apellidos
        self._correo = correo
        self._contrasea = contrasea
        self._imagen_perfil = imagen_perfil
        self._metodo_pago = metodo_pago
        self._idioma = idioma
        self._genero_favorito = genero_favorito

    @classmethod
    def from_dict(cls, dikt) -> 'UsuariosBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The usuarios_body of this UsuariosBody.  # noqa: E501
        :rtype: UsuariosBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def nombre(self) -> str:
        """Gets the nombre of this UsuariosBody.

        Nombre completo del usuario  # noqa: E501

        :return: The nombre of this UsuariosBody.
        :rtype: str
        """
        return self._nombre

    @nombre.setter
    def nombre(self, nombre: str):
        """Sets the nombre of this UsuariosBody.

        Nombre completo del usuario  # noqa: E501

        :param nombre: The nombre of this UsuariosBody.
        :type nombre: str
        """
        if nombre is None:
            raise ValueError("Invalid value for `nombre`, must not be `None`")  # noqa: E501

        self._nombre = nombre

    @property
    def apellidos(self) -> str:
        """Gets the apellidos of this UsuariosBody.

        Apellidos del Usuario  # noqa: E501

        :return: The apellidos of this UsuariosBody.
        :rtype: str
        """
        return self._apellidos

    @apellidos.setter
    def apellidos(self, apellidos: str):
        """Sets the apellidos of this UsuariosBody.

        Apellidos del Usuario  # noqa: E501

        :param apellidos: The apellidos of this UsuariosBody.
        :type apellidos: str
        """
        if apellidos is None:
            raise ValueError("Invalid value for `apellidos`, must not be `None`")  # noqa: E501

        self._apellidos = apellidos

    @property
    def correo(self) -> str:
        """Gets the correo of this UsuariosBody.

        Correo electrónico del usuario  # noqa: E501

        :return: The correo of this UsuariosBody.
        :rtype: str
        """
        return self._correo

    @correo.setter
    def correo(self, correo: str):
        """Sets the correo of this UsuariosBody.

        Correo electrónico del usuario  # noqa: E501

        :param correo: The correo of this UsuariosBody.
        :type correo: str
        """
        if correo is None:
            raise ValueError("Invalid value for `correo`, must not be `None`")  # noqa: E501

        self._correo = correo

    @property
    def contrasea(self) -> str:
        """Gets the contrasea of this UsuariosBody.

        Contraseña del usuario  # noqa: E501

        :return: The contrasea of this UsuariosBody.
        :rtype: str
        """
        return self._contrasea

    @contrasea.setter
    def contrasea(self, contrasea: str):
        """Sets the contrasea of this UsuariosBody.

        Contraseña del usuario  # noqa: E501

        :param contrasea: The contrasea of this UsuariosBody.
        :type contrasea: str
        """
        if contrasea is None:
            raise ValueError("Invalid value for `contrasea`, must not be `None`")  # noqa: E501

        self._contrasea = contrasea

    @property
    def imagen_perfil(self) -> str:
        """Gets the imagen_perfil of this UsuariosBody.

        URL de la imagen de perfil del usuario  # noqa: E501

        :return: The imagen_perfil of this UsuariosBody.
        :rtype: str
        """
        return self._imagen_perfil

    @imagen_perfil.setter
    def imagen_perfil(self, imagen_perfil: str):
        """Sets the imagen_perfil of this UsuariosBody.

        URL de la imagen de perfil del usuario  # noqa: E501

        :param imagen_perfil: The imagen_perfil of this UsuariosBody.
        :type imagen_perfil: str
        """

        self._imagen_perfil = imagen_perfil

    @property
    def metodo_pago(self) -> str:
        """Gets the metodo_pago of this UsuariosBody.

        Método de pago preferido del usuario  # noqa: E501

        :return: The metodo_pago of this UsuariosBody.
        :rtype: str
        """
        return self._metodo_pago

    @metodo_pago.setter
    def metodo_pago(self, metodo_pago: str):
        """Sets the metodo_pago of this UsuariosBody.

        Método de pago preferido del usuario  # noqa: E501

        :param metodo_pago: The metodo_pago of this UsuariosBody.
        :type metodo_pago: str
        """

        self._metodo_pago = metodo_pago

    @property
    def idioma(self) -> str:
        """Gets the idioma of this UsuariosBody.

        Idioma preferido (\"español\", \"inglés\", \"portugués\"...)  # noqa: E501

        :return: The idioma of this UsuariosBody.
        :rtype: str
        """
        return self._idioma

    @idioma.setter
    def idioma(self, idioma: str):
        """Sets the idioma of this UsuariosBody.

        Idioma preferido (\"español\", \"inglés\", \"portugués\"...)  # noqa: E501

        :param idioma: The idioma of this UsuariosBody.
        :type idioma: str
        """

        self._idioma = idioma

    @property
    def genero_favorito(self) -> str:
        """Gets the genero_favorito of this UsuariosBody.

        Género favorito del usuario  # noqa: E501

        :return: The genero_favorito of this UsuariosBody.
        :rtype: str
        """
        return self._genero_favorito

    @genero_favorito.setter
    def genero_favorito(self, genero_favorito: str):
        """Sets the genero_favorito of this UsuariosBody.

        Género favorito del usuario  # noqa: E501

        :param genero_favorito: The genero_favorito of this UsuariosBody.
        :type genero_favorito: str
        """

        self._genero_favorito = genero_favorito
