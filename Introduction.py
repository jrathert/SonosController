import logging

import soco
from soco import SoCo
from soco.music_services import Account
from soco.music_services import MusicService


def list_music_services():
    print(MusicService.get_subscribed_services_names())

def list_players():
    speakers = soco.discover()
    if speakers is not None and len(speakers) > 0:
        for s in speakers:
            print("Speaker '{}' has IP: {}".format(s.player_name, s.ip_address))
    else:
        print("No speaker found")

def get_device(roomname: str):
    speakers = soco.discover()
    spkr = None
    if speakers is not None:
        for spkr in speakers:
            if spkr.player_name == roomname:
                break
        else:
            spkr = None
    return spkr

def print_current_track_info(room):
    if type(room) == SoCo:
        speaker = room
    else:
        speaker = get_device(room)
    info = speaker.get_current_track_info()
    for k in ['artist', 'album', 'title', 'uri']:
        print ("{}: {}".format(k, info[k]))

def play_weekly_discover_in_room(room):
    if type(room) == SoCo:
        speaker = room
    else:
        speaker = get_device(room)

    # URI of my weekly discovery list
    # spotify:track:7HFaTkpIeG0pXINEm7EEG4
    # http://localhost:5005/Mobil/spotify/now/spotify:track:7HFaTkpIeG0pXINEm7EEG4

    # spotify:user:spotifydiscover:playlist:2fNlVzK3IlghhG87HZqpCA
    # http://localhost:5005/Mobil/spotify/now/spotify:user:spotifydiscover:playlist:2fNlVzK3IlghhG87HZqpCA

    #"x-rincon-cpcontainer:0006206c
    #my_uri = "spotify:user:spotifydiscover:playlist:2fNlVzK3IlghhG87HZqpCA"
    #x - sonos - spotify:

    #my_uri = "x-rincon-cpcontainer:0006206cspotify%3Auser%3Aspotifydiscover%3Aplaylist%3A2fNlVzK3IlghhG87HZqpCA"

    #speaker.clear_queue()

    # single song
    speaker.play_uri("x-sonos-spotify:spotify%3atrack%3a25D1lrwfv0TopyzaNfhc0E?sid=9&flags=8224&sn=9")

    # playlist of the week
    #speaker.play_uri("x-rincon-cpcontainer:spotify%3auser%3aspotifydiscover%3aplaylist%3a2fNlVzK3IlghhG87HZqpCA?sid=9&flags=8224&sn=9")
    #speaker.add_to_queue("x-sonos-spotify:spotify%3auser%3aspotifydiscover%3aplaylist%3a2fNlVzK3IlghhG87HZqpCA?sid=9&flags=8224&sn=9")


if __name__ == "__main__":
    LOG_LEVEL = logging.FATAL# FATAl, DEBUG, INFO
    logging.basicConfig(format="%(asctime)s [%(levelname)s]: %(message)s", level=LOG_LEVEL)
    #logging.getLogger("soco").setLevel(logging.FATAL)


    logging.info("Start program")
#    list_players()
    player = get_device("Mobil")
    player = SoCo('192.168.1.36')
    print("Plaver is: '{}'".format(player.ip_address))

    albums = player.music_library.get_albums(search_term='White')
    for album in albums:
        print('Added:', album.creator, "-", album.title)

    #spotify = MusicService('Spotify')
    #print(spotify.available_search_categories)
    #print(spotify.search("artists", "The Cure"))
    #s = get_device("Küche")
    #q = s.get_queue()
    #s.add_to_queue("spotify:track:7HFaTkpIeG0pXINEm7EEG4")

    #play_weekly_discover_in_room(player)
    logging.info("End program")
