{
    "name": "Base module for numerobis",
    "version": "16.0.0.1.0",
    "summary": "This is a base module for numerobis project",
    "description": """
        Add some speficic features to the numerobis project:

        - Add fonts Gilroy
    """,
    "author": "njeudy",
    "website": "https://github.com/Alusage/numerobis-addons",
    "category": "Uncategorized",
    "depends": ["base", "web", "website"],
    "data": [],
    "assets": {
        "web._assets_primary_variables": [
            "numerobis_base/static/src/scss/primary_variable.scss",
        ],
    },
    "installable": True,
    "application": False,
    "auto_install": False,
}
