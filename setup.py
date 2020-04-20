# -*- coding: utf-8 -*-

from setuptools import find_packages, setup


setup(
    name="python_records",
    version="0.0.1",
    description="Use to manage packages in python_records",
    packages=find_packages("src", exclude=["test"]),
    package_dir={"": "src"},
    install_requires=[
       "alembic==1.0.7",
       "requests==2.21.0",
       "PyYAML==5.1",
       "SQLAlchemy==1.3.3",
       "nameko==3.0.0-rc8",
       "graphene==2.1.3",
       "Flask==1.0.2",
       "Flask-GraphQL==2.0.0",
       "marshmallow==2.19.5",
       "mysql-connector-python==8.0.16",
       "elasticsearch-dsl>=6.0.0,<7.0.0",
       "redis==3.3.11",
    ],
    extras_require={
        "dev": [
            "flake8>=3.7.7",
            "pytest==4.5.0",
            "coverage==4.5.3",
            "mock==2.0.0",
        ]
    },
    zip_safe=True
)
