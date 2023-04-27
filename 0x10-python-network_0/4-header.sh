#!/bin/bash
# Script that sends a GET request to a URL with a header variable and displays the response body
curl -sH "X-School-User-Id:98" "$1"
