from elevenlabs import play
from elevenlabs import generate
from elevenlabs import set_api_key

# get voice-id from here:
# https://api.elevenlabs.io/v1/voices


set_api_key("API_KEY")

audio = generate(
    "Hello world! This is my first text-to-speech using ElevenLabs.")

play(audio)
