from odoo import models, fields, api

class Participante(models.Model):
    _name = 'habitos.participante'
    _description = 'Participante'

    id_participante = fields.Char(string="ID del Participante", required=True)
    nombre_completo = fields.Char(string="Nombre Completo", required=True)
    fecha_nacimiento = fields.Date(string="Fecha de Nacimiento", required=True)
    correo_electronico = fields.Char(string="Correo Electrónico", required=True)
    objetivo_principal = fields.Text(string="Objetivo Principal")
    fecha_registro = fields.Date(string="Fecha de Registro", default=fields.Date.context_today)
    genero = fields.Selection(
        [('masculino', 'Masculino'), ('femenino', 'Femenino'), ('otro', 'Otro')],
        string="Género",
        required=True
    )
    peso = fields.Float(string="Peso (kg)", required=True)
    altura = fields.Float(string="Altura (cm)", required=True)
    nivel_actividad = fields.Selection(
        [('sedentario', 'Sedentario'), ('moderado', 'Moderado'), ('activo', 'Activo')],
        string="Nivel de Actividad Física",
        required=True
    )
    categorias_trabajadas = fields.Text(string="Categorías Más Trabajadas")
    fecha_ultimo_seguimiento = fields.Date(string="Fecha del Último Seguimiento")
    total_habitos = fields.Integer(string="Total de Hábitos", default=0)
    habitos_completados = fields.Integer(string="Hábitos Completados", default=0)

    # Campos calculados
    imc = fields.Float(string="IMC", compute="_compute_imc", store=True)
    estado_general = fields.Char(string="Estado General", compute="_compute_estado_general", store=True)

    @api.depends('peso', 'altura')
    def _compute_imc(self):
        """Calcula el Índice de Masa Corporal (IMC)."""
        for record in self:
            if record.altura > 0:
                altura_metros = record.altura / 100
                record.imc = record.peso / (altura_metros ** 2)
            else:
                record.imc = 0.0

    @api.depends('habitos_completados', 'total_habitos', 'nivel_actividad')
    def _compute_estado_general(self):
        """Calcula el estado general basado en hábitos completados y nivel de actividad."""
        for record in self:
            if record.total_habitos > 0:
                porcentaje_habitos = (record.habitos_completados / record.total_habitos) * 100
            else:
                porcentaje_habitos = 0.0

            if porcentaje_habitos >= 80 and record.nivel_actividad == 'activo':
                record.estado_general = "Excelente"
            elif porcentaje_habitos >= 50 and record.nivel_actividad in ['moderado', 'activo']:
                record.estado_general = "Bueno"
            else:
                record.estado_general = "Mejorable"