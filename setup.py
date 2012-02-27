from setuptools import find_packages, setup


setup(

    # Basic package information.
    name = 'opencnam',
    version = '0.1',
    packages = find_packages(),

    # Packaging options.
    zip_safe = False,
    include_package_data = True,

    # Package dependencies.
    install_requires = ['slumber>=0.4'],
    tests_require = ['nose>=1.1.2'],

    # Metadata for PyPI.
    author = 'Randall Degges',
    author_email = 'rdegges@gmail.com',
    license = 'UNLICENSE',
    url = 'http://www.opencnam.com',
    keywords = 'voip http api rest caller id name cid cnam telephony ' \
            'telephone python library',
    description = 'A simple python library for getting caller ID name ' \
            'information using the opencnam API.',
    long_description = open('README.md').read(),
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Telecommunications Industry',
        'License :: Public Domain',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Communications',
        'Topic :: Communications :: Internet Phone',
        'Topic :: Communications :: Telephony',
        'Topic :: Internet',
        'Topic :: Utilities',
    ],

)
