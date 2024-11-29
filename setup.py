from setuptools import setup, find_packages

setup(
    name='app_de_gestion_de_horas_de_trabajo',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'Flask==2.0.1',
        'Flask-SQLAlchemy==2.5.1',
    ],
    entry_points={
        'console_scripts': [
            'app_de_gestion_de_horas_de_trabajo=main:main',
        ],
    },
)