import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields




def after_install():
	create_custom_fields(get_custom_fields())
	


    
def get_custom_fields():
	"""Education specific custom fields that needs to be added to the Sales Invoice DocType & Quotation Doctype."""
	return {
		"Sales Invoice": [
			{
				"fieldname": "custom_student_name",
				"fieldtype": "Link",
				"label": "Student Name",
				"options": "Student",
				"insert_after": "naming_series",
			},
        ],
      "Quotation": [
    {
        "fieldname": "custom_order_type",
        "fieldtype": "Select",
        "label": "Order Type",
        "options": "Property Sell\nProperty Rent\nProperty Maintenance\nSales\nMaintenance\nShopping Cart",
        "insert_after": "column_break1",
		"default": "Property Sell",
        "reqd": 1,
        "print_hide": 1,
        "in_standard_filter": 1
    },
  ],
 }