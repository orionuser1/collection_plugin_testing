# (c) 2012-2014, Michael DeHaan <michael.dehaan@gmail.com>
# (c) 2017 Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = '''
    callback: minimal
    type: stdout
    short_description: minimal Ansible screen output
    version_added: historical
    description:
        - This is the default output callback used by the ansible command (ad-hoc)
'''


from ansible.plugins.callback import CallbackBase
from ansible import constants as C

from ansible.module_utils.collection_inspect import get_dunders


class CallbackModule(CallbackBase):
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'stdout'
    CALLBACK_NAME = 'collection_inspect'

    def _command_generic_msg(self, host, result, caption):
        ''' output the result of a command run '''

        buf = "%s | %s | rc=%s >>\n" % (host, caption, result.get('rc', -1))
        buf += result.get('stdout', '')
        buf += result.get('stderr', '')
        buf += result.get('msg', '')

        return buf + "\n"

    def v2_runner_on_ok(self, result):
        self._clean_results(result._result, result._task.action)

        self._handle_warnings(result._result)

        if result._result.get('changed', False):
            color = C.COLOR_CHANGED
            state = 'CHANGED'
        else:
            color = C.COLOR_OK
            state = 'SUCCESS'

        if result._task.action in C.MODULE_NO_JSON:
            self._display.display(self._command_generic_msg(result._host.get_name(), result._result, state), color=color)
        else:
            self._display.display("%s | %s => %s" % (result._host.get_name(), state, self._dump_results(result._result, indent=4)), color=color)
        self._display.display("dunders: %s" % get_dunders(globals()))
