from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.core.text import LabelBase

class MyApp(App):
    def build(self):
        font_path = './fonts/New_Wild_Words.ttf'  # Ruta al archivo de fuente de texto
        LabelBase.register(name='New_Wild_Words', fn_regular=font_path)#registro de fuente de texto
        target_width = 2160 #ancho de la pantalla
        target_height = 1080 #alto de la pantalla
        Window.size = (target_width, target_height)#configuracion de la pantalla
        Window.rotation = 0 #rotacion de la pantalla para ponerla en horizontal
        #variables
        self.click_count=0 #contador de click's sobre el boton
        # Crear un layout principal
        self.layout = BoxLayout(orientation='vertical',spacing=10, padding=10)#configuracion de la pantalla
        self.exception_layout = BoxLayout(orientation='horizontal')#configuracion de espacio en la pantalla
        self.exception_layout1 = BoxLayout(orientation='horizontal')#configuracion de espacio en la pantalla
        self.exception_layout2 = BoxLayout(orientation='horizontal')#configuracion de espacio en la pantalla
        # Crear una etiqueta
        self.label = Label(text="Hola mundo", font_size=80 ,height=100, size_hint=(1, None),font_name='New_Wild_Words')#crea un espacio donde se coloca texto, font_size=tamaño de fuente, font_name=nombre de fuente
        # Crear un TextInput
        self.text_input = TextInput(multiline=False,font_size=30,height=110, size_hint=(1,None))#cuadro donde ingresar texto
        # Crear un botón1
        self.button1 = Button(text='aceptar',font_size=30, size_hint=(1,None),width=100,height=100,background_color=("red"),font_name='New_Wild_Words')#crea el boton especificando cada parametro
        self.button1.bind(on_press=self.read_text)#llama a una funcion que se ejecuta cuando es presionado el boton

        # Agregar la etiqueta, el TextInput y el botón al layout
        self.layout.add_widget(self.label)#agrega la linea de texto a la pantalla
        self.layout.add_widget(self.text_input)#agrega el cuadro de texto a la pantalla
        self.exception_layout.add_widget(self.button1)#pone el boton en un tipo de pantalla
        self.layout.add_widget(self.exception_layout)#vuelve visible la pantalla donde esta el boton
        return self.layout#retorna la pantalla

    def read_text(self, instance):#funcion que se ejecuta al presionar el boton
        self.exception_layout.remove_widget(self.button1)#funcion que elimina el boton de la pantalla
        texto_ingresado=self.text_input.text # variable que almacena lo escrito en el recuadro
        self.label.text=texto_ingresado#imprime en pantalla el texto ingresado
            
if __name__ == '__main__':
    MyApp().run()