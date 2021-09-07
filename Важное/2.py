from kivy.app import App
from kivy.uix.image import Image

class MainApp(App):
    def build(self):
        img = Image(source='C:/Users/kopte/OneDrive/Рабочий стол/862b056ef8f41140876f00a8ee5a4148.jpg',
                    size_hint=(1, .5),
                    pos_hint={'center_x':.5, 'center_y':.5})

        return img

if __name__ == '__main__':
    app = MainApp()
    app.run()
#"C:\Users\kopte\OneDrive\Рабочий стол\862b056ef8f41140876f00a8ee5a4148.jpg"






