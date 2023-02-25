#!/usr/bin/env python
from __future__ import print_function
import click

import click_odoo


@click.command()
@click.option('--fields', type=str, help='List of indicators to refresh', multiple=True)
@click_odoo.env_options(default_log_level='info')
def main(env, fields):
    partners = env['res.partner'].search([], limit=1)
    partners.recompute_indicators_for_all_records(fields)


if __name__ == '__main__':
    main()
