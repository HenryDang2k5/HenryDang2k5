import tkinter as tk
import tkinter.scrolledtext as tkst
import video_library as lib

videos = []

def add_video(name, director, rating):
    """
    Adds a new video to the video list.

    Parameters:
    name (str): The name of the video.
    director (str): The name of the director.
    rating (str): The rating of the video.
    """
    video = {
        'name': name,
        'director': director,
        'rating': rating
    }
    videos.append(video)

def list_all():
    """
    Returns a string representation of all videos in the list.

    Returns:
    str: A formatted string of all videos.
    """
    video_list = ""
    for video in videos:
        video_list += f"Name: {video['name']}, Director: {video['director']}, Rating: {video['rating']}\n"
    return video_list


class CreateVideoList:
    def __init__(self, window):
        """
        Initialize the CreateVideoList GUI application.

        Parameters:
        window (tk.Tk): The main window of the application.
        """
        window.geometry("750x350")  # Set the window size
        window.title("Create Video List")  # Set the window title

        # Create and place the "Add Video" button
        add_video_btn = tk.Button(window, text="Add Video", command=self.add_video_clicked)
        add_video_btn.grid(row=0, column=0, padx=10, pady=10)

        # Create and place the label and entry for video name
        name_lbl = tk.Label(window, text="Video Name")
        name_lbl.grid(row=1, column=0, padx=10, pady=10)
        self.name_txt = tk.Entry(window, width=30)
        self.name_txt.grid(row=1, column=1, padx=10, pady=10)

        # Create and place the label and entry for director name
        director_lbl = tk.Label(window, text="Director")
        director_lbl.grid(row=2, column=0, padx=10, pady=10)
        self.director_txt = tk.Entry(window, width=30)
        self.director_txt.grid(row=2, column=1, padx=10, pady=10)

        # Create and place the label and entry for video rating
        rating_lbl = tk.Label(window, text="Rating")
        rating_lbl.grid(row=3, column=0, padx=10, pady=10)
        self.rating_txt = tk.Entry(window, width=5)
        self.rating_txt.grid(row=3, column=1, padx=10, pady=10)

        # Create and place the text area for the list of videos
        self.video_list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.video_list_txt.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # ScrolledText widget to display saved videos
        self.add_video_txt = tkst.ScrolledText(window, width=70, height=10, wrap="none")
        self.add_video_txt.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # Create and place the status label
        self.status_lbl = tk.Label(window, text="")
        self.status_lbl.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def add_video_clicked(self):
        """
        Handle the "Add Video" button click event.
        """
        name = self.name_txt.get()
        director = self.director_txt.get()
        rating = self.rating_txt.get()

        if name and director and rating:
            # Add video to the library
            lib.add_video(name, director, rating)

            # Append the video details to the ScrolledText widget
            self.add_video_txt.insert(tk.END, f"Video Name: {name}\n")
            self.add_video_txt.insert(tk.END, f"Director Name: {director}\n")
            self.add_video_txt.insert(tk.END, f"Rating: {rating}\n")
            self.add_video_txt.insert(tk.END, "-"*50 + "\n")
            
            # Clear the entry fields after saving
            self.name_txt.delete(0, tk.END)
            self.director_txt.delete(0, tk.END)
            self.rating_txt.delete(0, tk.END)

            # Update the status label
            self.status_lbl.configure(text="Video saved successfully!")
        else:
            # Update the status label if any field is empty
            self.status_lbl.configure(text="Please fill in all fields!")

    def list_videos(self):
        """
        List all videos in the text area.
        """
        video_list = lib.list_all()
        self.video_list_txt.delete("1.0", tk.END)
        self.video_list_txt.insert(tk.END, video_list)

if __name__ == "__main__":
    window = tk.Tk()  # Create the main window object
    app = CreateVideoList(window)  # Create and open the CreateVideoList GUI
    app.list_videos()  # List all videos when the app starts
    window.mainloop()  # Run the main loop to react to events (button presses, etc.)
