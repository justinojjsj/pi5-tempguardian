# TempGuardian

## JUSTIFICATIVA DO SISTEMA

O sistema tem a função de capturar os dados via rede de um sensor de temperatura e umidade (industrial), armazenar as informações e gerar relatórios, a fim que se possa fazer uma gestão mais eficiente de energia. Dessa forma o nome TempGuardian refere-se ao guardião de temperatura, função do sistema.

## COMO CONFIGURAR OS SISTEMAS

Para funcionar os sistemas é necessário:

1. Instalar o docker desktop
  1.1.  Sistema Operacional Windows:
    1.1.1. Instalar o docker desktop;
    1.1.2. Fazer login do docker hub e conectar ao docker destop;
    1.1.3. IMPORTANTE: Reiniciar a máquina quando estiver tudo ok, antes de seguir para os próprios passos.

2. Fazer um clone no repositório https://github.com/justinojjsj/pi5-tempguardian.git
3. Criar a rede docker que será compartilhada entre os sistemas:
    ```
    docker network create --subnet=168.18.0.0/24 rede_default
    ```
4. Executar os containers docker. Existem duas formas:
- Método 1: 
    - Utilizando o power shell (windows) ou terminal (linux) acessar o diretório onde está salvo o arquivo docker-compose.yaml
    - Digitar o seguinte comando: 
    ```
    docker-compose up -d
    ```
- Método 2:
    - Instalar o VSCODE
    - Instalar o plugin docker
    - Abrir o projeto pi5-tempguardian no VSCODE
    - Encontrar o arquivo docker-compose.yaml
    - Clicar com o botão direito no arquivo e clicar em [compose-up]

5. Após estar com os containers em execução acessar o PhpmyAdmin através do navegador (usuário: root senha: tX84c=7OljSX):
    ```
    127.0.0.1:4089 
    ```
    - Criar um banco de dados com o nome: db_tempguardian
    - Importar arquivo db_DDMMYYYY.sql (mais recente) que está na pasta _db

6. Acessar o site do sistema:
    ```
    127.0.0.1:4087
    ```

7. Executar os containers e configurar o cron (esse passo não é necessário, a não ser que o sistema não esteja sendo alimentado automaticamente):
    ```
    docker exec -it tempguardian_python bash
    ```
    ```
    crontab -e
    ```
    - Selecionar opção 1 (vai selecionar o editor de texto NANO)
    - Copiar a seguinte linha ao final do arquivo (remova o espaço antes e depois)
    ```
    0,15,30,45 * * * * /app/script_executor.sh
    ```
    - Ctrl+o para salvar arquivo, Ctrol+x para sair do arquivo:
    - Digitar no terminal
    ```
    chmod u+x /app/script_executor.sh

8. Observações:

- A versão do python que está sendo instalada no container é a 3.7.5. Portanto, caso queira executar o script diretamente da sua máquina instale essa versão (ou utilize um ambiente python com essa versão pelo pyenv: https://blog.accurate.com.br/tutorial-pyenv/#Habilitando_o_ambiente_virtual_LinuxMacOs)

- Caso não queira ou possa instalar o python, utilize o próprio container para executar o script:

```
docker exec -it tempguardian_python bash
```

Em seguida execute:

```
python capture_temperature.py
```

