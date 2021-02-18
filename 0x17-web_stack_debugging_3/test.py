#!/usr/bin/env python3
from datadog import initialize, api

options = {
    'api_key': '0ac55746d7d75c9e9d8f6714e6e1db57',
    'app_key': '053d9a843325ed332b56fa41f18f0bf0fe97c260'
}

initialize(**options)

api.Hosts.search()
