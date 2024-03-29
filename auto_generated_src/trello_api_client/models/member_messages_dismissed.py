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

class MemberMessagesDismissed(object):
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
        'count': 'str',
        'last_dismissed': 'date',
        'id': 'TrelloID'
    }

    attribute_map = {
        'name': 'name',
        'count': 'count',
        'last_dismissed': 'lastDismissed',
        'id': '_id'
    }

    def __init__(self, name=None, count=None, last_dismissed=None, id=None):  # noqa: E501
        """MemberMessagesDismissed - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._count = None
        self._last_dismissed = None
        self._id = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if count is not None:
            self.count = count
        if last_dismissed is not None:
            self.last_dismissed = last_dismissed
        if id is not None:
            self.id = id

    @property
    def name(self):
        """Gets the name of this MemberMessagesDismissed.  # noqa: E501


        :return: The name of this MemberMessagesDismissed.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MemberMessagesDismissed.


        :param name: The name of this MemberMessagesDismissed.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def count(self):
        """Gets the count of this MemberMessagesDismissed.  # noqa: E501


        :return: The count of this MemberMessagesDismissed.  # noqa: E501
        :rtype: str
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this MemberMessagesDismissed.


        :param count: The count of this MemberMessagesDismissed.  # noqa: E501
        :type: str
        """

        self._count = count

    @property
    def last_dismissed(self):
        """Gets the last_dismissed of this MemberMessagesDismissed.  # noqa: E501


        :return: The last_dismissed of this MemberMessagesDismissed.  # noqa: E501
        :rtype: date
        """
        return self._last_dismissed

    @last_dismissed.setter
    def last_dismissed(self, last_dismissed):
        """Sets the last_dismissed of this MemberMessagesDismissed.


        :param last_dismissed: The last_dismissed of this MemberMessagesDismissed.  # noqa: E501
        :type: date
        """

        self._last_dismissed = last_dismissed

    @property
    def id(self):
        """Gets the id of this MemberMessagesDismissed.  # noqa: E501


        :return: The id of this MemberMessagesDismissed.  # noqa: E501
        :rtype: TrelloID
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MemberMessagesDismissed.


        :param id: The id of this MemberMessagesDismissed.  # noqa: E501
        :type: TrelloID
        """

        self._id = id

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
        if issubclass(MemberMessagesDismissed, dict):
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
        if not isinstance(other, MemberMessagesDismissed):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
