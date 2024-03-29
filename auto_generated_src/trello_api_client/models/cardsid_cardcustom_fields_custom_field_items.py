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

class CardsidCardcustomFieldsCustomFieldItems(object):
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
        'id_custom_field': 'object',
        'value': 'CardsidCardcustomFieldsValue',
        'id_value': 'object'
    }

    attribute_map = {
        'id_custom_field': 'idCustomField',
        'value': 'value',
        'id_value': 'idValue'
    }

    def __init__(self, id_custom_field=None, value=None, id_value=None):  # noqa: E501
        """CardsidCardcustomFieldsCustomFieldItems - a model defined in Swagger"""  # noqa: E501
        self._id_custom_field = None
        self._value = None
        self._id_value = None
        self.discriminator = None
        if id_custom_field is not None:
            self.id_custom_field = id_custom_field
        if value is not None:
            self.value = value
        if id_value is not None:
            self.id_value = id_value

    @property
    def id_custom_field(self):
        """Gets the id_custom_field of this CardsidCardcustomFieldsCustomFieldItems.  # noqa: E501

        The ID of the Custom Field  # noqa: E501

        :return: The id_custom_field of this CardsidCardcustomFieldsCustomFieldItems.  # noqa: E501
        :rtype: object
        """
        return self._id_custom_field

    @id_custom_field.setter
    def id_custom_field(self, id_custom_field):
        """Sets the id_custom_field of this CardsidCardcustomFieldsCustomFieldItems.

        The ID of the Custom Field  # noqa: E501

        :param id_custom_field: The id_custom_field of this CardsidCardcustomFieldsCustomFieldItems.  # noqa: E501
        :type: object
        """

        self._id_custom_field = id_custom_field

    @property
    def value(self):
        """Gets the value of this CardsidCardcustomFieldsCustomFieldItems.  # noqa: E501


        :return: The value of this CardsidCardcustomFieldsCustomFieldItems.  # noqa: E501
        :rtype: CardsidCardcustomFieldsValue
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CardsidCardcustomFieldsCustomFieldItems.


        :param value: The value of this CardsidCardcustomFieldsCustomFieldItems.  # noqa: E501
        :type: CardsidCardcustomFieldsValue
        """

        self._value = value

    @property
    def id_value(self):
        """Gets the id_value of this CardsidCardcustomFieldsCustomFieldItems.  # noqa: E501

        The ID of the option for the list type Custom Field. This is optional if Custom Field is not list type.  # noqa: E501

        :return: The id_value of this CardsidCardcustomFieldsCustomFieldItems.  # noqa: E501
        :rtype: object
        """
        return self._id_value

    @id_value.setter
    def id_value(self, id_value):
        """Sets the id_value of this CardsidCardcustomFieldsCustomFieldItems.

        The ID of the option for the list type Custom Field. This is optional if Custom Field is not list type.  # noqa: E501

        :param id_value: The id_value of this CardsidCardcustomFieldsCustomFieldItems.  # noqa: E501
        :type: object
        """

        self._id_value = id_value

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
        if issubclass(CardsidCardcustomFieldsCustomFieldItems, dict):
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
        if not isinstance(other, CardsidCardcustomFieldsCustomFieldItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
