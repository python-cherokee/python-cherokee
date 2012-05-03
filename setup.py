from distutils.core import setup

setup(
    name='Python Cherokee',
    version='0.1dev',
    packages=['cherokee', ],
    license='LICENSE',
    description='Python interface to manipulate cherokee.conf',
    long_description=open('README.md').read(),
    author='Calvin Cheng',
    author_email='calvin@calvinx.com',
    install_requires=[],
    entry_points={
        'console_scripts': [
            'pycherokee = cherokee.main:main',
        ]
    }
)
