# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ranchy_members(models.Model):
    _name = 'members.ranchy'
    _rec_name = 'member_firstname'
    
    member_id = fields.Id
    member_firstname = fields.Char(string="Name")
    member_lastname = fields.Char(string="Name of father/husband")
    member_addresss = fields.Char(string="Residential Address")
    add_permanent = fields.Char(string="Pemanent Address")
    business_addresss = fields.Char(string="Business Address")
    member_phone = fields.Char(string="phone number")
    member_pic = fields.Binary("image", help="select image here")
    member_age = fields.Char(string="Age")
    marital_status = fields.Selection(
        [('Single','Single'), ('married','married'),('divorced','Divorced'),('widow','widow')],
        'Marital status')
    education = fields.Selection(
        [('none','None'), ('primary','Primary'),('secondary','Secondary'),('tertiary','Tertiary')],
        'Formal Education')
    next_kin = fields.Char(string="Next of Kin Name")
    kin_phone = fields.Char(string="Next of Kin Phone")
    memberof = fields.Many2one('corps.ranchy',string="name of group")
    business_type = fields.Char(string="Type of Business")
    business_period = fields.Char(string="How long in business")
    average_income = fields.Char(string="Average monthly income")
    
class ranchy_corps(models.Model): 
    _name = 'corps.ranchy'
    _rec_name = 'corps_name'
    corps_id = fields.Id
    corps_name = fields.Char(string="name of coperative")
    corps_leader = fields.One2many
    corps_staff = fields.One2many
    
class ranchy_loans(models.Model):
    _name = 'ranchy.loans' 
    
    
    state = fields.Selection([
            ('new', 'New Apllication'),
            ('awaiting', 'awaiting approval'),
            ('approve', 'awaiting disbursement'),
            ('disburse', 'disbursed/repayment'),
            ('paid', 'paid'),
            ],default='new')
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
    amount_applied = fields.Monetary(
        'Amount applied for',
        # optional: currency_field='currency_id',
        )
    amount_approved = fields.Monetary(
        'Amount approved',
        # optional: currency_field='currency_id',
        )
    amount_balance = fields.Monetary(
        'Balance',
        # optional: currency_field='currency_id',
        )
    last_loan = fields.Monetary(
        'last loan recieved amount',
        # optional: currency_field='currency_id',
        )
    date_payed = fields.Date('Date loan was fully paid')
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
    installments = fields.Selection(
        [('23','23'), ('20','20'),('18','18')],
        'number of installments')
    date_firstinstall = fields.Date('Date of first installment')
    date_finalinstall = fields.Date('Date of last installment')
    any_family = fields.Boolean('Is any family member of yours registered with the group')
    if_true = fields.Char('If true mention name')
    or_reg = fields.Boolean('Or registered in any other group of ranchi empowerment centre')
    indebted = fields.Boolean('Are you indebted to any otherMFB/MFI')
    if_true2 = fields.Char('If true Name')
    if_true3 = fields.Char('Outstanding Balance')
       
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