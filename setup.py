from setuptools import find_packages, setup

version = '0.0.5'

setup(
    name='sdh.otl',
    version=version,
    url='https://bitbucket.org/sdh-llc/sdh-otl/',
    author='Software Development Hub LLC',
    author_email='dev-tools@sdh.com.ua',
    description='Django one time link generator and processor',
    license='BSD',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['sdh'],
    eager_resources=['sdh'],
    include_package_data=True,
    entry_points={},
    zip_safe=False,
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)