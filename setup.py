from setuptools import setup, find_namespace_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(

      name='hydroenvironmental-tools',

      author='Sebastian Gegenleithner',

      author_email='s.gegenleithner@gmail.com',

      version='0.1.0',

      description='Python tools for performing hydroenvironmental tasks',

      long_description=long_description,

      long_description_content_type="text/markdown",

      url='https://github.com/tuggegese/hydroenvironmental-tools',

      install_reqs = [
            'pyproj==1.9.6'
      ],
	  
      keywords = 'hydrology, hydrodynamics, ecology',

      scripts=[
	      "toolbox/Converters/EllipticToGeoid/elliptictogeoid.py"
	  ],

      classifiers=[

           'Development Status :: 3 - Alpha',

           'Intended Audience :: Hydroenvironmental researchers and engineers',

           'License :: OSI Approved :: MIT License',

           'Natural Language :: English',

           'Operating System :: OS Independent',

           'Programming Language :: Python :: 3'
      ],

      python_requires='>=3.6'

     )
