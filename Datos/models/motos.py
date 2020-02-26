from odoo import models, fields, api

class Motos(models.Model):
    _name = 'motos'
    codigo = fields.Integer('Codigo', required=True)
    modelo = fields.Char('Modelo', required=True)
    marca = fields.Char('Marca', required=True)
    matricula = fields.Char('Matricula', required=True)
    promociones = fields.Many2one('promociones', 'Promociones')