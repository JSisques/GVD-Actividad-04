# Configuración
cd /opt/bitnami/spark;
python -m venv venv;
source venv/bin/activate;
pip install -r requirements.txt;
# mkdir -p /root/.kaggle
# touch /root/.kaggle/kaggle.json
# chmod 600 /root/.kaggle/kaggle.json

# Descarga del dataset

# Procesamiento de datos
python ./code/process.py

# Jupyter

