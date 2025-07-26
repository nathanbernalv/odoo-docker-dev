from odoo import models, fields

class ApiService(models.Model):
    _name = 'api.service'
    _description = 'API Service Model'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
