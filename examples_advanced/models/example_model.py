from odoo import models, fields, api


class ExampleRecord(models.Model):
    _name = 'example.record'
    _description = 'Example Record Model'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Active', default=True)
    value = fields.Float(string='Value')
    partner_id = fields.Many2one('res.partner', string='Partner')

    @api.model
    def get_records_count(self):
        return self.search_count([])