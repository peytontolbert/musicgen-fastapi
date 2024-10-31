from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write

def generate_music(description, duration=8):
    model = MusicGen.get_pretrained("large")
    model.set_generation_params(duration=duration)  # generate 8 seconds.

    wav = model.generate([description])
    for idx, one_wav in enumerate(wav):
        # Will save under {idx}.wav, with loudness normalization at -14 db LUFS.
        audio_write(f'{idx}', one_wav.cpu(), model.sample_rate, strategy="loudness")
        
    return wav
