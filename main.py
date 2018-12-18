# coding: utf-8

import kivy
kivy.require("1.9.1")

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.properties import ObjectProperty, StringProperty
import socket, time
Window.clearcolor = get_color_from_hex("#b5b6b7")
#COMENTAR A LINHA ABAIXO AO GERAR O APK
Window.size = (450, 600)

kvcode = """

#:import C kivy.utils.get_color_from_hex

ScreenManager:
    Tela1:
        name: 'tela_1'
    Tela2:
        name: 'tela_2'
    Tela3:
        name: 'tela_3'
    Tela4:
        name: 'tela_4'

<Tela1>:
    FloatLayout:
        orientation: 'vertical'
        
        Label:
            text: 'QS - Que solo é?'
            font_size: '35sp'
            font_blended: True
            font_hinting: "mono"
            font_kerning: True
            font_name: 'DejaVuSans'
            bold: True
            color: C("#000c23")
            size_hint: .1, .1
            pos_hint: {"x": .45, "top":1}
            
        Button:
            text: 'Conectar Dispositivo'
            size_hint: .6, .15
            pos_hint: {"x": .2, "top": .8}
            background_color: C("#2365a8")
            background_normal: ""
            # on_release: root.conectar_servidor()
            on_release: root.manager.current = 'tela_2'
        
        Button:
            text: 'Análise'
            size_hint: .6, .15
            pos_hint: {"x": .2, "top": .55}
            background_color: C("#2365a8")
            background_normal: ""
            #on_press: root.troca_texto()
            on_release: root.manager.current = 'tela_4'
            #on_release: root.solicitar_servidor()
            
        Button:
            text: 'Desligar dispositivo'
            size_hint: .6, .15
            pos_hint: {"x": .2, "top": .3}
            background_color: C("#2365a8")
            background_normal: ""
            on_release: root.manager.current = 'tela_3'

<Tela2>:
    FloatLayout:
        Button:
            text: 'Voltar'
            size_hint: .6, .12
            pos_hint: {"x":.2, "top": .9}
            on_release: root.manager.current = 'tela_1'
            background_color: C("#25b270")
            background_normal: "" 
        
        Button:
            text: 'Conectar'
            size_hint: .6, .3
            pos_hint: {"x": .2, "top":.7 }
            background_color: C("#2365a8")
            background_normal: ""
            on_release: root.conectar_servidor()
        
        Label:
            text: root.textoConectar
            font_size: '30sp'
            font_blended: True
            font_hinting: "mono"
            font_kerning: True
            font_name: 'DejaVuSans'
            bold: True
            color: C("#000000")
            # color: C("#ffffff")
            size_hint: .9, .1
            pos_hint: {"x": .05, "top":.2}
            # canvas.before:
            #     Color:
            #         rgba: C("#000000")
            #     Rectangle:
            #         pos: self.pos
            #         size: self.size
                
<Tela3>:
    FloatLayout:
        Label:
            text: 'Deseja realmente desativar o dispositivo?'
            # text: root.msg_tela3
            font_size: '35sp'
            font_blended: True
            font_hinting: "mono"
            font_kerning: True
            font_name: 'DejaVuSans'
            bold: True
            # color: C("#ffffff")
            color: C("#050011")
            text_size: self.width, None
            size_hint: .8, None
            height: self.texture_size[1]
            pos_hint: {"x": .1, "top": .95}
            # canvas.before:
            #     Color:
            #         rgba: C("#04265b")
            #     Rectangle:
            #         pos: self.pos
            #         size: self.size
        
        Button:
            text: 'Voltar'
            size_hint: .8, .12
            pos_hint: {"x":.1, "top": .7}
            on_release:
                root.limpa_textoDesligar() 
                root.manager.current = 'tela_1'
            background_color: C("#25b270")
            background_normal: ""
        
        Button:
            text: 'Sim'
            # font_size: '30sp'
            size_hint: .8, .16
            pos_hint: {"x":.1, "top": .55}
            # on_release: self.func_teste()
            on_release: root.desligar_dispositivo()
            background_color: C("#2365a8")
            background_normal: "" 
            
        Button:
            text: 'Não'
            size_hint: .8, .16
            pos_hint: {"x":.1, "top": .35}
            on_release:
                root.limpa_textoDesligar() 
                root.manager.current = 'tela_1'
            background_color: C("#bc0f1d")
            background_normal: ""
        
        Label:
            text: root.textoDesligar
            font_size: '30sp'
            font_blended: True
            font_hinting: "mono"
            font_kerning: True
            font_name: 'DejaVuSans'
            bold: True
            color: C("#000000")
            size_hint: .9, .1
            pos_hint: {"x": .05, "top":.15}
            
<Tela4>:
    FloatLayout:
        Button:
            text: 'Voltar'
            size_hint: .6, .12
            pos_hint: {"x":.2, "top": .9}
            on_release: 
                root.limpa_textoAnalise()
                root.manager.current = 'tela_1'
            background_color: C("#25b270")
            background_normal: "" 
            
        Button:
            text: 'Executar Análise'
            size_hint: .6, .12
            pos_hint: {"x": .2, "top": .7}
            background_color: C("#2365a8")
            background_normal: ""
            on_release: root.executar_analise()
        
        Label:
            text: 'Resultado:'
            font_size: '40sp'
            font_blended: True
            font_hinting: "mono"
            font_kerning: True
            font_name: 'DejaVuSans'
            bold: True
            color: C("#000000")
            size_hint: .9, .1
            pos_hint: {"x": .05, "top":.5}
            
        Label:
            text: root.textoAnalise
            font_size: '30sp'
            font_blended: True
            font_hinting: "mono"
            font_kerning: True
            font_name: 'DejaVuSans'
            bold: True
            color: C("#000000")
            text_size: self.width, None
            size_hint: .9, .1
            height: self.texture_size[1]
            pos_hint: {"x": .05, "top":.35}
"""

class Pai(Screen):
    s = socket.socket()
    # host = '192.168.42.1'
    host = '127.0.0.1'
    port = 7000

    textoAnalise = StringProperty('')
    textoConectar = StringProperty('Desconectado')
    textoDesligar =  StringProperty('')

    def conectar_servidor(self):

        try:
            # print(self.textoConectar)
            if(self.textoConectar != 'Dispositivo Conectado'):
                self.s.connect((self.host, self.port))
                data = self.s.recv(1024).decode()
                data_str = str(data)
                self.textoConectar = ('Dispositivo Conectado')
        except:
            self.textoConectar = ('Impossível conectar')

    def executar_analise(self):
        try:
            self.s.send('Analise'.encode())
            var = self.receber_dados_servidor()
            self.textoAnalise = var
        except:
            self.textoAnalise = 'ERRO - Verifique sua conexão'

    def desligar_dispositivo(self):
        try:
            self.s.send('Desligar'.encode())
            time.sleep(12)
            self.textoDesligar = 'Dispositivo Desligado'
            # self.textoDesligar = 'Desligando...'
        except:
            self.textoDesligar = 'Dispositivo OFFLINE'

    def limpa_textoAnalise(self):
        self.textoAnalise = ''

    def s(self):
        self.textoDesligar = 'Desligado'

    def func_teste(self):
        self.textoDesligar = 'Desligando...'
        # Clock.schedule_once(s ,5)


    def limpa_textoDesligar(self):
        self.textoDesligar = ''

    def solicitar_servidor(self):
        self.s.send('Analise'.encode())
        self.receber_dados_servidor()

    def receber_dados_servidor(self):
        reply = self.s.recv(1024).decode()
        reply_str = str(reply)
        return reply_str
        #print(reply_str)

class Tela1(Pai):
    pass

class Tela2(Pai):
    pass

class Tela3(Pai):
    pass

class Tela4(Pai):
    pass

class QSApp(App):
    textoAnalise = StringProperty('Realizar Análise')

    def build(self):
        self.icon = "qs.png"
        self.title = "QS - Que solo é?"
        return Builder.load_string(kvcode)


if __name__ == "__main__":
    QSApp().run()