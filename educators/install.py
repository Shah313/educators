import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields




def after_install():
	create_custom_fields(get_custom_fields())
	


    
def get_custom_fields():
	"""Education specific custom fields that needs to be added to the Sales Invoice DocType."""
	return {
		"Sales Invoice": [
			{
				"fieldname": "custom_student_name",
				"fieldtype": "Link",
				"label": "Student Name",
				"options": "Student",
				"insert_after": "naming_series",
			},
        ]
    }