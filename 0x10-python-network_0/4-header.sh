#!/bin/bash
# Sends a GET request to the URL, and displays the body of the response
curl -s -X GET "$1" -H "X-HolbertonSchool-User-Id: 98"
