# Pipe Organ

This instrument is based on the [St. Stephen's pipe organ](https://mps-orgelseite.de/home/forum/index.php?thread/1019-st-stephens-st-augustines/&postID=9224)
recorded by Nicholas Appleton.  It is a church organ with 14 stops in three divisions.

| Great               | Swell     | Pedal       |
|---------------------|-----------|-------------|
| Bourdon 16'         | Gedact 8' | Bourdon 16' |
| Open Diapason 8'    | Gamba 8'  | Violon 16'  |
| Stopped Diapason 8' | Oboe 8'   |             |
| Dulciana 8'         | Octave 4' |             |
| Flute 4'            |           |             |
| Principal 4'        |           |             |
| Twelfth 3'          |           |             |
| Fifteenth 2'        |           |             |

Each stop is provided as a separate SFZ instrument.  They are suitable either for using individually
or for layering to create more complex sounds.  In addition, there are three files that allow varying
the sound within a single instrument.

- `Organ Single Stops.sfz` provides all of the stops in a single file with keyswitches to select
between them.  This allows you to easily switch between stops.

- `Organ Combinations.sfz` contains a variety of preset combinations of multiple stops, selectable with
keyswitches.  They provide typical combinations appropriate for a variety of musical contexts.

- `Organ All Stops.sfz` is a fully programmable instrument that allows all possible combinations of stops.
MIDI CC 16 through 29 are used to control the individual stops.  Set a CC to 127 to turn the corresponding
stop on, or 0 to turn it off.

All stops in the Swell division respond to the modulation controller (MIDI CC1), which functions as
a swell pedal.  It varies both the volume and brightness of the sound.