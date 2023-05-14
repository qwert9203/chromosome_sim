"""
Copyright (c) 2022 Yui Hong Chow

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import random
import tkinter.messagebox
from tkinter import *

from PIL import Image, ImageTk, ImageDraw, ImageFont

version = "1.0"

features2 = {
    "gender": {
        "variants": {
            0: "./sprites/gender_0.png",  # female
            1: "./sprites/gender_1.png",  # male
            2: "./sprites/gender_2.png"  # ???
        },
        "mods": {
            "!": {},
            "*": {
                0: (12, 8)
            },
            "=": {
                0: [360, 360]
            },
            "+": {}
        },
        "offset_x": 0,
        "offset_y": 0,
        "layer": 5
    },
    "hairstyle": {
        "variants": {
            0: "./sprites/hairstyle_0.png",  # long, curly
            1: "./sprites/hairstyle_1.png",  # long, wavy
            2: "./sprites/hairstyle_2.png",  # long, straight
            3: "./sprites/hairstyle_3.png",  # short, curly
            4: "./sprites/hairstyle_4.png",  # short, wavy
            5: "./sprites/hairstyle_5.png"  # short, straight
        },
        "mods": {
            "!": {
                0: [0, 0, 0],
                1: [51, 0, 0],
                2: [102, 51, 0],
                3: [153, 102, 0],
                4: [204, 204, 0],
                5: [255, 255, 0],
                6: [255, 255, 89],
                7: [255, 255, 204],
                8: [255, 255, 204],
                9: [10, 10, 10]
            },
            "*": {},
            "=": {},
            "+": {
                0: (1.5, 1, 1),
                1: (1.25, 1, 1),
                2: (1, 1, 1)
            }
        },
        "offset_x": 0,
        "offset_y": 0,
        "layer": 3
    },
    "faceshape": {
        "variants": {
            0: "./sprites/faceshape_0.png",  # round face
            1: "./sprites/faceshape_1.png"  # square face
        },
        "mods": {
            "!": {
                0: [255, 249, 226],  # 11
                1: [236, 215, 160],  # 19
                2: [223, 185, 120],  # 24
                3: [157, 107, 65],  # 27
                4: [100, 45, 14],  # 30
                5: [62, 26, 13],  # 34
                6: [45, 32, 36],  # 35
            },
            "*": {},
            "=": {},
            "+": {}
        },
        "offset_x": 0,
        "offset_y": 0,
        "layer": 0
    },
    "chinshape": {
        "variants": {
            0: "./sprites/chinshape_0.png",  # round chin
            1: "./sprites/chinshape_1.png"  # square chin
        },
        "mods": {
            "!": {
                0: [255, 249, 226],  # 11
                1: [236, 215, 160],  # 19
                2: [223, 185, 120],  # 24
                3: [157, 107, 65],  # 27
                4: [100, 45, 14],  # 30
                5: [62, 26, 13],  # 34
                6: [45, 32, 36],  # 35
            },
            "*": {},
            "=": {},
            "+": {}
        },
        "offset_x": 0,
        "offset_y": 0,
        "layer": 0
    },
    "chinshape2": {
        "variants": {
            0: "./sprites/chinshape_0.png",  # round chin
            1: "./sprites/chinshape_1.png"  # square chin
        },
        "mods": {
            "!": {
                0: [255, 249, 226],  # 11
                1: [236, 215, 160],  # 19
                2: [223, 185, 120],  # 24
                3: [157, 107, 65],  # 27
                4: [100, 45, 14],  # 30
                5: [62, 26, 13],  # 34
                6: [45, 32, 36],  # 35
            },
            "*": {},
            "=": {},
            "+": {}
        },
        "offset_x": 0,
        "offset_y": 0,
        "layer": 0
    },
    "cleftchin": {
        "variants": {
            0: "./sprites/empty.png",
            1: "./sprites/cleftchin.png"  # cleft chin
        },
        "mods": {
            "!": {},
            "*": {},
            "=": {},
            "+": {}
        },
        "offset_x": 0,
        "offset_y": 0,
        "layer": 1
    },
    "leye": {
        "variants": {
            0: "./sprites/leye_0.png",  # Almond
            1: "./sprites/leye_1.png",  # Round
        },
        "mods": {
            "!": {
                0: [36, 19, 5],
                1: [74, 45, 35],
                2: [41, 81, 249],
                3: [65, 133, 251],
                4: [140, 220, 254]
            },
            "*": {
                0: [1.1, 1.1],
                1: [1.0, 1.0],
                2: [0.8, 0.8]
            },
            "=": {
                0: [20, 0],
                1: [0, 0],
                2: [-20, 0]
            },
            "+": {}
        },
        "offset_x": 230,
        "offset_y": 380,
        "layer": 1
    },
    "reye": {
        "variants": {
            0: "./sprites/reye_0.png",  # almond
            1: "./sprites/reye_1.png",  # Round
        },
        "mods": {
            "!": {
                0: [36, 19, 5],
                1: [74, 45, 35],
                2: [41, 81, 249],
                3: [65, 133, 251],
                4: [140, 220, 254]
            },
            "*": {
                0: [1.1, 1.1],
                1: [1.0, 1.0],
                2: [0.8, 0.8]
            },
            "=": {
                0: [-20, 0],
                1: [0, 0],
                2: [20, 0]
            },
            "+": {}
        },
        "offset_x": 390,
        "offset_y": 380,
        "layer": 1
    },
    "widowspeak": {
        "variants": {
            0: "./sprites/empty.png",
            1: "./sprites/widowspeak.png"  # widows peak
        },
        "mods": {
            "!": {
                0: [0, 0, 0],
                1: [51, 0, 0],
                2: [102, 51, 0],
                3: [153, 102, 0],
                4: [204, 204, 0],
                5: [255, 255, 0],
                6: [255, 255, 89],
                7: [255, 255, 204],
                8: [255, 255, 204],
                9: [10, 10, 10]
            },
            "*": {},
            "=": {},
            "+": {}
        },
        "offset_x": 0,
        "offset_y": 0,
        "layer": 4
    },
    "leyebrow": {
        "variants": {
            0: "./sprites/leyebrow_0.png",  # almond
            1: "./sprites/leyebrow_1.png",  # round
        },
        "mods": {
            "!": {},
            "*": {},
            "=": {
                0: [20, 0],
                1: [0, 0],
                2: [-20, 0]
            },
            "+": {}
        },
        "offset_x": 220,
        "offset_y": 320,
        "layer": 2
    },
    "reyebrow": {
        "variants": {
            0: "./sprites/reyebrow_0.png",  # almond
            1: "./sprites/reyebrow_1.png",  # round
        },
        "mods": {
            "!": {},
            "*": {},
            "=": {
                0: [-20, 0],
                1: [0, 0],
                2: [20, 0]
            },
            "+": {}
        },
        "offset_x": 385,
        "offset_y": 320,
        "layer": 2
    },
    "leyelash": {
        "variants": {
            0: "./sprites/leyelash_0.png",  # almond
            1: "./sprites/leyelash_1.png",  # round
        },
        "mods": {
            "!": {},
            "*": {
                0: [1.1, 1.1],
                1: [1.0, 1.0],
                2: [0.8, 0.8]
            },
            "=": {
                0: [20, 0],
                1: [0, 0],
                2: [-20, 0]
            },
            "+": {}
        },
        "offset_x": 230,
        "offset_y": 380,
        "layer": 2
    },
    "reyelash": {
        "variants": {
            0: "./sprites/reyelash_0.png",  # almond
            1: "./sprites/reyelash_1.png",  # round
        },
        "mods": {
            "!": {},
            "*": {
                0: [1.1, 1.1],
                1: [1.0, 1.0],
                2: [0.8, 0.8]
            },
            "=": {
                0: [-20, 0],
                1: [0, 0],
                2: [20, 0]
            },
            "+": {}
        },
        "offset_x": 390,
        "offset_y": 380,
        "layer": 2
    },
    "mouth": {
        "variants": {
            0: "./sprites/mouth_0.png",  # thick, wide
            1: "./sprites/mouth_1.png",  # thick, avg
            2: "./sprites/mouth_2.png",  # thick, narrow
            3: "./sprites/mouth_3.png",  # thin, wide
            4: "./sprites/mouth_4.png",  # thin, avg
            5: "./sprites/mouth_5.png"  # thin, narrow
        },
        "mods": {
            "!": {},
            "*": {},
            "=": {},
            "+": {}
        },
        "offset_x": 290,
        "offset_y": 575,
        "layer": 1
    },
    "dimples": {
        "variants": {
            0: "./sprites/empty.png",
            1: "./sprites/dimples.png"  # dimples
        },
        "mods": {
            "!": {},
            "*": {},
            "=": {},
            "+": {}
        },
        "offset_x": 0,
        "offset_y": 0,
        "layer": 1
    },
    "nose": {
        "variants": {
            0: "./sprites/nose_0.png",  # rounded
            1: "./sprites/nose_1.png",  # pointed
        },
        "mods": {
            "!": {},
            "*": {
                0: [1.2, 1.2],
                1: [1.0, 1.0],
                2: [0.8, 0.8]
            },
            "=": {},
            "+": {}
        },
        "offset_x": 325,
        "offset_y": 455,
        "layer": 1
    },
    "earattachment": {
        "variants": {
            0: "./sprites/ear.png",  # ear without attachment
            1: "./sprites/earattachment.png"  # ear with attachment
        },
        "mods": {
            "!": {
                0: [255, 249, 226],  # 11
                1: [236, 215, 160],  # 19
                2: [223, 185, 120],  # 24
                3: [157, 107, 65],  # 27
                4: [100, 45, 14],  # 30
                5: [62, 26, 13],  # 34
                6: [45, 32, 36],  # 35
            },
            "*": {},
            "=": {},
            "+": {}
        },
        "offset_x": 0,
        "offset_y": 0,
        "layer": 1
    },
    "earhair": {
        "variants": {
            0: "./sprites/empty.png",
            1: "./sprites/earhair.png"  # hair on ears
        },
        "mods": {
            "!": {},
            "*": {},
            "=": {},
            "+": {}
        },
        "offset_x": 0,
        "offset_y": 0,
        "layer": 2
    },
    "cheekfreckles": {
        "variants": {
            0: "./sprites/empty.png",
            1: "./sprites/cheekfreckles.png"  # freckles on cheeks
        },
        "mods": {
            "!": {},
            "*": {},
            "=": {},
            "+": {}
        },
        "offset_x": 0,
        "offset_y": 0,
        "layer": 1
    },
    "foreheadfreckles": {
        "variants": {
            0: "./sprites/empty.png",
            1: "./sprites/foreheadfreckles.png"  # freckles on forehead
        },
        "mods": {
            "!": {},
            "*": {},
            "=": {},
            "+": {}
        },
        "offset_x": 0,
        "offset_y": 0,
        "layer": 1
    }
}

# 0 is dominant
chromosomes = {
    1: ["Ra", "rA"],
    2: ["Al", "aL"],
    3: ["SH", "sh"],
    4: ["aG", "Ag"],
    5: ["C", "c"],
    6: ["H", "h"],
    7: ["W", "w"],
    8: ["P", "p"],
    9: ["T2", "t1"],  # @
    10: ["HE", "he"],
    11: ["Fo", "fO"],
    12: ["IB", "ib"],
    13: ["V", "v"],
    14: ["U", "u"],
    15: ["M", "m"],
    16: ["k", "K"],
    17: ["Q", "q"],
    18: ["Hj", "hJ"],
    19: ["n", "N"],
    20: ["D", "d"],
    21: ["4", "3"],  # $
    22: ["Z", "z"],
    23: ["x", "y"]
}

chr_lettering = {
    "advanced": {
        1: ["Ra", "rA"],
        2: ["Al", "aL"],
        3: ["SH", "sh"],
        4: ["aG", "Ag"],
        5: ["C", "c"],
        6: ["H", "h"],
        7: ["W", "w"],
        8: ["P", "p"],
        9: ["T2", "t1"],  # @
        10: ["HE", "he"],
        11: ["Fo", "fO"],
        12: ["IB", "ib"],
        13: ["V", "v"],
        14: ["U", "u"],
        15: ["M", "m"],
        16: ["k", "K"],
        17: ["Q", "q"],
        18: ["Hj", "hJ"],
        19: ["n", "N"],
        20: ["D", "d"],
        21: ["4", "3"],  # $
        22: ["Z", "z"],
        23: ["X", "Y"]
    },
    "basic": {
        1: ["R", "r"],
        2: ["l", "L"],
        3: ["S", "s"],
        4: ["G", "g"],
        5: ["C", "c"],
        6: [" ", " "],
        7: ["W", "w"],
        8: ["P", "p"],
        9: ["T", "t"],  # @
        10: ["E", "e"],
        11: ["Fo", "fO"],
        12: ["IB", "ib"],
        13: ["V", "v"],
        14: ["U", "u"],
        15: ["M", "m"],
        16: ["k", "K"],
        17: ["Q", "q"],
        18: ["j", "J"],
        19: ["n", "N"],
        20: ["D", "d"],
        21: ["4", "3"],  # $
        22: ["Z", "z"],
        23: ["X", "Y"]
    }
}

features = {
    "WWxx": ["gender_0", "hairstyle_0"],  # curly haired female
    "Wwxx": ["gender_0", "hairstyle_1"],  # wavy haired female
    "wwxx": ["gender_0", "hairstyle_2"],  # straight haired female
    "WWxy": ["gender_1", "hairstyle_3"],  # curly haired male
    "Wwxy": ["gender_1", "hairstyle_4"],  # wavy haired male
    "wwxy": ["gender_1", "hairstyle_5"],  # straight haired male
    "WWyy": ["gender_2", "*gender_0", "hairstyle_0", "=gender_0"],  # covers the whole screen with an error
    "Wwyy": ["gender_2", "*gender_0", "hairstyle_0", "=gender_0"],
    "wwyy": ["gender_2", "*gender_0", "hairstyle_0", "=gender_0"],
    "RR": ["faceshape_0", "chinshape2_0"],  # round
    "Rr": ["faceshape_0", "chinshape2_0"],
    "rr": ["faceshape_1", "chinshape2_1"],  # square
    "LL": ["?chinshape_1", "?cleftchin_1", "?chinshape2_0"],
    "Ll": ["?chinshape_1", "?cleftchin_1", "?chinshape2_0"],
    "ll": ["?chinshape_0", "?cleftchin_0", "?chinshape2_1"],
    "SS": ["chinshape_0"],
    "Ss": ["chinshape_0"],
    "ss": ["chinshape_1"],
    "CC": ["cleftchin_1"],
    "Cc": ["cleftchin_1"],
    "cc": ["cleftchin_0"],
    "AAAAAA": ["!faceshape_0", "!chinshape_0", "!chinshape2_0", "!earattachment_0"],
    "AAAAAa": ["!faceshape_1", "!chinshape_1", "!chinshape2_1", "!earattachment_1"],
    "AAAAaa": ["!faceshape_2", "!chinshape_2", "!chinshape2_2", "!earattachment_2"],
    "AAAaaa": ["!faceshape_3", "!chinshape_3", "!chinshape2_3", "!earattachment_3"],  # default
    "AAaaaa": ["!faceshape_4", "!chinshape_4", "!chinshape2_4", "!earattachment_4"],
    "Aaaaaa": ["!faceshape_5", "!chinshape_5", "!chinshape2_5", "!earattachment_5"],
    "aaaaaa": ["!faceshape_6", "!chinshape_6", "!chinshape2_6", "!earattachment_6"],
    "HHHHHHHH": ["!hairstyle_0", "!widowspeak_0"],
    "HHHHHHHh": ["!hairstyle_1", "!widowspeak_1"],
    "HHHHHHhh": ["!hairstyle_2", "!widowspeak_2"],
    "HHHHHhhh": ["!hairstyle_3", "!widowspeak_3"],
    "HHHHhhhh": ["!hairstyle_4", "!widowspeak_4"],  # default
    "HHHhhhhh": ["!hairstyle_5", "!widowspeak_5"],
    "HHhhhhhh": ["!hairstyle_6", "!widowspeak_6"],
    "Hhhhhhhh": ["!hairstyle_7", "!widowspeak_7"],
    "hhhhhhhh": ["!hairstyle_8", "!widowspeak_8"],
    "BBFF": ["!leye_0", "!reye_0"],
    "BFFb": ["!leye_1", "!reye_1"],
    "FFbb": ["!leye_1", "!reye_1"],
    "BBFf": ["!leye_1", "!reye_1"],
    "BFbf": ["!leye_2", "!reye_2"],
    "Fbbf": ["!leye_2", "!reye_2"],
    "BBff": ["!leye_3", "!reye_3"],
    "Bbff": ["!leye_3", "!reye_3"],
    "bbff": ["!leye_4", "!reye_4"],
    "GG": ["+hairstyle_0"],
    "Gg": ["+hairstyle_1"],
    "gg": ["+hairstyle_2"],
    "PP": ["widowspeak_1"],
    "Pp": ["widowspeak_1"],
    "pp": ["widowspeak_0"],
    "TT": ["leyebrow_0", "reyebrow_0"],
    "Tt": ["leyebrow_0", "reyebrow_0"],
    "tt": ["leyebrow_1", "reyebrow_1"],
    "EE": ["=leyebrow_0", "=reyebrow_0"],
    "Ee": ["=leyebrow_1", "=reyebrow_1"],
    "ee": ["=leyebrow_2", "=reyebrow_2"],
    "OO": ["=leye_0", "=reye_0", "=leyelash_0", "=reyelash_0"],
    "Oo": ["=leye_1", "=reye_1", "=leyelash_2", "=reyelash_2"],
    "oo": ["=leye_2", "=reye_2", "=leyelash_2", "=reyelash_2"],
    "II": ["*leye_0", "*reye_0", "*leyelash_0", "*reyelash_0"],
    "Ii": ["*leye_1", "*reye_1", "*leyelash_1", "*reyelash_1"],
    "ii": ["*leye_2", "*reye_2", "*leyelash_2", "*reyelash_2"],
    "VV": ["leye_0", "reye_0", "leyelash_0", "reyelash_0"],
    "Vv": ["leye_0", "reye_0", "leyelash_0", "reyelash_0"],
    "vv": ["leye_1", "reye_1", "leyelash_1", "reyelash_1"],
    "MM": ["?leyelash_1", "?reyelash_1"],
    "Mm": ["?leyelash_1", "?reyelash_1"],
    "mm": ["?leyelash_0", "?reyelash_0"],
    "JJQQ": ["mouth_0"],  # thick wide
    "JJQq": ["mouth_1"],  # thick avg
    "JJqq": ["mouth_2"],  # thick narrow
    "JQQj": ["mouth_0"],
    "JQjq": ["mouth_1"],
    "Jjqq": ["mouth_2"],
    "QQjj": ["mouth_3"],  # thin wide
    "Qjjq": ["mouth_4"],  # thin avg
    "jjqq": ["mouth_5"],  # thin narrow
    "KK": ["dimples_1"],
    "Kk": ["dimples_1"],
    "kk": ["dimples_0"],
    "NN": ["*nose_0"],
    "Nn": ["*nose_1"],
    "nn": ["*nose_2"],
    "UU": ["nose_0"],
    "Uu": ["nose_0"],
    "uu": ["nose_1"],
    "ZZ": ["earattachment_0"],
    "Zz": ["earattachment_0"],
    "zz": ["earattachment_1"],
    "DD": ["earhair_1"],
    "Dd": ["earhair_1"],
    "dd": ["earhair_0"],
    "44": ["cheekfreckles_1"],
    "34": ["cheekfreckles_1"],
    "33": ["cheekfreckles_0"],
    "22": ["foreheadfreckles_1"],
    "12": ["foreheadfreckles_1"],
    "11": ["foreheadfreckles_0"]
}

basic_features = {
    "RR": ["faceshape_0", "chinshape2_0"],  # round
    "Rr": ["faceshape_0", "chinshape2_0"],
    "rr": ["faceshape_1", "chinshape2_1"],  # square
    "UU": ["nose_0"],
    "Uu": ["nose_0"],
    "uu": ["nose_1"],
    "PP": ["widowspeak_1", "hairstyle_4", "!widowspeak_9", "!hairstyle_9"],
    "Pp": ["widowspeak_1", "hairstyle_4", "!widowspeak_9", "!hairstyle_9"],
    "pp": ["widowspeak_0", "hairstyle_4", "!hairstyle_9"],
    "VV": ["leye_0", "reye_0"],
    "Vv": ["leye_0", "reye_0"],
    "vv": ["leye_1", "reye_1"],
    "XX": ["gender_0"],
    "XY": ["gender_1"],
    "JJ": ["mouth_1"],
    "Jj": ["mouth_1"],
    "jj": ["mouth_4"],
    "DD": ["earhair_1", "earattachment_0"],
    "Dd": ["earhair_1", "earattachment_0"],
    "dd": ["earhair_0", "earattachment_0"],
    "TT": ["leyebrow_0", "reyebrow_0"],
    "Tt": ["leyebrow_0", "reyebrow_0"],
    "tt": ["leyebrow_1", "reyebrow_1"]
}

table_info = {
    1: {
        "Trait": "Face shape",
        "Dominant": "Round face",
        "Recessive": "Square face",
        "Genotypes": {
            "RR": "Dominant",
            "Rr": "Dominant",
            "rr": "Recessive",
            "rR": "Dominant"
        }
    },
    8: {
        "Trait": "Hairline",
        "Dominant": "Widow's peak",
        "Recessive": "Straight hairline",
        "Genotypes": {
            "PP": "Dominant",
            "Pp": "Dominant",
            "pp": "Recessive",
            "pP": "Dominant",
        }
    },
    9: {
        "Trait": "Eyebrow",
        "Dominant": "Thick eyebrow",
        "Recessive": "Thin eyebrow",
        "Genotypes": {
            "TT": "Dominant",
            "Tt": "Dominant",
            "tt": "Recessive",
            "tT": "Dominant",
        }
    },
    13: {
        "Trait": "Eye shape",
        "Dominant": "Almond eye",
        "Recessive": "Round eye",
        "Genotypes": {
            "VV": "Dominant",
            "Vv": "Dominant",
            "vv": "Recessive",
            "vV": "Dominant",
        }
    },
    14: {
        "Trait": "Nose shape",
        "Dominant": "Round nose",
        "Recessive": "Pointed nose",
        "Genotypes": {
            "UU": "Dominant",
            "Uu": "Dominant",
            "uu": "Recessive",
            "uU": "Dominant",
        }
    },
    18: {
        "Trait": "Lip thickness",
        "Dominant": "Thick lip",
        "Recessive": "Thin lip",
        "Genotypes": {
            "JJ": "Dominant",
            "Jj": "Dominant",
            "jj": "Recessive",
            "jJ": "Dominant",
        }
    },
    20: {
        "Trait": "Hairy ear",
        "Dominant": "Hairy ear",
        "Recessive": "Not hairy ear",
        "Genotypes": {
            "DD": "Dominant",
            "Dd": "Dominant",
            "dd": "Recessive",
            "dD": "Dominant",
        }
    },
}

basic_chr = [0, 7, 8, 12, 13, 17, 19, 22]

feature_indices = [
    (0, 1),  # 12
    (2, 3),  # 34
    (4, 9),  # Aa
    (10, 11, 18, 19),  # BbFf
    (12, 13),  # Cc
    (14, 15),  # Dd
    (16, 17),  # Ee
    (20, 21),  # Gg
    (22, 29),  # Hh
    (30, 31),  # Ii
    (32, 33, 46, 47),  # JjQq
    (34, 35),  # Kk
    (36, 37),  # Ll
    (38, 39),  # Mm
    (40, 41),  # Nn
    (42, 43),  # Oo
    (44, 45),  # Pp
    (48, 49),  # Rr
    (50, 51),  # Ss
    (52, 53),  # Tt
    (54, 55),  # Uu
    (56, 57),  # Vv
    (58, 61),  # Wwxy
    (62, 63),  # Zz
]


class Feature:

    def __init__(self, name):
        self.name = name
        self.width = 0
        self.height = 0
        self.variants = {}
        self.loaded = False
        self.mod_data = {
            "!": {},  # shade, 3-tuple r, g, b
            "*": {},  # resize, 2-tuple x-scale, y-scale
            "=": {},  # translate, 2-tuple x-diff, y-diff
            "+": {},  # tint: 3-tuple r-%change, g-%change, b-%change
        }
        self.offset_x = 0
        self.offset_y = 0
        self.layer = 0

    def load(self):
        self.loaded = True
        self.variants = features2[self.name]["variants"]
        self.mod_data = features2[self.name]["mods"]
        self.offset_x = features2[self.name]["offset_x"]
        self.offset_y = features2[self.name]["offset_y"]
        self.layer = features2[self.name]["layer"]
        try:
            self.width, self.height = self.get_sprite(0).size
        except:
            self.width, self.height = 720, 720

    def get_sprite(self, variant: int):
        try:
            return Image.open(self.variants[variant]).convert("RGBA")
        except FileNotFoundError:
            return Image.new("RGBA", (self.width, self.height), (0, 0, 0, 0))

    def display_sprite(self, variant: int):
        self.get_sprite(variant).show()

    def render(self, variant: int, mods: dict):
        if not self.loaded:
            self.load()
        sprite = self.get_sprite(variant)
        local_offset_x = 0
        local_offset_y = 0
        if mods:
            for mod, variant in mods.items():
                try:
                    if mod == "?":
                        if variant == 0:
                            return Image.new('RGBA', (self.width, self.height), (0, 0, 0, 0)), 0, 0
                    else:
                        v = self.mod_data[mod][variant]
                        if mod == "!":
                            i = sprite.getdata()
                            for x in range(0, i.size[0]):  # process all pixels
                                for y in range(0, i.size[1]):
                                    data = i.getpixel((x, y))
                                    if data[0:3] == (255, 255, 255):
                                        sprite.putpixel((x, y), (v[0], v[1], v[2], data[3]))
                        elif mod == "*":
                            sprite = sprite.resize((int(self.width * v[0]), int(self.height * v[1])))
                            local_offset_x -= int((v[0] - 1) * self.width * 0.5)
                            local_offset_y -= int((v[1] - 1) * self.height * 0.5)
                        elif mod == "=":
                            local_offset_x += v[0]
                            local_offset_y += v[1]
                        elif mod == "+":
                            i = sprite.getdata()
                            for x in range(0, i.size[0]):
                                for y in range(0, i.size[1]):
                                    data = i.getpixel((x, y))
                                    sprite.putpixel((x, y), (
                                        int(data[0] * v[0]), int(data[1] * v[1]), int(data[2] * v[2]), data[3]))
                except KeyError:
                    print(self.name, mod, variant)
        return sprite, self.offset_x + local_offset_x, self.offset_y + local_offset_y


class Face:

    def __init__(self, seed: int):
        self.seed = seed
        self.letters = get_letters(seed)
        self.feature_list = get_features(self.letters)
        self.components = get_components(self.feature_list)

    def render(self, feats, extras=None):
        layers = {}
        base_canvas = Image.new("RGBA", (720, 720), (255, 255, 255))
        for x in feats:
            l = x.layer
            if l in layers.keys():
                layers[l].append(x)
            else:
                layers[l] = [x]
        for layer in [layers[x] for x in sorted(layers.keys())]:
            for x in layer:
                data = self.components[x.name]
                var = data["variant"]
                data.pop("variant")
                im, offset_x, offset_y = x.render(var, data)
                base_canvas.paste(im, box=(offset_x, offset_y), mask=im)
        if extras:
            e = Image.open(extras).convert("RGBA")
            base_canvas.paste(e, mask=e)
        return base_canvas


class ButtonManager:

    def __init__(self, gender, bgcolor, feats):
        self.locked = True
        self.dominance = {}  # true = dominant
        self.selection = {}  # true = selected
        self.selectable = {}  # true = selectable
        self.buttons = []
        self.bgcolor = bgcolor
        self.gender = gender
        self.advanced_init()
        self.selection_canvas = None
        self.selection_canvas_container = None
        self.selection_image = None
        self.advanced = True

        self.feats = feats

        self.image = None
        self.image2 = None

        self.canvas = None
        self.container = None
        self.forcelock = [44, 45]

    def reset_chr(self):
        for x in range(45):
            if x % 2 == 0:
                self.dominance[x] = True
            else:
                self.dominance[x] = False
        if self.gender == "male":
            self.dominance[44] = True
            self.dominance[45] = False
        else:
            self.dominance[44] = True
            self.dominance[45] = True

    def advanced_init(self):
        self.reset_chr()
        self.selection = {x: False for x in range(46)}  # true = selected
        self.selectable = {x: True for x in range(46)}  # true = selectable
        self.update_buttons()

    def basic_init(self):
        self.reset_chr()
        self.selection = {x: False for x in range(46)}  # true = selected
        self.selectable = {x: x // 2 in basic_chr for x in range(46)}  # true = selectable
        self.update_buttons()

    def reset(self):
        if self.advanced:
            self.advanced_init()
        else:
            self.basic_init()
        self.update_buttons()
        self.update_selection()
        self.update_canvas()

    def button_cb(self, number):
        if self.selectable[number]:
            if not self.locked and number not in self.forcelock:
                self.dominance[number] = not self.dominance[number]
            elif self.locked:
                opposite = self.get_opposite(number)
                self.selection[number] = not self.selection[number]
                if self.selection[number] and self.selection[opposite]:
                    self.selection[opposite] = False
                    self.buttons[opposite].update_status(dominant=self.dominance[opposite],
                                                         selected=self.selection[opposite],
                                                         selectable=self.selectable[opposite])

            self.buttons[number].update_status(dominant=self.dominance[number], selected=self.selection[number],
                                               selectable=self.selectable[number])
        self.update_selection()

    def update_selection(self):
        bg = Image.new("RGBA", (360, 300), self.bgcolor)
        sel = [get_button_sprite(x // 2, self.dominance[x], self.bgcolor, False) for x, y in self.selection.items()
               if y]
        for i, s in enumerate(sel):
            bg.paste(s, ((i % 12) * 30, (i // 12) * 150), mask=s)
        self.selection_image = ImageTk.PhotoImage(bg)
        self.selection_canvas.itemconfig(self.selection_canvas_container, image=self.selection_image)

    def add_canvas_container(self, canvas, container):
        self.canvas = canvas
        self.container = container

    def update_canvas(self):
        self.image = generate_face(self.feats, self.get_seed()).resize((480, 480))
        self.image2 = ImageTk.PhotoImage(self.image)
        self.canvas.itemconfig(self.container, image=self.image2)

    def toggle_lock(self):
        self.locked = not self.locked
        if not self.locked:
            self.selection = {x: False for x in range(46)}
        else:
            self.selection = {x: False for x in range(46)}
            self.update_canvas()
        self.update_selection()
        self.update_buttons()

    def toggle_mode(self):
        self.advanced = not self.advanced
        if self.advanced:
            self.advanced_init()
        else:
            self.basic_init()
        self.update_selection()
        self.update_buttons()

    def get_opposite(self, number):
        if number % 2 == 0:
            oppo = number + 1
        else:
            oppo = number - 1
        return oppo

    def get_selection_canvas(self, canvas):
        self.selection_canvas = canvas

    def get_selection_canvas_container(self, container):
        self.selection_canvas_container = container

    def get_seed(self):

        x = int(sum([(1 if y else 0) * 2 ** (45 - x) for x, y in self.dominance.items()]))
        return x

    def get_selected(self):
        x = int(sum([(1 if y and self.dominance[x] else 0) * 4 ** (22 - (x // 2)) for x, y in self.selection.items()]))
        return x

    def update_buttons(self):
        for i, button in enumerate(self.buttons):
            button.update_status(dominant=self.dominance[i], selected=self.selection[i], selectable=self.selectable[i])

    def get_simple_letters(self):
        s = [x for x, y in self.selection.items() if y]
        return "".join([chr_lettering["basic"][x // 2 + 1][0 if self.dominance[x] else 1] for x in s])

    def get_amount_selected(self):
        return sum([1 for x, y in self.selection.items() if y])

    def randomize_selection(self):
        f = []
        for x in range(23):
            f.extend([False, True] if random.randint(0, 1) else [True, False])
        self.selection = {x: f[x] if self.selectable[x] else False for x in range(46)}
        self.update_buttons()
        self.update_selection()

    def randomize_chromosomes(self):
        d = [[True, False], [False, True], [True, True], [False, False]]
        f = []
        for x in range(22):
            f.extend(d[random.randint(0, 3)])
        self.dominance = {x: f[x] for x in range(44)}
        if self.gender == "male":
            self.dominance[44] = True
            self.dominance[45] = False
        else:
            self.dominance[44] = True
            self.dominance[45] = True
        self.update_buttons()
        self.update_selection()
        self.update_canvas()


class SelectionButton(Button):

    def __init__(self, root, manager, index=0, bg_color=(255, 255, 255), **kw):
        super().__init__(root, command=self.toggle, **kw)
        self.index = index
        self.manager = manager
        self.bg_color = bg_color
        self.unselectable_color = (100, 100, 100)

    def update_status(self, dominant=False, selected=False, selectable=True):
        if selectable:
            bg = self.bg_color
        else:
            bg = self.unselectable_color
        if self.manager.advanced:
            mode = "advanced"
        else:
            mode = "basic"
        base_canvas = get_button_sprite(self.index // 2, dominant, bg, selected, mode=mode)
        x = ImageTk.PhotoImage(base_canvas)
        self.configure(image=x)
        self.image = x

    def toggle(self):
        self.manager.button_cb(self.index)


class ToggleButton(Button):

    def __init__(self, root, on=False, on_img=None, off_img=None, **kwargs):
        super().__init__(root, command=self.toggle, **kwargs)
        self.on = on
        self.on_image = off_img
        self.off_image = on_img
        self.toggle_func = None
        if not self.on:
            self.configure(image=self.off_image)
            self.image = self.off_image
        else:
            self.configure(image=self.on_image)
            self.image = self.on_image

    def toggle(self):
        for t in self.toggle_func:
            t()
        self.on = not self.on
        if not self.on:
            self.configure(image=self.off_image)
            self.image = self.off_image
        else:
            self.configure(image=self.on_image)
            self.image = self.on_image

    def add_toggle_func(self, *args):
        self.toggle_func = args


def get_button_sprite(chr_no, dominance, bg_color, selected, mode="advanced"):
    base_canvas = Image.new("RGBA", (30, 150), bg_color)
    path = f"./sprites/chr_{chr_no}_{int(dominance)}.png"
    letters = chr_lettering[mode][chr_no + 1][0 if dominance else 1]
    chr_image = Image.open(path).convert("RGBA")
    if selected:
        overlay = Image.new("RGBA", (27, 26), (50, 255, 84))
        base_canvas.paste(overlay, (2, 122), mask=overlay)
    base_canvas.paste(chr_image, (0, 0), mask=chr_image)
    font = ImageFont.truetype("./calibri_regular.ttf", 22)
    font2 = ImageFont.truetype("./calibri_regular.ttf", 16)
    render_1 = "1" in letters
    render_3 = "3" in letters
    letters = letters.replace("1", "")
    letters = letters.replace("2", "@")
    letters = letters.replace("3", "")
    letters = letters.replace("4", "$")
    d1 = ImageDraw.Draw(base_canvas)
    d1.text((2, 122), letters, font=font)
    if render_1:
        d1.text((2 + len(letters) * 15, 126), "@", font=font2)
    if render_3:
        d1.text((2, 126), "$", font=font2)
    return base_canvas


class Child:

    def __init__(self, male_manager, female_manager, canvas, feats, container, c2, c3):
        self.father = male_manager
        self.mother = female_manager
        self.feats = feats
        self.canvas = canvas
        self.container = container
        self.img = None
        self.img2 = None
        self.c2 = c2
        self.img3 = None
        self.img4 = None
        self.c3 = c3

    def generate(self):
        if self.father.advanced:
            self.generate_advanced()
        else:
            self.generate_basic()

    def generate_advanced(self):
        total = self.father.get_selected() * 2 + self.mother.get_selected()
        if self.father.get_amount_selected() == self.mother.get_amount_selected() == 23 and self.father.locked and self.mother.locked:
            self.img = generate_face(self.feats, total).resize((480, 480))
            # img.show()
            self.img2 = ImageTk.PhotoImage(self.img)

            self.canvas.itemconfig(self.container, image=self.img2)
        else:
            tkinter.messagebox.showinfo("Unable to render (advanced)", "All pairs of both parents needs to be selected")

    def generate_basic(self):
        m_l = self.father.get_simple_letters()
        f_l = self.mother.get_simple_letters()
        if [x // 2 for x, y in self.father.selection.items() if y] == [x // 2 for x, y in self.mother.selection.items()
                                                                       if y]:
            total = m_l + f_l
            f = SimpleFace(total)
            self.img = f.render(self.feats).resize((480, 480))
            self.img2 = ImageTk.PhotoImage(self.img)
            self.canvas.itemconfig(self.container, image=self.img2)
            self.img3 = get_basic_table(''.join(sorted(total, key=lambda x: x.lower())))
            self.img4 = ImageTk.PhotoImage(self.img3)
            self.c3.itemconfig(self.c2, image=self.img4)
        else:
            tkinter.messagebox.showinfo("Unable to render (basic)", "Unable to find matching pairs")


class SimpleFace:

    def __init__(self, letters):
        self.letters = sorted(letters, key=lambda x: x.lower())
        self.feature_list = get_basic_features(self.letters)
        self.components = get_components(self.feature_list)

    def render(self, feats):
        layers = {}
        base_canvas = Image.new("RGBA", (720, 720), (255, 255, 255))
        for x in feats:
            l = x.layer
            if l in layers.keys():
                layers[l].append(x)
            else:
                layers[l] = [x]
        for layer in [layers[x] for x in sorted(layers.keys())]:
            for x in layer:
                try:
                    data = self.components[x.name]
                    var = data["variant"]
                    data.pop("variant")
                    im, offset_x, offset_y = x.render(var, data)
                    base_canvas.paste(im, box=(offset_x, offset_y), mask=im)
                except KeyError:
                    pass
        return base_canvas


def get_basic_features(letters):
    f = []
    for x in range(len(letters) // 2):
        f.extend(basic_features[''.join(sorted(letters[2 * x: 2 * x + 2]))])
    return f


def main():
    feats = []
    for feature in features2.keys():
        feats.append(Feature(feature))
    for feature in feats:
        try:
            feature.load()
        except KeyError:
            print(feature.name)

    centralized_root = Tk()
    centralized_root.geometry("1920x1080")
    centralized_root.title("Chromosome simulation")
    centralized_root.resizable = True

    left_canvas = Canvas(centralized_root, width=600, height=1080)
    left_canvas.grid(row=0, column=0)
    mid_canvas = Canvas(centralized_root, width=720, height=1080)
    mid_canvas.grid(row=0, column=1)
    right_canvas = Canvas(centralized_root, width=600, height=1080)
    right_canvas.grid(row=0, column=2)

    i1 = ImageTk.PhotoImage(generate_face(feats, 46912496118441).resize((480, 480)))
    i2 = ImageTk.PhotoImage(generate_face(feats, 46912496118443).resize((480, 480)))
    i3 = ImageTk.PhotoImage(generate_face(feats, 0).resize((480, 480)))
    c1 = Canvas(left_canvas, width=600, height=480)
    c1.pack()
    c3 = Canvas(mid_canvas, width=720, height=480)
    c3.pack()
    c2 = Canvas(right_canvas, width=600, height=480)
    c2.pack()
    container1 = c1.create_image(300, 240, image=i1)
    container2 = c2.create_image(300, 240, image=i2)
    container3 = c3.create_image(360, 240, image=i3)

    male_manager = ButtonManager("male", (107, 200, 255), feats)
    male_manager.add_canvas_container(c1, container1)
    female_manager = ButtonManager("female", (255, 150, 244), feats)
    female_manager.add_canvas_container(c2, container2)

    selection_frame_left = Canvas(left_canvas, width=600, height=600)
    selection_frame_left.pack()
    left_buttons = []
    for x in range(44):
        y = SelectionButton(selection_frame_left, male_manager, index=x, bg_color=(107, 200, 255))
        y.grid(row=x // 16, column=x % 16)
        left_buttons.append(y)
    m1 = SelectionButton(selection_frame_left, male_manager, index=44, bg_color=(107, 200, 255))
    m1.grid(row=2, column=12)
    m2 = SelectionButton(selection_frame_left, male_manager, index=45, bg_color=(107, 200, 255))
    m2.grid(row=2, column=13)
    left_buttons.append(m1)
    left_buttons.append(m2)
    male_manager.buttons = left_buttons

    selection_frame_mid = Canvas(mid_canvas, width=720, height=600)
    selection_frame_mid.pack()

    c4 = Canvas(selection_frame_mid, width=240, height=200)
    c4.grid(row=2, column=1, rowspan=2)
    container4 = c4.create_image(120, 100,
                                 image=ImageTk.PhotoImage(Image.new("RGBA", (240, 200), (255, 255, 255, 255))))

    child = Child(male_manager, female_manager, c3, feats, container3, container4, c4)

    male_selected_canvas = Canvas(selection_frame_mid, width=360, height=300)
    male_selected_canvas.grid(row=0, column=0)
    m = ImageTk.PhotoImage(Image.new("RGBA", (360, 300), (107, 200, 255)))
    male_selected_canvas_container = male_selected_canvas.create_image(180, 150, image=m)
    male_manager.get_selection_canvas(male_selected_canvas)
    male_manager.get_selection_canvas_container(male_selected_canvas_container)

    f = ImageTk.PhotoImage(Image.new("RGBA", (360, 300), (255, 150, 244)))
    female_selected_canvas = Canvas(selection_frame_mid, width=360, height=300)
    female_selected_canvas.grid(row=0, column=1)
    female_selected_canvas_container = female_selected_canvas.create_image(180, 150, image=f)
    female_manager.get_selection_canvas(female_selected_canvas)
    female_manager.get_selection_canvas_container(female_selected_canvas_container)

    generate = ImageTk.PhotoImage(Image.open("./sprites/generate.png"))
    sperm_egg_img = ImageTk.PhotoImage(Image.open("./sprites/sperm_egg.png"))
    sperm_egg_label = Label(selection_frame_mid, image=sperm_egg_img).grid(row=1, column=0, columnspan=2)

    generate_button = Button(selection_frame_mid, command=child.generate, image=generate).grid(row=2, column=0)

    mode_button = ToggleButton(selection_frame_mid, on_img=ImageTk.PhotoImage(Image.open("./sprites/advanced.png")),
                               off_img=ImageTk.PhotoImage(Image.open("./sprites/basic.png")))
    mode_button.add_toggle_func(lambda: male_manager.toggle_mode(), lambda: female_manager.toggle_mode())
    mode_button.grid(row=3, column=0)

    selection_frame_right = Canvas(right_canvas, width=600, height=600)
    selection_frame_right.pack()
    right_buttons = []
    for x in range(46):
        y = SelectionButton(selection_frame_right, female_manager, index=x, bg_color=(255, 150, 244))
        y.grid(row=x // 16, column=x % 16)
        right_buttons.append(y)
    female_manager.buttons = right_buttons

    m_lock_button = ToggleButton(selection_frame_left, on_img=ImageTk.PhotoImage(Image.open("./sprites/m_locked.png")),
                                 off_img=ImageTk.PhotoImage(Image.open("./sprites/m_unlocked.png")))
    m_lock_button.add_toggle_func(male_manager.toggle_lock)
    m_lock_button.grid(row=3, column=12, columnspan=4)
    f_lock_button = ToggleButton(selection_frame_right, on_img=ImageTk.PhotoImage(Image.open("./sprites/f_locked.png")),
                                 off_img=ImageTk.PhotoImage(Image.open("./sprites/f_unlocked.png")))
    f_lock_button.add_toggle_func(female_manager.toggle_lock)
    f_lock_button.grid(row=3, column=12, columnspan=4)

    m_random_s_img = ImageTk.PhotoImage(Image.open("./sprites/m_random_s.png"))
    m_random_c_img = ImageTk.PhotoImage(Image.open("./sprites/m_random_c.png"))
    m_reset_img = ImageTk.PhotoImage(Image.open("./sprites/m_reset.png"))
    f_random_s_img = ImageTk.PhotoImage(Image.open("./sprites/f_random_s.png"))
    f_random_c_img = ImageTk.PhotoImage(Image.open("./sprites/f_random_c.png"))
    f_reset_img = ImageTk.PhotoImage(Image.open("./sprites/f_reset.png"))

    credit_img = ImageTk.PhotoImage(Image.open("./sprites/credit.png"))

    m_random_s = Button(selection_frame_left, image=m_random_s_img,
                        command=male_manager.randomize_selection).grid(row=3, column=0, columnspan=4)
    m_random_c = Button(selection_frame_left, image=m_random_c_img,
                        command=male_manager.randomize_chromosomes).grid(row=3, column=4, columnspan=4)
    m_reset = Button(selection_frame_left, image=m_reset_img,
                     command=male_manager.reset).grid(row=3, column=8, columnspan=4)

    f_random_s = Button(selection_frame_right, image=f_random_s_img,
                        command=female_manager.randomize_selection).grid(row=3, column=0, columnspan=4)
    f_random_c = Button(selection_frame_right, image=f_random_c_img,
                        command=female_manager.randomize_chromosomes).grid(row=3, column=4, columnspan=4)
    f_reset = Button(selection_frame_right, image=f_reset_img,
                     command=female_manager.reset).grid(row=3, column=8, columnspan=4)

    credit_button = Button(selection_frame_left, image=credit_img, command=show_credits).grid(row=2, column=14, columnspan=2)

    male_manager.update_buttons()
    female_manager.update_buttons()

    centralized_root.mainloop()


def show_credits():
    tkinter.messagebox.showinfo(title="Credits", message=f"Version: {version}:\nhttps://github.com/qwert9203/chromosome_sim\nCreated by Chow Yui Hong\nAdvisor: Ms. Lai Kam Fung, Head of Biology, St. Stephen's Girls' College\nReference: chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://www.letsgethealthy.org/wp-content/uploads/2013/08/Baby-Genome_make_a_baby_simulation_booklet.pdf")


def get_basic_table(letters):
    base_canvas = Image.new("RGBA", (240, 200), (255, 255, 255, 255))
    font = ImageFont.truetype("./calibri_regular.ttf", 16)
    i = 0
    for key, value in table_info.items():
        genotypes = value["Genotypes"]
        for l in genotypes.keys():
            if l in letters:
                dominance = genotypes[l]
                trait = value[dominance]
                d1 = ImageDraw.Draw(base_canvas)
                # ln = f"{key:4}|{l:10}|{dominance}: {trait}"
                d1.text((10, i * 20 + 5), str(key), font=font, fill=(0, 0, 0))
                d1.text((40, i * 20 + 5), l, font=font, fill=(0, 0, 0))
                d1.text((65, i * 20 + 5), f"{dominance}: ", font=font, fill=(0, 0, 0))
                d1.text((140, i * 20 + 5), trait, font=font, fill=(0, 0, 0))
                i += 1
    return base_canvas


def random_face(feats, gender=None):
    seed = random.randint(0, 70368744177664)
    if gender == "m":
        seed = (seed // 4) * 4 + 1
    elif gender == "f":
        seed = (seed // 4) * 4
    f = Face(seed)
    return f.render(feats)


def generate_face(feats, seed):
    print(f"Generating {seed}")
    f = Face(seed)
    return f.render(feats)


def validate_seed(seed):
    def clamp(seed):
        if 0 <= seed <= 70368744177664:
            return seed
        else:
            return 0

    try:
        return clamp(int(seed))
    except:
        return 0


def view_c(feats):
    seed = input("Input valid seed: ")
    f = Face(validate_seed(seed))
    f.render(feats)


def get_binary_list(seed):
    return [int(i) for i in list('{0:0b}'.format(int(seed + 70368744177664)))][1:]


def get_letters(seed: int):
    return ''.join(
        sorted(
            ''.join([chromosomes[i // 2 + 1][abs(1 - int(str(bin(seed + 70368744177664))[i + 3]))] for i in range(46)]),
            key=lambda x: x.lower()))


def get_features(letters: str):
    f = []
    for x in feature_indices:
        f.extend(*[
            features[''.join(sorted(''.join([letters[x[0 + 2 * y]: x[1 + 2 * y] + 1] for y in range(len(x) // 2)])))]])
    return sorted(f)


def get_components(f: list):
    g = {}
    for x in f:
        mod = x[0]
        if mod in ["!", "*", "=", "+", "?"]:
            name = x[1:x.find("_")]
            m = mod
        else:
            name = x[:x.find("_")]
            m = "variant"
        if name in g.keys():
            g[name][m] = int(x[x.find("_") + 1:])
        else:
            g[name] = {m: int(x[x.find("_") + 1:])}
    return g


if __name__ == "__main__":
    main()
