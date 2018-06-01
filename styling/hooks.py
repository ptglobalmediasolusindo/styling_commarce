# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "styling"
app_title = "Styling"
app_publisher = "bobzz.zone@gmail.com"
app_description = "For Change Design"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "bobzz.zone@gmail.com"
app_license = "MIT"
website_context = {
	"favicon": 	"/assets/styling/images/commarce_favicon.png",
	"splash_image": "/assets/styling/images/commarce.png"
}
# Includes in <head>
# ------------------
app_include_css = "/assets/styling/css/custom.css"
web_include_css = "/assets/styling/css/custom.css"
# include js, css files in header of desk.html
# app_include_css = "/assets/styling/css/styling.css"
# app_include_js = "/assets/styling/js/styling.js"
app_include_js = "assets/js/styling.min.js"
# include js, css files in header of web template
# web_include_css = "/assets/styling/css/styling.css"
# web_include_js = "/assets/styling/js/styling.js"

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
# get_website_user_home_page = "styling.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "styling.install.before_install"
# after_install = "styling.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "styling.notifications.get_notification_config"

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

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"styling.tasks.all"
# 	],
# 	"daily": [
# 		"styling.tasks.daily"
# 	],
# 	"hourly": [
# 		"styling.tasks.hourly"
# 	],
# 	"weekly": [
# 		"styling.tasks.weekly"
# 	]
# 	"monthly": [
# 		"styling.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "styling.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "styling.event.get_events"
# }

