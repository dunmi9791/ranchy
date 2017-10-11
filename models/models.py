# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ranchy_members(models.Model):
    _name = 'members.ranchy'
    
    member_id = fields.Id
    member_firstname = fields.Char("FirstName")
    member_lastname = fields.Char("Last")
    member_addresss = fields.Text("Address")
    member_phone = fields.Char
    member_pic = fields.Binary
    memberof = fields.Many2one
    
class ranchy_corps(models.Model): 
    _name = 'corps.ranchy'
    corps_id = fields.Id
    corps_name = fields.Char
    corps_leader = fields.One2many
    corps_staff = fields.One2many
    
class ranchy_loans(models.Model):
    _name = 'ranchy.loans'
    loan_id = fields.Id
    amount = fields.Monetary
    disburse_date = fields.Date
    member_id = fields.Many2one
        
       

    
    

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100