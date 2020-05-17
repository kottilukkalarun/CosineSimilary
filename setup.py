from distutils.core import setup
setup(
  name = 'CosineSimilarityFinder',         # How you named your package folder (MyLib)
  packages = ['CosineSimilarityFinder'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'FINDS COSINE SIMILARITY BETWEEN TWO TEXTS',   # Give a short description about your library
  author = 'ARUN KESAVAN KOTTILUKKAL',                   # Type in your name
  author_email = 'arunkottilukkal@outlook.in',      # Type in your E-Mail
  url = 'https://github.com/kottilukkalarun/CosineSimilary',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/kottilukkalarun/CosineSimilary/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['COSINE SIMILARITY', 'TEXT SIMILARITY', 'STRING SIMILARITY'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'certifi==2020.4.5.1',
          'chardet==3.0.4',
          'click==7.1.2',
          'dnspython==1.16.0',
          'eventlet==0.25.2',
          'greenlet==0.4.15',
          'idna==2.9',
          'joblib==0.15.1',
          'monotonic==1.5',
          'nltk==3.5',
          'numpy==1.18.4',
          'pandas==1.0.3',
          'python-dateutil==2.8.1',
          'pytz==2020.1',
          'regex==2020.5.14',
          'requests==2.23.0',
          'scikit-learn==0.23.0',
          'scipy==1.4.1',
          'six==1.14.0',
          'threadpoolctl==2.0.0',
          'tqdm==4.46.0',
          'urllib3==1.25.9',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)