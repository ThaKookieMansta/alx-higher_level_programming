#!/bin/bash
# This script sends a request to a URL passed as an arg
curl -s -o /dev/null -w "%{http_code}" "$1"
