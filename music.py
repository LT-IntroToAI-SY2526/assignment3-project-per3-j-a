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

Album_db: List[Tuple[str, str, int, List[str]]] = [
    #Juan's 15 sections of albums
    (#1
        "amarcord",  # name of song 
        "federico fellini",  # director
        1974,  # year
        [
            "magali noel",
            "bruno zanin",
            "pupella maggio",
            "armando drancia",
        ],  # actors/actresses
    ),
    (#2
        "the big easy",
        "jim mcbride",
        1987,
        [
            "dennis quaid",
            "ellen barkin",
            "ned beatty",
            "lisa jane persky",
            "john goodman",
            "charles ludlam",
        ],
    ),
    (#3
        "boyz n the hood",
        "john singleton",
        1991,
        [
            "cuba gooding jr.",
            "ice cube",
            "larry fishburne",
            "tyra ferrell",
            "morris chestnut",
        ],
    ),
    (#4
        "dead again",
        "kenneth branagh",
        1991,
        [
            "kenneth branagh",
            "emma thompson",
            "andy garcia",
            "derek jacobi",
            "hanna schygulla",
        ],
    ),
    (#5
        "the godfather",
        "francis ford coppola",
        1972,
        ["marlon brando", "al pacino", "james caan", "robert duvall", "diane keaton"],
    ),
    (#6
        "an american in paris",
        "vincente minnelli",
        1952,
        ["gene kelley", "leslie caron", "oscar levant", "nina foch", "george guetary"],
    ),
    (#7
        "casablanca",
        "michael curtiz",
        1942,
        [
            "humphrey bogart",
            "ingrid bergman",
            "paul henreid",
            "claude rains",
            "sydney greenstreet",
            "peter lorre",
            "s z sakall",
            "conrad veidt",
            "dooley wilson",
        ],
    ),

    #Max's Section
    (#1
        "Currents",
        "Tame Impala",
        2015,
        [
            "Let It Happen", 
            "The Less I Know The Better", 
            "New Person, Same Old Mistakes", 
            "Eventually"
        ],
    ),
    (#2
        "Views",
        "Drake",
        2016,
        [
            "9",
            "Summers Over Interlude",
            "Views",
            "Controlla",
        ],
    ),
    (#3
        "DAMN",
        "Kendrick Lamar",
        2017,
        [
            "DNA",
            "Humble",
            "PRIDE",
            "DUCKWORTH",
        ],
    ),
    (#4
        "ASTROWORLD",
        "Travis Scott",
        2018,
        [
            "SKELETONS",
            "SICKO MODE",
            "5% TNT",
            "BUTTERFLY EFFECT",
        ],
    ),
    (#5
        "Igor",
        "Tyler, The Creator",
        2019,
        [
            "EARFQUAKE",
            "IGOR'S THEME",
            "NEW MAGIC WAND",
            "ARE WE STILL FRIENDS?",
        ],
    ),
    #Adrian's Section
    (#1
        "After Hours",
        "The Weekend",
        2020,
        [
            "Blinding Lights",
            "Save Your Tears",
            "After Hours",
            "Heartless",
        ],
    ),
    (#2
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