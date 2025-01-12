import frappe
from educators.install import update_quotation_order_type


def execute():
	update_quotation_order_type()
