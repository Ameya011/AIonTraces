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
from hansken.trace import expand_types
from datetime import datetime, date
import os

# we define a function to do the things we wanted to do
def search_and_process(context):
    # our argument "context" is a hansken.remote.ProjectContext, see the docs
    # for what it can do other than searching for traces
    with context:
        # query was copied from Hansken Expert UI
        query = '''  '''
        # search for traces matching the query
        results = context.search(query)
        properties = expand_types(results.model,
        'account',
        'accountArchive',
        'address',
        'addressBook',
        'application',
        'applicationArchive',
        'attachment',
        'audio',
        'bookmark',
        'bookmarkArchive',
        'browserHistory',
        'browserHistoryLog',
        'calendar',
        'calendarEntry',
        'carved',
        'certificate',
        'chatConversation',
        'chatEvent',
        'chatLog',
        'chatMessage',
        'compressed',
        'connection',
        'connectionArchive',
        'contact',
        'cookie',
        'cookieArchive',
        'cryptoKey',
        'cryptoKeyPair',
        'cryptocurrencyWallet',
        'data',
        'deleted',
        'document',
        'email',
        'emailArchive',
        'emailFolder',
        'encrypted',
        'event',
        'eventLog',
        'executable',
        'file',
        'fileArchive',
        'fileTransfer',
        'fileTransferLog',
        'filesystem',
        'folder',
        'gps',
        'gpsLog',
        'image',
        'intercept',
        'interceptLocation',
'ipSession',
'dns',
'link',
'memory',
'memoryImage',
'note',
'noteFolder',
'noteArchive',
'phoneCall',
'phoneCallLog',
'picture',
'process',
'registry',
'registryEntry',
'signed',
'task',
'taskList',
'textMessage',
'textMessageArchive',
'textMessageFolder',
'thumbnail',
'thumbnailArchive',
'track',
'unallocated',
'url',
'video',
'volume',
)

        print(properties)
        properties.remove("image.description")

        properties2 = ["system.extracted."+prop for prop in properties] 

        for trace in results:
            # process the results, print some details for each trace we've found
            print(trace.uid, trace.name)
#            for prop in properties2:
#                print(prop)
#                print(trace.get(prop))
#                print(prop + "->"  + str(trace.get(prop)))
#                if isinstance(trace.get(prop), datetime):
#                    print("******************************************")
#                    exit(0)

            dates = [int(trace.get(prop).strftime("%s")) for prop in properties2 if isinstance(trace.get(prop), datetime)]
            print(dates)
            for D in dates:
                Filename = str(D)+"-"+trace.uid
                Group = D-(D%(5*60))
                GroupName = str(Group)
                n = 2
                GroupName2= "/".join([GroupName[i:i+n] for i in range(0, len(GroupName), n)])
                print (GroupName2)
                os.makedirs(GroupName2,exist_ok=True)
                with open(GroupName2+"/"+Filename,"w") as file:
                    file.write(str(trace))

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
