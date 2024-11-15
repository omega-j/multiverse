from midiutil import MIDIFile

# Function to generate the dancehall rhythm with stabs
def generate_dancehall_rhythm(output_file):
    # Create a MIDI file
    mid = MIDIFile(1)  # One track
    track = 0
    mid.addTrackName(track, 0, "Dancehall Rhythm")
    mid.addTempo(track, 0, 95)  # 95 BPM, typical dancehall tempo

    # Timing variables
    ticks_per_beat = 480  # 480 ticks per beat (standard resolution)
    time_per_note = ticks_per_beat // 4  # 1/16 notes (for hi-hats)
    
    # Kick Drum (C4) - On beats 1 and 3
    kick = 36  # MIDI note number for kick drum
    mid.addNote(track, 0, kick, 0, 1, 100)  # Kick on 1st beat
    mid.addNote(track, 0, kick, 2, 1, 100)  # Kick on 3rd beat

    # Snare Drum (D4) - On beats 2 and 4
    snare = 38  # MIDI note number for snare
    mid.addNote(track, 0, snare, 1, 1, 100)  # Snare on 2nd beat
    mid.addNote(track, 0, snare, 3, 1, 100)  # Snare on 4th beat

    # Hi-Hat (F#4) - 16th notes
    hi_hat = 42  # MIDI note number for hi-hat
    for i in range(0, 4):
        mid.addNote(track, 0, hi_hat, i * time_per_note, time_per_note, 60)  # Hi-hats on each 16th note

    # Dancehall synth stab (A4) on the off-beats
    stab = 69  # MIDI note number for synth stab (A4)
    for i in range(0, 4):
        mid.addNote(track, 0, stab, (i * 2 + 1) * time_per_note, time_per_note, 80)  # Stab on off-beats

    # Save the MIDI file
    with open(output_file, "wb") as output:
        mid.writeFile(output)
    print(f"Dancehall rhythm MIDI file saved as {output_file}")

# Generate the dancehall rhythm MIDI
output_file = "dancehall_rhythm.mid"
generate_dancehall_rhythm(output_file)