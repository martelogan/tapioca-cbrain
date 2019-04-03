# Tapioca cbrain

## Installation
**Note:** pending stable deployment on [pypi](https://pypi.org/user/martelogan/), we recommend the following developer install. 
```
git clone https://github.com/martelogan/tapioca-cbrain.git
cd tapioca-cbrain
python setup.py install
```
Ideally, it is advised to manage Python virtual environments via [`conda`](https://docs.continuum.io/anaconda/) in order to safely segregate module dependencies. In this case, it is recommended to locallize [`pip`](https://pip.pypa.io/en/stable/installing/) installations during conda environment creation, to avoid dependency conflicts, by instantiating the environment with its own [`pip`](https://pip.pypa.io/en/stable/installing/) setup, à la `conda create --name custom_venv_name pip` then [activating it](https://conda.io/docs/user-guide/tasks/manage-environments.html#activating-an-environment) (linux example: `source activate custom_venv_name`)

## Getting Started

``` python
from tapioca_cbrain import Cbrain

# assuming credentials known in advance:
api = Cbrain(cbrain_api_token="<your_api_token_string>")

# get user profile details as response object
user_response_obj = api.users(id='<your_user_id>').get()

# print user profile dict
user_data = user_response_obj().data
print user_data

# post to create a new CBrain session, and store response (with credentials)
session_payload = {'login': '<your_username_string>', 'password': '<your_password_string>'}
session_response_obj = api.session(id='').post(data=session_payload)
session_data = session_response_obj().data

# credential print statements
print session_data['cbrain_api_token']
print session_data['user_id']

```

## Jupyter Notebook

Through this simple (minimalist) wrapper, our workflow can readily take advantage of Jupyter Notebook. 

For example, listing available endpoints by typing `api.` + pressing `tab`

``` python
>>> api.
api.bourreaux                    api.data_providers               api.data_providers_browse
api.data_providers_delete        api.data_providers_isalive       api.data_providers_register
...
```

Or typing `api.users?` + presssing `enter` to get
``` python
>>> api.users?
Docstring:
Automatic generated __doc__ from resource_mapping.
Resource: {id}/
Docs: https://portal.cbrain.mcgill.ca/swagger#!/Users
...
```

## Disclaimer

Significant work remains to ensure complete api support, but this should suffice to get up & running.

A quick demo [CLI gist](https://gist.github.com/martelogan/da677da2d85f9b0b92f2f43d733e3367) demonstrates how we could automate session creation and apply this wrapper to easily expose our api to end-users.

Note also, for the sake of this project, a simple (presently unmaintained) [swagger2tapioca utility gist](https://gist.github.com/martelogan/86aa7efd83916d6d77bfca01d9c08b1b) was written to convert generic OpenAPI/Swagger v2.0(JSON) to tapioca `resource_mapping.py` files (ie. effectively automate [tapioca](http://tapioca-wrapper.readthedocs.org/en/stable/quickstart.html) wrapper creation)
