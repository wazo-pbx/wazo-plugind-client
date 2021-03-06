# -*- coding: utf-8 -*-
# Copyright 2017-2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

import json
from wazo_lib_rest_client import RESTCommand

DEFAULT_HEADERS = {'Accept': 'application/json', 'Content-Type': 'application/json'}


class MarketCommand(RESTCommand):

    resource = 'market'

    def get(self, namespace, name):
        url = '{}/{}/{}'.format(self.base_url, namespace, name)
        r = self.session.get(url, headers=DEFAULT_HEADERS)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def list(self, *args, **kwargs):
        params = dict(kwargs)
        if args:
            params['search'] = args[0]

        r = self.session.get(self.base_url, params=params, headers=DEFAULT_HEADERS)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()


class PluginCommand(RESTCommand):

    resource = 'plugins'

    def get(self, namespace, name):
        url = '{}/{}/{}'.format(self.base_url, namespace, name)
        r = self.session.get(url, headers=DEFAULT_HEADERS)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def install(self, url=None, method=None, options=None, **kwargs):
        data = {'method': method,
                'options': options or {}}

        query_string = {}
        if kwargs.get('reinstall'):
            query_string['reinstall'] = True

        if url:
            data['options']['url'] = url

        r = self.session.post(
            self.base_url,
            headers=DEFAULT_HEADERS,
            params=query_string,
            data=json.dumps(data),
        )

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def list(self):
        r = self.session.get(self.base_url, headers=DEFAULT_HEADERS)
        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def uninstall(self, namespace, name):
        url = '{base_url}/{namespace}/{name}'.format(
            base_url=self.base_url,
            namespace=namespace,
            name=name,
        )
        r = self.session.delete(url, headers=DEFAULT_HEADERS)

        if r.status_code != 204:
            self.raise_from_response(r)

        return r.json()


class ConfigCommand(RESTCommand):

    resource = 'config'

    def get(self):
        r = self.session.get(self.base_url, headers=DEFAULT_HEADERS)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()
