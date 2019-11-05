#!/usr/bin/env python3
# encoding=utf-8

# NOTE: this template script uses Python 3 syntax, edit the hashbang above
#       or use __future__ imports if you'll be running this using Python 2

# script downloaded from Hansken Expert UI (version master-333, 2019-10-02T08:05:03.592Z)
# with Hansken (build 34.5.1, 2019-10-01T11:46:42.492Z)
# see https://frontend01.prod.hansken.holmes.nl/docs/python/ for additional information

# this template script will read connection and authentication details from
# both the command line and environment variables, see
#   python3 [this_script.py] --help
# and the documentation to learn more

from hansken.tool import run


# we define a function to do the things we wanted to do
def search_and_process(context):
    # our argument "context" is a hansken.remote.ProjectContext, see the docs
    # for what it can do other than searching for traces
    with context:
        # query was copied from Hansken Expert UI
        query = '''  '''
        # search for traces matching the query
        results = context.search(query)

        for trace in results:
            # process the results, print some details for each trace we've found
            print(trace.uid, trace.name)
            print(trace)
            #print(trace.dates)


# call the hansken.py command line, but make it call our function
run(with_context=search_and_process,
    # the gatekeeper REST endpoint when this script was exported, note that
    # this can be overridden by passing -e/--endpoint on the command line
    endpoint='https://gatekeeper01.prod.hansken.holmes.nl/gatekeeper/',
    # the keystore REST endpoint when this script was exported, note that
    # this can be overridden with --keystore
    keystore='https://keystore01.prod.hansken.holmes.nl/keystore/',
    # the project id of the project named "Proficiency Test Windows 10",
    project='69788e12-2da6-42e5-a0b9-f5d40f690930')
