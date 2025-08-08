# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    amount_total_words = fields.Char(
        string="Amount total in words",
        compute="_compute_amount_total_words",
        store=False,  
    )

    @api.depends('amount_total', 'currency_id', 'partner_id.lang')
    def _compute_amount_total_words(self):
        for order in self:
            lang_ctx = {}
            if order.partner_id and order.partner_id.lang:
                lang_ctx['lang'] = order.partner_id.lang
            order.amount_total_words = (
                order.currency_id.with_context(**lang_ctx)
                .amount_to_text(order.amount_total)
                .replace(',', '')
            )
