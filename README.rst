==================
ckanext-omlp_theme
==================

Tema del repositorio de datos del OMLP (Observatorio Medioambiental La Plata).
http://omlp.sedici.unlp.edu.ar/

------------
Installation
------------

.. Add any additional install steps to the list below.
   For example installing any non-Python dependencies or adding any required
   config settings.

To install ckanext-omlp_theme:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Install the ckanext-omlp_theme Python package into your virtual environment::

     pip install git+https://github.com/FacundoAdorno/ckanext-omlp_theme#egg=ckanext-omlp_theme

3. Add ``omlp_theme`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/production.ini``).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload


-------------------------
In Developemnt Enviroment
-------------------------

To contribute with your own code, clone this repository. Run the following commands::

     git clone https://github.com/FacundoAdorno/ckanext-omlp_theme
     cd ckanext-omlp_theme/
     python setup.py develop

Then, do the steps 3 and 4 described before.
