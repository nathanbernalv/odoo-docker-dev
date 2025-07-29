from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    tipo_entrega = fields.Selection(
        [
            ('normal', 'Normal'),
            ('express', 'Express'),
            ('programada', 'Programada')
        ],
        string='Tipo de Entrega'
    )
