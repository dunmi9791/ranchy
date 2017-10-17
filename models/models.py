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
    amount = fields.Monetary(string="Amount",# optional: currency_field='currency_id')
    disburse_date = fields.Date(string="Date of Disburse")
    member_id = fields.Many2one('members.ranchy', string="Member")
    tenure = fields.Char(string="loan tenure")
    
    total_repayments = fields.Float(string="Total repayed")
    balance = fields.Float(string="Outstanding Balance")
    
    
       

    
    

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100