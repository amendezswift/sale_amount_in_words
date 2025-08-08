# -*- coding: utf-8 -*-
from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    display_sale_amount_total_words = fields.Boolean(
        string="Total amount of quotation in letters",
        related='company_id.display_sale_amount_total_words',
        readonly=False,
    )
