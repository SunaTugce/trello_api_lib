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

class IdCardCustomFieldsBody(object):
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
        'custom_field_items': 'list[CardsidCardcustomFieldsCustomFieldItems]'
    }

    attribute_map = {
        'custom_field_items': 'customFieldItems'
    }

    def __init__(self, custom_field_items=None):  # noqa: E501
        """IdCardCustomFieldsBody - a model defined in Swagger"""  # noqa: E501
        self._custom_field_items = None
        self.discriminator = None
        if custom_field_items is not None:
            self.custom_field_items = custom_field_items

    @property
    def custom_field_items(self):
        """Gets the custom_field_items of this IdCardCustomFieldsBody.  # noqa: E501

        An array of objects containing the custom field ID, key and value, and ID of list type option.  # noqa: E501

        :return: The custom_field_items of this IdCardCustomFieldsBody.  # noqa: E501
        :rtype: list[CardsidCardcustomFieldsCustomFieldItems]
        """
        return self._custom_field_items

    @custom_field_items.setter
    def custom_field_items(self, custom_field_items):
        """Sets the custom_field_items of this IdCardCustomFieldsBody.

        An array of objects containing the custom field ID, key and value, and ID of list type option.  # noqa: E501

        :param custom_field_items: The custom_field_items of this IdCardCustomFieldsBody.  # noqa: E501
        :type: list[CardsidCardcustomFieldsCustomFieldItems]
        """

        self._custom_field_items = custom_field_items

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
        if issubclass(IdCardCustomFieldsBody, dict):
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
        if not isinstance(other, IdCardCustomFieldsBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
