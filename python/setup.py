# -*- coding: utf-8 -*-

from setuptools import find_packages, setup


setup(
    name="iadz",
    version="0.0.1",
    description="Use to manage iadz",
    packages=find_packages("src", exclude=["test"]),
    package_dir={"": "src"},
    install_requires=[
       "alembic==1.0.7",
       "requests==2.21.0",
       "PyYAML>=5.4",
       "SQLAlchemy==1.3.3",
       "nameko==3.0.0-rc8",
       "marshmallow==2.19.5",
       "mysql-connector-python==8.0.16",
       "elasticsearch-dsl>=7.0.0,<8.0.0",
       "redis==3.3.11",
       "pycountry>=19.8.18",
       "SQLAlchemy-Utils>=0.36.5",
       "sshtunnel==0.1.5",
       "boto3==1.14.25",
       "pycryptodome==3.9.8",
       "tqdm==4.54.0",
       "pytz>=2021.1",
    ],
    extras_require={
        "dev": [
            "pytest==6.0.1",
            "requests-mock==1.8.0",
            "flake8==3.7.8",
            "coverage==4.5.4",
            "mock==2.0.0",
            "behave==1.2.6",
            "black==20.8b1",
        ]
    },
    zip_safe=True
)
