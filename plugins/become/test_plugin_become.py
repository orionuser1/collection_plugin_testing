# -*- coding: utf-8 -*-
# Copyright: (c) 2018, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


from ansible.plugins.become import BecomeBase


class BecomeModule(BecomeBase):

    name = 'test_become'

    # messages for detecting prompted password issues
    fail = ('Sorry, try again.',)
    missing = ('Sorry, a password is required to run sudo', 'sudo: a password is required')

    def build_become_command(self, cmd, shell):
        super(BecomeModule, self).build_become_command(cmd, shell)

        if not cmd:
            return cmd

        becomecmd = self.get_option('become_exe') or self.name

        flags = self.get_option('become_flags') or ''
        prompt = ''
        if self.get_option('become_pass'):
            self.prompt = '[sudo via ansible, key=%s] password:' % self._id
            if flags:  # this could be simplified, but kept as is for now for backwards string matching
                flags = flags.replace('-n', '')
            prompt = '-p "%s"' % (self.prompt)

        user = self.get_option('become_user') or ''
        if user:
            user = '-u %s' % (user)

        return ' '.join([becomecmd, flags, prompt, user, self._build_success_command(cmd, shell)])
