# Wait for the Streamlit server to start
echo "Waiting for Streamlit server to open port ${port}..."
echo "TIMING - Starting wait at: $(date)"
if wait_until_port_used "${host}:${port}" 120; then
  echo "Discovered Streamlit server listening on port ${port}!"
  echo "TIMING - Wait ended at: $(date)"
else
  echo "Timed out waiting for Streamlit server to open port ${port}!"
  echo "TIMING - Wait ended at: $(date)"
  pkill -P ${SCRIPT_PID}
  clean_up 1
fi
sleep 2
