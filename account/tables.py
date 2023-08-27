import django_tables2 as tables
from django_tables2.utils import A
from django.utils.html import format_html
from .models import Account

class Meta:
    model = Account

class AccountTable(tables.Table):
    action_template = "action_column.html"
    user = tables.Column()
    customer_id = tables.Column()
    active = tables.Column()
    action = tables.TemplateColumn(template_name=action_template, verbose_name="action")
