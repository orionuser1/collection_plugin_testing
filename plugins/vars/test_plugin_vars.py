# Copyright 2017 RedHat, inc
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#############################################
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = '''
    vars: host_group_vars
    version_added: "2.4"
    short_description: In charge of loading group_vars and host_vars
    description:
        - Loads YAML vars into corresponding groups/hosts in group_vars/ and host_vars/ directories.
        - Files are restricted by extension to one of .yaml, .json, .yml or no extension.
        - Hidden (starting with '.') and backup (ending with '~') files and directories are ignored.
        - Only applies to inventory sources that are existing paths.
    options:
      _valid_extensions:
        default: [".yml", ".yaml", ".json"]
        description:
          - "Check all of these extensions when looking for 'variable' files which should be YAML or JSON or vaulted versions of these."
          - 'This affects vars_files, include_vars, inventory and vars plugins among others.'
        env:
          - name: ANSIBLE_YAML_FILENAME_EXT
        ini:
          - section: yaml_valid_extensions
            key: defaults
        type: list
'''
import logging
import sys

from ansible.plugins.vars import BaseVarsPlugin

log = logging.getLogger(__name__)
FOUND = {}


class VarsModule(BaseVarsPlugin):

    def get_vars(self, loader, path, entities, cache=True):
        if not isinstance(entities, list):
            entities = [entities]

        super(VarsModule, self).get_vars(loader, path, entities)

        data = {
          'test_plugin_vars': True,
        }
        return data
