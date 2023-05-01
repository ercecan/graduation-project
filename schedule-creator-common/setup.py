import setuptools

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name='schedule-creator-common',
    version='0.0.1',
    authors=['Barış Emre Mişe', 'Ömer Farul Özkan', 'Erce Can Bektüre'],
    author_email='mise18@itu.edu.tr',
    description='Common Package of Schedule Creator Graduation Project',
    url='#',
    license='MIT',
    packages=['models', 'enums', 'services', 'dtos'],
    install_requires=required,
    zip_safe=False
)