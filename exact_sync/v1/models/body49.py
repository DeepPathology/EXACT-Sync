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


class Body49(object):
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
        'imagesets': 'list[int]'
    }

    attribute_map = {
        'name': 'name',
        'imagesets': 'imagesets'
    }

    def __init__(self, name=None, imagesets=None):  # noqa: E501
        """Body49 - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._imagesets = None
        self.discriminator = None
        self.name = name
        self.imagesets = imagesets

    @property
    def name(self):
        """Gets the name of this Body49.  # noqa: E501


        :return: The name of this Body49.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Body49.


        :param name: The name of this Body49.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def imagesets(self):
        """Gets the imagesets of this Body49.  # noqa: E501


        :return: The imagesets of this Body49.  # noqa: E501
        :rtype: list[int]
        """
        return self._imagesets

    @imagesets.setter
    def imagesets(self, imagesets):
        """Sets the imagesets of this Body49.


        :param imagesets: The imagesets of this Body49.  # noqa: E501
        :type: list[int]
        """
        if imagesets is None:
            raise ValueError("Invalid value for `imagesets`, must not be `None`")  # noqa: E501

        self._imagesets = imagesets

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
        if issubclass(Body49, dict):
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
        if not isinstance(other, Body49):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
