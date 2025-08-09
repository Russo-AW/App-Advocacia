import os
import firebase_admin
from firebase_admin import credentials, storage

# Caminho absoluto para o arquivo de credenciais
# Recomendo usar variável de ambiente, mas você também pode usar o nome diretamente



# Identificador do projeto e bucket (ajuste conforme seu Firebase)

STORAGE_BUCKET = 'projeto-advocacia-tales.appspot.com'

# Inicialização do Firebase Admin SDK (evita reinicializações múltiplas)
if not firebase_admin._apps:
    cred = credentials.Certificate({
        "type": "service_account",
        "project_id": os.environ.get("FIREBASE_PROJECT_ID"),
        "private_key_id": os.environ.get("FIREBASE_PRIVATE_KEY_ID"),
        "private_key": os.environ.get("FIREBASE_PRIVATE_KEY").replace("\\n", "\n"),
        "client_email": os.environ.get("FIREBASE_CLIENT_EMAIL"),
        "client_id": os.environ.get("FIREBASE_CLIENT_ID"),
        "auth_uri": os.environ.get("FIREBASE_AUTH_URI"),
        "token_uri": os.environ.get("FIREBASE_TOKEN_URI"),
        "auth_provider_x509_cert_url": os.environ.get("FIREBASE_AUTH_PROVIDER_X509_CERT_URL"),
        "client_x509_cert_url": os.environ.get("FIREBASE_CLIENT_X509_CERT_URL")
    })
    firebase_admin.initialize_app(cred, {
        'projectId': os.environ.get("FIREBASE_PROJECT_ID"),
        'storageBucket': os.environ.get("GOOGLE_CLOUD_BUCKET")
    })

# Opcional: exporta o bucket para facilitar uso em outros arquivos
firebase_storage_bucket = storage.bucket()