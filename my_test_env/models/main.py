# -*- coding: utf-8 -*-

import os, json, logging, re
from odoo import models, fields, api, _
from odoo.tools import config, date_utils

_logger = logging.getLogger(__name__)

class MyTestENV(models.Model):
    _name = 'my.test.env'
    _description = 'my.test.env'
    
    name = fields.Char('Name')
    description = fields.Text('Description')
    
    def action_test(self):
        self.ensure_one()
        
        self.name = str(fields.Datetime.to_string(fields.Datetime.now()))
        self.description = json.dumps(config.options, sort_keys=True, indent=4, default=date_utils.json_default)
    