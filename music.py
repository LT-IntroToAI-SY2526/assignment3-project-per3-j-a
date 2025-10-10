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

    (#10
        "Doris",
        "Earl Sweatshirt",
        2013,
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
        1973,
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
    (
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
    (
        "the dresser",
        "peter yates",
        1984,
        ["albert finney", "tom courtenay", "edward fox", "zena walker"],
    ),
    (
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
    (
        "the exorcist",
        "william friedkin",
        1973,
        [
            "ellen burstyn",
            "linda blair",
            "jason miller",
            "max von sydow",
            "kitty winn",
            "lee j cobb",
        ],
    ),
    (
        "a fish called wanda",
        "michael chrichton",
        1988,
        [
            "john cleese",
            "jamie lee curtis",
            "kevin kline",
            "michael palin",
            "maria aitken",
            "tom georgeson",
            "patricia hayes",
        ],
    ),
    (
        "flirting",
        "john duigan",
        1992,
        [
            "noah taylor",
            "thandie newton",
            "nicole kidman",
            "bartholomew rose",
            "felix nobis",
            "josh picker",
            "kiri paramore",
        ],
    ),
    ("gates of heaven", "errol morris", 1978, []),
    (
        "house of games",
        "david mamet",
        1987,
        [
            "lindsay crouse",
            "joe mantegna",
            "mike nussman",
            "lilia skala",
            "j t walsh",
            "jack wallace",
        ],
    ),
    (
        "iceman",
        "fred schepisi",
        1984,
        ["timothy hutton", "john lone", "lindsay crouse"],
    ),
    (
        "jaws",
        "steven spielberg",
        1975,
        [
            "roy scheider",
            "robert shaw",
            "richard dreyfuss",
            "lorraine gary",
            "murray hamilton",
        ],
    ),
    (
        "johnny got his gun",
        "dalton trumbo",
        1971,
        [
            "timothy bottoms",
            "kathy fields",
            "jason robards",
            "diane varsi",
            "donald sutherland",
            "eduard franz",
        ],
    ),
    (
        "local hero",
        "bill forsyth",
        1983,
        [
            "burt lancaster",
            "peter reigert",
            "peter capaldi",
            "fulton mckay",
            "denis lawson",
        ],
    ),
    (
        "malcolm x",
        "spike lee",
        1992,
        [
            "denzel washington",
            "angela basset",
            "albert hall",
            "al freeman jr",
            "delroy lindo",
            "spike lee",
        ],
    ),
    (
        "departed", 
        "martin scorsese",
        2006,
        [
            "leonardo dicaprio",
            "jack nicholson",
            "matt Damon",
            "mark wahlberg",
            "martin sheen",
        ]

    )
        (
        "pulp fiction",
        "quentin tarantino",
        1994,
        [
            "john travolta",
            "uma thurman",
            "samuel l. jackson",
            "bruce willis",
            "ving rhames",
        ],
    ),
    (
        "the shawshank redemption",
        "frank darabont",
        1994,
        [
            "tim robbins",
            "morgan freeman",
            "bob gunton",
            "william sadler",
            "clancy brown",
        ],
    ),
    (
        "parasite",
        "bong joon-ho",
        2019,
        [
            "song kang-ho",
            "lee sun-kyun",
            "cho yeo-jeong",
            "choi woo-shik",
            "park so-dam",
        ],
    ),
    (
        "black panther",
        "ryan coogler",
        2018,
        [
            "chadwick boseman",
            "michael b. jordan",
            "lupita nyong'o",
            "danai gurira",
            "letitia wright",
        ],
    ),
    (
        "mad max: fury road",
        "george miller",
        2015,
        [
            "tom hardy",
            "charlize theron",
            "nicholas hoult",
            "zoe kravitz",
            "rosi",
        ],
    )    

]