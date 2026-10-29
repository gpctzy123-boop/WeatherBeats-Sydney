# WeatherBeats Sydney

WeatherBeats Sydney is a TunePad prototype that maps a manually selected weather condition to a short musical phrase.

**Live prototype:** https://tunepad.com/project/135123

## Run the shared TunePad project

1. Open the TunePad project.
2. Press Play on Sunny, Overcast, Rainy, or Cloudy.
3. Press Stop All before starting another phrase if one is still playing.

## Rebuild the prototype from this repository

This project is designed to run inside TunePad. The Python snippets are not standalone command-line programs because TunePad provides the `playNote()` and `rest()` music functions.

1. Create or open a TunePad project.
2. Add a Python code cell named exactly `Weather_mapping`.
3. Copy the contents of `weatherbeats_tunepad.py` into that cell, then run the cell to define `WEATHER_MUSIC` and `play_weather()`.
4. Add four separate Keys cells named `Sunny`, `Overcast`, `Rainy`, and `Cloudy`.
5. Copy the matching file from `tunepad_cells/` into each Keys cell. Each file imports from `Weather_mapping` and calls `play_weather()` with one weather condition.
6. Run or play one condition cell at a time. Use TunePad's Stop All control before changing conditions.

If the imported mapping is not available, confirm that the shared cell is named `Weather_mapping` exactly and has been run before the condition cell.

## How the code works

The `Weather_mapping` cell stores all four patterns in one Python dictionary. Each pattern has a description, a velocity, and a sequence of (note, beat-length) pairs. The `play_weather` function checks the requested condition, retrieves its pattern, and loops through the sequence. It calls TunePad's `playNote()` for notes and `rest()` for timed pauses.

Each Keys cell imports the shared mapping and function from `Weather_mapping`, then calls `play_weather()` with its own condition. The mapping cell only defines the data and function; it does not play a phrase by itself. This keeps all note patterns and velocity values in one place, so the four buttons cannot silently drift to different settings.

## Files

- `weatherbeats_tunepad.py` — local copy of the TunePad `Weather_mapping` cell.
- `tunepad_cells/Sunny.py` — code for the Sunny Keys cell.
- `tunepad_cells/Overcast.py` — code for the Overcast Keys cell.
- `tunepad_cells/Rainy.py` — code for the Rainy Keys cell.
- `tunepad_cells/Cloudy.py` — code for the Cloudy Keys cell.
- `.gitignore` — ignores local Python/editor files and the separate reflection PDF draft.

The Keys-cell files are TunePad cell snippets. Each starts with the explicit Python import `from Weather_mapping import *`, which makes the shared function available in that cell. Run them in TunePad, which provides `playNote()` and `rest()`; they are not standalone command-line programs.

## Current scope and limitations

Weather is selected manually; this prototype does not fetch live Bureau of Meteorology observations. The mapping uses these velocity values in every weather button: Sunny 105, Overcast 55, Rainy 82, and Cloudy 88. Velocity controls note loudness, not tempo. The four note patterns are intentionally different; edit them in the central mapping cell.

## Acknowledgements

- TunePad's `playNote()` and `rest()` functions are documented by [TunePad](https://learn.tunepad.com/docs/).
- No third-party code has been copied into this repository. The built-in TunePad music API is used as documented above.
