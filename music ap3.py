from music import Album_db
from match import match
from typing import List, Tuple, Callable, Any

# The projection functions, that give us access to certain parts of a "album" (a tuple)
def get_album(Album_db: Tuple[str, str, int, List[str]]) -> str:
    return Album_db[0]


def get_artist(Album_db: Tuple[str, str, int, List[str]]) -> str:
    return Album_db[1]


def get_year(Album_db: Tuple[str, str, int, List[str]]) -> int:
    return Album_db[2]


def get_songs(Album_db: Tuple[str, str, int, List[str]]) -> List[str]:
    return Album_db[3]


# Below are a set of actions. Each takes a list argument and returns a list of answers
# according to the action and the argument. It is important that each function returns a
# list of the answer(s) and not just the answer itself.


def album_by_year(matches: List[str]) -> List[str]:
    """Finds all Albums made in the passed in year

    Args:
        matches - a list of 1 string, just the year. Note that this year is passed as a
            string and should be converted to an int

    Returns:
        a list of Album albums made in the passed in year
    """
    #["1974"]
    year = int(matches[0])
    result = []
    for Album in Album_db:
        if get_year(Album) == year:
            result.append(get_album(Album))
    return result    


def album_by_year_range(matches: List[str]) -> List[str]:
    """Finds all Albums made in the passed in year range

    Args:
        matches - a list of 2 strings, the year beginning the range and the year ending
            the range. For example, to get Albums from 1991-1994 matches would look like
            this - ["1991", "1994"] Note that these years are passed as strings and
            should be converted to ints.

    Returns:
        a list of Album albums made during those years, inclusive (meaning if you pass
        in ["1991", "1994"] you will get Albums made in 1991, 1992, 1993 & 1994)
    """
    result = []
    start_year =  int(matches[0])
    end_year =  int(matches[1])

    for Album in Album_db:
        Album_year = get_year(Album)
        if start_year <= Album_year <= end_year:
            result.append(get_album(Album))
    return result

def album_before_year(matches: List[str]) -> List[str]:
    """Finds all Albums made before the passed in year

    Args:
        matches - a list of 1 string, just the year. Note that this year is passed as a
            string and should be converted to an int

    Returns:
        a list of Album albums made before the passed in year, exclusive (meaning if you
        pass in 1992 you won't get any Albums made that year, only before)
    """
    year = int(matches[0])
    result = []
    for Album in Album_db:
            if get_year(Album) < year:
             result.append(get_album(Album))
    return result    

def album_after_year(matches: List[str]) -> List[str]:
    """Finds all Albums made after the passed in year

    Args:
        matches - a list of 1 string, just the year. Note that this year is passed as a
            string and should be converted to an int

    Returns:
        a list of Album albums made after the passed in year, exclusive (meaning if you
        pass in 1992 you won't get any Albums made that year, only after)
    """
    year = int(matches[0])
    result = []
    for Album in Album_db:
            if get_year(Album) > year:
             result.append(get_album(Album))
    return result


def artist_by_album(matches: List[str]) -> List[str]:
    """Finds artist of Album based on album

    Args:
        matches - a list of 1 string, just the album

    Returns:
        a list of 1 string, the artist of the Album
    """
    result = []
    album = matches[0]

    for Album in Album_db:
        if get_album(Album) == album:
            result.append(get_artist(Album))
    return result


def album_by_artist(matches: List[str]) -> List[str]:
    """Finds Albums directed by the passed in artist

    Args:
        matches - a list of 1 string, just the artist

    Returns:
        a list of Albums albums directed by the passed in artist
    """
    result = []
    artist = matches[0]

    for Album in Album_db:
        if get_artist(Album) == artist:
            result.append(get_album(Album))
    return result


def songs_by_album(matches: List[str]) -> List[str]:
    """Finds songs who acted in the passed in Album album

    Args:
        matches - a list of 1 string, just the Album album

    Returns:
        a list of songs who acted in the passed in album
    """

    result = []
    album = matches[0]

    for Album in Album_db:
        if get_album(Album) == album:
            result = get_songs(Album)
            break
    return result



def year_by_album(matches: List[str]) -> List[int]:
    """Finds year of passed in Album album

    Args:
        matches - a list of 1 string, just the Album album

    Returns:
        a list of one item (an int), the year that the Album was made
    """
    result = []
    album = (matches[0])
    for Album in Album_db:
        if get_album(Album) == album:
            result.append(get_year(Album))
    return result   


def album_by_song(matches: List[str]) -> List[str]:
    """Finds albums of all Albums that the given song was in

    Args:
        matches - a list of 1 string, just the song

    Returns:
        a list of Album albums that the song acted in
    """
    result = []
    song_name = matches[0]

    for Album in Album_db:
        songs = get_songs(Album)

        for song in songs:
            if song_name in song:
                result.append(get_album(Album))
                break
    return result

def artist_by_year(matches: List[str]) -> List[int]:
    """Finds year of passed in Album album

    Args:
        matches - a list of 1 string, just the Album album

    Returns:
        a list of one item (an int), the year that the Album was made
    """
    result = []
    year = matches[0]

    for Album in Album_db:
        if get_artist(Album) == year:
            result = get_artist(Album)
            break
    return result

# dummy argument is ignored and doesn't matter
def bye_action(dummy: List[str]) -> None:
    raise KeyboardInterrupt


# The pattern-action list for the natural language query system A list of tuples of
# pattern and action It must be declared here, after all of the function definitions
pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("what Albums were made in _"), album_by_year),
    (str.split("what Albums were made between _ and _"), album_by_year_range),
    (str.split("what Albums were made before _"), album_before_year),
    (str.split("what Albums were made after _"), album_after_year),
    # note there are two valid patterns here two different ways to ask for the artist
    # of a Album
    (str.split("who directed %"), artist_by_album),
    (str.split("who was the artist of %"), artist_by_album),
    (str.split("what Albums were directed by %"), album_by_artist),
    (str.split("who acted in %"), songs_by_album),
    (str.split("when was % made"), year_by_album),
    (str.split("in what Albums did % appear"), album_by_song),
    (str.split("Who directed a Album in _"),artist_by_year)
    (["bye"], bye_action),
]


def search_pa_list(src: List[str]) -> List[str]:
    """Takes source, finds matching pattern and calls corresponding action. If it finds
    a match but has no answers it returns ["No answers"]. If it finds no match it
    returns ["I don't understand"].

    Args:
        source - a phrase represented as a list of words (strings)

    Returns:
        a list of answers. Will be ["I don't understand"] if it finds no matches and
        ["No answers"] if it finds a match but no answers
    """

    for pat, act in pa_list:
        mat = match(pat,src)

        if mat is not None:
            answer = act(mat)
            return answer if answer else ["No answers"]
    return ["I don't understand"]



def query_loop() -> None:
    """The simple query loop. The try/except structure is to catch Ctrl-C or Ctrl-D
    characters and exit gracefully.
    """
    print("Welcome to the Album database!\n")
    while True:
        try:
            print()
            query = input("Your query? ").replace("?", "").lower().split()
            answers = search_pa_list(query)
            for ans in answers:
                print(ans)

        except (KeyboardInterrupt, EOFError):
            break

    print("\nSo long!\n")


# uncomment the following line once you've written all of your code and are ready to try
# it out. Before running the following line, you should make sure that your code passes
# the existing asserts.
# query_loop()
"""
if __name__ == "__main__":
    assert isinstance(album_by_year(["1974"]), list), "album_by_year not returning a list"
    assert sorted(album_by_year(["1974"])) == sorted(
        ["amarcord", "chinatown"]
    ), "failed album_by_year test"
    assert isinstance(album_by_year_range(["1970", "1972"]), list), "album_by_year_range not returning a list"
    assert sorted(album_by_year_range(["1970", "1972"])) == sorted(
        ["the godfather", "johnny got his gun"]
    ), "failed album_by_year_range test"
    assert isinstance(album_before_year(["1950"]), list), "album_before_year not returning a list"
    assert sorted(album_before_year(["1950"])) == sorted(
        ["casablanca", "citizen kane", "gone with the wind", "metropolis"]
    ), "failed album_before_year test"
    assert isinstance(album_after_year(["1990"]), list), "album_after_year not returning a list"
    assert sorted(album_after_year(["1990"])) == sorted(
        ["boyz n the hood", "dead again", "the crying game", "flirting", "malcolm x", "Silence of the Lambs"]
    ), "failed album_after_year test"
    assert isinstance(artist_by_album(["jaws"]), list), "artist_by_album not returning a list"
    assert sorted(artist_by_album(["jaws"])) == sorted(
        ["steven spielberg"]
    ), "failed artist_by_album test"
    assert isinstance(album_by_artist(["steven spielberg"]), list), "album_by_artist not returning a list"
    assert sorted(album_by_artist(["steven spielberg"])) == sorted(
        ["jaws"]
    ), "failed album_by_artist test"
    assert isinstance(songs_by_album(["jaws"]), list), "songs_by_album not returning a list"
    assert sorted(songs_by_album(["jaws"])) == sorted(
        [
            "roy scheider",
            "robert shaw",
            "richard dreyfuss",
            "lorraine gary",
            "murray hamilton",
        ]
    ), "failed songs_by_album test"
    assert sorted(songs_by_album(["Album not in database"])) == [], "failed songs_by_album not in database test"
    assert isinstance(year_by_album(["jaws"]), list), "year_by_album not returning a list"
    assert sorted(year_by_album(["jaws"])) == sorted(
        [1975]
    ), "failed year_by_album test"
    assert isinstance(album_by_song(["orson welles"]), list), "album_by_song not returning a list"
    assert sorted(album_by_song(["orson welles"])) == sorted(
        ["citizen kane", "othello"]
    ), "failed album_by_song test"
    
    
    assert sorted(search_pa_list(["hi", "there"])) == sorted(
        ["I don't understand"]
    ), "failed search_pa_list test 1"
    assert sorted(search_pa_list(["who", "directed", "jaws"])) == sorted(
        ["steven spielberg"]
    ), "failed search_pa_list test 2"
    assert sorted(
        search_pa_list(["what", "Albums", "were", "made", "in", "2020"])
    ) == sorted(["No answers"]), "failed search_pa_list test 3"

    print("All tests passed!")
    """