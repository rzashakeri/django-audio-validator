How To Use ? 📌
===============

1. First Install The Library Use The Command :

.. code-block:: 

   pip install django-audio-validator

2. Import Library In Your Model :

.. code-block:: 

   from audio_validator.validator import AudioValidator

3. Pass Validator To Your Model And Set Type Of Audio :

Template :

.. code-block:: 

   AudioValidator("Audio Type Supported") 


4. Usage Example :

.. code-block:: 

        audio = models.FileField(
            upload_to=user_directory_path,
            validators=[AudioValidator("mp3")],
        )

.. important::
   You must enter the audio type as a string