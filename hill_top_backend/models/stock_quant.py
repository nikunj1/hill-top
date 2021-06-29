# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
import logging
_logger = logging.getLogger(__name__)
from odoo.tools.float_utils import float_round


class StockQuant(models.Model):
    _inherit = 'stock.quant'

    length = fields.Float(string="Length",compute='compute_length_width')
    width = fields.Float(string="Width",compute='compute_length_width')
    area = fields.Float(string="Area", compute='compute_area')

    def compute_length_width(self):
        for record in self:
            move_line = self.env['stock.move.line'].search([('product_id','=',record.product_id.id),('lot_id','=',record.lot_id.id),('location_dest_id','=',record.location_id.id)])
            record.length = move_line.length
            record.width = move_line.width

    @api.depends('length', 'width')
    def compute_area(self):
        for record in self:
            record.area = (record.length * record.width) - record.length