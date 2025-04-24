#!/bin/bash
npm run build
docker-compose -f docker-compose.yml up --build