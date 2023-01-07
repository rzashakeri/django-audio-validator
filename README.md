<img src="https://img.shields.io/badge/Django-092E20.svg?logo=Django&logoColor=white"> <img src="https://img.shields.io/badge/Python-3776AB.svg?logo=Python&logoColor=white"> [![Downloads](https://static.pepy.tech/personalized-badge/django-audio-validator?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads)](https://pepy.tech/project/django-audio-validator) [![PyPI version](https://badge.fury.io/py/django-audio-validator.svg)](https://badge.fury.io/py/django-audio-validator) [![Documentation Status](https://readthedocs.org/projects/django-audio-validator/badge/?version=latest)](https://django-audio-validator.readthedocs.io/en/latest/?badge=latest)

----------

# file validator
I made a more complete library with which you can validate all types of files, the new project has been tested and also supports more types, you can access it through the following link:
[file validator](https://github.com/rzashakeri/file_validator)

----------


# Django Audio Validator 🔉

This Library a Audio Validator For Django With d MIME type checking the magic numbers signature And Extension Use FileType Library

# Feature 📌

1. Audio File Type Check Use MIME Type
2. Audio File Extension Check


# Audio Type Supported ✅

- aac - `audio/aac`
- midi - `audio/midi`
- mp3 - `audio/mpeg`
- m4a - `audio/mp4`
- ogg - `audio/ogg`
- flac - `audio/x-flac`
- wav - `audio/x-wav`
- amr - `audio/amr`
- aiff - `audio/x-aiff`

# How Use ? 👇

1. First Install The Library Use The Command :

   `pip install django-audio-validator`

2. Import Library In Your Model :

    `from audio_validator.validator import AudioValidator`

3. Pass Validator To Your Model And Set Type Of Audio :


    Template : ``` AudioValidator("Audio Type Supported") ```

    **Code Example :**

    ```
    class Attachment(models.Model):

        audio = models.FileField(
            upload_to=user_directory_path,
            blank=True,
            validators=[AudioValidator("mp3")],
        )
        created_at = models.DateTimeField(auto_now_add=True)
    ```

# Contribute This Project 🔗
If you would like to help me develop this project, you can do so through this [link](https://github.com/rzashakeri/django-audio-validator)
