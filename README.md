# Aplicativo de Blog

Este é um aplicativo de blog simples construído em Flask, onde os usuários podem criar postagens, comentar nas postagens de outros usuários e interagir com as postagens usando curtidas. O aplicativo possui um sistema de autenticação para registrar e fazer login como usuário.

# Funcionalidades

Registro de usuário com validação de entrada.
Login de usuário com autenticação de senha segura.
Criação de postagens pelos usuários autenticados.
Exclusão de postagens pelo autor da postagem.
Comentários em postagens existentes.
Exclusão de comentários pelo autor do comentário ou pelo autor da postagem.
Interagir com postagens usando curtidas.
Interface amigável ao usuário.

# Tecnologias utilizadas

Flask: um framework web em Python.
SQLAlchemy: uma biblioteca ORM (Object-Relational Mapping) para interagir com o banco de dados SQLite.
Flask-Login: uma extensão do Flask para gerenciamento de sessões e autenticação de usuários.
Werkzeug: uma biblioteca para segurança de senhas.

# Pré-requisitos

Python 3.x
Flask e suas dependências (instaladas via pip)
SQLAlchemy (instalado via pip)

# Como executar o aplicativo

Clone este repositório para o seu ambiente local.
Instale as dependências necessárias listadas no arquivo requirements.txt.
Execute o arquivo app.py para iniciar o aplicativo.
Acesse o aplicativo em seu navegador em http://localhost:5000.

# Personalização

O aplicativo pode ser personalizado modificando os templates HTML localizados na pasta templates.
Você pode estilizar a aparência do aplicativo editando os arquivos CSS na pasta static/css.
Para personalizar ainda mais o aplicativo, você pode modificar a lógica dos roteadores em views.py e os modelos de banco de dados em models.py.

# Observações

Este é um aplicativo de blog básico, e mais recursos avançados podem ser adicionados, como pesquisa de postagens, ordenação por data, páginas de perfil do usuário, etc.

O aplicativo usa um banco de dados SQLite, que é adequado para fins de desenvolvimento e testes. Para um ambiente de produção, é recomendado usar um banco de dados mais robusto, como o MySQL ou PostgreSQL.

# Autor
Valter Neto

# Licença
Este projeto está licenciado sob a Licença MIT.
