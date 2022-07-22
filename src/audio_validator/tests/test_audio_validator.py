from multiprocessing import Value
import pytest
import os
from audio_validator.validator import AudioValidator
import pygame


class TestMp3AudioType:
    def test_if_validator_accepted_wrong_type(self):
        module_dir = os.path.dirname(__file__)
        file_path = os.path.join(module_dir, "test_files", "mp3", "test_image.mp3")
        pygame.mixer.init()
        file = pygame.mixer.music.load(file_path)
        audio_validator = AudioValidator(audio_type="mp3")
        audio_validator(value=file)