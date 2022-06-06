from django.core import validators
from django.core.exceptions import ValidationError
import filetype
from django.core.files.uploadedfile import TemporaryUploadedFile
from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible

@deconstructible
class AudioValidator:
    def __init__(self, audio_type):
        """
        Pass the audio file type as a string : (str)
        aac
        midi
        mp3
        m4a
        ogg
        flac
        wav
        amr
        aiff
        """
        # getting audio types with the filetype library
        audio_type_dic = {
            "aac": filetype.TYPES[26],
            "midi": filetype.TYPES[27],
            "mp3": filetype.TYPES[28],
            "m4a": filetype.TYPES[29],
            "ogg": filetype.TYPES[30],
            "flac": filetype.TYPES[31],
            "wav": filetype.TYPES[32],
            "amr": filetype.TYPES[33],
            "aiff": filetype.TYPES[34],
        }
        # We check the audio type set admin in supported audio types dictionary which getting used the filetype library
        if audio_type in audio_type_dic.keys():
            # get the audio type use filetype library
            file_audio_type = audio_type_dic[audio_type]
        else:
            # if the audio type is not available in a dictionary show value error
            raise ValueError(
                "The audio_type '%s' is unknown. Supported: %s"
                % (audio_type, list(audio_type_dic.keys()))
            )
        # set audio type extension
        self.audio_type_extension = audio_type
        # set the audio type
        self.audio_type = file_audio_type
        # get and set the audio extension use filetype library
        self.audio_type_extension = file_audio_type.extension

    def __call__(self, value):
        # get audio file
        file = value.file
        # get audio file temporary path saved django
        file_path = TemporaryUploadedFile.temporary_file_path(file)
        # We check the file type of c?
        is_audio = filetype.is_audio(file_path)
        # We check the extension file is audio
        file_extension = filetype.guess_extension(file_path)
        # get the file type use filetype library
        file_type = filetype.guess(file_path)
        # We check if the upload file extension is equal to the extension we specified
        if file_extension == self.audio_type_extension:
            # check file is audio type
            if is_audio:
                # Check if the upload file type is the same as the one we specified
                if file_type == self.audio_type:
                    pass
                else:
                    # show validation error for this file is not audio type
                    raise ValidationError(
                        f"please upload a valid {self.audio_type_extension} file , your file : {file.name} , valid type : {self.audio_type_extension}"
                    )
            else:
                # show validation error for this file is not audio by type
                raise ValidationError(
                    f"please upload a valid {self.audio_type_extension} file , your file : {file.name} , valid type : {self.audio_type_extension}"
                )
        else:
            # show validation error for this file is not audio by extension
            raise ValidationError(
                f"please upload a valid {self.audio_type_extension} file , your file : {file.name} , valid type : {self.audio_type_extension}"
            )