'''
A bunch of utility functions for use across the project
'''
import os


def get_env_variable(var_name):
    """Get the env var value or throw an exception"""
    try:
        return os.environ[var_name]
    except KeyError as e:
        #This will only work in Python >= 3.11
        #e.add_note("Set the %s environment variable" % var_name)
        raise
