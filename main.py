class MediaPlayer:
    def play(self, file_type, file_name):
        pass


# Legacy Class (Old System - only supports MP3)
class LegacyMediaPlayer:
    def play_mp3(self, file_name):
        print(f"[Legacy] Playing MP3 file: {file_name}")


# New Advanced Players (Different Interfaces)
class MP4Player:
    def play_mp4(self, file_name):
        print(f"[Advanced] Playing MP4 file: {file_name}")


class VLCPlayer:
    def play_vlc(self, file_name):
        print(f"[Advanced] Playing VLC file: {file_name}")


# Adapter Class
class MediaAdapter(MediaPlayer):
    def __init__(self, file_type):
        if file_type == "mp4":
            self.player = MP4Player()
        elif file_type == "vlc":
            self.player = VLCPlayer()
        else:
            self.player = None

    def play(self, file_type, file_name):
        if file_type == "mp4":
            self.player.play_mp4(file_name)
        elif file_type == "vlc":
            self.player.play_vlc(file_name)
        else:
            print("Format not supported by adapter")


# Client Class
class AudioPlayer(MediaPlayer):
    def __init__(self):
        self.legacy_player = LegacyMediaPlayer()

    def play(self, file_type, file_name):
        if file_type == "mp3":
            self.legacy_player.play_mp3(file_name)
        elif file_type in ["mp4", "vlc"]:
            adapter = MediaAdapter(file_type)
            adapter.play(file_type, file_name)
        else:
            print(f"Invalid format: {file_type}")


# Usage
if __name__ == "__main__":
    player = AudioPlayer()

    player.play("mp3", "song.mp3")
    player.play("mp4", "video.mp4")
    player.play("vlc", "movie.vlc")
    player.play("avi", "clip.avi")