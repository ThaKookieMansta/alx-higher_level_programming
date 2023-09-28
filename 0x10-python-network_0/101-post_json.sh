#!/bin/bash
# This script sends a JSON post to a url passed as an arg
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
