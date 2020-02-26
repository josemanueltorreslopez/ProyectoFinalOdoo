from odoo import models, fields, api

class Personal(models.Model):
    _name = 'personal'
    codigo = fields.Integer('Codigo', required=True)
    nombre = fields.Char('Nombre', required=True)
    puesto = fields.Char('Puesto', required=True)
    fechContrato = fields.Char('Fecha Contrato', required=True)
    sueldo = fields.Integer('Sueldo', required=True)