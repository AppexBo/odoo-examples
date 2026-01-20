{
    'name': "Examples Advanced",
    'summary': "Advanced examples for controllers, templates, and view inheritance",
    'description': """
        This module provides examples of:
        - Controllers with HTTP and JSON routes
        - QWeb templates creation
        - XML view inheritance with xpath
        - OWL template inheritance
        - QWeb report templates (PDF, HTML, Text)
        - Report template inheritance
    """,
    'author': "Appex Latam",
    'category': 'Examples',
    'version': '18.0.1.0.0',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/examples_views.xml',
        'views/examples_templates.xml',
        'views/examples_inheritance_views.xml',
        'report/report_templates.xml',
        'report/report_templates_inheritance.xml',
        'report/ir_actions_report.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'examples_advanced/static/src/xml/templates_inheritance.xml',
        ],
    },
}