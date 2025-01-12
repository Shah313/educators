import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from educators.install import update_quotation_order_type


def execute():
	create_custom_fields(update_quotation_order_type())
