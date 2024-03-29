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

class EnterpriseAuditLogOrganizationEnterpriseJoinRequest(object):
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
        'id_enterprise': 'TrelloID',
        'id_member': 'TrelloID',
        '_date': 'date'
    }

    attribute_map = {
        'id_enterprise': 'idEnterprise',
        'id_member': 'idMember',
        '_date': 'date'
    }

    def __init__(self, id_enterprise=None, id_member=None, _date=None):  # noqa: E501
        """EnterpriseAuditLogOrganizationEnterpriseJoinRequest - a model defined in Swagger"""  # noqa: E501
        self._id_enterprise = None
        self._id_member = None
        self.__date = None
        self.discriminator = None
        if id_enterprise is not None:
            self.id_enterprise = id_enterprise
        if id_member is not None:
            self.id_member = id_member
        if _date is not None:
            self._date = _date

    @property
    def id_enterprise(self):
        """Gets the id_enterprise of this EnterpriseAuditLogOrganizationEnterpriseJoinRequest.  # noqa: E501


        :return: The id_enterprise of this EnterpriseAuditLogOrganizationEnterpriseJoinRequest.  # noqa: E501
        :rtype: TrelloID
        """
        return self._id_enterprise

    @id_enterprise.setter
    def id_enterprise(self, id_enterprise):
        """Sets the id_enterprise of this EnterpriseAuditLogOrganizationEnterpriseJoinRequest.


        :param id_enterprise: The id_enterprise of this EnterpriseAuditLogOrganizationEnterpriseJoinRequest.  # noqa: E501
        :type: TrelloID
        """

        self._id_enterprise = id_enterprise

    @property
    def id_member(self):
        """Gets the id_member of this EnterpriseAuditLogOrganizationEnterpriseJoinRequest.  # noqa: E501


        :return: The id_member of this EnterpriseAuditLogOrganizationEnterpriseJoinRequest.  # noqa: E501
        :rtype: TrelloID
        """
        return self._id_member

    @id_member.setter
    def id_member(self, id_member):
        """Sets the id_member of this EnterpriseAuditLogOrganizationEnterpriseJoinRequest.


        :param id_member: The id_member of this EnterpriseAuditLogOrganizationEnterpriseJoinRequest.  # noqa: E501
        :type: TrelloID
        """

        self._id_member = id_member

    @property
    def _date(self):
        """Gets the _date of this EnterpriseAuditLogOrganizationEnterpriseJoinRequest.  # noqa: E501


        :return: The _date of this EnterpriseAuditLogOrganizationEnterpriseJoinRequest.  # noqa: E501
        :rtype: date
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this EnterpriseAuditLogOrganizationEnterpriseJoinRequest.


        :param _date: The _date of this EnterpriseAuditLogOrganizationEnterpriseJoinRequest.  # noqa: E501
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
        if issubclass(EnterpriseAuditLogOrganizationEnterpriseJoinRequest, dict):
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
        if not isinstance(other, EnterpriseAuditLogOrganizationEnterpriseJoinRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
