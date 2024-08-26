# Hashzap
# botao de iniciar chat
# popup para entrar no chat
# titulo: Bem vindo ao hashzap
# campo de texto -> escreva seu nome no chat
# botão: entrar no chat:
# sumir com titulo 'hashzap'
# Fechar janela (popup)
# carregar o chat:
# mensagens que já foram enviadas (chat)
# campo: digite sua mensagem
# botão: enviar
# quando entrar no chat: (aparece para todo mundo)
# a mensagem que você entrou no chat
# o campo e o botão de enviar mensagem
# a cada mensagem que você envia (aparece para todo mundo)
# Nome: Texto da Mensagem

import flet as ft


# criar a função principal do seu aplicativo
def main(pagina):
    # criar todas as funcionalidades

    # criar o elemento
    titulo = ft.Text('HasZap')

    chat = ft.Column()

    def enviar_mensagem_tunel(mensagem):
        texto_chat = ft.Text(mensagem)
        chat.controls.append(texto_chat)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        texto_mensagem = campo_mensagem.value
        nome_usuario = campo_nome_usuario.value
        mensagem = f'{nome_usuario.title()}: {texto_mensagem}'
        pagina.pubsub.send_all(mensagem)
        campo_mensagem.value = ''
        pagina.update()

    campo_mensagem = ft.TextField(
        label='Digite sua mensagem', on_submit=enviar_mensagem)
    botao_enviar_mensagem = ft.ElevatedButton(
        'Enviar', on_click=enviar_mensagem)

    linha_mensagem = ft.Row([campo_mensagem, botao_enviar_mensagem])

    def entrar_chat(evento):
        pagina.remove(titulo)
        pagina.remove(botao_iniciar)
        janela.open = False

        pagina.add(chat)
        pagina.add(linha_mensagem)
        mensagem = f'{campo_nome_usuario.value.title()} Entrou no chat'
        pagina.pubsub.send_all(mensagem)
        pagina.update()

    titulo_janela = ft.Text('Bem vindo ao HashZap')
    campo_nome_usuario = ft.TextField(
        label='Escreva seu nome no chat', on_submit=entrar_chat)
    botao_entrar = ft.ElevatedButton('Entrar no Chat', on_click=entrar_chat)
    janela = ft.AlertDialog(
        title=titulo_janela,
        content=campo_nome_usuario,
        actions=[botao_entrar])

    def iniciar_chat(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton('Iniciar Chat', on_click=iniciar_chat)

    # adicionarr o elemento na pagina
    pagina.add(titulo)
    pagina.add(botao_iniciar)


# rodar o aplicativo
ft.app(main, view=ft.WEB_BROWSER)
