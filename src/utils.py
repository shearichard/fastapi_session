'''
A bunch of utility functions for use across the project
'''
import os
from datetime import datetime, timezone


def get_env_variable(var_name):
    """Get the env var value or throw an exception"""
    try:
        return os.environ[var_name]
    except KeyError as e:
        #This will only work in Python >= 3.11
        #e.add_note("Set the %s environment variable" % var_name)
        raise


def get_local_dt_iso_with_tz_info():
    # get current datetime in UTC
    dt = datetime.now(timezone.utc)
    # add local timezone information to datetime
    tz_dt = dt.astimezone()
    # Get current iso 8601 format datetime string including the default timezone
    iso_date = tz_dt.isoformat()
    #
    return(iso_date)
