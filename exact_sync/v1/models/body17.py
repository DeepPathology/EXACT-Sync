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


class Body17(object):
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
        'image_sets': 'list[int]',
        'product_set': 'list[int]'
    }

    attribute_map = {
        'name': 'name',
        'image_sets': 'image_sets',
        'product_set': 'product_set'
    }

    def __init__(self, name=None, image_sets=None, product_set=None):  # noqa: E501
        """Body17 - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._image_sets = None
        self._product_set = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if image_sets is not None:
            self.image_sets = image_sets
        if product_set is not None:
            self.product_set = product_set

    @property
    def name(self):
        """Gets the name of this Body17.  # noqa: E501


        :return: The name of this Body17.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Body17.


        :param name: The name of this Body17.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def image_sets(self):
        """Gets the image_sets of this Body17.  # noqa: E501


        :return: The image_sets of this Body17.  # noqa: E501
        :rtype: list[int]
        """
        return self._image_sets

    @image_sets.setter
    def image_sets(self, image_sets):
        """Sets the image_sets of this Body17.


        :param image_sets: The image_sets of this Body17.  # noqa: E501
        :type: list[int]
        """

        self._image_sets = image_sets

    @property
    def product_set(self):
        """Gets the product_set of this Body17.  # noqa: E501


        :return: The product_set of this Body17.  # noqa: E501
        :rtype: list[int]
        """
        return self._product_set

    @product_set.setter
    def product_set(self, product_set):
        """Sets the product_set of this Body17.


        :param product_set: The product_set of this Body17.  # noqa: E501
        :type: list[int]
        """

        self._product_set = product_set

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
        if issubclass(Body17, dict):
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
        if not isinstance(other, Body17):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
