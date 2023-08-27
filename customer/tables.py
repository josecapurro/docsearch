import django_tables2 as tables
from django_tables2.utils import A
from django.utils.html import format_html
from .models import Customer

class Meta:
    model = Customer

class CustomerTable(tables.Table):
    action_template = "action_column.html"
    name = tables.Column()
    description = tables.Column()
    storagebackend = tables.Column()
    searchbackend = tables.Column()
    active = tables.Column()
    action = tables.TemplateColumn(template_name=action_template, verbose_name="action")
