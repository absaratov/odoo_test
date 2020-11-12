from odoo import api, fields, models
from odoo.exceptions import Warning

class Partner(models.Model):
    _inherit = 'res.partner'
    _name = 'my_partner'
    inn = fields.Char(help="INN of the partner organisation")
    kpp = fields.Char(help="KPP of the partner organisation")         
    
    @api.multi
    def write(self, values):
        if not self.is_INN_and_KPP_pair_repeats_w(values):
            return super(Partner, self).write(values)
        
    @api.model
    @api.returns('self', lambda value: value.id)
    def create(self, values):              
        if not self.is_INN_and_KPP_pair_repeats_w(values):
            return super(Partner, self).create(values)

    def is_INN_and_KPP_pair_repeats_w(self, values):
        if not 'inn' in values and not 'kpp' in values:
            return False
        if 'inn' in values:
            inn = values['inn']
        else: inn = self.inn
        if 'kpp' in values:
            kpp = values['kpp']
        else: kpp = self.kpp
        
        rep = self.search([('inn', '=', inn),('kpp', '=', kpp)], limit=1)
        if rep: 
            raise Warning(('INN and KPP pair repeats with partner %(p)s') % {'p': rep.name})    