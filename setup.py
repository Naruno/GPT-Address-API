from setuptools import setup


setup(name='gpt_address_api',
version='0.1.0',
description="""Decentralized GPT API for everyone !""",
long_description_content_type="text/markdown",
include_package_data=True,
long_description="".join(open("README.md", encoding="utf-8").readlines()),
url='https://github.com/Naruno/GPT-Address-API',
author="Naruno Developers",
author_email='onur.atakan.ulusoy@naruno.org',
license='MIT',
packages=["gpt_address_api"],
package_dir={'':'src'},
install_requires=[
    "fire==0.5.0",
    "openai==0.27.2"
],
entry_points = {
    'console_scripts': ['gptaapi=gpt_address_api.gpt_address_api:main'],
},
python_requires=">= 3",
zip_safe=False)