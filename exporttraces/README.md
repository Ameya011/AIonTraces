# AIonTraces
AI on Forensic Traces

exportall.py
------------

This tool iterates all traces in the Windows10 proficiency extraction.
The tool only stores traces that contain at least one timestamp.

Traces are stored in clusters of 5\*60 seconds.
To reduce the load on the directory structures of the filesystem a directory
hierarchy is created based on the unixtimestamp of the used trace.

A result of the method is that traces MAY be stored in multiple clusters. E.g.
a file has several timestamps, when those timestamps fall in different
clusters the file will be stored in each of these clusters.
