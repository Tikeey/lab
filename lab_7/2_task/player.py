import pygame
import keyboard
import os

pygame.mixer.init()


songs = [
    "songs/song_1.mp3",
    "songs/song_2.mp3",
    "songs/song_3.mp3"
]

songs = [song for song in songs if os.path.exists(song)]

if not songs:

    print("No valid songs found. Add MP3 files in the directory.")

    exit()

current_index = 0

def play_music():

    pygame.mixer.music.load(songs[current_index])

    pygame.mixer.music.play()
    
    print(f"▶️ Playing: {songs[current_index]}")

def stop_music():

    pygame.mixer.music.stop()

    print("⏹️ Music Stopped.")

def next_song():

    global current_index

    current_index = (current_index + 1) % len(songs)

    play_music()

def previous_song():

    global current_index

    current_index = (current_index - 1) % len(songs)

    play_music()

keyboard.add_hotkey("w", play_music)
keyboard.add_hotkey("s", stop_music).add_hotkey("d", next_song)
keyboard.add_hotkey("a", previous_song)

print("🎵 Music Player Started! Controls:")

print("Press 'W' to Play, 'S' to Stop, 'D' for Next, 'A' for Previous")

keyboard.wait("esc")
