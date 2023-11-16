#! /bin/bash
pip install -r /opt/requirements.txt
pip install pip install --upgrade transformers accelerate datasets[audio]

# ls -l /app
streamlit run /app/transcripcion.py --server.port=8080
