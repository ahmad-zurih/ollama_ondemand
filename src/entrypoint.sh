#!/bin/sh
set -x
exec streamlit run /app/app.py \
	--server.port "$SERVER_PORT" \
	--browser.serverAddress "$SERVER_ADDRESS" \
	--server.baseUrlPath "$BASEURLPATH" \
	--server.headless true \
	--browser.gatherUsageStats false
