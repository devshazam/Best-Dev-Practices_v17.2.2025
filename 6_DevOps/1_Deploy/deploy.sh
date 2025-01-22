#!/bin/bash

# cd /apps/client && . ./deploy.sh
pwd
git pull
npm run build
pm2 restart index.js
pm2 save
