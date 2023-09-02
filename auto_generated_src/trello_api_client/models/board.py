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

class Board(object):
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
        'desc': 'str',
        'desc_data': 'str',
        'closed': 'bool',
        'id_member_creator': 'TrelloID',
        'id_organization': 'TrelloID',
        'pinned': 'bool',
        'url': 'str',
        'short_url': 'str',
        'prefs': 'Prefs',
        'label_names': 'BoardLabelNames',
        'limits': 'Limits',
        'starred': 'bool',
        'memberships': 'str',
        'short_link': 'str',
        'subscribed': 'bool',
        'power_ups': 'str',
        'date_last_activity': 'date',
        'date_last_view': 'date',
        'id_tags': 'str',
        'date_plugin_disable': 'date',
        'creation_method': 'str',
        'ix_update': 'int',
        'template_gallery': 'str',
        'enterprise_owned': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'desc': 'desc',
        'desc_data': 'descData',
        'closed': 'closed',
        'id_member_creator': 'idMemberCreator',
        'id_organization': 'idOrganization',
        'pinned': 'pinned',
        'url': 'url',
        'short_url': 'shortUrl',
        'prefs': 'prefs',
        'label_names': 'labelNames',
        'limits': 'limits',
        'starred': 'starred',
        'memberships': 'memberships',
        'short_link': 'shortLink',
        'subscribed': 'subscribed',
        'power_ups': 'powerUps',
        'date_last_activity': 'dateLastActivity',
        'date_last_view': 'dateLastView',
        'id_tags': 'idTags',
        'date_plugin_disable': 'datePluginDisable',
        'creation_method': 'creationMethod',
        'ix_update': 'ixUpdate',
        'template_gallery': 'templateGallery',
        'enterprise_owned': 'enterpriseOwned'
    }

    def __init__(self, id=None, name=None, desc=None, desc_data=None, closed=None, id_member_creator=None, id_organization=None, pinned=None, url=None, short_url=None, prefs=None, label_names=None, limits=None, starred=None, memberships=None, short_link=None, subscribed=None, power_ups=None, date_last_activity=None, date_last_view=None, id_tags=None, date_plugin_disable=None, creation_method=None, ix_update=None, template_gallery=None, enterprise_owned=None):  # noqa: E501
        """Board - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._desc = None
        self._desc_data = None
        self._closed = None
        self._id_member_creator = None
        self._id_organization = None
        self._pinned = None
        self._url = None
        self._short_url = None
        self._prefs = None
        self._label_names = None
        self._limits = None
        self._starred = None
        self._memberships = None
        self._short_link = None
        self._subscribed = None
        self._power_ups = None
        self._date_last_activity = None
        self._date_last_view = None
        self._id_tags = None
        self._date_plugin_disable = None
        self._creation_method = None
        self._ix_update = None
        self._template_gallery = None
        self._enterprise_owned = None
        self.discriminator = None
        self.id = id
        if name is not None:
            self.name = name
        if desc is not None:
            self.desc = desc
        if desc_data is not None:
            self.desc_data = desc_data
        if closed is not None:
            self.closed = closed
        if id_member_creator is not None:
            self.id_member_creator = id_member_creator
        if id_organization is not None:
            self.id_organization = id_organization
        if pinned is not None:
            self.pinned = pinned
        if url is not None:
            self.url = url
        if short_url is not None:
            self.short_url = short_url
        if prefs is not None:
            self.prefs = prefs
        if label_names is not None:
            self.label_names = label_names
        if limits is not None:
            self.limits = limits
        if starred is not None:
            self.starred = starred
        if memberships is not None:
            self.memberships = memberships
        if short_link is not None:
            self.short_link = short_link
        if subscribed is not None:
            self.subscribed = subscribed
        if power_ups is not None:
            self.power_ups = power_ups
        if date_last_activity is not None:
            self.date_last_activity = date_last_activity
        if date_last_view is not None:
            self.date_last_view = date_last_view
        if id_tags is not None:
            self.id_tags = id_tags
        if date_plugin_disable is not None:
            self.date_plugin_disable = date_plugin_disable
        if creation_method is not None:
            self.creation_method = creation_method
        if ix_update is not None:
            self.ix_update = ix_update
        if template_gallery is not None:
            self.template_gallery = template_gallery
        if enterprise_owned is not None:
            self.enterprise_owned = enterprise_owned

    @property
    def id(self):
        """Gets the id of this Board.  # noqa: E501


        :return: The id of this Board.  # noqa: E501
        :rtype: TrelloID
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Board.


        :param id: The id of this Board.  # noqa: E501
        :type: TrelloID
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Board.  # noqa: E501

        The name of the board.  # noqa: E501

        :return: The name of this Board.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Board.

        The name of the board.  # noqa: E501

        :param name: The name of this Board.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def desc(self):
        """Gets the desc of this Board.  # noqa: E501


        :return: The desc of this Board.  # noqa: E501
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this Board.


        :param desc: The desc of this Board.  # noqa: E501
        :type: str
        """

        self._desc = desc

    @property
    def desc_data(self):
        """Gets the desc_data of this Board.  # noqa: E501


        :return: The desc_data of this Board.  # noqa: E501
        :rtype: str
        """
        return self._desc_data

    @desc_data.setter
    def desc_data(self, desc_data):
        """Sets the desc_data of this Board.


        :param desc_data: The desc_data of this Board.  # noqa: E501
        :type: str
        """

        self._desc_data = desc_data

    @property
    def closed(self):
        """Gets the closed of this Board.  # noqa: E501


        :return: The closed of this Board.  # noqa: E501
        :rtype: bool
        """
        return self._closed

    @closed.setter
    def closed(self, closed):
        """Sets the closed of this Board.


        :param closed: The closed of this Board.  # noqa: E501
        :type: bool
        """

        self._closed = closed

    @property
    def id_member_creator(self):
        """Gets the id_member_creator of this Board.  # noqa: E501


        :return: The id_member_creator of this Board.  # noqa: E501
        :rtype: TrelloID
        """
        return self._id_member_creator

    @id_member_creator.setter
    def id_member_creator(self, id_member_creator):
        """Sets the id_member_creator of this Board.


        :param id_member_creator: The id_member_creator of this Board.  # noqa: E501
        :type: TrelloID
        """

        self._id_member_creator = id_member_creator

    @property
    def id_organization(self):
        """Gets the id_organization of this Board.  # noqa: E501


        :return: The id_organization of this Board.  # noqa: E501
        :rtype: TrelloID
        """
        return self._id_organization

    @id_organization.setter
    def id_organization(self, id_organization):
        """Sets the id_organization of this Board.


        :param id_organization: The id_organization of this Board.  # noqa: E501
        :type: TrelloID
        """

        self._id_organization = id_organization

    @property
    def pinned(self):
        """Gets the pinned of this Board.  # noqa: E501


        :return: The pinned of this Board.  # noqa: E501
        :rtype: bool
        """
        return self._pinned

    @pinned.setter
    def pinned(self, pinned):
        """Sets the pinned of this Board.


        :param pinned: The pinned of this Board.  # noqa: E501
        :type: bool
        """

        self._pinned = pinned

    @property
    def url(self):
        """Gets the url of this Board.  # noqa: E501


        :return: The url of this Board.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Board.


        :param url: The url of this Board.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def short_url(self):
        """Gets the short_url of this Board.  # noqa: E501


        :return: The short_url of this Board.  # noqa: E501
        :rtype: str
        """
        return self._short_url

    @short_url.setter
    def short_url(self, short_url):
        """Sets the short_url of this Board.


        :param short_url: The short_url of this Board.  # noqa: E501
        :type: str
        """

        self._short_url = short_url

    @property
    def prefs(self):
        """Gets the prefs of this Board.  # noqa: E501


        :return: The prefs of this Board.  # noqa: E501
        :rtype: Prefs
        """
        return self._prefs

    @prefs.setter
    def prefs(self, prefs):
        """Sets the prefs of this Board.


        :param prefs: The prefs of this Board.  # noqa: E501
        :type: Prefs
        """

        self._prefs = prefs

    @property
    def label_names(self):
        """Gets the label_names of this Board.  # noqa: E501


        :return: The label_names of this Board.  # noqa: E501
        :rtype: BoardLabelNames
        """
        return self._label_names

    @label_names.setter
    def label_names(self, label_names):
        """Sets the label_names of this Board.


        :param label_names: The label_names of this Board.  # noqa: E501
        :type: BoardLabelNames
        """

        self._label_names = label_names

    @property
    def limits(self):
        """Gets the limits of this Board.  # noqa: E501


        :return: The limits of this Board.  # noqa: E501
        :rtype: Limits
        """
        return self._limits

    @limits.setter
    def limits(self, limits):
        """Sets the limits of this Board.


        :param limits: The limits of this Board.  # noqa: E501
        :type: Limits
        """

        self._limits = limits

    @property
    def starred(self):
        """Gets the starred of this Board.  # noqa: E501


        :return: The starred of this Board.  # noqa: E501
        :rtype: bool
        """
        return self._starred

    @starred.setter
    def starred(self, starred):
        """Sets the starred of this Board.


        :param starred: The starred of this Board.  # noqa: E501
        :type: bool
        """

        self._starred = starred

    @property
    def memberships(self):
        """Gets the memberships of this Board.  # noqa: E501


        :return: The memberships of this Board.  # noqa: E501
        :rtype: str
        """
        return self._memberships

    @memberships.setter
    def memberships(self, memberships):
        """Sets the memberships of this Board.


        :param memberships: The memberships of this Board.  # noqa: E501
        :type: str
        """

        self._memberships = memberships

    @property
    def short_link(self):
        """Gets the short_link of this Board.  # noqa: E501


        :return: The short_link of this Board.  # noqa: E501
        :rtype: str
        """
        return self._short_link

    @short_link.setter
    def short_link(self, short_link):
        """Sets the short_link of this Board.


        :param short_link: The short_link of this Board.  # noqa: E501
        :type: str
        """

        self._short_link = short_link

    @property
    def subscribed(self):
        """Gets the subscribed of this Board.  # noqa: E501


        :return: The subscribed of this Board.  # noqa: E501
        :rtype: bool
        """
        return self._subscribed

    @subscribed.setter
    def subscribed(self, subscribed):
        """Sets the subscribed of this Board.


        :param subscribed: The subscribed of this Board.  # noqa: E501
        :type: bool
        """

        self._subscribed = subscribed

    @property
    def power_ups(self):
        """Gets the power_ups of this Board.  # noqa: E501


        :return: The power_ups of this Board.  # noqa: E501
        :rtype: str
        """
        return self._power_ups

    @power_ups.setter
    def power_ups(self, power_ups):
        """Sets the power_ups of this Board.


        :param power_ups: The power_ups of this Board.  # noqa: E501
        :type: str
        """

        self._power_ups = power_ups

    @property
    def date_last_activity(self):
        """Gets the date_last_activity of this Board.  # noqa: E501


        :return: The date_last_activity of this Board.  # noqa: E501
        :rtype: date
        """
        return self._date_last_activity

    @date_last_activity.setter
    def date_last_activity(self, date_last_activity):
        """Sets the date_last_activity of this Board.


        :param date_last_activity: The date_last_activity of this Board.  # noqa: E501
        :type: date
        """

        self._date_last_activity = date_last_activity

    @property
    def date_last_view(self):
        """Gets the date_last_view of this Board.  # noqa: E501


        :return: The date_last_view of this Board.  # noqa: E501
        :rtype: date
        """
        return self._date_last_view

    @date_last_view.setter
    def date_last_view(self, date_last_view):
        """Sets the date_last_view of this Board.


        :param date_last_view: The date_last_view of this Board.  # noqa: E501
        :type: date
        """

        self._date_last_view = date_last_view

    @property
    def id_tags(self):
        """Gets the id_tags of this Board.  # noqa: E501


        :return: The id_tags of this Board.  # noqa: E501
        :rtype: str
        """
        return self._id_tags

    @id_tags.setter
    def id_tags(self, id_tags):
        """Sets the id_tags of this Board.


        :param id_tags: The id_tags of this Board.  # noqa: E501
        :type: str
        """

        self._id_tags = id_tags

    @property
    def date_plugin_disable(self):
        """Gets the date_plugin_disable of this Board.  # noqa: E501


        :return: The date_plugin_disable of this Board.  # noqa: E501
        :rtype: date
        """
        return self._date_plugin_disable

    @date_plugin_disable.setter
    def date_plugin_disable(self, date_plugin_disable):
        """Sets the date_plugin_disable of this Board.


        :param date_plugin_disable: The date_plugin_disable of this Board.  # noqa: E501
        :type: date
        """

        self._date_plugin_disable = date_plugin_disable

    @property
    def creation_method(self):
        """Gets the creation_method of this Board.  # noqa: E501


        :return: The creation_method of this Board.  # noqa: E501
        :rtype: str
        """
        return self._creation_method

    @creation_method.setter
    def creation_method(self, creation_method):
        """Sets the creation_method of this Board.


        :param creation_method: The creation_method of this Board.  # noqa: E501
        :type: str
        """

        self._creation_method = creation_method

    @property
    def ix_update(self):
        """Gets the ix_update of this Board.  # noqa: E501


        :return: The ix_update of this Board.  # noqa: E501
        :rtype: int
        """
        return self._ix_update

    @ix_update.setter
    def ix_update(self, ix_update):
        """Sets the ix_update of this Board.


        :param ix_update: The ix_update of this Board.  # noqa: E501
        :type: int
        """

        self._ix_update = ix_update

    @property
    def template_gallery(self):
        """Gets the template_gallery of this Board.  # noqa: E501


        :return: The template_gallery of this Board.  # noqa: E501
        :rtype: str
        """
        return self._template_gallery

    @template_gallery.setter
    def template_gallery(self, template_gallery):
        """Sets the template_gallery of this Board.


        :param template_gallery: The template_gallery of this Board.  # noqa: E501
        :type: str
        """

        self._template_gallery = template_gallery

    @property
    def enterprise_owned(self):
        """Gets the enterprise_owned of this Board.  # noqa: E501


        :return: The enterprise_owned of this Board.  # noqa: E501
        :rtype: bool
        """
        return self._enterprise_owned

    @enterprise_owned.setter
    def enterprise_owned(self, enterprise_owned):
        """Sets the enterprise_owned of this Board.


        :param enterprise_owned: The enterprise_owned of this Board.  # noqa: E501
        :type: bool
        """

        self._enterprise_owned = enterprise_owned

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
        if issubclass(Board, dict):
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
        if not isinstance(other, Board):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
