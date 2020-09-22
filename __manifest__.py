{
    'name': "Custom Form Treatment",
    'summary': """
        Modul custom menu treatment """,
    'description': """
        Modul custom menu treatment
    """,
    'author': "Muhammad Aziz - 087881071515, Haris - 082398371825",
    'website': "https://www.tutorialopenerp.wordpress.com/",
    'category': 'Treatment',
    'version': '0.1',
    'depends': ['base', 'acs_hms', 'acs_hms_insurance', 'acs_hms_hospitalization',],
    'data': [
        'security/ir.model.access.csv',
        'views/hms_treatment_view.xml',
    ],
    'demo': [
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
