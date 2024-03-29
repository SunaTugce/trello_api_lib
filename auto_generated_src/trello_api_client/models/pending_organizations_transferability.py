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

class PendingOrganizationsTransferability(object):
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
        'transferrable': 'bool',
        'new_billable_members': 'list[PendingOrganizationsTransferabilityNewBillableMembers]',
        'restricted_members': 'list[PendingOrganizationsTransferabilityNewBillableMembers]'
    }

    attribute_map = {
        'transferrable': 'transferrable',
        'new_billable_members': 'newBillableMembers',
        'restricted_members': 'restrictedMembers'
    }

    def __init__(self, transferrable=None, new_billable_members=None, restricted_members=None):  # noqa: E501
        """PendingOrganizationsTransferability - a model defined in Swagger"""  # noqa: E501
        self._transferrable = None
        self._new_billable_members = None
        self._restricted_members = None
        self.discriminator = None
        if transferrable is not None:
            self.transferrable = transferrable
        if new_billable_members is not None:
            self.new_billable_members = new_billable_members
        if restricted_members is not None:
            self.restricted_members = restricted_members

    @property
    def transferrable(self):
        """Gets the transferrable of this PendingOrganizationsTransferability.  # noqa: E501


        :return: The transferrable of this PendingOrganizationsTransferability.  # noqa: E501
        :rtype: bool
        """
        return self._transferrable

    @transferrable.setter
    def transferrable(self, transferrable):
        """Sets the transferrable of this PendingOrganizationsTransferability.


        :param transferrable: The transferrable of this PendingOrganizationsTransferability.  # noqa: E501
        :type: bool
        """

        self._transferrable = transferrable

    @property
    def new_billable_members(self):
        """Gets the new_billable_members of this PendingOrganizationsTransferability.  # noqa: E501


        :return: The new_billable_members of this PendingOrganizationsTransferability.  # noqa: E501
        :rtype: list[PendingOrganizationsTransferabilityNewBillableMembers]
        """
        return self._new_billable_members

    @new_billable_members.setter
    def new_billable_members(self, new_billable_members):
        """Sets the new_billable_members of this PendingOrganizationsTransferability.


        :param new_billable_members: The new_billable_members of this PendingOrganizationsTransferability.  # noqa: E501
        :type: list[PendingOrganizationsTransferabilityNewBillableMembers]
        """

        self._new_billable_members = new_billable_members

    @property
    def restricted_members(self):
        """Gets the restricted_members of this PendingOrganizationsTransferability.  # noqa: E501


        :return: The restricted_members of this PendingOrganizationsTransferability.  # noqa: E501
        :rtype: list[PendingOrganizationsTransferabilityNewBillableMembers]
        """
        return self._restricted_members

    @restricted_members.setter
    def restricted_members(self, restricted_members):
        """Sets the restricted_members of this PendingOrganizationsTransferability.


        :param restricted_members: The restricted_members of this PendingOrganizationsTransferability.  # noqa: E501
        :type: list[PendingOrganizationsTransferabilityNewBillableMembers]
        """

        self._restricted_members = restricted_members

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
        if issubclass(PendingOrganizationsTransferability, dict):
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
        if not isinstance(other, PendingOrganizationsTransferability):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
