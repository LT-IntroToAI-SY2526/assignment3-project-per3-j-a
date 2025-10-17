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

    (#2
        "Childish Gambino",
        "Camp",
        2011,
        [
            "L.E.S", 
            "Fire Fly", 
            "Bonfire", 
            "Heartbeat", 
        ],
    ),

    (#3
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

    (#4 
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
   
    (#5
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
  
    #Max's Sections
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
        "Donda",
        "Kanye West ",
        2021,
        [
            "Hurricane",
            "Praise God",
            "Off The Grid",
            "Believe What I Say",
            "New Again",
        ],
    ),

    (#3
        "Mr. Morale & the Big Steppers",
        "Kendrick Lamar",
        2022,
        [
            "Father Time",
            "Die Hard",
            "Count Me Out",
            "Mr. Morale",
        ],
    ),

    (#4
        "For All The Dogs",
        "Drake",
        2023,
        [
         "Slime You Out", 
         "First Person Shooter", 
         "Virginia Beach", 
         "Bahamas Promises"
         ],
    ),

    (#5
        "Chromakopia",
        "Tyler, The Creator",
        2024,
        [
            "St. chroma",
            "Like Him",
            "Noid",
            "Sticky",
        ],
    ),

]
