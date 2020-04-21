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


class Body34(object):
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
        'name': 'str',
        'filename': 'str',
        'height': 'int',
        'width': 'int',
        'mpp': 'float',
        'objective_power': 'float',
        'image_type': 'float',
        'image_set': 'int',
        'annotations': 'list[int]'
    }

    attribute_map = {
        'name': 'name',
        'filename': 'filename',
        'height': 'height',
        'width': 'width',
        'mpp': 'mpp',
        'objective_power': 'objectivePower',
        'image_type': 'image_type',
        'image_set': 'image_set',
        'annotations': 'annotations'
    }

    def __init__(self, name=None, filename=None, height=None, width=None, mpp=None, objective_power=None, image_type=None, image_set=None, annotations=None):  # noqa: E501
        """Body34 - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._filename = None
        self._height = None
        self._width = None
        self._mpp = None
        self._objective_power = None
        self._image_type = None
        self._image_set = None
        self._annotations = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if filename is not None:
            self.filename = filename
        if height is not None:
            self.height = height
        if width is not None:
            self.width = width
        if mpp is not None:
            self.mpp = mpp
        if objective_power is not None:
            self.objective_power = objective_power
        if image_type is not None:
            self.image_type = image_type
        if image_set is not None:
            self.image_set = image_set
        if annotations is not None:
            self.annotations = annotations

    @property
    def name(self):
        """Gets the name of this Body34.  # noqa: E501


        :return: The name of this Body34.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Body34.


        :param name: The name of this Body34.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def filename(self):
        """Gets the filename of this Body34.  # noqa: E501


        :return: The filename of this Body34.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this Body34.


        :param filename: The filename of this Body34.  # noqa: E501
        :type: str
        """

        self._filename = filename

    @property
    def height(self):
        """Gets the height of this Body34.  # noqa: E501


        :return: The height of this Body34.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this Body34.


        :param height: The height of this Body34.  # noqa: E501
        :type: int
        """

        self._height = height

    @property
    def width(self):
        """Gets the width of this Body34.  # noqa: E501


        :return: The width of this Body34.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this Body34.


        :param width: The width of this Body34.  # noqa: E501
        :type: int
        """

        self._width = width

    @property
    def mpp(self):
        """Gets the mpp of this Body34.  # noqa: E501


        :return: The mpp of this Body34.  # noqa: E501
        :rtype: float
        """
        return self._mpp

    @mpp.setter
    def mpp(self, mpp):
        """Sets the mpp of this Body34.


        :param mpp: The mpp of this Body34.  # noqa: E501
        :type: float
        """

        self._mpp = mpp

    @property
    def objective_power(self):
        """Gets the objective_power of this Body34.  # noqa: E501


        :return: The objective_power of this Body34.  # noqa: E501
        :rtype: float
        """
        return self._objective_power

    @objective_power.setter
    def objective_power(self, objective_power):
        """Sets the objective_power of this Body34.


        :param objective_power: The objective_power of this Body34.  # noqa: E501
        :type: float
        """

        self._objective_power = objective_power

    @property
    def image_type(self):
        """Gets the image_type of this Body34.  # noqa: E501


        :return: The image_type of this Body34.  # noqa: E501
        :rtype: float
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        """Sets the image_type of this Body34.


        :param image_type: The image_type of this Body34.  # noqa: E501
        :type: float
        """

        self._image_type = image_type

    @property
    def image_set(self):
        """Gets the image_set of this Body34.  # noqa: E501


        :return: The image_set of this Body34.  # noqa: E501
        :rtype: int
        """
        return self._image_set

    @image_set.setter
    def image_set(self, image_set):
        """Sets the image_set of this Body34.


        :param image_set: The image_set of this Body34.  # noqa: E501
        :type: int
        """

        self._image_set = image_set

    @property
    def annotations(self):
        """Gets the annotations of this Body34.  # noqa: E501


        :return: The annotations of this Body34.  # noqa: E501
        :rtype: list[int]
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this Body34.


        :param annotations: The annotations of this Body34.  # noqa: E501
        :type: list[int]
        """

        self._annotations = annotations

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
        if issubclass(Body34, dict):
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
        if not isinstance(other, Body34):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
