# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2016 seeroo IT SOLUTIONS PVT.LTD(<http://www.seeroo.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
import logging
from odoo import api, fields, models, tools, _
import datetime

_logger = logging.getLogger(__name__)


class FactoryFactory(models.Model):
    _name = 'factory.factory'
    _description = 'Factory'

    name = fields.Char(string='Name', required=True)


class CrmProjectType(models.Model):
    _name = 'crm.project.type'
    _description = 'Crm Project Type'

    name = fields.Char(string='Name', required=True)


class CrmStages(models.Model):
    _inherit = 'crm.stage'

    state_id = fields.Selection([('quoted', 'Quoted'), 
                                 ('securable', 'Securable'), 
                                 ('onhold', 'On Hold'),
                                 ('lost_closed', 'Lost / Closed'), 
                                 ('awarded', 'Awarded'),
                                 ('not_yet_quoted', 'Not Yet Quoted')],
                                required=True, default='quoted')

    active = fields.Boolean(string='Active', default=True)


class CrmLead(models.Model):
    _inherit = 'crm.lead'
    
    
    @api.depends('cost_ids')
    def compute_cost_count(self):
        for record in self:
            record.cost_count = len(record.cost_ids.ids)
            

    enquiry_number = fields.Char(string='Enquiry Number')
    project_name = fields.Char(string='Project Name')
    project_emirate = fields.Char(string='Project Emirate')
    factory_id = fields.Many2one('factory.factory', string='Factory')
    project_type_id = fields.Many2one('crm.project.type', string='Type')
    capacity = fields.Float(string='Capacity(Kg)')
    quantity = fields.Float(string='Quantity')
    speed = fields.Char(string='Speed(in mps)')
    stop = fields.Float(string='Stop')
    specification_count = fields.Integer(string='Specification Count')
    # Extra Information
    ayees_cost = fields.Float(string='AYEES Cost(in AED)')
    ayee_no = fields.Char(string='AYEE NO')
    factory_offer = fields.Float(string='Factory Offer')
    landed_cost = fields.Float(string='Landed Cost(in AED)')
    consultant_id = fields.Many2one('res.partner', string='Consultant')
    created_on = fields.Date(string='Created ON')
    currency_id = fields.Many2one(comodel_name='res.currency', string='Currency',
                                  default=lambda self: self.env.company.currency_id)

    field_create_month = fields.Selection([('january', 'January'),
                                            ('february', 'February'),
                                            ('march', 'March'),
                                            ('april', 'April'),
                                            ('may', 'May'),
                                            ('june', 'June'),
                                            ('july', 'July'),
                                            ('august', 'August'),
                                            ('september', 'September'),
                                            ('october', 'October'),
                                            ('november', 'November'),
                                            ('december', 'December'),],
                                           string='Field Created Month')
    field_create_year = fields.Selection([(str(num), str(num)) 
                                          for num in range(((datetime.datetime.now().year)-10), 
                                                           ((datetime.datetime.now().year)+2))],
                                          string='F year')
    selling_price = fields.Float(string='Selling Price(in AED)',
                                 help="Selling Price excluding VAT(in AED)")
    offer_amount = fields.Float(string='Offer Amount')
    offer_date = fields.Date(string='Offer Date')
    client_id = fields.Many2one('res.partner', string='Client')
    contractor_id = fields.Many2one('res.partner', string='Contractor')
    last_updated_on = fields.Datetime(string='Last Updated On')
    handle_by = fields.Char(string='')
    handle_id = fields.Many2one('res.partner', string='Handled By')
    first_quotation_month = fields.Selection([('january', 'January'),
                                            ('february', 'February'),
                                            ('march', 'March'),
                                            ('april', 'April'),
                                            ('may', 'May'),
                                            ('june', 'June'),
                                            ('july', 'July'),
                                            ('august', 'August'),
                                            ('september', 'September'),
                                            ('october', 'October'),
                                            ('november', 'November'),
                                            ('december', 'December'),],
                                              string='First Quotation Month')
    first_quotation_year = fields.Selection([(str(num), str(num)) 
                                             for num in range(((datetime.datetime.now().year)-10), 
                                                           ((datetime.datetime.now().year)+2))],
                                             string='FQ year')
    cost_ids = fields.One2many('cost.estimation', 'lead_id',
                               string='Cost Estimation')
    cost_count = fields.Integer(string='Cost count',
                                compute='compute_cost_count')

    
    @api.model
    def create(self, vals):
        seq_pool = self.env['ir.sequence']
        vals['enquiry_number'] = seq_pool.next_by_code('crm.lead') or _('New')
        result = super(CrmLead, self).create(vals)
        return result
    
    
    def action_cost_estimation(self):
        self.ensure_one()
        for_xml_id = "sr_crm_customization.action_cost_estimation_load"
        action = self.env["ir.actions.actions"]._for_xml_id(for_xml_id)
        domain = [('id', 'in', self.cost_ids.ids)]
        context = {
                    'default_lead_id': self.id,
                   }
        action.update({
            'context': context,
            'domain': domain,
        })
        return action

    def action_specification(self):
        return True


