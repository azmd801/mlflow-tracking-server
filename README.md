This repo contains code base to start MLFlow server at particaular URL with integrated SQL databases and s3 bucket as backeend store, this server can be called during model training and experimentation for logginf parametres, artifacts, packaging model with prediction endpoints and registring the model


## Setting up environment
### Creating environment
``virtualenv venv``
### Activate environment
``source venv/Scripts/activate``
### Install dependencies
```pip install -r requirements.txt```

### To strat the server run

`pythoon server_run.py`