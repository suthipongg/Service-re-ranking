#!/bin/bash

source venv/bin/activate 

pm2 del service-re-ranking
pm2 start