import setuptools  

with open('README.md', 'r', encoding='utf-8') as f:
    longdescription = f.read()

__version__ = '0.0.0'

REPO_NAME = 'Insurance-Premium-End-to-End'
AUTHOR_USER_NAME = 'peteray-dev'
SRC_REPO = 'inproject'
AUTHOR_EMAIL = 'peteraydev@gmail.com'

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author= AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='End to End project with machine learning',
    long_description=longdescription,
    url=f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}',
    project_urls={
        "Bug Tracker": f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues'
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where='src')
)