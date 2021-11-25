from odoo import api, fields, models
from datetime import datetime


class ComponentRequest(models.Model):
    _name = 'component.request'
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Component Request"

    _rec_name = "name_seq"

    employee_id = fields.Many2one('hr.employee', string='Employee',
                                  required=True)
    requisition_date = fields.Date(string='Requisition Date', required=True)
    department_id = fields.Many2one('hr.department', string='Department',
                                    required=True)
    name_seq = fields.Char('Component Request', required=True, index=True,
                           copy=False, default='New')
    request_line_ids = fields.One2many('component.requisition.lines',
                                       'partner_id', string='Requisition Lines',
                                       required=True)
    state = fields.Selection([('new', 'New'), ('approved', 'Approved'),
                              ('confirmed', 'Confirmed')], default='new',
                             string='State')

    def action_approve(self):
        self.state = 'approved'

    def action_confirm(self):
        self.state = 'confirmed'

    def action_cancel(self):
        self.state = 'new'

    def action_create_quotation(self):
        quotation_lines = [(5, 0, 0)]
        data = self.env['component.request'].search([('id', '=',
                                                      self.id)])
        print(data)
        print(data.request_line_ids)

        for rec in data.request_line_ids:
            print(rec.requisition_action)
            if rec.requisition_action == 'purchase order':
                val = {
                    'name': rec.product_id.name,
                    'product_id': rec.product_id.id,
                    'product_qty': rec.product_qty,
                    'price_unit': rec.product_price,
                    'taxes_id': False,
                    'date_order': datetime.today(),
                }
                print(val)
                quotation_lines.append((0, 0, val))
            if rec.requisition_action == 'purchase order':
                po = self.env['purchase.order'].create({
                    'partner_id': data.employee_id.id,
                    'order_line': quotation_lines
                })
                po.button_confirm()






#     for line in data.request_line_ids:
#         for rec in line:
#             val = {
#                 'name': rec.product_id.name,
#                 'product_id': rec.product_id.id,
#                 'product_qty': rec.product_qty,
#                 'price_unit': rec.product_price,
#                 'taxes_id': False,
#                 'date_order': datetime.today(),
#             }
#             print(val)
#
#             quotation_lines.append((0, 0, val))
#
# po = self.env['purchase.order'].create({
#     'partner_id': data.employee_id.id,
#     'order_line': quotation_lines
# })
# po.button_confirm()


@api.model
def create(self, vals):
    vals['name_seq'] = self.env['ir.sequence'].next_by_code(
        'component.request')
    return super(ComponentRequest, self).create(vals)


class ComponentRequisitionLines(models.Model):
    _name = "component.requisition.lines"
    _description = "Component Requisition Lines"

    requisition_action = fields.Selection([
        ('purchase order', 'Purchase Order'),
        ('internal transfer', 'Internal Transfer')], required=True)
    product_id = fields.Many2one('product.product', string="Product ID")
    product_qty = fields.Integer(string="Product Qty")
    product_price = fields.Float(string="Product Price")
    partner_id = fields.Many2one('component.request', string='Partner ID')

    # def action_create(self):
    #     data = self.env['component.request'].search([('id', '=',
    #                                                   self.partner_id.id)])
    #     print(data)
    #     quotation_lines = [(5, 0, 0)]
    #     # if data.request_line_ids.requisition_action == 'purchase order':
    #     for line in data.request_line_ids:
    #         val = {
    #             'name': line.product_id.name,
    #             'product_id': line.product_id.id,
    #             'product_qty': line.product_qty,
    #             'price_unit': line.product_price,
    #             'taxes_id': False,
    #             'date_order': datetime.today(),
    #         }
    #         print(val)
    #         quotation_lines.append((0, 0, val))
    #
    #     po = self.env['purchase.order'].create({
    #         'partner_id': data.employee_id.id,
    #         'order_line': quotation_lines
    #     })
    #     po.button_confirm()

    # def unlink(self):
    #     to_unlink = self.filtered(lambda r: r.requisition_action
    #                                         not in ['purchase order'])
    #     print(to_unlink)
    #     to_unlink.mapped('request_line_ids').unlink()
    #     return super(ComponentRequisitionLines, self).unlink()
