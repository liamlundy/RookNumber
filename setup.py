from setuptools import setup, find_packages

setup(name='rook_number',
      version='0.0.1',
      author='Liam Lundy',
      author_email='llundy@gmail.com',
      packages=find_packages(),
      include_package_data=True,
      install_requires=[],
      setup_requires=[
          'pytest-runner',
      ],
      tests_require=[
          'pytest',
          'coverage'
      ],
      )
