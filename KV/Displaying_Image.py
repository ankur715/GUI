# Displaying an Image

from kivy.app import App
from kivy.uix.image import Image, AsyncImage

class MainApp(App):
    def build(self):
        img = Image(source='kivy.png',
                    #   https://miro.medium.com/max/785/1*NfDLXFFLp79soRwo7nPifQ.png
                    size_hint=(1, .5),
                    pos_hint={'center_x':.5, 'center_y':.5})
        img2 = AsyncImage(source="https://miro.medium.com/max/785/1*NfDLXFFLp79soRwo7nPifQ.png")

        return img

if __name__ == '__main__':
    app = MainApp()
    app.run()

