#!/bin/bash
# This script displays the byte size of a http response
curl -s "$1" | wc -c
