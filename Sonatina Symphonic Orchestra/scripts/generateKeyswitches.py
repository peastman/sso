# This script merges instruments together to create keyswitch files.  To run it,
# cd to the parent directory then type
#
# python scripts/generateKeyswitches.py

windArticulations = (
    ("Sustain (looped)", " Sustain (looped)", 0),
    ("Sustain (non-looped)", " Sustain", 1),
    ("Marcato (looped)", " Marcato (looped)", 2),
    ("Marcato (non-looped)", " Marcato", 3),
    ("Staccato", " Staccato", 4),
    ("Legato", " Legato", 5)
)

hornArticulations = (
    ("Sustain", " Sustain", 0),
    ("Marcato", " Marcato", 2),
    ("Staccato", " Staccato", 4),
    ("Legato", " Legato", 5)
)

sustainArticulations = (
    ("Sustain (looped)", " Sustain (looped)", 0),
    ("Sustain (non-looped)", " Sustain", 1),
    ("Legato", " Legato", 2)
)

stringArticulations = (
    ("Sustain", " Sustain", 0),
    ("Legato", " Legato", 1),
    ("Marcato", " Marcato", 2),
    ("Staccato", " Staccato", 4),
    ("Pizzicato", " Pizzicato", 5),
    ("Tremolo", " Tremolo", 7),
    ("Harmonics", " Harmonics", 9)
)


bassArticulations = (
    ("Sustain", " Sustain", 0),
    ("Legato", " Legato", 1),
    ("Marcato", " Marcato", 2),
    ("Staccato", " Staccato", 4),
    ("Pizzicato", " Pizzicato", 5),
    ("Tremolo", " Tremolo", 7)
)

soloArticulations = (
    ("Sustain (non-looped)", "", 0),
    ("Sustain (looped)", " (looped)", 1),
    ("Sustain (looped, decay)", " (looped, decay)", 2),
    ("Legato", " Legato", 4),
)

soloViolin1Articulations = (
    ("Sustain (non-looped)", "", 0),
    ("Sustain (looped)", " (looped)", 1),
    ("Legato", " Legato", 2),
    ("Marcato (non-looped)", " Marcato", 3),
    ("Marcato (looped)", " Marcato (looped)", 4),
    ("Spiccato", " Spiccato", 5),
    ("Pizzicato", " Pizzicato", 7)
)

soloViolin2Articulations = (
    ("Sustain", " Sustain", 0),
    ("Sustain Non-Vibrato", " Sustain Non-Vibrato", 1),
    ("Legato", " Legato", 2),
    ("Legato Non-Vibrato", " Legato Non-Vibrato", 3),
    ("Marcato", " Marcato", 4),
    ("Marcato Non-Vibrato", " Marcato Non-Vibrato", 5),
    ("Spiccato", " Spiccato", 6),
    ("Pizzicato", " Pizzicato", 7),
    ("Tremolo", " Tremolo", 8)
)

soloViolaArticulations = (
    ("Sustain", " Sustain", 0),
    ("Legato", " Legato", 1),
    ("Marcato", " Marcato", 2),
    ("Staccato", " Staccato", 4),
    ("Pizzicato", " Pizzicato", 5)
)

soloCelloArticulations = (
    ("Sustain (non-looped)", "", 0),
    ("Sustain (looped)", " (looped)", 2),
    ("Legato", " Legato", 4)
)

soloFluteArticulations = (
    ("Sustain", " Sustain", 0),
    ("Sustain Non-Vibrato", " Sustain Non-Vibrato", 1),
    ("Legato", " Legato", 2),
    ("Legato Non-Vibrato", " Legato Non-Vibrato", 3),
    ("Staccato", " Staccato", 4)
)

keyNames = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b'] 

def noteName(id):
    return '%s%d' % (keyNames[id%12], id/12)

def createFile(directory, instrument, articulations, base):
    with open(f'{directory}/{instrument} KS.sfz', 'w') as output:
        for name, fileSuffix, key in articulations:
            content = open(f'{directory}/{instrument}{fileSuffix}.sfz').read()
            commands = """
sw_default=%s
sw_lokey=%s
sw_hikey=%s
sw_last=%s
sw_label=%s""" % (noteName(base), noteName(base), noteName(base+max(a[2] for a in articulations)),
                    noteName(base+key), name)
            content = content.replace('<group>', '<group>'+commands)
            output.write(content)
            output.write('\n\n')

for directory in ['Brass - Notation', 'Brass - Performance']:
    createFile(directory, "Horns", hornArticulations, 72)
    createFile(directory, "Trumpets", windArticulations, 24)
    createFile(directory, "Trombones", windArticulations, 72)
    createFile(directory, "Tuba", windArticulations, 72)

    createFile(directory, "Horn Solo", soloArticulations, 72)
    createFile(directory, "Trumpet Solo", soloArticulations, 24)
    createFile(directory, "Tenor Trombone Solo", soloArticulations, 72)
    createFile(directory, "Bass Trombone Solo", soloArticulations, 72)

for directory in ['Woodwinds - Notation', 'Woodwinds - Performance']:
    createFile(directory, "Flutes", windArticulations, 24)
    createFile(directory, "Oboes", sustainArticulations, 24)
    createFile(directory, "Clarinets", sustainArticulations, 24)
    createFile(directory, "Bassoons", sustainArticulations, 72)

    createFile(directory, "Piccolo Solo", soloArticulations, 24)
    createFile(directory, "Flute Solo 1", soloArticulations, 24)
    createFile(directory, "Flute Solo 2", soloFluteArticulations, 24)
    createFile(directory, "Alto Flute Solo", soloArticulations, 24)
    createFile(directory, "Oboe Solo", soloArticulations, 24)
    createFile(directory, "Cor Anglais Solo", soloArticulations, 24)
    createFile(directory, "Clarinet Solo", soloArticulations, 24)
    createFile(directory, "Bass Clarinet Solo", soloArticulations, 72)
    createFile(directory, "Bassoon Solo", soloArticulations, 72)
    createFile(directory, "Contrabassoon Solo", soloArticulations, 72)

for directory in ['Strings - Notation', 'Strings - Performance']:
    createFile(directory, "1st Violins", stringArticulations, 24)
    createFile(directory, "2nd Violins", stringArticulations, 24)
    createFile(directory, "Violas", stringArticulations, 24)
    createFile(directory, "Celli", stringArticulations, 72)
    createFile(directory, "Basses", bassArticulations, 72)

    createFile(directory, "Violin Solo 1", soloViolin1Articulations, 24)
    createFile(directory, "Violin Solo 2", soloViolin2Articulations, 24)
    createFile(directory, "Viola Solo", soloViolaArticulations, 24)
    createFile(directory, "Cello Solo", soloCelloArticulations, 79)
