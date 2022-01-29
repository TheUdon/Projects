import tkinter
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import *
from PIL import Image, ImageTk

THEME_COLOR = "#252A34"
FONT = ("Arial", 20, "italic")

# ---------------------------------------------Setting up the UI--------------------------------------------- #
class WatermarkApp:
    def __init__(self):
        self.window = Tk()
        self.window.title("Watermarking App")
        self.window.config(padx=50, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(height=900, width=1600, bg="white", highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=3, pady=30)

        self.canvas_img = Image.open("imgs/placeholder.png")
        self.canvas_img = self.canvas_img.resize((1600, 900))
        self.image = ImageTk.PhotoImage(self.canvas_img)
        self.label = Label(self.window, image=self.image, borderwidth=2)
        self.label.image = self.image
        self.label.grid(column=0, row=1, columnspan=3)

        self.upload_text = tkinter.StringVar()
        self.upload_file_button = Button(textvariable=self.upload_text, command=self.upload_file, width=20, font="Ariel")
        self.upload_text.set("Upload Image")
        self.upload_file_button.grid(column=0, row=3, sticky=W, pady=5)

        self.watermark_text = tkinter.StringVar()
        self.watermark_button = Button(width=20, command=self.add_watermark, textvariable=self.watermark_text, font="Ariel")
        self.watermark_text.set("Uplaod Watermark")
        self.watermark_button.grid(column=0, row=4, sticky=W)

        self.save_text = tkinter.StringVar()
        self.save_button = Button(width=20, command=self.save, textvariable=self.save_text, font="Ariel")
        self.save_text.set("Save Image")
        self.save_button.grid(column=0, row=5, columnspan=2, sticky=W, pady=5)

        self.quit_button = Button(width=20, text="Quit", command=self.finish, font="Ariel")
        self.quit_button.grid(column=2, row=5, sticky=E)

        self.complete_text = tkinter.StringVar()
        self.complete_text.set(" ")
        self.complete_label = tkinter.Label(self.window, textvariable=self.complete_text, background=THEME_COLOR, font="Ariel", fg="white")
        self.complete_label.grid(column=1, row=4)

        self.window.mainloop()

    # ----------------------------------Developing the functions of the buttons---------------------------------- #
    def add_watermark(self):
        self.watermark_text.set("Browsing...")
        watermark_image = askopenfilename(initialdir=".../Documents", title="Select a Watermark",
                                          filetype=(("jpg files", "*.jpg"), ("all files", "*.*")))
        self.original_watermark_combine = Image.open(watermark_image).convert("RGBA")
        self.original_watermark = ImageTk.PhotoImage(Image.open(watermark_image))
        if watermark_image:
            watermark_image = Image.open(watermark_image)
            if watermark_image.size[0] > self.upload_img.width() or watermark_image.size[1] > self.upload_img.height():
                wider_width = watermark_image.size[0] / self.upload_img.width()
                taller_height = watermark_image.size[1] / self.upload_img.height()
                if wider_width >= taller_height:
                    watermark_image = watermark_image.resize(
                        (int(watermark_image.size[0] / (5 * wider_width)), int(watermark_image.size[1] / (5 * wider_width))))
                else:
                    watermark_image = watermark_image.resize(
                        (int(watermark_image.size[0] / (5 * taller_height)), int(watermark_image.size[1] / (5 * taller_height))))
            else:
                watermark_image = watermark_image.resize(
                    (int(self.upload_img.width() / 5), int(self.upload_img.height() / 5)))
        self.scale_original()
        self.wm_img = ImageTk.PhotoImage(watermark_image)
        self.wm_img_for_combining = watermark_image.convert("RGBA")
        self.label.config(image="")

        position = (self.upload_img.width() - self.wm_img.width(), self.upload_img.height() - self.wm_img.height())
        transparent = Image.new('RGBA', (self.upload_img.width(), self.upload_img.height()), (0, 0, 0, 0))
        transparent.paste(self.img_for_combining, (0, 0))
        transparent.paste(self.wm_img_for_combining, position, mask=self.wm_img_for_combining)
        self.transparent = ImageTk.PhotoImage(transparent)
        self.label = Label(self.window, image=self.transparent, borderwidth=0)
        self.label.image = transparent
        self.label.grid(column=1, row=1)
        self.watermark_text.set("Upload Watermark")

    def upload_file(self):
        self.complete_text.set(" ")
        self.upload_text.set("Browsing...")
        photo = askopenfilename(initialdir=".../Documents", title="Select an Image",
                                filetype=(("jpg files", "*.jpg"), ("all files", "*.*")))
        self.photo = photo
        self.original_upload_combine = Image.open(photo).convert("RGBA")
        self.original_upload = ImageTk.PhotoImage(Image.open(photo))
        if photo:
            upload_img = Image.open(photo)
            if upload_img.size[0] > self.canvas.winfo_width() or upload_img.size[1] > self.canvas.winfo_height():
                wider_width = upload_img.size[0]/self.canvas.winfo_width()
                taller_height = upload_img.size[1]/self.canvas.winfo_height()
                if wider_width >= taller_height:
                    upload_img = upload_img.resize((int(upload_img.size[0]/wider_width), int(upload_img.size[1]/wider_width)))
                else:
                    upload_img = upload_img.resize((int(upload_img.size[0] / taller_height), int(upload_img.size[1] / taller_height)))

            self.upload_img = ImageTk.PhotoImage(upload_img)
            self.img_for_combining = upload_img.convert("RGBA")
            self.label.config(image="")
            self.label = Label(self.window, image=self.upload_img, borderwidth=0)
            self.label.image = upload_img
            self.label.grid(column=1, row=1)

        self.upload_text.set("Upload Image")

    def save(self):
        self.save_text.set("Saving...")
        finished_img = self.original_transparent.convert("RGB")
        finished_img_name = self.photo[:-4] + " WM.jpg"
        finished_img.save(finished_img_name)
        self.complete_text.set("Your image has been saved!")
        self.save_text.set("Save Image")

    def scale_original(self):
        if self.original_watermark.width() > self.original_upload.width() or self.original_watermark.height() > self.original_upload.height():
            wider_width = self.original_watermark.width() / self.original_upload.width()
            taller_height = self.original_watermark.height() / self.original_upload.height()
            if wider_width >= taller_height:
                self.original_watermark_combine = self.original_watermark_combine.resize(
                    (int(self.original_watermark_combine.size[0] / (5 * wider_width)),
                     int(self.original_watermark_combine.size[1] / (5 * wider_width))))
            else:
                self.original_watermark_combine = self.original_watermark_combine.resize(
                    (int(self.original_watermark_combine.size[0] / (5 * taller_height)),
                     int(self.original_watermark_combine.size[1] / (5 * taller_height))))
        else:
            self.original_watermark_combine = self.original_watermark_combine.resize(
                (int(self.original_upload.width() / 5), int(self.original_upload.height() / 5)))

        original_position = (self.original_upload.width() - self.original_watermark_combine.size[0], self.original_upload.height() - self.original_watermark_combine.size[1])
        self.original_transparent = Image.new('RGBA', (self.original_upload.width(), self.original_upload.height()), (0, 0, 0, 0))
        self.original_transparent.paste(self.original_upload_combine, (0, 0))
        self.original_transparent.paste(self.original_watermark_combine, original_position, mask=self.original_watermark_combine)

    def finish(self):
        self.window.destroy()