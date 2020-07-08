#!/usr/bin/env python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

register_check_parameters(
    subgroup_os,
    "aix_comp_mem",
    _("AIX Comp% memory utilization"),
    Dictionary(
        help = _("AIX comutational memory level check"),
        elements = [
            ('warn', Float(title = _("Warning at"), default_value = 80.0)),
            ('crit', Float(title = _("Critical at"), default_value = 90.0)),
        ]
    ),
    TextAscii(
        title = _("mem_type"),
        allow_empty = False,
    ),
    match_type = "dict",
)

