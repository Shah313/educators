import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def after_install():
    # Add custom fields defined in get_custom_fields
    create_custom_fields(get_custom_fields())

    # Update order_type options in Quotation
    update_quotation_order_type()

def get_custom_fields():
    """Define custom fields for Sales Invoice and other doctypes."""
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
    }

def update_quotation_order_type():
    """Update order_type options in the Quotation doctype."""
    if frappe.db.exists('DocType', 'Quotation'):
        doc = frappe.get_doc('DocType', 'Quotation')
        for field in doc.fields:
            if field.fieldname == 'order_type':
                # Get current options or set empty list if none exist
                current_options = field.options.split('\n') if field.options else []
                # Define new options
                new_options = ['Rent', 'Property Sell', 'Property Maintenance']
                # Merge options and remove duplicates
                updated_options = list(set(current_options + new_options))
                # Update the field options
                field.options = '\n'.join(updated_options)
                doc.save()
                # Clear cache to reflect changes
                frappe.clear_cache(doctype='Quotation')
