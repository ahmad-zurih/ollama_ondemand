#!/bin/sh
set -x

# Start the Ollama server in the background
ollama serve &
sleep 10

# Start Streamlit
exec streamlit run /app/app.py \
	--server.port "$SERVER_PORT" \
	--server.address 0.0.0.0 \
	--browser.serverAddress "$SERVER_ADDRESS" \
	--server.baseUrlPath "$BASEURLPATH" \
	--server.headless true \
	--browser.gatherUsageStats false
