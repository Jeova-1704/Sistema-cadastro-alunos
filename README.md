# Sistema de Registro de Alunos 
Este é um Sistema de Registro de Alunos desenvolvido em Python usando a biblioteca Tkinter para a interface gráfica, o Pillow para manipulação de imagens e o Tkcalendar para seleção de datas. O sistema permite que você cadastre, visualize, atualize e exclua informações de alunos em um banco de dados SQLite.

## Tela inicial:
![Captura de tela_20230722_225721](https://github.com/Jeova-1704/Sistema-cadastro-alunos/assets/127805808/b559402a-ae46-4a2e-b18f-879082a228dc)

## Inserido dados:
Primeiro você insere os dados para cadastar no sistema e respectivamente no banco de dados:
![Captura de tela_20230722_225846](https://github.com/Jeova-1704/Sistema-cadastro-alunos/assets/127805808/2ad9c959-d0f1-4dd0-99fb-5d6321247776)

Após inserir todos os dados, apertar em "Adicionar" e você será registado com suecesso.
![Captura de tela_20230722_225902](https://github.com/Jeova-1704/Sistema-cadastro-alunos/assets/127805808/cbf549fa-89e9-416e-984c-d8f7df8073c1)

## Atualizando dados:
Primeiro você insere o id do perfil que deseja atualizar os dados e após isso aperta em procurar e edita os dados.
![Captura de tela_20230722_230013](https://github.com/Jeova-1704/Sistema-cadastro-alunos/assets/127805808/7c2d7a74-2c03-4bfc-9bf6-3dbe49cefbcf)

Após editar os dados aperta em "Atualizar" e os dados serão atualizados com sucesso.
![Captura de tela_20230722_230034](https://github.com/Jeova-1704/Sistema-cadastro-alunos/assets/127805808/e1b94583-4c23-43e9-af89-8b7c4e311739)

## deletando dados:
Adicionna o Id do perfil que deseja deletar
![Captura de tela_20230722_230055](https://github.com/Jeova-1704/Sistema-cadastro-alunos/assets/127805808/2be50d40-cc56-4031-b716-082843ea7213)

Após isso aperta em deletar e o usuario sera deletado com sucesso
![Captura de tela_20230722_225721](https://github.com/Jeova-1704/Sistema-cadastro-alunos/assets/127805808/1ea8868b-e4f0-4bf9-8a1e-636bbff8e7b6)



# Requisitos
Antes de executar o programa, certifique-se de ter instalado as seguintes bibliotecas:

- tkinter
- pillow
- tkcalendar
- sqlite3

Para instalar as bibliotecas, você pode usar o gerenciador de pacotes pip:
- `pip install tkcalendar`
- `pip install pillow`
- `pip install tkinter`


# O projeto é composto por dois arquivos principais:

1. main.py
Este arquivo contém toda a lógica da interface gráfica e é responsável por criar a janela principal, os frames, campos de entrada, botões e tabelas. Além disso, ele importa o segundo arquivo bd.py, que contém a classe SistemaDeRegistro, responsável pelas operações CRUD (Create, Read, Update, Delete) no banco de dados.

2. bd.py
Neste arquivo, está definida a classe SistemaDeRegistro, que gerencia as operações no banco de dados. A classe é inicializada com uma conexão ao banco de dados SQLite (estudante.db) e possui os seguintes métodos:

- create_table(): Cria a tabela estudantes se ela ainda não existir.
register_student(estudante): Insere um novo aluno no banco de dados com as informações fornecidas.
- view_all_students(): Retorna uma lista com todos os alunos cadastrados no banco de dados.
- searsh_studant(id): Procura um aluno pelo ID e retorna suas informações.
- update_studants(novos_valores): Atualiza as informações de um aluno existente com os novos valores fornecidos.
- delete_studante(id): Deleta um aluno do banco de dados pelo ID.
## Execução
Para executar o sistema, basta executar o arquivo main.py.
`python main.py`

## Interface Gráfica
A interface do sistema é composta por uma janela principal onde são exibidos os campos para cadastro de alunos, uma tabela para visualização dos alunos cadastrados e botões para realizar as operações de adicionar, atualizar e excluir alunos.

## A janela possui os seguintes campos para preenchimento:

- Nome: Nome do aluno (campo obrigatório).
- Email: Endereço de email do aluno (campo obrigatório).
- Telefone: Número de telefone do aluno (campo obrigatório).
- Sexo: Sexo do aluno, selecionado através de um menu suspenso com as opções "M" (masculino), "F" (feminino) e "T" (outros).
- Data de Nascimento: Data de nascimento do aluno, selecionada através de um calendário.
- Endereço: Endereço do aluno (campo obrigatório).
- Curso: Curso do aluno, selecionado através de um menu suspenso com diversas opções.
- Carregar Foto: Permite ao usuário carregar uma foto do aluno (opcional).
Screenshot

# Funcionalidades do Sistema de Registro de Alunos
O Sistema de Registro de Alunos possui as seguintes funcionalidades:
### - Adicionar Aluno
Permite adicionar um novo aluno ao sistema fornecendo informações como nome, email, telefone, sexo, data de nascimento, endereço, curso e uma foto opcional. Antes de adicionar um novo aluno, os campos obrigatórios (nome, email, telefone e endereço) devem ser preenchidos. Após o cadastro, uma mensagem de sucesso é exibida.
### - Visualizar Alunos
Exibe todos os alunos cadastrados em uma tabela com colunas para ID, Nome, Email, Telefone, Sexo, Data de Nascimento, Endereço e Curso. Os dados dos alunos são obtidos do banco de dados SQLite e apresentados de forma organizada na tabela.
### - Procurar Aluno
Permite procurar um aluno específico pelo seu ID. Ao inserir o ID do aluno no campo "Procurar aluno [Inserir ID]" e clicar no botão "Procurar", as informações desse aluno são exibidas nos campos de entrada, permitindo a visualização e edição dos dados.
### - Atualizar Aluno
Permite atualizar as informações de um aluno existente. Após procurar o aluno pelo ID, as informações preenchidas são atualizadas no banco de dados. É possível modificar os dados do aluno nos campos de entrada e, em seguida, clicar no botão "Atualizar" para salvar as alterações. Uma mensagem de sucesso é exibida após a atualização.
### - Deletar Aluno
Permite deletar um aluno do sistema. Após procurar o aluno pelo ID, o botão "Deletar" exclui permanentemente o aluno do banco de dados. Uma mensagem de sucesso é exibida após a exclusão.
### - Escolher Foto do Aluno
Permite ao usuário carregar uma foto do aluno a ser cadastrado. A foto é exibida em um espaço reservado no formulário de cadastro. A foto é opcional e não é um campo obrigatório.












## Operações CRUD
O sistema oferece quatro operações básicas para manipulação dos dados dos alunos no banco de dados, conhecidas como CRUD (Create, Read, Update e Delete):

1. Create (Criar)
O botão "Adicionar" permite inserir um novo aluno no banco de dados.
Antes de adicionar um novo aluno, os campos marcados com "*" (Nome, Email, Telefone, Endereço) devem ser preenchidos.
2. Read (Ler)
Os alunos cadastrados são exibidos na tabela, mostrando suas informações como ID, Nome, Email, Telefone, Sexo, Data de Nascimento, Endereço e Curso.
3. Update (Atualizar)
O botão "Atualizar" permite modificar as informações de um aluno existente.
Para atualizar um aluno, primeiro é necessário procurar o aluno pelo seu ID, preenchendo o campo "Procurar aluno [Inserir ID]" e clicando no botão "Procurar".
Uma vez que o aluno seja encontrado, as informações são preenchidas automaticamente nos campos de entrada. É possível modificar as informações e, em seguida, clicar em "Atualizar" para salvar as alterações.
4. Delete (Deletar)
O botão "Deletar" permite excluir um aluno do sistema.
Para deletar um aluno, primeiro é necessário procurá-lo pelo seu ID, preenchendo o campo "Procurar aluno [Inserir ID]" e clicando no botão "Procurar".
Clique em "Deletar" para remover o aluno do banco de dados.
Observações
Os campos marcados com "*" são obrigatórios e devem ser preenchidos antes de adicionar um novo aluno.
As imagens dos alunos são armazenadas em formato de texto (caminho do arquivo) no banco de dados.
Este é um projeto simples, e pode ser aprimorado de diversas maneiras. Fique à vontade para modificar, expandir e melhorar o código de acordo com suas necessidades e criatividade.


# Conclusão
O Sistema de Registro de Alunos oferece uma maneira simples de gerenciar informações de alunos em um banco de dados SQLite usando uma interface gráfica amigável. Ele pode ser útil para pequenas aplicações que necessitem de um sistema de cadastro e controle de informações de alunos. Você pode personalizá-lo e adaptá-lo conforme suas necessidades específicas. Se tiver alguma dúvida ou sugestão de melhoria, sinta-se à vontade para entrar em contato.
