from setuptools import setup

setup(name='thepian-lib',
      version=0.1,
      description="The Thepian Library",
      long_description="""\
""",
      keywords='thepian lib',
      author='Henrik Vendelbo',
      author_email='hvendelbo.dev@googlemail.com',
      url='www.thepian.org',
      license='GPL',
      packages= ['fs'],
      include_package_data=True,
      zip_safe=True,
      setup_requires=['setuptools',],
      classifiers=[
        'Development Status :: Alpha',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        ], 
      )