# Contents of the TunePad cell named Weather_mapping.
# Weather is selected manually in this prototype; live BOM data is not connected.

# Store each condition's label, sound level, and sequence in one place.
# Each step is a (MIDI note, beat length) pair. None means a timed rest.
WEATHER_MUSIC = {
    "sunny": {
        "description": "bright and upbeat",
        "velocity": 105,
        "steps": [
            (60, 0.5), (64, 0.5), (67, 0.5), (72, 0.5),
            (67, 0.5), (72, 0.5), (67, 0.5), (64, 0.5),
        ],
    },
    "overcast": {
        "description": "low and subdued",
        "velocity": 55,
        "steps": [(48, 1), (51, 1), (55, 1), (51, 1)],
    },
    "rainy": {
        "description": "a steady repeating pulse",
        "velocity": 82,
        "steps": [
            (48, 0.5), (48, 0.5), (53, 0.5), (48, 0.5),
            (48, 0.5), (48, 0.5), (53, 0.5), (48, 0.5),
        ],
    },
    "cloudy": {
        "description": "changeable, with uneven notes and pauses",
        "velocity": 88,
        "steps": [
            (60, 0.5), (None, 0.25), (67, 0.5), (None, 0.25),
            (62, 0.75), (69, 0.5), (None, 0.25), (64, 0.5), (62, 0.5),
        ],
    },
}


def play_weather(condition):
    """Play one mapped phrase for a supported weather condition."""
    if condition not in WEATHER_MUSIC:
        print("Choose sunny, overcast, rainy, or cloudy.")
        return

    mood = WEATHER_MUSIC[condition]
    print("Sydney weather:", condition, "-", mood["description"])

    # A None note becomes a rest; every other step plays at this mood's velocity.
    for note, beats in mood["steps"]:
        if note is None:
            rest(beats)
        else:
            playNote(note, beats=beats, velocity=mood["velocity"])
