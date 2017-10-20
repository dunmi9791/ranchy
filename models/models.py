# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ranchy_members(models.Model):
    _name = 'members.ranchy'
    
    member_id = fields.Id
    member_firstname = fields.Char(string="FirstName")
    member_lastname = fields.Char(string="Last")
    member_addresss = fields.Text(string="Address")
    member_phone = fields.Char(string="phone number")
    member_pic = fields.Binary("image", help="select image here")
    memberof = fields.Many2one('corps.ranchy')
    
class ranchy_corps(models.Model): 
    _name = 'corps.ranchy'
    corps_id = fields.Id
    corps_name = fields.Char(string="name of coperative")
    corps_leader = fields.One2many
    corps_staff = fields.One2many
    
class ranchy_loans(models.Model):
    _name = 'ranchy.loans'
    loan_id = fields.Id
    currency_id = fields.Many2one(
        'res.currency', string='Currency')
    total_repayments = fields.Monetary(
        'Total Repayments',
        # optional: currency_field='currency_id',
        )
    amount_disburse = fields.Monetary(
        'Amount',
        # optional: currency_field='currency_id',
        )
    amount_balance = fields.Monetary(
        'Balance',
        # optional: currency_field='currency_id',
        )
    date_disburse = fields.Date('Date')
    member_id = fields.Many2one(
        'members.ranchy', string='Member',
        # optional:
        ondelete='restrict',
        context={},
        domain=[],
        )
    stage = fields.Selection(
        [('1st','First'), ('2nd','Second'),('3rd','third')],
        'Stage')
       
class loan_payments(models.Model):
    _name = 'loan.payments'
    loanpayments_id = fields.id
    member_id = fields.Many2one('members.ranchy', string='Member')
    loan_id = fields.Many2one('ranchy.loans', string='Loan')
    currency_id = fields.Many2one(
        'res.currency', string='Currency')
    amount_repaid = fields.Monetary(
        'Amount',
        # optional: currency_field='currency_id',
        )
    date = fields.Date('Date')
 
class savings_saved(models.Model):
    _name = 'savings.saved'
    saving_id = fields.id
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
    
class withdrawals(models.Model):
    _name = 'withdrawals'
    withdrawal_id = fields.id
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