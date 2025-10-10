# the content of the movie database is taken from the textbook Concrete Abstractions: An
# Introduction to Computer Science Using Scheme, by Max Hailperin, Barbara Kaiser, and
# Karl Knight, Copyright (c) 1998 by the authors. Full text is available for free at
# http://www.gustavus.edu/+max/concrete-abstractions.html

# the Scheme file, Revision 1.3 as of 2005/12/20 14:09:37, has been reformated for
# Python. The original file is available as
# http://www.gustavus.edu/academics/mcs/max/concabs/code/movie.scm

# list of tuples w/ following format (the first tuple in the list is also annotated):
# each tuple contains title, director, year and actors/actresses
# `[(title, director, year, [actress_one, actor_two, ...]), ...]`
from typing import List, Tuple

album_db: List[Tuple[str, str, int, List[str]]] = [
    #Juan's 15 sections of albums
    (#1
        "Plastic Beach",  # name of song 
        "Gorillaz",  # director
        2010,  # year
        [
            "Plastic Beach",
            "On Melancholy Hill",
            "Rhinestone Eyes",
            "Glitter Freeze",
        ],  # actors/actresses
    ),

    (#5
        "Childish Gambino",
        "Camp",
        2011,
        [
            "L.E.S", 
            "Fire Fly", 
            "Bonfire", 
            "Heartbeat", 
        ],
    )
    (#7
        "Frank Ocean",
        "Channel Orange",
        2012,
        [
            "Pink Matter",
            "Super Rich Kids",
            "Thinking Bout You",
            "End",
        ],
    ),
    (#8
        "citizen kane",
        "orson welles",
        1941,
        [
            "orson welles",
            "joseph cotten",
            "dorothy comingore",
            "ray collins",
            "george coulouris",
            "agnes moorehead",
            "ruth warrick",
        ],
    ),
    (#9
        "gone with the wind",
        "victor fleming",
        1939,
        [
            "clark gable",
            "vivien leigh",
            "leslie howard",
            "olivia de havilland",
            "hattie mcdaniel",
            "butterfly mcqueen",
        ],
    ),
    (#10
        "lawrence of arabia",
        "david lean",
        1962,
        [
            "Woah",
            "Sasquatch",
            "Molasses",
            "Chum",
           
        ],
    ),
   
    (#13
        "The Black Keys",
        "Turn Blue",
        2014,
        [
            "Weight of Love",
            "Turn Blue",
            "Fever",
            "In Time",
        ],
    ),
    
    (
        "after the rehearsal",
        "ingmar bergman",
        1984,
        ["erland josephson", "ingrid thulin", "lena olin", "nadja palmstjerna-weiss"],
    ),
    (
        "amadeus",
        "milos forman",
        1984,
        [
            "f murray abraham",
            "tom hulce",
            "elizabeth berridge",
            "simon callow",
            "roy dotrice",
            "christine ebersole",
            "jeffrey jones",
        ],
    ),
    (
        "blood simple",
        "joel coen",
        1985,
        [
            "john getz",
            "frances mcdormand",
            "dan hedaya",
            "m emmet walsh",
            "samm-art williams",
        ],
    ),
    (
        "chinatown",
        "roman polanski",
        1974,
        [
            "jack nicholson",
            "faye dunaway",
            "john huston",
            "perry lopez",
            "john hillerman",
            "darrell zwerling",
            "diane ladd",
            "roman polanski",
        ],
    ),
    (
        "the cotton club",
        "francis ford coppola",
        1984,
        [
            "richard gere",
            "gregory hines",
            "diane lane",
            "lonette mckee",
            "bob hoskins",
            "james remar",
            "fred gwynne",
        ],
    ),
    (
        "the crying game",
        "neil jordan",
        1992,
        [
            "stephen rea",
            "jaye davidson",
            "forest whitaker",
            "miranda richardson",
            "adrian dunbar",
            "breffini mckenna",
            "joe savino",
        ],
    ),
    (
        "the day of the jackal",
        "fred zinnemann",
        2,
        [
            "edward fox",
            "terence alexander",
            "michel auclair",
            "alan badel",
            "tony britton",
            "denis carey",
            "olga georges-picot",
            "cyril cusack",
        ],
    ),
    (#3
        "diva",
        "jean-jacques beineix",
        1981,
        [
            "wilhelmenia wiggins fernandez",
            "frederic andrei",
            "richard bohringer",
            "thay an luu",
            "jacques fabbri",
            "chantal deruaz",
        ],
    ),
    (#4
        "the dresser",
        "peter yates",
        1984,
        ["albert finney", 
         "tom courtenay", 
         "edward fox", 
         "zena walker"
        ],
    ),
    (#5
        "el norte",
        "gregory nava",
        1983,
        [
            "zaide silvia gutierrez",
            "david villalpando",
            "ernesto gomez cruz",
            "alicia del lago",
            "trinidad silva",
        ],
    ),
]