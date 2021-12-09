from odoo import api, models, fields


class ProductBrand(models.Model):
    _inherit = 'product.product'

    brand_id = fields.Char(string='Brand')
