import django_tables2 as tables
from django_tables2.utils import A
from django.utils.html import format_html

class SearchTable(tables.Table):
    action_template = "action_column.html"
    bucket = tables.Column()
    key = tables.Column()
    action = tables.TemplateColumn(template_name=action_template, verbose_name="action")
