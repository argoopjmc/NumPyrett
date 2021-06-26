from distutils.core import setup
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'NumPyrett',        
  packages = ['NumPyrett'],   
  version = '0.4',     
  license='MIT',        
  description = 'Prettyprint NumPy polynomials, matrices and arrays using LaTeX',
  long_description=long_description,
  long_description_content_type='text/markdown' ,
  author = 'Rahul Gupta',                  
  author_email = 'rahul.gupta@gmconsultants.com',    
  url = 'https://github.com/argoopjmc/NumPyrett',  
  download_url = 'https://github.com/argoopjmc/NumPyrett/archive/refs/tags/v_04.tar.gz',
  keywords = ['NumPy', 'Education', 'Latex'],
  install_requires=[            
          'numpy'
      ],
  classifiers=[
    'Development Status :: 4 - Beta',   
    'Intended Audience :: Science/Research',
    'Intended Audience :: Education',
    'Topic :: Scientific/Engineering',
    'Topic :: Text Processing :: Markup :: LaTeX',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3.6',      
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8'
  ],
)