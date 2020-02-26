from odoo import models, fields, api

class Coches(models.Model):
    _name = 'coches'
    codigo = fields.Integer('Codigo', required=True)
    modelo = fields.Char('Modelo', required=True)
    marca = fields.Char('Marca', required=True)
    matricula = fields.Char('Matricula', required=True)
    precio = fields.Integer('Precio', required=True)
    precio_Final = fields.Integer(compute = "get_precioFinal", String = "Precio Final", required=True)

    def get_precioFinal(self):
        for record in self:
            record.precio_Final = record.precio + (record.precio * 0.21)