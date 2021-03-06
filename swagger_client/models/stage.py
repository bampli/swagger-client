# coding: utf-8

"""
    bampli-api

    The API for the Business Amplifier project.  # noqa: E501

    OpenAPI spec version: 1.0.0-oas3
    Contact: josemotta@bampli.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Stage(object):
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
        'stage_id': 'str',
        'name': 'str',
        'active': 'bool',
        'cyclo_id': 'str'
    }

    attribute_map = {
        'stage_id': 'stage_id',
        'name': 'name',
        'active': 'active',
        'cyclo_id': 'cyclo_id'
    }

    def __init__(self, stage_id=None, name=None, active=True, cyclo_id=None):  # noqa: E501
        """Stage - a model defined in Swagger"""  # noqa: E501
        self._stage_id = None
        self._name = None
        self._active = None
        self._cyclo_id = None
        self.discriminator = None
        self.stage_id = stage_id
        self.name = name
        if active is not None:
            self.active = active
        self.cyclo_id = cyclo_id

    @property
    def stage_id(self):
        """Gets the stage_id of this Stage.  # noqa: E501

        Auto-generated primary key field  # noqa: E501

        :return: The stage_id of this Stage.  # noqa: E501
        :rtype: str
        """
        return self._stage_id

    @stage_id.setter
    def stage_id(self, stage_id):
        """Sets the stage_id of this Stage.

        Auto-generated primary key field  # noqa: E501

        :param stage_id: The stage_id of this Stage.  # noqa: E501
        :type: str
        """
        if stage_id is None:
            raise ValueError("Invalid value for `stage_id`, must not be `None`")  # noqa: E501

        self._stage_id = stage_id

    @property
    def name(self):
        """Gets the name of this Stage.  # noqa: E501


        :return: The name of this Stage.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Stage.


        :param name: The name of this Stage.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def active(self):
        """Gets the active of this Stage.  # noqa: E501


        :return: The active of this Stage.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this Stage.


        :param active: The active of this Stage.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def cyclo_id(self):
        """Gets the cyclo_id of this Stage.  # noqa: E501

        This property is a reference to a Cyclo  # noqa: E501

        :return: The cyclo_id of this Stage.  # noqa: E501
        :rtype: str
        """
        return self._cyclo_id

    @cyclo_id.setter
    def cyclo_id(self, cyclo_id):
        """Sets the cyclo_id of this Stage.

        This property is a reference to a Cyclo  # noqa: E501

        :param cyclo_id: The cyclo_id of this Stage.  # noqa: E501
        :type: str
        """
        if cyclo_id is None:
            raise ValueError("Invalid value for `cyclo_id`, must not be `None`")  # noqa: E501

        self._cyclo_id = cyclo_id

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
        if issubclass(Stage, dict):
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
        if not isinstance(other, Stage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
