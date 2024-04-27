#!/bin/bash

# Getring the byte size of the HTTP response header for a given URL.
curl -so /dev/null "$1" -w "%{size_download}"
