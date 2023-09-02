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

class CheckItem(object):
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
        'id_checklist': 'TrelloID',
        'state': 'str',
        'id': 'TrelloID',
        'name': 'str',
        'name_data': 'str',
        'pos': 'str'
    }

    attribute_map = {
        'id_checklist': 'idChecklist',
        'state': 'state',
        'id': 'id',
        'name': 'name',
        'name_data': 'nameData',
        'pos': 'pos'
    }

    def __init__(self, id_checklist=None, state=None, id=None, name=None, name_data=None, pos=None):  # noqa: E501
        """CheckItem - a model defined in Swagger"""  # noqa: E501
        self._id_checklist = None
        self._state = None
        self._id = None
        self._name = None
        self._name_data = None
        self._pos = None
        self.discriminator = None
        if id_checklist is not None:
            self.id_checklist = id_checklist
        if state is not None:
            self.state = state
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if name_data is not None:
            self.name_data = name_data
        if pos is not None:
            self.pos = pos

    @property
    def id_checklist(self):
        """Gets the id_checklist of this CheckItem.  # noqa: E501


        :return: The id_checklist of this CheckItem.  # noqa: E501
        :rtype: TrelloID
        """
        return self._id_checklist

    @id_checklist.setter
    def id_checklist(self, id_checklist):
        """Sets the id_checklist of this CheckItem.


        :param id_checklist: The id_checklist of this CheckItem.  # noqa: E501
        :type: TrelloID
        """

        self._id_checklist = id_checklist

    @property
    def state(self):
        """Gets the state of this CheckItem.  # noqa: E501


        :return: The state of this CheckItem.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this CheckItem.


        :param state: The state of this CheckItem.  # noqa: E501
        :type: str
        """
        allowed_values = ["complete", "incomplete"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def id(self):
        """Gets the id of this CheckItem.  # noqa: E501


        :return: The id of this CheckItem.  # noqa: E501
        :rtype: TrelloID
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CheckItem.


        :param id: The id of this CheckItem.  # noqa: E501
        :type: TrelloID
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this CheckItem.  # noqa: E501


        :return: The name of this CheckItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CheckItem.


        :param name: The name of this CheckItem.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def name_data(self):
        """Gets the name_data of this CheckItem.  # noqa: E501


        :return: The name_data of this CheckItem.  # noqa: E501
        :rtype: str
        """
        return self._name_data

    @name_data.setter
    def name_data(self, name_data):
        """Sets the name_data of this CheckItem.


        :param name_data: The name_data of this CheckItem.  # noqa: E501
        :type: str
        """

        self._name_data = name_data

    @property
    def pos(self):
        """Gets the pos of this CheckItem.  # noqa: E501


        :return: The pos of this CheckItem.  # noqa: E501
        :rtype: str
        """
        return self._pos

    @pos.setter
    def pos(self, pos):
        """Sets the pos of this CheckItem.


        :param pos: The pos of this CheckItem.  # noqa: E501
        :type: str
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
        if issubclass(CheckItem, dict):
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
        if not isinstance(other, CheckItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other