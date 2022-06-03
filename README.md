<img src="https://img.shields.io/badge/Django-092E20.svg?style=for-the-badge&logo=Django&logoColor=white"> <img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white">

# Django Audio Validator 🔉

This Library a Audio Validator For Django With MIME And Extension Use FileType Library

# Feature 📌

1. Audio File Type Check
2. Audio File Extension Check

# How Use ? 👇

1. First Install The Library Use The Command :

   `pip install `

2. Import Library In Your Model :

    `from audio_validator.validator import AudioValidator`

3. Pass Validator To Your Model And Set Type Of Audio :

    Audio Type Supported :
    - aac
    - midi
    - mp3
    - m4a
    - ogg
    - flac
    - wav
    - amr
    - aiff

Template : ``` AudioValidator("Audio Type Supported") ```

Code Example :

    ```
    class Attachment(models.Model):

        audio = models.FileField(
            upload_to=user_directory_path,
            blank=True,
            validators=[AudioValidator("mp3")],
        )
        created_at = models.DateTimeField(auto_now_add=True)
    ```

# Contribute This Project