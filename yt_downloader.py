import tkinter
import customtkinter
from pytube import YouTube
import os

# Youtube Downloader

# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
header_font = ("Lato", 16, "bold")
has_video = False

# Frame
app = customtkinter.CTk()
app.geometry("650x400")
app.title("Youtube Downloader")

# UI Elements
title = customtkinter.CTkLabel(app, text="Insert a youtube link:", font=header_font)
title.pack(padx=10, pady=10)

# Find Desktop Directory
user_home = os.path.expanduser("~")

# Construct Path
desktop_path = os.path.join(user_home, "Desktop")

# Print Desktop Path
print("Desktop Path:", desktop_path)


# Change format to be downloaded
def changeFormat():
    global has_video
    try:
        if has_video:
            has_video = False
            print("Changed Format - MP3")
        else:
            has_video = True
            print("Changed Format - MP4")
    except:
        print("Change format error.")


# Download MP3 or MP4 - According to toggle option
def startDownload():
    global has_video
    try:
        progressBar.set(0)
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        if has_video == True:
            mp_format = ytObject.streams.get_highest_resolution()
        else:
            mp_format = ytObject.streams.get_audio_only()

        mp_format.download(output_path=f"{desktop_path}") # Download on desktop

        finishLabel.configure(text="Download Complete!", text_color="green")

    except:
        finishLabel.configure(text="Download Error.", text_color="red")


# Display percent
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream. filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int (percentage_of_completion))
    percentage.configure(text=per + '%')
    percentage.update()
    # Update progress bar
    progressBar.set(float(percentage_of_completion) / 100 )


# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Display Completion
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Download Button
download = customtkinter.CTkButton(app, text="Download", corner_radius=32,
hover_color="#EC5800", border_color="#FFFFFF", border_width=2, command=startDownload)

download.pack(padx=20, pady=10)

# Choose MP3 or MP4
mp_toggle = customtkinter.CTkSwitch(app, text="Download with Video", corner_radius=32,
            border_color="#FFFFFF", border_width=2, command=changeFormat)

mp_toggle.pack(padx=0, pady=40)

# Display Progress Bar
percentage = customtkinter.CTkLabel(app, text="0%")
percentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=40)

# Run app
app.mainloop()
