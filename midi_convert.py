import mido
from mido import MidiFile, MidiTrack, Message

def convert_chordz_to_midi(chordz_file, output_file):
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    # Read the input file
    with open(chordz_file, 'r') as file:
        for line in file:
            # Strip leading and trailing spaces
            line = line.strip()

            # Skip empty lines
            if not line:
                continue

            # Remove comments (everything after "//")
            line = line.split('//')[0].strip()

            # Skip if line is empty after removing comment
            if not line:
                continue

            # Remove trailing commas, if any
            line = line.rstrip(',')

            # Process valid lines
            try:
                print(f"Processing line: {line}")  # Debugging line

                # Split the line into parts
                parts = line.split(',')

                # Skip lines that don't have the correct number of parts
                if len(parts) < 8:
                    print(f"Skipping invalid line (too few parts): {line}")
                    continue

                # Convert parts to integers
                bar, beat, measure, _ = map(int, parts[:4])
                notes = list(map(int, parts[4:]))  # These are the notes

                # Add program change to set the instrument (optional)
                if bar == 0 and beat == 0:
                    track.append(Message('program_change', program=12))  # Example instrument: Electric Piano

                # Add note on and note off events for each chord in the progression
                for note in notes:
                    track.append(Message('note_on', note=note, velocity=64, time=0))
                    track.append(Message('note_off', note=note, velocity=64, time=480))  # Duration: 480 ticks

            except ValueError:
                print(f"Skipping invalid line (cannot convert parts to integers): {line}")
                continue  # Skip invalid lines

    # Save the MIDI file
    mid.save(output_file)
    print(f"Conversion complete. MIDI file saved as {output_file}.")

# Example usage
convert_chordz_to_midi('chordz_input.txt', 'output.mid')