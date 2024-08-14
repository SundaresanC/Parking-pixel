from kivy.uix.floatlayout import FloatLayout
from kivy.properties import BooleanProperty, StringProperty
import os
import tkinter as tk
import tkinter.filedialog
from final import run, regionconversion
from set_regions import SmartCarParking
from kivymd.app import MDApp

overallcount = 0
total = 0
def select_video_file():
    root = tk.Tk()
    root.withdraw()
    file_path = tk.filedialog.askopenfilename(filetypes=[('Video files', '*.mp4 *.avi *.mkv')])
    root.destroy()
    return file_path


class MyWidget(FloatLayout):
    condition_met = BooleanProperty(False)
    video_path = StringProperty('')
    region_file_path = StringProperty('')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.font_name = 'RussoOne-Regular.ttf'

    def select_video(self):
        # Create a file chooser to select a video file
        root = tk.Tk()
        root.withdraw()
        file_path = tk.filedialog.askopenfilename(filetypes=[('Video files', '*.mp4 *.avi *.mkv')])
        root.destroy()
        print(file_path)
        self.video_path = file_path

        region_file = self.video_path.rsplit('.', 1)[0] + '.p'
        if not os.path.exists(region_file):
            self.set_region_file_path()
        else:
            self.region_file_path = region_file
        print(region_file)
        print(self.video_path)
        self.condition_met = True
        self.update_visibility()

    def set_region_file_path(self):
        # Example function for setting the region file path
        self.region_file_path = self.video_path.rsplit('.', 1)[0] + '.p'
        # Implement the logic to set regions here
        app = SmartCarParking(self.video_path, self.region_file_path)
        app.run1()
        print(f"Setting region for video: {self.video_path}")
        print(f"Region file path: {self.region_file_path}")

    def set_region(self):
        # Implement the logic to set regions here
        print(f"Setting region with file path: {self.region_file_path}")
        app = SmartCarParking(self.video_path, self.region_file_path)
        app.run1()
        self.detect()

    def detect(self):
        # Implement the logic for detection here
        region_source = regionconversion(self.region_file_path)
        global overallcount
        global total
        total += len(region_source)
        run(self.video_path, region_source,overallcount,total)
        print(f"Detecting in video: {self.video_path}")


    def update_visibility(self):
        for button in [self.ids.btn2, self.ids.btn3]:
            button.opacity = 1 if self.condition_met else 0
            button.disabled = not self.condition_met


class MyApp(MDApp):
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    MyApp().run()
