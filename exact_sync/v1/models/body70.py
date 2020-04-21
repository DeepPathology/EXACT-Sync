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


class Body70(object):
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
        'annotation_type': 'int',
        'vector': 'object',
        'image': 'int',
        'last_editor': 'int',
        'user': 'int',
        'deleted': 'bool',
        'description': 'str',
        'unique_identifier': 'str',
        'uploaded_media_files': 'list[int]',
        'meta_data': 'object'
    }

    attribute_map = {
        'annotation_type': 'annotation_type',
        'vector': 'vector',
        'image': 'image',
        'last_editor': 'last_editor',
        'user': 'user',
        'deleted': 'deleted',
        'description': 'description',
        'unique_identifier': 'unique_identifier',
        'uploaded_media_files': 'uploaded_media_files',
        'meta_data': 'meta_data'
    }

    def __init__(self, annotation_type=None, vector=None, image=None, last_editor=None, user=None, deleted=None, description=None, unique_identifier=None, uploaded_media_files=None, meta_data=None):  # noqa: E501
        """Body70 - a model defined in Swagger"""  # noqa: E501
        self._annotation_type = None
        self._vector = None
        self._image = None
        self._last_editor = None
        self._user = None
        self._deleted = None
        self._description = None
        self._unique_identifier = None
        self._uploaded_media_files = None
        self._meta_data = None
        self.discriminator = None
        if annotation_type is not None:
            self.annotation_type = annotation_type
        if vector is not None:
            self.vector = vector
        if image is not None:
            self.image = image
        if last_editor is not None:
            self.last_editor = last_editor
        if user is not None:
            self.user = user
        if deleted is not None:
            self.deleted = deleted
        if description is not None:
            self.description = description
        if unique_identifier is not None:
            self.unique_identifier = unique_identifier
        if uploaded_media_files is not None:
            self.uploaded_media_files = uploaded_media_files
        if meta_data is not None:
            self.meta_data = meta_data

    @property
    def annotation_type(self):
        """Gets the annotation_type of this Body70.  # noqa: E501


        :return: The annotation_type of this Body70.  # noqa: E501
        :rtype: int
        """
        return self._annotation_type

    @annotation_type.setter
    def annotation_type(self, annotation_type):
        """Sets the annotation_type of this Body70.


        :param annotation_type: The annotation_type of this Body70.  # noqa: E501
        :type: int
        """

        self._annotation_type = annotation_type

    @property
    def vector(self):
        """Gets the vector of this Body70.  # noqa: E501


        :return: The vector of this Body70.  # noqa: E501
        :rtype: object
        """
        return self._vector

    @vector.setter
    def vector(self, vector):
        """Sets the vector of this Body70.


        :param vector: The vector of this Body70.  # noqa: E501
        :type: object
        """

        self._vector = vector

    @property
    def image(self):
        """Gets the image of this Body70.  # noqa: E501


        :return: The image of this Body70.  # noqa: E501
        :rtype: int
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this Body70.


        :param image: The image of this Body70.  # noqa: E501
        :type: int
        """

        self._image = image

    @property
    def last_editor(self):
        """Gets the last_editor of this Body70.  # noqa: E501


        :return: The last_editor of this Body70.  # noqa: E501
        :rtype: int
        """
        return self._last_editor

    @last_editor.setter
    def last_editor(self, last_editor):
        """Sets the last_editor of this Body70.


        :param last_editor: The last_editor of this Body70.  # noqa: E501
        :type: int
        """

        self._last_editor = last_editor

    @property
    def user(self):
        """Gets the user of this Body70.  # noqa: E501


        :return: The user of this Body70.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Body70.


        :param user: The user of this Body70.  # noqa: E501
        :type: int
        """

        self._user = user

    @property
    def deleted(self):
        """Gets the deleted of this Body70.  # noqa: E501


        :return: The deleted of this Body70.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this Body70.


        :param deleted: The deleted of this Body70.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def description(self):
        """Gets the description of this Body70.  # noqa: E501


        :return: The description of this Body70.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Body70.


        :param description: The description of this Body70.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def unique_identifier(self):
        """Gets the unique_identifier of this Body70.  # noqa: E501


        :return: The unique_identifier of this Body70.  # noqa: E501
        :rtype: str
        """
        return self._unique_identifier

    @unique_identifier.setter
    def unique_identifier(self, unique_identifier):
        """Sets the unique_identifier of this Body70.


        :param unique_identifier: The unique_identifier of this Body70.  # noqa: E501
        :type: str
        """

        self._unique_identifier = unique_identifier

    @property
    def uploaded_media_files(self):
        """Gets the uploaded_media_files of this Body70.  # noqa: E501


        :return: The uploaded_media_files of this Body70.  # noqa: E501
        :rtype: list[int]
        """
        return self._uploaded_media_files

    @uploaded_media_files.setter
    def uploaded_media_files(self, uploaded_media_files):
        """Sets the uploaded_media_files of this Body70.


        :param uploaded_media_files: The uploaded_media_files of this Body70.  # noqa: E501
        :type: list[int]
        """

        self._uploaded_media_files = uploaded_media_files

    @property
    def meta_data(self):
        """Gets the meta_data of this Body70.  # noqa: E501


        :return: The meta_data of this Body70.  # noqa: E501
        :rtype: object
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        """Sets the meta_data of this Body70.


        :param meta_data: The meta_data of this Body70.  # noqa: E501
        :type: object
        """

        self._meta_data = meta_data

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
        if issubclass(Body70, dict):
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
        if not isinstance(other, Body70):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
