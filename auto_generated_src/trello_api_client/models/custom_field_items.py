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

class CustomFieldItems(object):
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
        'value': 'CustomFieldItemsValue',
        'id_custom_field': 'TrelloID',
        'id_model': 'TrelloID',
        'model_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'value': 'value',
        'id_custom_field': 'idCustomField',
        'id_model': 'idModel',
        'model_type': 'modelType'
    }

    def __init__(self, id=None, value=None, id_custom_field=None, id_model=None, model_type=None):  # noqa: E501
        """CustomFieldItems - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._value = None
        self._id_custom_field = None
        self._id_model = None
        self._model_type = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if value is not None:
            self.value = value
        if id_custom_field is not None:
            self.id_custom_field = id_custom_field
        if id_model is not None:
            self.id_model = id_model
        if model_type is not None:
            self.model_type = model_type

    @property
    def id(self):
        """Gets the id of this CustomFieldItems.  # noqa: E501


        :return: The id of this CustomFieldItems.  # noqa: E501
        :rtype: TrelloID
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CustomFieldItems.


        :param id: The id of this CustomFieldItems.  # noqa: E501
        :type: TrelloID
        """

        self._id = id

    @property
    def value(self):
        """Gets the value of this CustomFieldItems.  # noqa: E501


        :return: The value of this CustomFieldItems.  # noqa: E501
        :rtype: CustomFieldItemsValue
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CustomFieldItems.


        :param value: The value of this CustomFieldItems.  # noqa: E501
        :type: CustomFieldItemsValue
        """

        self._value = value

    @property
    def id_custom_field(self):
        """Gets the id_custom_field of this CustomFieldItems.  # noqa: E501


        :return: The id_custom_field of this CustomFieldItems.  # noqa: E501
        :rtype: TrelloID
        """
        return self._id_custom_field

    @id_custom_field.setter
    def id_custom_field(self, id_custom_field):
        """Sets the id_custom_field of this CustomFieldItems.


        :param id_custom_field: The id_custom_field of this CustomFieldItems.  # noqa: E501
        :type: TrelloID
        """

        self._id_custom_field = id_custom_field

    @property
    def id_model(self):
        """Gets the id_model of this CustomFieldItems.  # noqa: E501


        :return: The id_model of this CustomFieldItems.  # noqa: E501
        :rtype: TrelloID
        """
        return self._id_model

    @id_model.setter
    def id_model(self, id_model):
        """Sets the id_model of this CustomFieldItems.


        :param id_model: The id_model of this CustomFieldItems.  # noqa: E501
        :type: TrelloID
        """

        self._id_model = id_model

    @property
    def model_type(self):
        """Gets the model_type of this CustomFieldItems.  # noqa: E501


        :return: The model_type of this CustomFieldItems.  # noqa: E501
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """Sets the model_type of this CustomFieldItems.


        :param model_type: The model_type of this CustomFieldItems.  # noqa: E501
        :type: str
        """
        allowed_values = ["card", "board", "member"]  # noqa: E501
        if model_type not in allowed_values:
            raise ValueError(
                "Invalid value for `model_type` ({0}), must be one of {1}"  # noqa: E501
                .format(model_type, allowed_values)
            )

        self._model_type = model_type

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
        if issubclass(CustomFieldItems, dict):
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
        if not isinstance(other, CustomFieldItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
