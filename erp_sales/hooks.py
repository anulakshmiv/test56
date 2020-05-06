# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "erp_sales"
app_title = "Manage Shipping"
app_publisher = "frappe"
app_description = "Manage Shipping "
app_icon = "icon-book"
app_color = "blue"
app_email = "anu@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/erp_sales/css/erp_sales.css"
# app_include_js = "/assets/erp_sales/js/erp_sales.js"

# include js, css files in header of web template
# web_include_css = "/assets/erp_sales/css/erp_sales.css"
# web_include_js = "/assets/erp_sales/js/erp_sales.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "erp_sales.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "erp_sales.install.before_install"
# after_install = "erp_sales.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erp_sales.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Sales Order": {
		"validate": "erp_sale.erp_sale.manage_shipping.sales_order_custom.calculate_total_weight"
    }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"erp_sales.tasks.all"
# 	],
# 	"daily": [
# 		"erp_sales.tasks.daily"
# 	],
# 	"hourly": [
# 		"erp_sales.tasks.hourly"
# 	],
# 	"weekly": [
# 		"erp_sales.tasks.weekly"
# 	]
# 	"monthly": [
# 		"erp_sales.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "erp_sales.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "erp_sales.event.get_events"
# }

fixtures = ["Custom Field"]
