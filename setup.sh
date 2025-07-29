
#!/usr/bin/env bash
set -e

# Cria ambiente virtual
python3 -m venv venv
source venv/bin/activate

# Atualiza pip e instala dependências
pip install --upgrade pip
pip install -r requirements.txt

# Inicializa repositório Git
git init
echo "venv/" >> .gitignore

echo "Configuração concluída. Copie config.py.example para config.py e ajuste as credenciais."

