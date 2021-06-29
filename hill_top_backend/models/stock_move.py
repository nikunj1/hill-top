# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
import logging
_logger = logging.getLogger(__name__)
from odoo.tools.float_utils import float_round
from odoo.exceptions import ValidationError


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    length = fields.Float(string="Length",required=0)
    width = fields.Float(string="Width",required=0)
    area = fields.Float(string="Area" , compute='compute_area')


    def write(self,vals):
        if vals.get('lot_id'):
            if vals.get('length') and vals.get('width'):
                if vals.get('length') <= 0.0 or vals.get('width') <= 0.0:
                    raise ValidationError(_(
                        'Add Length And Width Value Grater Then 0.0'))
            else:
                if self.length <= 0.0 or self.width <= 0.0:
                    raise ValidationError(_(
                        'Add Length And Width Value Grater Then 0.'))
            return super(StockMoveLine, self).write(vals)


    @api.depends('length', 'width')
    def compute_area(self):
        for record in self:
            record.area = (record.length * record.width) - record.length