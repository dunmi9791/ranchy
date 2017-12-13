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
        [('Single', 'Single'), ('married', 'married'), ('divorced', 'Divorced'), ('widow', 'widow')],
        'Marital status')
    education = fields.Selection(
        [('none', 'None'), ('primary', 'Primary'), ('secondary', 'Secondary'), ('tertiary', 'Tertiary')],
        'Formal Education')
    next_kin = fields.Char(string="Next of Kin Name")
    kin_phone = fields.Char(string="Next of Kin Phone")
    memberof = fields.Many2one('corps.ranchy', string="name of group")
    business_type = fields.Char(string="Type of Business")
    business_period = fields.Char(string="How long in business")
    average_income = fields.Char(string="Average monthly income")
    loan_ids = fields.One2many('ranchy.loans', 'member_ids', string='Loans', store='true')
    date_disburse = fields.Date('Date', related='loan_ids.date_disburse')

    loan_id = fields.Many2one('ranchy.loans', compute='_compute_loan_id', string='Current Loan', store='true',
                              help='Latest loan of member')
    loan_count = fields.Integer(compute='_compute_loan_count', string='Loans')

    def _compute_loan_id(self):
        """ get the lastest loan """
        Loan = self.env['ranchy.loans']
        for member in self:
            member.loan_id = Loan.search([('member_ids', '=', member.id)], order='date_disburse desc', limit=1)

    def _compute_loan_count(self):
        # read_group as sudo, since contract count is displayed on form view
        loan_data = self.env['ranchy.loans'].sudo().read_group([('member_ids', 'in', self.ids)], ['member_ids'],
                                                               ['member_ids'])
        result = dict((data['member_ids'][0], data['member_ids_count']) for data in loan_data)
        for member in self:
            member.loan_count = result.get(member.id, 0)




