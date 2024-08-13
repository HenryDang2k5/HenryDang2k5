class LibraryItem:
    def __init__(self, video_id, video_name, director_name, rating):
        self.video_id = video_id
        self.video_name = video_name
        self.director_name = director_name
        self.rating = rating

    @property
    def video_id(self):
        return self._video_id

    @video_id.setter
    def video_id(self, value):
        if not value.isdigit() or int(value) <= 0:
            raise ValueError("Video ID must be a positive integer.")
        self._video_id = value

    @property
    def video_name(self):
        return self._video_name

    @video_name.setter
    def video_name(self, value):
        if not value:
            raise ValueError("Video name cannot be empty.")
        self._video_name = value

    @property
    def director_name(self):
        return self._director_name

    @director_name.setter
    def director_name(self, value):
        if not value:
            raise ValueError("Director name cannot be empty.")
        self._director_name = value

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if not (0 <= value <= 10):
            raise ValueError("Rating must be between 0 and 10.")
        self._rating = value
