Cadastro - Automatização de Formulário com Selenium
Este repositório contém um script em Python que utiliza a biblioteca Selenium para automatizar o preenchimento de um formulário de cadastro. O formulário está hospedado na seguinte URL: Cadastro .

Pré-requisitos
Antes de executar o script, você precisa ter instalado:

Python 3.x
Pip (gerenciador de pacotes do Python)
Google Chrome
Driver do Chrome
Instalação
Clonar ou repositório:
bater

Copiar
git clone https://github.com/seu_usuario/nome_do_repositorio.git
cd nome_do_repositorio
Instale as dependências necessárias:
bater

Copiar
pip install selenium webdriver-manager
Uso
Abra o arquivo do script: O script pode ser encontrado no arquivo cadastro.py.
Execute o script:
bater

Copiar
python cadastro.py
Descrição do Código
O script realiza as seguintes etapas:

Configure o serviço do ChromeDriver : Utilize o webdriver_managerpara gerenciar a instalação do ChromeDriver automaticamente.
Inicializa o navegador : Abre uma nova janela do Google Chrome.
Acesse a página de cadastro : Navega até a URL fornecida.
Preenche ou formulário :
Nome Completo: "João Vitor Lopes Vieira"
Cidade: "Arinos"
Estado: "Minas Gerais"
País: "Brasil"
Clique no botão de cadastro : O script simula um clique no botão de cadastro.
Aguarda alguns segundos : Permite que o usuário veja a ação antes de fechar o navegador.
Data do navegador : Encerra a sessão do navegador após 10 segundos.
Observações
Certifique-se de que o Google Chrome esteja instalado e atualizado para a versão compatível com o ChromeDriver.
O script pode ser modificado para preencher diferentes dados ou acessar outras páginas conforme necessário.
Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir um problema ou enviar uma solicitação pull.

Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.

Para mais informações ou dúvidas, entre em contato com o autor do projeto.
