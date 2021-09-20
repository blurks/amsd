from setuptools import setup, find_packages


setup(
    name='amsd',
    version='0.0',
    description='amsd',
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author='EVA DLCE Dev',
    author_email='dlce.rdm@eva.mpg.de',
    keywords='web pyramid pylons',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'clld>=8.0.0',
        'pyramid>=2.0',
        'csvw>=1.11.0',
        'clldmpg>=4.2.0',
        'sqlalchemy>=1.4.23',
        'waitress>=1.4.4',
    ],
    extras_require={
        'dev': [
            'flake8',
            'tox',
        ],
        'test': [
            'psycopg2>=2.8.6',
            'mock>=4.0.3',
            'pytest>=6.2.4',
            'pytest-clld>=1.0.2',
            'pytest-mock>=3.6.1',
            'pytest-cov>=2.12.1',
            'coverage>=5.5',
            'selenium>=3.141',
            'zope.component>=5.0.1',
        ],
    },
    test_suite="amsd",
    entry_points="""\
    [paste.app_factory]
    main = amsd:main
""")
