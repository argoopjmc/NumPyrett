from distutils.core import setup
setup(
  name = 'NumPyrett',        
  packages = ['NumPyrett'],   
  version = '0.1',     
  license='MIT',        
  description = 'Prettyprint NumPy polynomials, matrices and arrays using LaTeX',  
  author = 'Rahul Gupta',                  
  author_email = 'rahul.gupta@gmconsultants.com',    
  url = 'https://github.com/argoopjmc/NumPyrett',  
  download_url = 'https://github.com/argoopjmc/NumPyrett/archive/refs/tags/v_01.tar.gz',
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