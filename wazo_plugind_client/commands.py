# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

import json
from xivo_lib_rest_client import RESTCommand


class PluginCommand(RESTCommand):

    resource = 'plugins'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def install(self, url, method):
        data = {'url': url, 'method': method}
        r = self.session.post(self.base_url, headers=self.headers, data=json.dumps(data))

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()
