# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ranchy_corps(models.Model): 
    _name = 'corps.ranchy'
    _rec_name = 'corps_name'
    corps_id = fields.Id
    corps_name = fields.Char(string="name of coperative")
    corps_leader = fields.One2many
    corps_staff = fields.One2many
    

class ranchy_repayments(models.Model):
    _name = 'ranchy.repayments'
    loanpayments_id = fields.Id
    member_id = fields.Many2one('members.ranchy', string='Member')
    loan_id = fields.Many2one('ranchy.loans', string='Loan')
    currency_id = fields.Many2one(
        'res.currency', string='Currency')
    amount_repaid = fields.Monetary(
        'Amount',
        # optional: currency_field='currency_id',
        )
    date = fields.Date('Date')
 
class ranchy_saving(models.Model):
    _name = 'ranchy.saving'
    saving_id = fields.Id
    member_id = fields.Many2one('members.ranchy', string='Member')
    date = fields.Date('Date') 
    currency_id = fields.Many2one(
        'res.currency', string='Currency')
    amount = fields.Monetary(
        'Amount',
        # optional: currency_field='currency_id',
        )
    balance = fields.Monetary(
        'Balance',
        # optional: currency_field='currency_id',
        )
    
class ranchy_withdrawals(models.Model):
    _name = 'ranchy.withdrawals'
    withdrawal_id = fields.Id
    member_id = fields.Many2one('members.ranchy', string='Member')
    currency_id = fields.Many2one(
        'res.currency', string='Currency')
    amount = fields.Monetary(
        'Amount',
        # optional: currency_field='currency_id',
        )
    date = fields.Date('Date')    
    

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100