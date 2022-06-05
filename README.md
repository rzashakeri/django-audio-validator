<img src="https://img.shields.io/badge/Django-092E20.svg?style=for-the-badge&logo=Django&logoColor=white"> <img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white">

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