from odoo import models, fields, api

class Promociones(models.Model):
    _name = 'promociones'
    codigo = fields.Integer('Codigo', required=True)
    nombre = fields.Char('Nombre', required=True)
    descripcion = fields.Char('Descripcion', required=True)
    fechInicio = fields.Char('Fecha Inicio', required=True)
    fechFinal = fields.Char('Fecha Final', required=True)

    def codigo_get(self):
        res = []
        for record in self:
            codigo = record.codigo
            res.append((record.id, codigo))
        return res