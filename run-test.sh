#!/bin/bash
echo "Running local server"
python wsgi.py &
echo "Sleeping for 3 seconds"
sleep 3
echo "Setting dev env"
export IS_DEV=True
echo "Running test.."
test-resurface --request "python" --app-name "aiohttp-test-app"
