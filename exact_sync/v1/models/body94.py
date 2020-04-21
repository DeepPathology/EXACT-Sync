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


class Body94(object):
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
        'annotation': 'int',
        'user': 'int',
        'verified': 'bool'
    }

    attribute_map = {
        'annotation': 'annotation',
        'user': 'user',
        'verified': 'verified'
    }

    def __init__(self, annotation=None, user=None, verified=None):  # noqa: E501
        """Body94 - a model defined in Swagger"""  # noqa: E501
        self._annotation = None
        self._user = None
        self._verified = None
        self.discriminator = None
        self.annotation = annotation
        self.user = user
        if verified is not None:
            self.verified = verified

    @property
    def annotation(self):
        """Gets the annotation of this Body94.  # noqa: E501


        :return: The annotation of this Body94.  # noqa: E501
        :rtype: int
        """
        return self._annotation

    @annotation.setter
    def annotation(self, annotation):
        """Sets the annotation of this Body94.


        :param annotation: The annotation of this Body94.  # noqa: E501
        :type: int
        """
        if annotation is None:
            raise ValueError("Invalid value for `annotation`, must not be `None`")  # noqa: E501

        self._annotation = annotation

    @property
    def user(self):
        """Gets the user of this Body94.  # noqa: E501


        :return: The user of this Body94.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Body94.


        :param user: The user of this Body94.  # noqa: E501
        :type: int
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def verified(self):
        """Gets the verified of this Body94.  # noqa: E501


        :return: The verified of this Body94.  # noqa: E501
        :rtype: bool
        """
        return self._verified

    @verified.setter
    def verified(self, verified):
        """Sets the verified of this Body94.


        :param verified: The verified of this Body94.  # noqa: E501
        :type: bool
        """

        self._verified = verified

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
        if issubclass(Body94, dict):
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
        if not isinstance(other, Body94):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
