
{
    'name' : 'Sr CRM Customization ',
    'version' : '1.0.09',
    'summary': 'Module for CRM Customization.',
    'description': "OTP LOGIN",
    'category': 'Accounting/Accounting',
    'depends' : ['crm','crm_iap_lead_enrich'],
    'data': [
        'data/crm_stages.xml',
        'data/ir_sequence_data.xml',
        
        'security/ir.model.access.csv',
        
        'views/factory_view.xml',
        'views/enquiry_type.xml',
        'views/cost_estimation.xml',
        'views/crm_lead_view.xml',
        'views/res_partner_inherit.xml',
        
        'menu.xml',
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'author': 'Athira P Nair',
    # 'website': 'https://www.seeroo.com',
}