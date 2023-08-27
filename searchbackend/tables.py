import django_tables2 as tables
from django_tables2.utils import A
from django.utils.html import format_html
from .models import SearchBackend

class Meta:
    model = SearchBackend

class SearchBackendTable(tables.Table):
    action_template = "action_column.html"
    name = tables.Column()
    description = tables.Column()
    host = tables.Column()
    port = tables.Column()
    user = tables.Column()
    password = tables.Column()
    active = tables.Column()
    action = tables.TemplateColumn(template_name=action_template, verbose_name="action")
