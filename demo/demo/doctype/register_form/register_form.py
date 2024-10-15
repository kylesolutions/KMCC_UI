# Copyright (c) 2024, demo and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class RegisterForm(Document):
    def on_update(self):
        frappe.msgprint(f"{self.name} created successfully.", indicator="green", alert=True)
