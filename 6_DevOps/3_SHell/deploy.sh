#!/bin/bash

# cd /apps/client && . ./deploy.sh
echo -e "\nenter the path to directory"
git pull && npm run build
pm2 restart index.js
pm2 save
