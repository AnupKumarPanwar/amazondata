from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name='amazondata',
    version='0.0.1',
    description='A python package to get amazon product and search data in json form. The package does not require any API keys as it works by scraping the amazon page.',
    long_description_content_type="text/markdown",
    long_description=README,
    license='MIT',
    packages=find_packages(),
    author='Anup Kumar Panwar',
    author_email='1anuppanwar@gmail.com',
    keywords=['Amazon', 'Scraper'],
    url='https://github.com/AnupKumarPanwar/amazondata',
    download_url='https://pypi.org/project/amazondata/'
)

install_requires = [
    'selectorlib',
    'requests'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
