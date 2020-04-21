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


class Body38(object):
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
        'path': 'str',
        'location': 'str',
        'description': 'str',
        'images': 'list[int]',
        'product_set': 'list[int]',
        'main_annotation_type': 'int',
        'set_tags': 'list[int]',
        'team': 'int',
        'creator': 'int'
    }

    attribute_map = {
        'name': 'name',
        'path': 'path',
        'location': 'location',
        'description': 'description',
        'images': 'images',
        'product_set': 'product_set',
        'main_annotation_type': 'main_annotation_type',
        'set_tags': 'set_tags',
        'team': 'team',
        'creator': 'creator'
    }

    def __init__(self, name=None, path=None, location=None, description=None, images=None, product_set=None, main_annotation_type=None, set_tags=None, team=None, creator=None):  # noqa: E501
        """Body38 - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._path = None
        self._location = None
        self._description = None
        self._images = None
        self._product_set = None
        self._main_annotation_type = None
        self._set_tags = None
        self._team = None
        self._creator = None
        self.discriminator = None
        self.name = name
        if path is not None:
            self.path = path
        if location is not None:
            self.location = location
        if description is not None:
            self.description = description
        self.images = images
        self.product_set = product_set
        if main_annotation_type is not None:
            self.main_annotation_type = main_annotation_type
        self.set_tags = set_tags
        self.team = team
        if creator is not None:
            self.creator = creator

    @property
    def name(self):
        """Gets the name of this Body38.  # noqa: E501


        :return: The name of this Body38.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Body38.


        :param name: The name of this Body38.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def path(self):
        """Gets the path of this Body38.  # noqa: E501


        :return: The path of this Body38.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this Body38.


        :param path: The path of this Body38.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def location(self):
        """Gets the location of this Body38.  # noqa: E501


        :return: The location of this Body38.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Body38.


        :param location: The location of this Body38.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def description(self):
        """Gets the description of this Body38.  # noqa: E501


        :return: The description of this Body38.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Body38.


        :param description: The description of this Body38.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def images(self):
        """Gets the images of this Body38.  # noqa: E501


        :return: The images of this Body38.  # noqa: E501
        :rtype: list[int]
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this Body38.


        :param images: The images of this Body38.  # noqa: E501
        :type: list[int]
        """
        if images is None:
            raise ValueError("Invalid value for `images`, must not be `None`")  # noqa: E501

        self._images = images

    @property
    def product_set(self):
        """Gets the product_set of this Body38.  # noqa: E501


        :return: The product_set of this Body38.  # noqa: E501
        :rtype: list[int]
        """
        return self._product_set

    @product_set.setter
    def product_set(self, product_set):
        """Sets the product_set of this Body38.


        :param product_set: The product_set of this Body38.  # noqa: E501
        :type: list[int]
        """
        if product_set is None:
            raise ValueError("Invalid value for `product_set`, must not be `None`")  # noqa: E501

        self._product_set = product_set

    @property
    def main_annotation_type(self):
        """Gets the main_annotation_type of this Body38.  # noqa: E501


        :return: The main_annotation_type of this Body38.  # noqa: E501
        :rtype: int
        """
        return self._main_annotation_type

    @main_annotation_type.setter
    def main_annotation_type(self, main_annotation_type):
        """Sets the main_annotation_type of this Body38.


        :param main_annotation_type: The main_annotation_type of this Body38.  # noqa: E501
        :type: int
        """

        self._main_annotation_type = main_annotation_type

    @property
    def set_tags(self):
        """Gets the set_tags of this Body38.  # noqa: E501


        :return: The set_tags of this Body38.  # noqa: E501
        :rtype: list[int]
        """
        return self._set_tags

    @set_tags.setter
    def set_tags(self, set_tags):
        """Sets the set_tags of this Body38.


        :param set_tags: The set_tags of this Body38.  # noqa: E501
        :type: list[int]
        """
        if set_tags is None:
            raise ValueError("Invalid value for `set_tags`, must not be `None`")  # noqa: E501

        self._set_tags = set_tags

    @property
    def team(self):
        """Gets the team of this Body38.  # noqa: E501


        :return: The team of this Body38.  # noqa: E501
        :rtype: int
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this Body38.


        :param team: The team of this Body38.  # noqa: E501
        :type: int
        """
        if team is None:
            raise ValueError("Invalid value for `team`, must not be `None`")  # noqa: E501

        self._team = team

    @property
    def creator(self):
        """Gets the creator of this Body38.  # noqa: E501


        :return: The creator of this Body38.  # noqa: E501
        :rtype: int
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this Body38.


        :param creator: The creator of this Body38.  # noqa: E501
        :type: int
        """

        self._creator = creator

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
        if issubclass(Body38, dict):
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
        if not isinstance(other, Body38):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
