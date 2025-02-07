# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PluginResultEntry(object):
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
        'id': 'int',
        'pluginresult': 'int',
        'created_time': 'datetime',
        'name': 'str',
        'visible': 'bool',
        'default_threshold' : 'float',
        'annotation_results': 'list[int]',
        'bitmap_results': 'list[int]'
    }

    attribute_map = {
        'id': 'id',
        'pluginresult': 'pluginresult',
        'created_time': 'created_time',
        'name': 'name',
        'visible': 'visible',
        'default_threshold' : 'default_threshold',
        'annotation_results': 'annotation_results',
        'bitmap_results': 'bitmap_results'
    }

    def __init__(self, id=None, pluginresult=None, created_time=None, name=None, default_threshold=None, visible=None, annotation_results=None, bitmap_results=None):  # noqa: E501
        """PluginResultEntry - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._pluginresult = None
        self._created_time = None
        self._name = None
        self._visible = None
        self._annotation_results = None
        self._bitmap_results = None
        self.discriminator = None
        self.default_threshold = None
        if default_threshold is not None:
            self.default_threshold = default_threshold
        if id is not None:
            self.id = id
        self.pluginresult = pluginresult
        if created_time is not None:
            self.created_time = created_time
        self.name = name
        if visible is not None:
            self.visible = visible
        self.annotation_results = annotation_results
        self.bitmap_results = bitmap_results

    @property
    def id(self):
        """Gets the id of this PluginResultEntry.  # noqa: E501


        :return: The id of this PluginResultEntry.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PluginResultEntry.


        :param id: The id of this PluginResultEntry.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def pluginresult(self):
        """Gets the pluginresult of this PluginResultEntry.  # noqa: E501


        :return: The pluginresult of this PluginResultEntry.  # noqa: E501
        :rtype: int
        """
        return self._pluginresult

    @pluginresult.setter
    def pluginresult(self, pluginresult):
        """Sets the pluginresult of this PluginResultEntry.


        :param pluginresult: The pluginresult of this PluginResultEntry.  # noqa: E501
        :type: int
        """
        if pluginresult is None:
            raise ValueError("Invalid value for `pluginresult`, must not be `None`")  # noqa: E501

        self._pluginresult = pluginresult

    @property
    def created_time(self):
        """Gets the created_time of this PluginResultEntry.  # noqa: E501


        :return: The created_time of this PluginResultEntry.  # noqa: E501
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this PluginResultEntry.


        :param created_time: The created_time of this PluginResultEntry.  # noqa: E501
        :type: datetime
        """

        self._created_time = created_time

    @property
    def name(self):
        """Gets the name of this PluginResultEntry.  # noqa: E501


        :return: The name of this PluginResultEntry.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PluginResultEntry.


        :param name: The name of this PluginResultEntry.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def visible(self):
        """Gets the visible of this PluginResultEntry.  # noqa: E501


        :return: The visible of this PluginResultEntry.  # noqa: E501
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        """Sets the visible of this PluginResultEntry.


        :param visible: The visible of this PluginResultEntry.  # noqa: E501
        :type: bool
        """

        self._visible = visible

    @property
    def annotation_results(self):
        """Gets the annotation_results of this PluginResultEntry.  # noqa: E501


        :return: The annotation_results of this PluginResultEntry.  # noqa: E501
        :rtype: list[int]
        """
        return self._annotation_results

    @annotation_results.setter
    def annotation_results(self, annotation_results):
        """Sets the annotation_results of this PluginResultEntry.


        :param annotation_results: The annotation_results of this PluginResultEntry.  # noqa: E501
        :type: list[int]
        """
        if annotation_results is None:
            raise ValueError("Invalid value for `annotation_results`, must not be `None`")  # noqa: E501

        self._annotation_results = annotation_results

    @property
    def bitmap_results(self):
        """Gets the bitmap_results of this PluginResultEntry.  # noqa: E501


        :return: The bitmap_results of this PluginResultEntry.  # noqa: E501
        :rtype: list[int]
        """
        return self._bitmap_results

    @bitmap_results.setter
    def bitmap_results(self, bitmap_results):
        """Sets the bitmap_results of this PluginResultEntry.


        :param bitmap_results: The bitmap_results of this PluginResultEntry.  # noqa: E501
        :type: list[int]
        """
        if bitmap_results is None:
            raise ValueError("Invalid value for `bitmap_results`, must not be `None`")  # noqa: E501

        self._bitmap_results = bitmap_results

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
        if issubclass(PluginResultEntry, dict):
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
        if not isinstance(other, PluginResultEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
