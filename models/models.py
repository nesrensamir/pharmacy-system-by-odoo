# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Medicine(models.Model):
    _inherit = 'product.template'
    # _name = 'iti42.pharmacy.medicine'
    _description = 'pharmacy.medicines.model'

   # name = fields.Char()
   # barcode = fields.Char()
   # description = fields.Char()
    usage_type = fields.Char()
    sale_price = fields.Float()
    scientific_name = fields.Char()
    moves = fields.One2many(comodel_name='iti42.pharmacy.moves', inverse_name='medicine')
    quantity_available = fields.Float(compute='_get_quantity', store=True)

    @api.depends('moves.quantity')
    def _get_quantity(self):
        for record in self:
            total = 0.0
            moves_items = self.env['iti42.pharmacy.moves'].search([('medicine', '=', record.id)])
            for move in moves_items:
                total += move.quantity
            record.quantity_available = total
        # record.quantity_available = sum(record.moves.mapped('quantity'))


class MedicineMoves(models.Model):
    _name = 'iti42.pharmacy.moves'
    _description = 'Medicine Moves'

    name = fields.Char()
    quantity = fields.Float()
    timestamp = fields.Datetime()
    medicine = fields.Many2one(comodel_name='product.template')
    # medicine = fields.Many2one(comodel_name='iti42.pharmacy.medicine')
