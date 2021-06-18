This repo is for testing the continuos integration (CI) and continuos deployment (CD) pipeline for a python (dash) based webapp.

Trying to adopt the model-view-controller (mvc) design pattern.
Link to WebApp: https://test-python-ci-cd.herokuapp.com/

CI using github actions:
1. set up remote operating system 
1. install dependencies from requirements.txt
1. analyze code with flake8 (linting)
1. run tests with unittest
1. create docs with sphinx (not jet implemented)

CD using github and Heroku
1. deploy docs with read the docs (not jet implemented)
1. deploy webapp with heroku