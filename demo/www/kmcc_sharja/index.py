import frappe
from frappe.utils import escape_html

@frappe.whitelist(allow_guest=True)
def create_register_form(first_name, last_name, phone, email, iqama_number, blood_group, age):
    try:
        frappe.log(f"Received data - First Name: {first_name}, Last Name: {last_name}, Phone: {phone}, Email: {email}")
        if not first_name or not last_name or not phone or not email:
            frappe.throw("Missing required fields")

        doc = frappe.get_doc({
            'doctype': 'Register Form',
            'first_name': escape_html(first_name),
            'last_name': escape_html(last_name),
            'phone': escape_html(phone),
            'email': escape_html(email),
            'iqama_number': escape_html(iqama_number),
            'blood_group': escape_html(blood_group),
            'age': escape_html(age)
        })

        doc.insert()
        frappe.msgprint(f"{doc.name} created successfully.", indicator="green", alert=True)
        frappe.db.commit()

        return {"message": "success"}

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Register Form Submission Error")
        return {"message": str(e)}
