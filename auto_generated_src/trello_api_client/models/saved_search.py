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

class SavedSearch(object):
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
        'name': 'str',
        'query': 'str',
        'pos': 'PosStringOrNumber'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'query': 'query',
        'pos': 'pos'
    }

    def __init__(self, id=None, name=None, query=None, pos=None):  # noqa: E501
        """SavedSearch - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._query = None
        self._pos = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if query is not None:
            self.query = query
        if pos is not None:
            self.pos = pos

    @property
    def id(self):
        """Gets the id of this SavedSearch.  # noqa: E501


        :return: The id of this SavedSearch.  # noqa: E501
        :rtype: TrelloID
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SavedSearch.


        :param id: The id of this SavedSearch.  # noqa: E501
        :type: TrelloID
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this SavedSearch.  # noqa: E501


        :return: The name of this SavedSearch.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SavedSearch.


        :param name: The name of this SavedSearch.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def query(self):
        """Gets the query of this SavedSearch.  # noqa: E501


        :return: The query of this SavedSearch.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this SavedSearch.


        :param query: The query of this SavedSearch.  # noqa: E501
        :type: str
        """

        self._query = query

    @property
    def pos(self):
        """Gets the pos of this SavedSearch.  # noqa: E501


        :return: The pos of this SavedSearch.  # noqa: E501
        :rtype: PosStringOrNumber
        """
        return self._pos

    @pos.setter
    def pos(self, pos):
        """Sets the pos of this SavedSearch.


        :param pos: The pos of this SavedSearch.  # noqa: E501
        :type: PosStringOrNumber
        """

        self._pos = pos

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
        if issubclass(SavedSearch, dict):
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
        if not isinstance(other, SavedSearch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
