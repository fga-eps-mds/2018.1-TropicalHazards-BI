#!/bin/bash


# Start python script on background
python3 /setup-files/metabase_setup.py &

# Starting metabase
/app/run_metabase.sh $@


