from odoo import models, fields, api
from datetime import timedelta, datetime
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning


class ACSTreatment(models.Model):
    _inherit = 'hms.treatment'

    finding = fields.Text(string="Keluhan Utama", states={'cancel': [
                          ('readonly', True)], 'done': [('readonly', True)]})
    anamnesis = fields.Text(string="Anamnesis", states={'cancel': [
                            ('readonly', True)], 'done': [('readonly', True)]})
    pemeriksaan_fisik = fields.Text(string="Pemeriksaan Fisik", states={'cancel': [
                                    ('readonly', True)], 'done': [('readonly', True)]})
    tindakan = fields.Text(string="Tindakan", states={'cancel': [
                           ('readonly', True)], 'done': [('readonly', True)]})
    appointment = fields.Many2one(
        'hms.appointment', ondelete="restrict", string='Appointment', readonly=True)
    second_diagnosis_id = fields.Many2one('hms.diseases', string='Diagnosis 2',
                                          states={'cancel': [('readonly', True)], 'done': [('readonly', True)]})

    @api.model
    def _get_default_physician(self):
        physician = self.env['hms.physician'].search(
            [('user_id', '=', self.env.user.id)])
        if physician:
            return physician.id

    physician_id = fields.Many2one('hms.physician', ondelete='restrict', string='Physician', help='Physician who treated or diagnosed the patient', states={
                                   'cancel': [('readonly', True)], 'done': [('readonly', True)]}, default=_get_default_physician)

    def treatment_running(self):
        result = super().treatment_running()

        # add second desase
        print('set second disease')
        print(self.second_diagnosis_id.name)
        # self.patient_disease_id.write({
        #     'second_disease_id': self.second_diagnosis_id.id
        # })

        my_disease = self.env['hms.patient.disease'].search(
            [('id', '=', self.patient_disease_id.id)], limit=1)

        my_disease.write({
            'second_disease': self.second_diagnosis_id.id
        })

        return result
