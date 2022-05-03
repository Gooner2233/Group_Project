import kivy
import image_io
#importing calculations file that I wrote for our magic colour theory formula
from Calculate import drip
#importing my own recommendation algorithm
from Calculate import recommendation
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.camera import Camera
from kivy.lang import Builder


class Layout(GridLayout):
    def __init__(self, **kwargs):
        super(Layout, self).__init__(**kwargs)
        #inner grid

        self.inside = GridLayout()
        #styling
        presetation = Builder.load_file("cam.kv")
        self.inside.cols = 2
        self.inside.add_widget(Label(text="Who are we checking out today? "))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)
        self.inside.add_widget(Label(text="I am going..."))
        self.activity = TextInput(multiline=False)
        self.inside.add_widget(self.activity)

        # initializing a camera object
        self.camera_object = Camera(play=False)
        self.camera_object.play = True
        self.camera_object.resolution = (300, 600)  # resolution
        # button for snapping photo and beginning drip analysis algorithm
        self.camara_button = Button(text="Rate my drip!")
        self.camara_button.size_hint = (.5, .2)
        self.camara_button.pos_hint = {'x': .25, 'y': .75}
        # binding
        self.camara_button.bind(on_press=self.onCameraClick)
        # adding camera object to the grid

        self.add_widget(self.inside)
        self.add_widget(Image(source="Logo.JPG"))
        self.add_widget(self.camera_object)
        self.add_widget(self.camara_button)
        self.cols = 1
        self.rating = TextInput(multiline=False)
        self.add_widget(self.rating)


    def onCameraClick(self, *args):
        self.camera_object.export_to_png('./selfie.png')
        name = self.name.text
        activity = self.activity.text
        im = image_io.read_file("selfie.png")
        drip_rating = drip(im)
        recommend = recommendation(im)
        if name != "" and activity != "":
            self.rating.text = ""
            self.rating.text += "You're drip rating is: " + str(drip_rating)
            if drip_rating > 5:
                self.rating.text += f" Woof! Looking great {name}, you're going to look good going {activity}. \n Eventhough you look great, think about toning down " \
                                    f"the {recommend[0]} in the top half of your outfit and the {recommend[1]} in the bottom half!"
            else:
                self.rating.text += f" Yikes. Drip or drown. You are drowning! {name} if you go {activity} looking like that you'll get exposed! \nTrust us" \
                                    f" and tone down " \
                                    f"the {recommend[0]} in the top half of your outfit and the {recommend[1]} in the bottom half! Embarrassing!"
        else:
            self.rating.text += f'Please let us know who you are and where you are going!'
        #clearing the fields after execution
        self.name.text = ""
        self.activity.text = ""
class IsItDrip(App):
    def build(self):
        return Layout()

if __name__ == "__main__":
    IsItDrip().run()
