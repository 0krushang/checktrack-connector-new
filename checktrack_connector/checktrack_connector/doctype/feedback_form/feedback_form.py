# Copyright (c) 2025, satat tech llp and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class FeedbackForm(Document):
    def after_insert(self):
        if self.task_type_id:
            # Update the Preventive Maintenance Task with feedback link
            frappe.db.set_value(
                self.type,
                self.task_type_id,
                "feedback",  # Make sure this field exists in the Task DocType
                self.name
            )
