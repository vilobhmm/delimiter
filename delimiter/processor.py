# -*- coding: utf-8 -*-

#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import abc

import six


@six.add_metaclass(abc.ABCMeta)
class Processor(object):
    """The abstraction that all limit processors derive from."""

    @abc.abstractmethod
    def create(self, limit):
        """Given some limit, turn it into a **internal** details dict."""

    @abc.abstractmethod
    def decode(self, details):
        """Turn a **internal** details dict into a user-viewable one."""

    @abc.abstractmethod
    def update(self, details, limit):
        """Given **internal** details dict update it with the given limit."""

    @abc.abstractmethod
    def process(self, details, amount):
        """Given **internal** details dict process the amount given (or die).

        Updates (and returns) the internal details dict if
        successful (otherwise raises some useful exception).
        """
