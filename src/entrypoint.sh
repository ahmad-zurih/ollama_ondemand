#!/bin/sh
set -x

# Start the Ollama server in the background
ollama serve &
sleep 10

# Start Streamlit
exec streamlit run /app/app.py \
	--browser.serverAddress "$SERVER_ADDRESS" \
	--server.baseUrlPath "$BASEURLPATH" \
	--server.headless true \
	--browser.gatherUsageStats false

	# --server.port "$SERVER_PORT" \
	# --browser.serverAddress "$SERVER_ADDRESS" \
	# --server.baseUrlPath "$BASEURLPATH" \
	# --server.headless true \
	# --browser.gatherUsageStats false
