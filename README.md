Sonatina Symphonic Orchestra
============================

Sonatina Symphonic Orchestra (SSO) is a free library of sampled orchestral instruments.  The original version was
created by Mattias Westlund in 2011, and quickly earned a following for its excellent quality and wide selection of
instruments.  This repository hosts the ongoing development of the library.  Mattias is no longer directly involved
(although he has given his permission for continuing to develop it) and has not personally reviewed all of the changes.
In other words, don't email him with questions about it!

[**Download SSO**](https://github.com/peastman/sso/releases)

The instruments are packaged in SFZ format.  They can be used with any compatible player, such as
[Sforzando](https://www.plogue.com/products/sforzando/), [sfizz](https://sfz.tools/sfizz/),
[Linux Sampler](https://www.linuxsampler.org/), and
[ARIA Player](https://www.garritan.com/products/personal-orchestra-5/aria-player/).

Instruments
-----------

SSO includes the following instruments and articulations:

**Strings**

|Instrument|Articulations|
|----------|-------------|
|1st Violins|Sustain, Marcato, Staccato, Pizzicato, Tremolo|
|2nd Violins|Sustain, Marcato, Staccato, Pizzicato, Tremolo|
|Violas|Sustain, Marcato, Staccato, Pizzicato|
|Cellos|Sustain, Marcato, Staccato, Pizzicato|
|Basses|Sustain, Marcato, Staccato, Pizzicato|
|Solo Violin|Sustain (non-looped, looped, decay)|
|Solo Violin 2|Sustain, Sustain non-vibrato, Marcato, Marcato non-vibrato, Spiccato, Pizzicato, Tremolo|
|Solo Cello|Sustain (non-looped, looped, decay)|

**Brass**

|Instrument|Articulations|
|----------|-------------|
|Trumpets|Sustain (looped, non-looped), Marcato (looped, non-looped), Staccato|
|French Horns|Sustain (looped, non-looped), Marcato (looped, non-looped), Staccato|
|Trombones|Sustain (looped, non-looped), Marcato (looped, non-looped), Staccato|
|Tuba|Sustain (looped, non-looped), Marcato (looped, non-looped), Staccato|
|Solo Trumpet|Sustain (non-looped, looped, decay)|
|Solo French Horn|Sustain (non-looped, looped, decay)|
|Solo Tenor Trombone|Sustain (non-looped, looped, decay)|
|Solo Bass Trombone|Sustain (non-looped, looped, decay)|

**Woodwinds**

|Instrument|Articulations|
|----------|-------------|
|Flutes|Sustain (looped, non-looped), Marcato (looped, non-looped), Staccato|
|Oboes|Sustain (looped, non-looped)|
|Clarinets|Sustain (looped, non-looped)|
|Bassoons|Sustain (looped, non-looped)|
|Solo Piccolo|Sustain (non-looped, looped, decay)|
|Solo Flute|Sustain (non-looped, looped, decay)|
|Solo Flute 2|Sustain, Sustain non-vibrato, Staccato|
|Solo Alto Flute|Sustain (non-looped, looped, decay)|
|Solo Cor Anglais|Sustain (non-looped, looped, decay)|
|Solo Oboe|Sustain (non-looped, looped, decay)|
|Solo Clarinet|Sustain (non-looped, looped, decay)|
|Solo Bass Clarinet|Sustain (non-looped, looped, decay)|
|Solo Bassoon|Sustain (non-looped, looped, decay)|
|Solo Contrabassoon|Sustain (non-looped, looped, decay)|

**Pitched Percussion**

|Instrument|Variations|
|----------|----------|
|Timpani|Right hand hits, Left hand hits, Rolls|
|Glockenspiel| - |
|Xylophone| - |
|Chimes| - |

**Percussion**

|Instrument|Variations|
|----------|----------|
|Bass Drum|Soft hit, Hard hit|
|Snare Drum|Left hand hit, Right hand hit, Roll|
|Cymbals|Hit, 4 Rolls|
|Conga|Muffled, Open, Slap|
|Bar Chimes|3 Variations|
|Tamtam|3 Variations|
|Triangle|Mute, Half-open, Open, Roll|
|Tambourine|Soft hit, Hard hit, Shake, Roll|
|Wood Blocks|High, Low|
|Cabasa|2 Variations|
|Shaker|3 Variations|
|Sleigh Bells|Soft hit, Hard hit|
|Castanets|2 Variations|
|Ratchet| - |
|Vibraslap| - |
|Bell Tree| - |

**Miscellaneous**

|Instrument|Articulations|
|----------|-------------|
|Grand Piano| - |
|Concert Harp| - |
|Chorus| Mixed, Large |
|Harpsichord| 4', 8', Full |

Instruments with multiple articulations are packaged in two ways.  Use whichever one is more convenient for your
workflow.

- As a separate SFZ instrument for each articulation.
- As a keyswitched instrument with all articulations in a single file.  You can switch between articulations by pressing
  keys outside the range of the instrument.

Most solo instruments have three versions:

- A non-looped version that simply plays each sample once.  This gives the most natural sound, but sets a strict limit
  on how long any note can be held.
- A looped version that can be held indefinitely, but sounds less natural than the non-looped version.
- A looped version that adds a gradual decay and gentle modulation.  This tries to give a more natural sound than the
  simple looped version, but still not place a strict limit on how long notes can be held.

There are two different solo violin instruments, and likewise two different solo flutes.  In each case, one of the two
instruments has the standard three versions listed above.  The other has many more articulations, but does not offer a
looped version.  The sustained notes are held long enough that the lack of looping is usually not a problem.

Many instruments are provided in separate "notation" and "performance" versions.  They differ in how they are controlled.

- Notation instruments use a control system convenient for use in notation programs.
  - All instruments use velocity to set the volume.
  - Marcato articulations use the mod wheel (MIDI control channel 1) to adjust the strength of the initial attack.  This
    lets you smoothly blend between a gentle sustain and a strong marcato.
- Performance instruments are better for use in live performance.
  - Long articulations use the mod wheel (MIDI control channel 1) to set the volume.  This allows you to continuously
    shape each note.
  - Marcato articulations use the mod wheel to set the overall volume and velocity to control the strength of the
    initial attack.
  - Short articulations use velocity to set the volume.

Technical Details
-----------------

All samples are stereo, 16 bit, 44 kHz.  Most instruments are sampled in minor 3rds.  Staccato and pizzicato
articulations use 2x round robin.

Most samples have only a small amount of reverb baked into them, so adding a realistic reverb is important for producing
a good overall sound.  Given that the samples came from a variety of different sources, this is also important for
making them sound like a unified orchestra.

License
-------

SSO may be used and distributed under the terms of the
[Creative Commons Sampling Plus 1.0 license](https://creativecommons.org/licenses/sampling+/1.0/).

Mattias Westlund included the following statement with SSO 1.0 regarding the sources and licensing of the samples:

> SSO was created from the following free/CC-licensed/public domain instrument samples:
> [The University of Iowa MIS](http://theremin.music.uiowa.edu/MIS.html),
> [MSLP](http://www.mediafire.com/?zqff4hkyeec22),
> [Philharmonia samples](http://www.philharmonia.co.uk/thesoundexchange/make_music/samples/library/),
> [OLPC project](http://wiki.laptop.org/go/Free_sound_samples),
> [The Complete K2000](http://www.sweetwater.com/k2000/sounds.html),
> [ldk1609 violin](http://www.freesound.org/usersViewSingle.php?id=692375),
> [stamperadam Kelon Xylophone](http://www.freesound.org/packsViewSingle.php?id=6168),
> [Corsica_S Cello Pizzicato](http://www.freesound.org/packsViewSingle.php?id=2680),
> [davidjwoll cymbal rolls](http://www.freesound.org/packsViewSingle.php?id=5577),
> [Satoration Castanets](http://www.freesound.org/samplesViewSingle.php?id=57299),
> Thores Triangle, Mystified timpani, Eddie's English Horn and a variety of classic soundfonts by Campbell Barton,
> [Nando Florestan](http://oui.com.br/n/download.php?list.2), and
> [Ethan Winer](http://www.ethanwiner.com/ewsf2.html).
>
> In the case of a few very old soundfonts I have no idea who the original authors were or what licensing might apply.
> But as these files have been modified by different people and included in countless GM banks and other soundfont
> compilations over the last decade, I'm assuming that they are to be considered public domain or at least free to use
> for sampling projects.
>
> I have done my very best to avoid samples of questionable legality, but as it is impossible for me to know the exact
> origin of everything (i.e. I have no way of knowing if a soundfont labeled as "public domain" isn't actually sampled
> from a proprietary source), I would appreciate if you let me know if you find anything fishy. 

Related Projects
----------------

SSO was the first high quality, free orchestral library.  More recently, a few others have become available.  Each one
has its own sound, so try them all out.

- [Virtual Playing Orchestra](http://virtualplaying.com/virtual-playing-orchestra/)
- [Versilian Studios Chamber Orchestra Community Edition](http://vis.versilstudios.net/vsco-community.html)
- [No Budget Orchestra](https://nbo.libreorchestra.net/download/)
