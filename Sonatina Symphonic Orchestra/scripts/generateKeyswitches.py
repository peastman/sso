# This script merges instruments together to create keyswitch files.  To run it,
# cd to the parent directory then type
#
# python scripts/generateKeyswitches.py

windArticulations = (
    ("Sustain (looped)", " Sustain (looped)", 0),
    ("Sustain (non-looped)", " Sustain", 1),
    ("Marcato (looped, mod wheel)", " Marcato (looped, mod wheel)", 2),
    ("Marcato (non-looped, mod wheel)", " Marcato (mod wheel)", 3),
    ("Staccato", " Staccato", 4)
)

sustainArticulations = (
    ("Sustain (looped)", " Sustain (looped)", 0),
    ("Sustain (non-looped)", " Sustain", 1)
)

stringArticulations = (
    ("Sustain", " Sustain", 0),
    ("Marcato (mod wheel)", " Marcato (mod wheel)", 2),
    ("Staccato", " Staccato", 4),
    ("Pizzicato", " Pizzicato", 5)
)

violinArticulations = (
    ("Sustain", " Sustain", 0),
    ("Marcato (mod wheel)", " Marcato (mod wheel)", 2),
    ("Staccato", " Staccato", 4),
    ("Pizzicato", " Pizzicato", 5),
    ("Tremolo", " Tremolo", 7)
)

soloArticulations = (
    ("Sustain (non-looped)", "", 0),
    ("Sustain (looped)", " (looped)", 1),
    ("Sustain (looped, decay)", " (looped, decay)", 2)
)

chorusArticulations = (
    ("Sustain (non-looped)", "", 0),
    ("Sustain (looped)", " (looped)", 1),
    ("Sustain (looped, velocity)", " (looped, velocity)", 2)
)

soloViolinArticulations = (
    ("Sustain", " Sustain", 0),
    ("Sustain Non-Vibrato", " Sustain Non-Vibrato", 1),
    ("Marcato (mod wheel)", " Marcato (mod wheel)", 2),
    ("Marcato Non-Vibrato (mod wheel)", " Marcato Non-Vibrato (mod wheel)", 3),
    ("Spiccato", " Spiccato", 4),
    ("Pizzicato", " Pizzicato", 5),
    ("Tremolo", " Tremolo", 7)
)

keyNames = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b'] 

def noteName(id):
    return '%s%d' % (keyNames[id%12], id/12)

def createFile(instrument, articulations, base):
    with open('%s KS.sfz' % instrument, 'w') as output:
        for name, fileSuffix, key in articulations:
            content = open("%s%s.sfz" % (instrument, fileSuffix)).read()
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

createFile("Brass - Horns", windArticulations, 72)
createFile("Brass - Trumpets", windArticulations, 24)
createFile("Brass - Trombones", windArticulations, 72)
createFile("Brass - Tuba", windArticulations, 72)

createFile("Brass - Horn Solo", soloArticulations, 72)
createFile("Brass - Trumpet Solo", soloArticulations, 24)
createFile("Brass - Tenor Trombone Solo", soloArticulations, 72)
createFile("Brass - Bass Trombone Solo", soloArticulations, 72)

createFile("Woodwinds - Flutes", windArticulations, 24)
createFile("Woodwinds - Oboes", sustainArticulations, 24)
createFile("Woodwinds - Clarinets", sustainArticulations, 24)
createFile("Woodwinds - Bassoons", sustainArticulations, 72)

createFile("Woodwinds - Piccolo Solo", soloArticulations, 24)
createFile("Woodwinds - Flute Solo", soloArticulations, 24)
createFile("Woodwinds - Alto Flute Solo", soloArticulations, 24)
createFile("Woodwinds - Oboe Solo", soloArticulations, 24)
createFile("Woodwinds - Cor Anglais Solo", soloArticulations, 24)
createFile("Woodwinds - Clarinet Solo", soloArticulations, 24)
createFile("Woodwinds - Bass Clarinet Solo", soloArticulations, 72)
createFile("Woodwinds - Bassoon Solo", soloArticulations, 72)
createFile("Woodwinds - Contrabassoon Solo", soloArticulations, 72)

createFile("Strings - 1st Violins", violinArticulations, 24)
createFile("Strings - 2nd Violins", violinArticulations, 24)
createFile("Strings - Violas", stringArticulations, 24)
createFile("Strings - Celli", stringArticulations, 72)
createFile("Strings - Basses", stringArticulations, 72)

createFile("Strings - Violin Solo", soloArticulations, 24)
createFile("Strings - Violin Solo 2", soloViolinArticulations, 24)
createFile("Strings - Cello Solo", soloArticulations, 79)

createFile("Chorus - Male", chorusArticulations, 24)
createFile("Chorus - Female", chorusArticulations, 24)
createFile("Chorus - Mixed", chorusArticulations, 24)

