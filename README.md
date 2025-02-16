## Guia de Desenvolvimento com Django e Django Ninja  
  ### 📌 Requisitos
    Python instalado
    Virtualenv configurado
    Conhecimentos básicos de Django
Este documento fornece um passo a passo para configurar um ambiente de desenvolvimento Django, incluindo a instalação de bibliotecas, estruturação do projeto e execução do servidor.  
#### Observação:
#### 🔗 Integração com o Aplicativo Flet  

Este backend foi desenvolvido para ser integrado com um aplicativo frontend criado com **Flet**, permitindo a interação via API REST.  
#### link do flet:
````
https://github.com/Djohnn/App-Mobile
````
O aplicativo Flet consome os endpoints desta API para:  
- Criar alunos  
- Listar alunos cadastrados  
- Registrar aulas realizadas  
- Exibir o progresso dos alunos
- Atulizar dados do aluno 

### Configuração da Integração  

Para garantir o funcionamento correto, o backend deve estar rodando antes de iniciar o aplicativo Flet.  


##  Configuração do Ambiente  

## Para iniciar o projeto, é necessário criar um ambiente virtual, que ajuda a isolar as dependências do projeto. 

### Criar um ambiente virtual
  ```sh
  Linux: python3 -m venv venv
  Windows: python -m venv venv
  ```  
 ### Ativar o ambiente virtual 
 ```sh
  Linux: source venv/bin/activate
  Windows: venv\Scripts\Activate
  ```
O processo varia de acordo com o sistema operacional.

Após a criação do ambiente virtual, ele deve ser ativado antes da instalação das bibliotecas necessárias. 
Em alguns casos, pode ser necessário ajustar a política de execução do sistema para evitar erros.  

### 📦 Instalação das Bibliotecas 

 ```sh
pip install django
pip install pillow
pip install django-ninja
```
Com o ambiente virtual ativado, o próximo passo é instalar o Django e outras bibliotecas essenciais. 
Entre elas, estão ferramentas para o desenvolvimento de APIs e manipulação de arquivos. 

### 🚀 Criação do Projeto
 ```sh
django-admin startproject core .

```
### Rodar o servidor para testar
 ```sh
python manage.py runserver

```
### Criar um aplicativo Django chamado treino
```sh
python manage.py startapp treino
```


## 📂 Estrutura do Projeto  
````
.
├── core/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│   └── ...
├── treino/
│   ├── migrations/
│   ├── templates/
│   │   ├── base.html
│   │   ├── alunos.html
│   │   └── progresso.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── api.py
│   ├── schemas.py
│   └── serializers.py
├── media/
├── static/
│   ├── css/
│   ├── js/
│   └── img/
├── venv/
├── manage.py
└── requirements.txt

````
O projeto Django segue uma estrutura padrão, onde inicialmente é criado o diretório do projeto principal. 
Além disso, é necessário criar um aplicativo dentro do projeto para organizar funcionalidades específicas, como a gestão de alunos.  

Para definir as rotas da API, um sistema de roteamento é implementado. 
Ele facilita a organização das requisições e respostas dentro do projeto.  

## ▶ Executando o Projeto  

Após configurar o ambiente e definir a estrutura do projeto, o servidor de desenvolvimento pode ser iniciado para testar a aplicação. Isso permite validar se as configurações estão corretas e se a API está funcionando conforme o esperado.  

---

