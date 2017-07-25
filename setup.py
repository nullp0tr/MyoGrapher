from setuptools import setup

setup (
    name='MyoGrapher',
    version='0.0.1',
    description='Portable plotting for MYO EMG data',
    url='https://github.com/RaquenaTeam/MyoGrapher',
    author='nullp0tr',
    author_email='ahmed@shnaboo.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='Myo EMG IMU graphing plotting',
    install_requires=['pygame']
)
