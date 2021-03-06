from setuptools import setup, find_packages
import os

version = '1.0b6.dev0'
long_description = open("README.rst").read() + "\n" + \
                   open(os.path.join("docs", "INSTALL.rst")).read() + "\n" + \
                   open(os.path.join("docs", "CREDITS.rst")).read() + "\n" + \
                   open(os.path.join("docs", "HISTORY.rst")).read()

setup(name='collective.twitter.portlets',
      version=version,
      description="This product allows you to add different kinds of portlets to your site to get tweets.",
      long_description=long_description,
      classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone twitter portlet',
      author='Franco Pellegrini',
      author_email='frapell@gmail.com',
      url='https://github.com/collective/collective.twitter.portlets',
      license='GPL',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['collective', 'collective.twitter'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        'collective.prettydate>=1.1',
        'collective.twitter.accounts>=1.0.3',
        ],
      extras_require={
        'test': ['plone.app.testing'],
        },
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
