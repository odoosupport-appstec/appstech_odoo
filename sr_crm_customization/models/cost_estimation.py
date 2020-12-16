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


_logger = logging.getLogger(__name__)


class CostEstimation(models.Model):
    _name = 'cost.estimation'
    _description = 'Cost Estimation'
    _rec_name = 'enquiry_number'

    name = fields.Char(string='Name')
    salesman_id = fields.Many2one('res.partner',string='Sales Man')
    ayees_enq_no = fields.Many2one('crm.lead',string='AYEES Inquiry No')
    project_id = fields.Many2one('project.project',string='Project Name')
    project_location_id = fields.Many2one('res.location', string='Project Location')
    project_address = fields.Char(string='Project Address')
    project_location_from_sonapur_camp = fields.Char(string='Project Location From Sonapur Camp')
    lc_in_dollar = fields.Float(string='LC In $')
    lc_in_euro = fields.Float(string='LC In €')
    client_owner_id = fields.Many2one('res.partner',string='Client/Owner Name')
    consultant_id = fields.Many2one('res.partner', string='Consultant')
    contractor_id = fields.Many2one('res.partner', string='Contractor')
    
    lead_id = fields.Many2one('crm.lead',string='Lead')
    enquiry_number = fields.Char(string='Enquiry Number',
                                 related='lead_id.enquiry_number',
                                 store=True)
    project_name = fields.Char(string='Project Name',
                               related='lead_id.project_name',
                               store=True)
    project_emirate = fields.Char(string='Project Emirate',
                                  related='lead_id.project_emirate',
                                  store=True)






