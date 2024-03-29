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

class MemberMarketingOptIn(object):
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
        'opted_in': 'bool',
        '_date': 'date'
    }

    attribute_map = {
        'opted_in': 'optedIn',
        '_date': 'date'
    }

    def __init__(self, opted_in=None, _date=None):  # noqa: E501
        """MemberMarketingOptIn - a model defined in Swagger"""  # noqa: E501
        self._opted_in = None
        self.__date = None
        self.discriminator = None
        if opted_in is not None:
            self.opted_in = opted_in
        if _date is not None:
            self._date = _date

    @property
    def opted_in(self):
        """Gets the opted_in of this MemberMarketingOptIn.  # noqa: E501


        :return: The opted_in of this MemberMarketingOptIn.  # noqa: E501
        :rtype: bool
        """
        return self._opted_in

    @opted_in.setter
    def opted_in(self, opted_in):
        """Sets the opted_in of this MemberMarketingOptIn.


        :param opted_in: The opted_in of this MemberMarketingOptIn.  # noqa: E501
        :type: bool
        """

        self._opted_in = opted_in

    @property
    def _date(self):
        """Gets the _date of this MemberMarketingOptIn.  # noqa: E501


        :return: The _date of this MemberMarketingOptIn.  # noqa: E501
        :rtype: date
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this MemberMarketingOptIn.


        :param _date: The _date of this MemberMarketingOptIn.  # noqa: E501
        :type: date
        """

        self.__date = _date

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
        if issubclass(MemberMarketingOptIn, dict):
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
        if not isinstance(other, MemberMarketingOptIn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
