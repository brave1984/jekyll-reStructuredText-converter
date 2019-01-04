#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from docutils.core import publish_parts

settings = {
    'syntax_highlight': 'short',
    'initial_header_level': 2,
    'raw_enabled': False,
}


def convert(source, settings=None, part="html_body"):
    parts = publish_parts(source,
                          writer_name="html5",
                          settings_overrides=settings)
    return parts.get(part, '')


if __name__ == "__main__":
    sys.stdout.write(convert(sys.stdin.read(), settings))
