# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ConnectionResetSharedKey(Model):
    """ConnectionResetSharedKey.

    :param key_length: The virtual network connection reset shared key length
    :type key_length: long
    """

    _attribute_map = {
        'key_length': {'key': 'keyLength', 'type': 'long'},
    }

    def __init__(self, *, key_length: int=None, **kwargs) -> None:
        super(ConnectionResetSharedKey, self).__init__(**kwargs)
        self.key_length = key_length
