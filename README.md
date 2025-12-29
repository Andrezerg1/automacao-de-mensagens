# automacao-de-mensagens
Este projeto consiste em uma automação desenvolvida em Python para envio de mensagens a clientes, utilizando dados extraídos de uma planilha. A aplicação acessa uma base de dados contendo informações como nome, número de telefone e data de vencimento, e realiza o envio automatizado de mensagens personalizadas, com foco em lembretes de pagamento.

O sistema foi desenvolvido com o objetivo de automatizar tarefas repetitivas, aplicando conceitos de lógica de programação, manipulação de dados e automação de processos. A solução pode ser facilmente adaptada para diferentes contextos de comunicação empresarial.

Tecnologias Utilizadas:
Python
openpyxl
urllib
webbrowser
pyautogui

Para utilizar o sistema, é nescessário uma planilha com as informações dos clientes (nome e número de telefone).
Vale ressaltar que o número deve seguir o seguinte padrão:
(codigo do pais, DDD, 9, Número de telefone), Ex: 5543912345678
Caso contrário, o sistema não será capaz de ler e identificar o cliente.

