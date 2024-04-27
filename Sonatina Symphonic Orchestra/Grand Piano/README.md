# Grand Piano

This is a modified version of the Splendid Grand Piano from
https://github.com/sfzinstruments/SplendidGrandPiano.  It is a Steinway grand
recorded by Akai and scripted by kinwie.  It has the following changes from the
original version.

- Added support for half pedaling.
- Changed some envelope settings that did not work correctly on some SFZ players.
- Removed two samples whose sound was inconsistent with the surrounding notes
  and tended to stand out.
- Added a little equalization to boost the treble.
- Increased the default resonance to 100%.

This instrument is in the public domain.

The following is the README from the original version of the instrument.

-------------------------------------------------------------------------------

# Splendid Grand Piano

Public Domain samples by AKAI

This samples set was released as public domain in early 2000 by Akai company.
It's a Steinway samples with 4 velocity layers.
The version we put here is the 256 MB version.
All samples has been properly fixed and converted to flac,
and mapped to SFZ format with ARIA extensions by kinwie.

## SFZ Details

- Added 5th layer at lowest velocity using filter cutoff
- High notes are undampened mode
- Release control time up to 2s, initial at 0.7s
- Veltrack control to adjust volume response to velocity
- Some additional tweaks has been added to this sfz version
- Later tweaks by user can be easily made,
for example to adjust dynamics range to suit personal playing and taste

## String Resonance
Updated to include the string resonance simulation created by P.Eastman.
Active when the sustain pedal is down/pressed.
Turn down the "Resonance" control to 0 will also turn off the resonance polyphony.
