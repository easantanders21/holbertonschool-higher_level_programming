#!/bin/bash
# sends a request and displays all HTTP methods the server will accept.
curl -sI "$1" | grep "Allow" | awk '{print $2,$3, $4}'
