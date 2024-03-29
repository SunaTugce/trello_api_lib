# coding: utf-8

"""
    Trello REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Token(object):
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
        'id': 'TrelloID',
        'identifier': 'str',
        'id_member': 'TrelloID',
        'date_created': 'datetime',
        'date_expires': 'datetime',
        'permissions': 'list[TokenPermission]'
    }

    attribute_map = {
        'id': 'id',
        'identifier': 'identifier',
        'id_member': 'idMember',
        'date_created': 'dateCreated',
        'date_expires': 'dateExpires',
        'permissions': 'permissions'
    }

    def __init__(self, id=None, identifier=None, id_member=None, date_created=None, date_expires=None, permissions=None):  # noqa: E501
        """Token - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._identifier = None
        self._id_member = None
        self._date_created = None
        self._date_expires = None
        self._permissions = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if identifier is not None:
            self.identifier = identifier
        if id_member is not None:
            self.id_member = id_member
        if date_created is not None:
            self.date_created = date_created
        if date_expires is not None:
            self.date_expires = date_expires
        if permissions is not None:
            self.permissions = permissions

    @property
    def id(self):
        """Gets the id of this Token.  # noqa: E501


        :return: The id of this Token.  # noqa: E501
        :rtype: TrelloID
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Token.


        :param id: The id of this Token.  # noqa: E501
        :type: TrelloID
        """

        self._id = id

    @property
    def identifier(self):
        """Gets the identifier of this Token.  # noqa: E501


        :return: The identifier of this Token.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this Token.


        :param identifier: The identifier of this Token.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def id_member(self):
        """Gets the id_member of this Token.  # noqa: E501


        :return: The id_member of this Token.  # noqa: E501
        :rtype: TrelloID
        """
        return self._id_member

    @id_member.setter
    def id_member(self, id_member):
        """Sets the id_member of this Token.


        :param id_member: The id_member of this Token.  # noqa: E501
        :type: TrelloID
        """

        self._id_member = id_member

    @property
    def date_created(self):
        """Gets the date_created of this Token.  # noqa: E501


        :return: The date_created of this Token.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this Token.


        :param date_created: The date_created of this Token.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def date_expires(self):
        """Gets the date_expires of this Token.  # noqa: E501


        :return: The date_expires of this Token.  # noqa: E501
        :rtype: datetime
        """
        return self._date_expires

    @date_expires.setter
    def date_expires(self, date_expires):
        """Sets the date_expires of this Token.


        :param date_expires: The date_expires of this Token.  # noqa: E501
        :type: datetime
        """

        self._date_expires = date_expires

    @property
    def permissions(self):
        """Gets the permissions of this Token.  # noqa: E501


        :return: The permissions of this Token.  # noqa: E501
        :rtype: list[TokenPermission]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this Token.


        :param permissions: The permissions of this Token.  # noqa: E501
        :type: list[TokenPermission]
        """

        self._permissions = permissions

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
        if issubclass(Token, dict):
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
        if not isinstance(other, Token):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
