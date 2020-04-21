# coding: utf-8

"""
    EXACT - API

    API to interact with the EXACT Server  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Body54(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'image': 'int',
        'user': 'int',
        'screening_tiles': 'object',
        'x_steps': 'int',
        'y_steps': 'int',
        'x_resolution': 'int',
        'y_resolution': 'int',
        'current_index': 'int'
    }

    attribute_map = {
        'image': 'image',
        'user': 'user',
        'screening_tiles': 'screening_tiles',
        'x_steps': 'x_steps',
        'y_steps': 'y_steps',
        'x_resolution': 'x_resolution',
        'y_resolution': 'y_resolution',
        'current_index': 'current_index'
    }

    def __init__(self, image=None, user=None, screening_tiles=None, x_steps=None, y_steps=None, x_resolution=None, y_resolution=None, current_index=None):  # noqa: E501
        """Body54 - a model defined in Swagger"""  # noqa: E501
        self._image = None
        self._user = None
        self._screening_tiles = None
        self._x_steps = None
        self._y_steps = None
        self._x_resolution = None
        self._y_resolution = None
        self._current_index = None
        self.discriminator = None
        self.image = image
        self.user = user
        if screening_tiles is not None:
            self.screening_tiles = screening_tiles
        if x_steps is not None:
            self.x_steps = x_steps
        if y_steps is not None:
            self.y_steps = y_steps
        if x_resolution is not None:
            self.x_resolution = x_resolution
        if y_resolution is not None:
            self.y_resolution = y_resolution
        if current_index is not None:
            self.current_index = current_index

    @property
    def image(self):
        """Gets the image of this Body54.  # noqa: E501


        :return: The image of this Body54.  # noqa: E501
        :rtype: int
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this Body54.


        :param image: The image of this Body54.  # noqa: E501
        :type: int
        """
        if image is None:
            raise ValueError("Invalid value for `image`, must not be `None`")  # noqa: E501

        self._image = image

    @property
    def user(self):
        """Gets the user of this Body54.  # noqa: E501


        :return: The user of this Body54.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Body54.


        :param user: The user of this Body54.  # noqa: E501
        :type: int
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def screening_tiles(self):
        """Gets the screening_tiles of this Body54.  # noqa: E501


        :return: The screening_tiles of this Body54.  # noqa: E501
        :rtype: object
        """
        return self._screening_tiles

    @screening_tiles.setter
    def screening_tiles(self, screening_tiles):
        """Sets the screening_tiles of this Body54.


        :param screening_tiles: The screening_tiles of this Body54.  # noqa: E501
        :type: object
        """

        self._screening_tiles = screening_tiles

    @property
    def x_steps(self):
        """Gets the x_steps of this Body54.  # noqa: E501


        :return: The x_steps of this Body54.  # noqa: E501
        :rtype: int
        """
        return self._x_steps

    @x_steps.setter
    def x_steps(self, x_steps):
        """Sets the x_steps of this Body54.


        :param x_steps: The x_steps of this Body54.  # noqa: E501
        :type: int
        """

        self._x_steps = x_steps

    @property
    def y_steps(self):
        """Gets the y_steps of this Body54.  # noqa: E501


        :return: The y_steps of this Body54.  # noqa: E501
        :rtype: int
        """
        return self._y_steps

    @y_steps.setter
    def y_steps(self, y_steps):
        """Sets the y_steps of this Body54.


        :param y_steps: The y_steps of this Body54.  # noqa: E501
        :type: int
        """

        self._y_steps = y_steps

    @property
    def x_resolution(self):
        """Gets the x_resolution of this Body54.  # noqa: E501


        :return: The x_resolution of this Body54.  # noqa: E501
        :rtype: int
        """
        return self._x_resolution

    @x_resolution.setter
    def x_resolution(self, x_resolution):
        """Sets the x_resolution of this Body54.


        :param x_resolution: The x_resolution of this Body54.  # noqa: E501
        :type: int
        """

        self._x_resolution = x_resolution

    @property
    def y_resolution(self):
        """Gets the y_resolution of this Body54.  # noqa: E501


        :return: The y_resolution of this Body54.  # noqa: E501
        :rtype: int
        """
        return self._y_resolution

    @y_resolution.setter
    def y_resolution(self, y_resolution):
        """Sets the y_resolution of this Body54.


        :param y_resolution: The y_resolution of this Body54.  # noqa: E501
        :type: int
        """

        self._y_resolution = y_resolution

    @property
    def current_index(self):
        """Gets the current_index of this Body54.  # noqa: E501


        :return: The current_index of this Body54.  # noqa: E501
        :rtype: int
        """
        return self._current_index

    @current_index.setter
    def current_index(self, current_index):
        """Sets the current_index of this Body54.


        :param current_index: The current_index of this Body54.  # noqa: E501
        :type: int
        """

        self._current_index = current_index

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Body54, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Body54):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
