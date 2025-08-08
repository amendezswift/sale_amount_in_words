# -*- coding: utf-8 -*-
from odoo import models, fields

class ResCompany(models.Model):
    _inherit = 'res.company'

    display_sale_amount_total_words = fields.Boolean(
        string="Total amount of quotation in letters",
        help="Si está activo, mostrará el total en letras en las cotizaciones/pedidos."
    )
