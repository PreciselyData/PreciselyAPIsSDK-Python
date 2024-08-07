"""
    Precisely APIs

    Enhance & enrich your data, applications, business processes, and workflows with rich location, information, and identify APIs.  # noqa: E501

    The version of the OpenAPI document: 17.1.0
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "com.precisely.apis"
VERSION = "18.1.1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
  "requests"
]

setup(
    name=NAME,
    version=VERSION,
    description="Precisely APIs",
    author="Precisely APIs Support",
    author_email="PreciselyAPIs-Support@precisely.com",
    url="https://developer.precisely.com/",
    keywords=["Precisely APIs"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Apache 2.0",
    long_description="""\
    Enhance and enrich your data, applications, business processes, and workflows with rich location, information, and identify APIs. """
)
