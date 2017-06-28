from setuptools import setup

setup(
    name='xontrib-schedule',
    version='0.0.1',
    url='https://github.com/astronouth7303/xontrib-schedule',
    license='MIT',
    author='Jamie Bliss',
    author_email='astronouth7303@gmail.com',
    description='Xonsh Task Scheduling',
    install_requires=['schedule', 'pause'],
    packages=['xontrib'],
    package_dir={'xontrib': 'xontrib'},
    package_data={'xontrib': ['*.xsh']},
    platforms='any',
)
