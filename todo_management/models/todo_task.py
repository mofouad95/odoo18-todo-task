from odoo import models, fields

class TodoTask(models.Model):
    _name = 'todo.task'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'To-Do List Model'


    name = fields.Char(required=True, string='Task Name')
    assign_to = fields.Many2one('res.users', string='Assign To')
    description = fields.Text(string='Description')
    due_date = fields.Date(string='Due Date')
    status = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'IN Progress'),
        ('completed', 'Completed')
    ], string='Status', default='new')








