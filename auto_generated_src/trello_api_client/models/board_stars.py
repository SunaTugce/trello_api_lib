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

class BoardStars(object):
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
        'id_board': 'TrelloID',
        'pos': 'int'
    }

    attribute_map = {
        'id': 'id',
        'id_board': 'idBoard',
        'pos': 'pos'
    }

    def __init__(self, id=None, id_board=None, pos=None):  # noqa: E501
        """BoardStars - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._id_board = None
        self._pos = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if id_board is not None:
            self.id_board = id_board
        if pos is not None:
            self.pos = pos

    @property
    def id(self):
        """Gets the id of this BoardStars.  # noqa: E501


        :return: The id of this BoardStars.  # noqa: E501
        :rtype: TrelloID
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BoardStars.


        :param id: The id of this BoardStars.  # noqa: E501
        :type: TrelloID
        """

        self._id = id

    @property
    def id_board(self):
        """Gets the id_board of this BoardStars.  # noqa: E501


        :return: The id_board of this BoardStars.  # noqa: E501
        :rtype: TrelloID
        """
        return self._id_board

    @id_board.setter
    def id_board(self, id_board):
        """Sets the id_board of this BoardStars.


        :param id_board: The id_board of this BoardStars.  # noqa: E501
        :type: TrelloID
        """

        self._id_board = id_board

    @property
    def pos(self):
        """Gets the pos of this BoardStars.  # noqa: E501


        :return: The pos of this BoardStars.  # noqa: E501
        :rtype: int
        """
        return self._pos

    @pos.setter
    def pos(self, pos):
        """Sets the pos of this BoardStars.


        :param pos: The pos of this BoardStars.  # noqa: E501
        :type: int
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
        if issubclass(BoardStars, dict):
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
        if not isinstance(other, BoardStars):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
