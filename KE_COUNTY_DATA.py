''' Run this from the management/commands directory'''


from django.core.management.base import BaseCommand

from core.sites.models import County, Constituency, Ward


class Command(BaseCommand):
    help = "Load the County, Constituency and Wards"

    def handle(self, *args, **kwargs):
        County.objects.all().delete()
        Constituency.objects.all().delete()
        Ward.objects.all().delete()

        counties = [
            "Mombasa",
            "Kwale",
            "Kilifi",
            "Tana River",
            "Lamu",
            "Taita Taveta",
            "Garissa",
            "Wajir",
            "Mandera",
            "Marsabit",
            "Isiolo",
            "Meru",
            "Tharaka Nithi",
            "Embu",
            "Kitui",
            "Machakos",
            "Makueni",
            "Nyandarua",
            "Nyeri",
            "Kirinyaga",
            "Murang'a",
            "Kiambu",
            "Turkana",
            "West Pokot",
            "Samburu",
            "Trans Nzoia",
            "Uasin Gishu",
            "Elgeyo Marakwet",
            "Nandi",
            "Baringo",
            "Laikipia",
            "Nakuru",
            "Narok",
            "Kajiado",
            "Kericho",
            "Bomet",
            "Kakamega",
            "Vihiga",
            "Bungoma",
            "Busia",
            "Siaya",
            "Kisumu",
            "Homa Bay",
            "Migori",
            "Kisii",
            "Nyamira",
            "Nairobi",
        ]

        kenyan_data = [
            {
                "county_name": "MOMBASA",
                "constituencies": [
                    {
                        "constituency_name": "CHANGAMWE",
                        "wards": [
                            "PORT REITZ",
                            "KIPEVU",
                            "AIRPORT",
                            "CHANGAMWE",
                            "CHAANI",
                        ],
                    },
                    {
                        "constituency_name": "JOMVU",
                        "wards": ["JOMVU KUU", "MIRITINI", "MIKINDANI"],
                    },
                    {
                        "constituency_name": "KISAUNI",
                        "wards": [
                            "MJAMBERE",
                            "JUNDA",
                            "BAMBURI",
                            "MWAKIRUNGE",
                            "MTOPANGA",
                            "MAGOGONI",
                            "SHANZU",
                        ],
                    },
                    {
                        "constituency_name": "NYALI",
                        "wards": [
                            "FRERE TOWN",
                            "ZIWA LA NG'OMBE",
                            "MKOMANI",
                            "KONGOWEA",
                            "KADZANDANI",
                        ],
                    },
                    {
                        "constituency_name": "LIKONI",
                        "wards": [
                            "MTONGWE",
                            "SHIKA ADABU",
                            "BOFU",
                            "LIKONI",
                            "TIMBWANI",
                        ],
                    },
                    {
                        "constituency_name": "MVITA",
                        "wards": [
                            "MJI WA KALE/MAKADARA",
                            "TUDOR",
                            "TONONOKA",
                            "SHIMANZI/GANJONI",
                            "MAJENGO",
                        ],
                    },
                ],
            },
            {
                "county_name": "KWALE",
                "constituencies": [
                    {
                        "constituency_name": "MSAMBWENI",
                        "wards": ["GOMBATO BONGWE", "UKUNDA", "KINONDO", "RAMISI"],
                    },
                    {
                        "constituency_name": "LUNGALUNGA",
                        "wards": ["PONGWE/KIKONENI", "DZOMBO", "MWERENI", "VANGA"],
                    },
                    {
                        "constituency_name": "MATUGA",
                        "wards": [
                            "TSIMBA GOLINI",
                            "WAA",
                            "TIWI",
                            "KUBO SOUTH",
                            "MKONGANI",
                        ],
                    },
                    {
                        "constituency_name": "KINANGO",
                        "wards": [
                            "NDAVAYA",
                            "PUMA",
                            "KINANGO",
                            "MACKINNON ROAD",
                            "CHENGONI/SAMBURU",
                            "MWAVUMBO",
                            "KASEMENI",
                        ],
                    },
                ],
            },
            {
                "county_name": "KILIFI",
                "constituencies": [
                    {
                        "constituency_name": "KILIFI_NORTH",
                        "wards": [
                            "TEZO",
                            "SOKONI",
                            "KIBARANI",
                            "DABASO",
                            "MATSANGONI",
                            "WATAMU",
                            "MNARANI",
                        ],
                    },
                    {
                        "constituency_name": "KILIFI_SOUTH",
                        "wards": [
                            "JUNJU",
                            "MWARAKAYA",
                            "SHIMO LA TEWA",
                            "CHASIMBA",
                            "MTEPENI",
                        ],
                    },
                    {
                        "constituency_name": "KALOLENI",
                        "wards": ["MARIAKANI", "KAYAFUNGO", "KALOLENI", "MWANAMWINGA"],
                    },
                    {
                        "constituency_name": "RABAI",
                        "wards": [
                            "MWAWESA",
                            "RURUMA",
                            "KAMBE/RIBE",
                            "RABAI/KISURUTINI",
                        ],
                    },
                    {
                        "constituency_name": "KANZE",
                        "wards": ["GANZE", "BAMBA", "JARIBUNI", "SOKOKE"],
                    },
                    {
                        "constituency_name": "MALINDI",
                        "wards": [
                            "JILORE",
                            "KAKUYUNI",
                            "GANDA",
                            "MALINDI TOWN",
                            "SHELLA",
                        ],
                    },
                    {
                        "constituency_name": "MAGARINI",
                        "wards": [
                            "MARAFA",
                            "MAGARINI",
                            "GONGONI",
                            "ADU",
                            "GARASHI",
                            "SABAKI",
                        ],
                    },
                ],
            },
            {
                "county_name": "TANA RIVER",
                "constituencies": [
                    {
                        "constituency_name": "GARSEN",
                        "wards": [
                            "KIPINI EAST",
                            "GARSEN SOUTH",
                            "KIPINI WEST",
                            "GARSEN CENTRAL",
                            "GARSEN WEST",
                            "GARSEN NORTH",
                        ],
                    },
                    {
                        "constituency_name": "GALOLE",
                        "wards": ["KINAKOMBA", "MIKINDUNI", "CHEWANI", "WAYU"],
                    },
                    {
                        "constituency_name": "BURA",
                        "wards": ["CHEWELE", "HIRIMANI", "BANGALE", "SALA", "MADOGO"],
                    },
                ],
            },
            {
                "county_name": "LAMU",
                "constituencies": [
                    {
                        "constituency_name": "LAMU_EAST",
                        "wards": ["FAZA", "KIUNGA", "BASUBA"],
                    },
                    {
                        "constituency_name": "LAMU_WEST",
                        "wards": [
                            "SHELLA",
                            "MKOMANI",
                            "HINDI",
                            "MKUNUMBI",
                            "HONGWE",
                            "WITU",
                            "BAHARI",
                        ],
                    },
                ],
            },
            {
                "county_name": "TAITA TAVETA",
                "constituencies": [
                    {
                        "constituency_name": "TAVETA",
                        "wards": ["CHALA", "MAHOO", "BOMANI", "MBOGHONI", "MATA"],
                    },
                    {
                        "constituency_name": "WUNDANYI",
                        "wards": [
                            "WUNDANYI/MBALE",
                            "WERUGHA",
                            "WUMINGU/KISHUSHE",
                            "MWANDA/MGANGE",
                        ],
                    },
                    {
                        "constituency_name": "MWATATE",
                        "wards": [
                            "RONG'E",
                            "MWATATE",
                            "BURA",
                            "CHAWIA",
                            "WUSI/KISHAMBA",
                        ],
                    },
                    {
                        "constituency_name": "VOI",
                        "wards": [
                            "MBOLOLO",
                            "SAGALLA",
                            "KALOLENI",
                            "MARUNGU",
                            "KASIGAU",
                            "NGOLIA",
                        ],
                    },
                ],
            },
            {
                "county_name": "GARISSA",
                "constituencies": [
                    {
                        "constituency_name": "GARISSATOWNSHIP",
                        "wards": ["WABERI", "GALBET", "TOWNSHIP", "IFTIN"],
                    },
                    {
                        "constituency_name": "BALAMBALA",
                        "wards": [
                            "BALAMBALA",
                            "DANYERE",
                            "JARA JARA",
                            "SAKA",
                            "SANKURI",
                        ],
                    },
                    {
                        "constituency_name": "LAGDERA",
                        "wards": [
                            "MODOGASHE",
                            "BENANE",
                            "GOREALE",
                            "MAALIMIN",
                            "SABENA",
                            "BARAKI",
                        ],
                    },
                    {
                        "constituency_name": "DADAAB",
                        "wards": [
                            "DERTU",
                            "DADAAB",
                            "LABASIGALE",
                            "DAMAJALE",
                            "LIBOI",
                            "ABAKAILE",
                        ],
                    },
                    {
                        "constituency_name": "FAFI",
                        "wards": ["BURA", "DEKAHARIA", "JARAJILA", "FAFI", "NANIGHI"],
                    },
                    {
                        "constituency_name": "IJARA",
                        "wards": ["HULUGHO", "SANGAILU", "IJARA", "MASALANI"],
                    },
                ],
            },
            {
                "county_name": "WAJIR",
                "constituencies": [
                    {
                        "constituency_name": "WAJIR_NORTH",
                        "wards": [
                            "GURAR",
                            "BUTE",
                            "KORONDILE",
                            "MALKAGUFU",
                            "BATALU",
                            "DANABA",
                            "GODOMA",
                        ],
                    },
                    {
                        "constituency_name": "WAJIR_EAST",
                        "wards": ["WAGBERI", "TOWNSHIP", "BARWAGO", "HOROF/HARAR"],
                    },
                    {
                        "constituency_name": "TARBAJ",
                        "wards": ["ELBEN", "SARMAN", "TARBAJ", "WARGADUD"],
                    },
                    {
                        "constituency_name": "WAJIR_WEST",
                        "wards": [
                            "ARBAJAHAN",
                            "HADADO/ATHIBOHOL",
                            "ADAMASAJIDE",
                            "ANYURE/WAGALLA",
                        ],
                    },
                    {
                        "constituency_name": "ELDAS",
                        "wards": [
                            "ELDAS",
                            "DELLA",
                            "LAKOLEY SOUTH/BASIR",
                            'ELNUR/TULA TULA"',
                            "BENANE",
                            "BURDER",
                            "DADAJA BULLA",
                        ],
                    },
                    {
                        "constituency_name": "WAJIR_SOUTH",
                        "wards": [
                            "HABASSWEIN",
                            "LAGBOGHOL SOUTH",
                            "IBRAHIM URE",
                            "DIIF",
                        ],
                    },
                ],
            },
            {
                "county_name": "MANDERA",
                "constituencies": [
                    {
                        "constituency_name": "MANDERA_WEST",
                        "wards": [
                            "TAKABA SOUTH",
                            "TAKABA",
                            "LAGSURE",
                            "DANDU",
                            "GITHER",
                        ],
                    },
                    {
                        "constituency_name": "BANISSA",
                        "wards": [
                            "BANISSA",
                            "DERKHALE",
                            "GUBA",
                            "MALKAMARI",
                            "KILIWEHIRI",
                        ],
                    },
                    {
                        "constituency_name": "MANDERA_NORTH",
                        "wards": [
                            "ASHABITO",
                            "GUTICHA",
                            "MOROTHILE",
                            "RHAMU",
                            "RHAMU-DIMTU",
                        ],
                    },
                    {
                        "constituency_name": "MANDERA_SOUTH",
                        "wards": [
                            "WARGADUD",
                            "KUTULO",
                            "ELWAK SOUTH",
                            "ELWAK NORTH",
                            "SHIMBIR FATUMA",
                        ],
                    },
                    {
                        "constituency_name": "MANDERA_EAST",
                        "wards": ["ARABIA", "TOWNSHIP", "NEBOI", "KHALALIO", "LIBEHIA"],
                    },
                    {
                        "constituency_name": "LAFEY",
                        "wards": ["SALA", "FINO", "LAFEY", "WARANQARA", "ALANGO GOF"],
                    },
                ],
            },
            {
                "county_name": "MARSABIT",
                "constituencies": [
                    {
                        "constituency_name": "MOYALE",
                        "wards": [
                            "BUTIYE",
                            "SOLOLO",
                            "HEILLU/MANYATTA",
                            "GOLBO",
                            "MOYALE TOWNSHIP",
                            "URAN",
                            "OBBU",
                        ],
                    },
                    {
                        "constituency_name": "NORTH_HORR",
                        "wards": [
                            "DUKANA",
                            "MAIKONA",
                            "TURBI",
                            "NORTH HORR",
                            "ILLERET",
                        ],
                    },
                    {
                        "constituency_name": "SAKU",
                        "wards": ["KARARE", "SAGANTE/JALDESA", "MARSABIT CENTRAL"],
                    },
                    {
                        "constituency_name": "LAISAMIS",
                        "wards": [
                            "LOIYANGALANI",
                            "KARGI/SOUTH HORR",
                            "KORR/NGURUNIT",
                            "LOGO LOGO",
                            "LAISAMIS",
                        ],
                    },
                ],
            },
            {
                "county_name": "ISIOLO",
                "constituencies": [
                    {
                        "constituency_name": "ISIOLO_NORTH",
                        "wards": [
                            "WABERA",
                            "BULLA PESA",
                            "CHARI",
                            "CHERAB",
                            "NGARE MARA",
                            "BURAT",
                            "OLDO/NYIRO",
                        ],
                    },
                    {
                        "constituency_name": "ISIOLO_SOUTH",
                        "wards": ["GARBATULLA", "KINNA", "SERICHO"],
                    },
                ],
            },
            {
                "county_name": "MERU",
                "constituencies": [
                    {
                        "constituency_name": "IGEMBE_SOUTH",
                        "wards": [
                            "MAUA",
                            "KIEGOI/ANTUBOCHIU",
                            "ATHIRU GAITI",
                            "AKACHIU",
                            "KANUNI",
                        ],
                    },
                    {
                        "constituency_name": "IGEMBE_CENTRAL",
                        "wards": [
                            "AKIRANG'ONDU",
                            "ATHIRU RUUJINE",
                            "IGEMBE EAST",
                            "NJIA",
                            "NJIA",
                        ],
                    },
                    {
                        "constituency_name": "IGEMBE_NORTH",
                        "wards": [
                            "ANTUAMBUI",
                            "NTUNENE",
                            "ANTUBETWE KIONGO",
                            "NAATHU",
                            "AMWATHI",
                        ],
                    },
                    {
                        "constituency_name": "TIGANIA_WEST",
                        "wards": ["ATHWANA", "AKITHII", "KIANJAI", "NKOMO", "MBEU"],
                    },
                    {
                        "constituency_name": "TIGANIA_EAST",
                        "wards": [
                            "THANGATHA",
                            "MIKINDURI",
                            "KIGUCHWA",
                            "MUTHARA",
                            "KARAMA",
                        ],
                    },
                    {
                        "constituency_name": "NORTH_IMENTI",
                        "wards": [
                            "MUNICIPALITY",
                            "NTIMA EAST",
                            "NTIMA WEST",
                            "NYAKI WEST",
                            "NYAKI EAST",
                        ],
                    },
                    {
                        "constituency_name": "BUURI",
                        "wards": ["TIMAU", "KISIMA", "KIIRUA/NAARI", "RUIRI/RWARERA"],
                    },
                    {
                        "constituency_name": "CENTRAL_IMENTI",
                        "wards": [
                            "KIBIRICHIA",
                            "MWANGANTHIA",
                            "ABOTHUGUCHI CENTRAL",
                            "ABOTHUGUCHI WEST",
                            "KIAGU",
                        ],
                    },
                    {
                        "constituency_name": "SOUTH_IMENTI",
                        "wards": [
                            "MITUNGUU",
                            "IGOJI EAST",
                            "IGOJI WEST",
                            "ABOGETA EAST",
                            "ABOGETA WEST",
                            "NKUENE",
                        ],
                    },
                ],
            },
            {
                "county_name": "EMBU",
                "constituencies": [
                    {
                        "constituency_name": "MANYATTA",
                        "wards": [
                            "RUGURU/NGANDORI",
                            "KITHIMU",
                            "NGINDA",
                            "MBETI NORTH",
                            "KIRIMARI",
                            "URGATURI SOUTHAN",
                        ],
                    },
                    {
                        "constituency_name": "RUNYENJES",
                        "wards": [
                            "GATURI NORTH",
                            "KAGAARI SOUTH",
                            "CENTRAL  WARD",
                            "KAGAARI NORTH",
                            "ILLKYENI NORTHERET",
                            "KYENI SOUTH",
                        ],
                    },
                    {
                        "constituency_name": "MBEERE_SOUTH",
                        "wards": [
                            "MWEA",
                            "MAKIMA",
                            "MBETI SOUTH",
                            "MAVURIA",
                            "KIAMBERE",
                        ],
                    },
                    {
                        "constituency_name": "MBEERE_NORTH",
                        "wards": ["NTHAWA", "MUMINJI", "EVURORE"],
                    },
                ],
            },
            {
                "county_name": "TharakaNithi",
                "constituencies": [
                    {
                        "constituency_name": "MAARA",
                        "wards": ["MITHERU", "MUTHAMBI", "MWIMBI", "GANGA", "CHOGORIA"],
                    },
                    {
                        "constituency_name": "CHUKA/IGAMBANG'OMBE",
                        "wards": [
                            "MARIANI",
                            "KARINGANI",
                            "MAGUMONI",
                            "MUGWE",
                            "IGAMBANG'OMBE",
                        ],
                    },
                    {
                        "constituency_name": "THARAKA",
                        "wards": [
                            "GATUNGA",
                            "MUKOTHIMA",
                            "NKONDI",
                            "CHIAKARIGA",
                            "MARIMANTI",
                        ],
                    },
                ],
            },
            {
                "county_name": "KITUI",
                "constituencies": [
                    {
                        "constituency_name": "MWINGI_NORTH",
                        "wards": ["NGOMENI", "KYUSO", "MUMONI", "TSEIKURU", "THARAKA"],
                    },
                    {
                        "constituency_name": "MWINGI_WEST",
                        "wards": [
                            "KYOME/THAANA",
                            "NGUUTANI",
                            "MIGWANI",
                            "KIOMO/KYETHANI",
                        ],
                    },
                    {
                        "constituency_name": "MWINGI_CENTRAL",
                        "wards": ["CENTRAL", "KIVOU", "KIVOU", "NUU", "MUI", "WAITA"],
                    },
                    {
                        "constituency_name": "KITUI_WEST",
                        "wards": [
                            "MUTONGUNI",
                            "KAUWI",
                            "MATINYANI",
                            "KWA MUTONGA/KITHUMULA",
                        ],
                    },
                    {
                        "constituency_name": "KITUI_RURAL",
                        "wards": ["KISASI", "MBITINI", "KWAVONZA/YATTA", "KANYANGI"],
                    },
                    {
                        "constituency_name": "KITUI_CENTRAL",
                        "wards": [
                            "MIAMBANI",
                            "TOWNSHIP ",
                            "KYANGWITHYA WEST",
                            "MULANGO",
                            "KYANGWITHYA EAST",
                        ],
                    },
                    {
                        "constituency_name": "KITUI_EAST",
                        "wards": [
                            "ZOMBE/MWITIKA",
                            "NZAMBANI",
                            "CHULUNI",
                            "VOO/KYAMATU",
                            "ENDAU/MALALANI",
                            "MUTITO/KALIKU",
                        ],
                    },
                    {
                        "constituency_name": "KITUI_SOUTH",
                        "wards": [
                            "IKANGA/KYATUNE",
                            "MUTOMO",
                            "MUTHA",
                            "IKUTHA",
                            "KANZIKO",
                            "ATHI",
                        ],
                    },
                ],
            },
            {
                "county_name": "MACHAKOS",
                "constituencies": [
                    {
                        "constituency_name": "MASINGA",
                        "wards": [
                            "KIVAA",
                            "MASINGA CENTRAL",
                            "EKALAKALA",
                            "MUTHESYA",
                            "NDITHINI",
                        ],
                    },
                    {
                        "constituency_name": "YATTA",
                        "wards": ["NDALANI", "MATUU", "KITHIMANI", "IKOMBE", "KATANGI"],
                    },
                    {
                        "constituency_name": "KANGUNDO",
                        "wards": [
                            "KANGUNDO NORTH",
                            "KANGUNDO CENTRA",
                            "KANGUNDO EAST",
                            "KANGUNDO WEST",
                        ],
                    },
                    {
                        "constituency_name": "MATUNGULU",
                        "wards": [
                            "TALA",
                            "MATUNGULU NORTH",
                            "MATUNGULU EAST",
                            " MATUNGULU WEST",
                            "KYELENI",
                        ],
                    },
                    {
                        "constituency_name": "KATHIANI",
                        "wards": [
                            "MITABONI",
                            "KATHIANI CENTRAL",
                            "UPPER KAEWA/IVETI",
                            "LOWER KAEWA/KAANI",
                        ],
                    },
                    {
                        "constituency_name": "MAVOKO",
                        "wards": [
                            "ATHI RIVER",
                            "KINANIE ",
                            "MUTHWANI",
                            "SYOKIMAU/MULOLONGO",
                        ],
                    },
                    {
                        "constituency_name": "MACHAKOS_TOWN",
                        "wards": [
                            "KALAMA",
                            "MUA",
                            "MUTITUNI",
                            "MACHAKOS CENTRAL",
                            "MUMBUNI NORTH",
                            "MUVUTI/KIIMA-KIMWE",
                            "KOLA",
                        ],
                    },
                    {
                        "constituency_name": "MWALA",
                        "wards": [
                            "MBIUNI",
                            "MAKUTANO/ MWALA",
                            "MASII",
                            "MUTHETHENI",
                            "WAMUNYU",
                            "KIBAUNI",
                        ],
                    },
                ],
            },
            {
                "county_name": "MAKUENI",
                "constituencies": [
                    {
                        "constituency_name": "MBOONI",
                        "wards": [
                            "TULIMANI",
                            "MBOONI",
                            "KITHUNGO/KITUNDU",
                            "KITETA/KISAU",
                            "WAIA-KAKO",
                            "KALAWA",
                        ],
                    },
                    {
                        "constituency_name": "KILOME",
                        "wards": ["KASIKEU", "MUKAA", "KIIMA KIU/KALANZONI"],
                    },
                    {
                        "constituency_name": "KAITI",
                        "wards": ["UKIA", "KEE", "KILUNGU", "ILIMA"],
                    },
                    {
                        "constituency_name": "MAKUENI",
                        "wards": [
                            "WOTE",
                            "MUVAU/KIKUUMINI",
                            "MAVINDINI",
                            "KITISE/KITHUKI",
                            "KATHONZWENI",
                            "NZAUI/KILILI/KALAMBA",
                            "MBITINI",
                        ],
                    },
                    {
                        "constituency_name": "KIBWEZI_WEST",
                        "wards": [
                            "MAKINDU",
                            "NGUUMO",
                            "KIKUMBULYU NORTH",
                            "KIKUMBULYU SOUTH",
                            "NGUU/MASUMBA",
                            "EMALI/MULALA",
                        ],
                    },
                    {
                        "constituency_name": "KIBWEZI_EAST",
                        "wards": [
                            "MASONGALENI",
                            "MTITO ANDEI ",
                            "THANGE",
                            "IVINGONI/NZAMBANI",
                        ],
                    },
                ],
            },
            {
                "county_name": "Nyandarua",
                "constituencies": [
                    {
                        "constituency_name": "KINANGOP",
                        "wards": [
                            "ENGINEER",
                            "GATHARA",
                            "NORTH KINANGOP",
                            "MURUNGARU",
                            "NJABINI\KIBURU",
                            "NYAKIO",
                            "GITHABAI",
                            "MAGUMU",
                        ],
                    },
                    {
                        "constituency_name": "KIPIPIRI",
                        "wards": ["WANJOHI", "KIPIPIRI", "GETA", "GITHIORO"],
                    },
                    {
                        "constituency_name": "OL_KALOU",
                        "wards": [
                            "KARAU",
                            "KANJUIRI RANGE",
                            "MIRANGINE",
                            "KAIMBAGA",
                            "RURII",
                        ],
                    },
                    {
                        "constituency_name": "OL_JOROK",
                        "wards": ["GATHANJI", "GATIMU", "WERU", "CHARAGITA"],
                    },
                    {
                        "constituency_name": "NDARAGWA",
                        "wards": ["LESHAU/PONDO", "KIRIITA", "CENTRAL", "SHAMATA"],
                    },
                ],
            },
            {
                "county_name": "Nyeri",
                "constituencies": [
                    {
                        "constituency_name": "TETU",
                        "wards": ["DEDAN KIMANTHI", "WAMAGANA", "AGUTHI-GAAKI"],
                    },
                    {
                        "constituency_name": "KIENI",
                        "wards": [
                            "MWEIGA",
                            "NAROMORU KIAMATHAGA",
                            "MWIYOGO/ENDARASHA",
                            "MUGUNDA",
                            "GATARAKWA",
                            "THEGU RIVER",
                            "KABARU",
                            "GAKAWA",
                        ],
                    },
                    {
                        "constituency_name": "MATHIRA",
                        "wards": [
                            "MAGUTU",
                            "RUGURU",
                            "IRIAINI",
                            "KONYU",
                            "KIRIMUKUYU",
                            "KARATINA TOWN",
                        ],
                    },
                    {
                        "constituency_name": "OTHAYA",
                        "wards": ["MAHIGA", "IRIA-INI", "CHINGA", "KARIMA"],
                    },
                    {
                        "constituency_name": "MUKURWEINI",
                        "wards": [
                            "GIKONDI",
                            "RUGI",
                            "MUKURWE-INI WEST",
                            "MUKURWE-INI CENTRAL",
                        ],
                    },
                    {
                        "constituency_name": "NYERI_TOWN",
                        "wards": [
                            "KIGANJO/MATHARI",
                            "RWARE",
                            "GATITU/MURUGURU",
                            "RURING'U",
                            "KAMAKWA/MUKARO",
                        ],
                    }
                ],
            },
            {
                "county_name": "Kirinyaga",
                "constituencies": [
                    {
                        "constituency_name": "MWEA",
                        "wards": [
                            "MUTITHI",
                            "KANGAI",
                            "THIBA",
                            "WAMUMU",
                            "NYANGATI",
                            "MURINDUKO",
                            "GATHIGIRIRI",
                            "TEBERE",
                        ],
                    },
                    {
                        "constituency_name": "GICHUGU",
                        "wards": [
                            "KABARE",
                            "BARAGWI",
                            "NJUKIINI",
                            "NGARIAMA",
                            "KARUMANDI",
                        ],
                    },
                    {
                        "constituency_name": "NDIA",
                        "wards": ["MUKURE", "KIINE", "KARITI"],
                    },
                    {
                        "constituency_name": "KIRINYAGA_CENTRAL",
                        "wards": ["MUTIRA", "KANYEKINI", "KERUGOYA", "INOI"],
                    },
                ],
            },
            {
                "county_name": "Muranga",
                "constituencies": [
                    {
                        "constituency_name": "KANGEMA",
                        "wards": ["KANYENYA-INI", "MUGURU", "RWATHIA"],
                    },
                    {
                        "constituency_name": "MATHIOYA",
                        "wards": ["GITUGI", "KIRU", "KAMACHARIA"],
                    },
                    {
                        "constituency_name": "KIHARU",
                        "wards": [
                            "WANGU",
                            "MUGOIRI",
                            "MBIRI",
                            "TOWNSHIP",
                            "MURARANDIA",
                            "GATURI",
                        ],
                    },
                    {
                        "constituency_name": "KIGUMO",
                        "wards": [
                            "KAHUMBU",
                            "MUTHITHI",
                            "KIGUMO",
                            "KANGARI",
                            "KINYONA",
                        ],
                    },
                    {
                        "constituency_name": "MARAGWA",
                        "wards": [
                            "KIMORORI/WEMPA",
                            "MAKUYU",
                            "KAMBITI",
                            "KAMAHUHA",
                            "ICHAGAKI",
                            "NGINDA",
                        ],
                    },
                    {
                        "constituency_name": "KANDARA",
                        "wards": [
                            "NG'ARARIA",
                            "MURUKA",
                            "KAGUNDU-INI",
                            "GAICHANJIRU",
                            "ITHIRU",
                            "RUCHU",
                        ],
                    },
                    {
                        "constituency_name": "GATANGA",
                        "wards": [
                            "ITHANGA",
                            "KAKUZI/MITUBIRI",
                            "MUGUMO-INI",
                            "KIHUMBU-INI",
                            "GATANGA",
                            "KARIARA",
                        ],
                    },
                ],
            },
            {
                "county_name": "Kiambu",
                "constituencies": [
                    {
                        "constituency_name": "GATUNDU_SOUTH",
                        "wards": ["KIAMWANGI", "KIGANJO", "NDARUGU", "NGENDA"],
                    },
                    {
                        "constituency_name": "GATUNDU_NORTH",
                        "wards": ["GITUAMBA", "GITHOBOKONI", "CHANIA", "MANG'U"],
                    },
                    {
                        "constituency_name": "JUJA",
                        "wards": ["MURERA", "THETA", "JUJA", "WITEITHIE", "KALIMONI"],
                    },
                    {
                        "constituency_name": "THIKA_TOWN",
                        "wards": [
                            "TOWNSHIP",
                            "KAMENU",
                            "HOSPITAL",
                            "GATUANYAGA",
                            "NGOLIBA",
                        ],
                    },
                    {
                        "constituency_name": "RUIRU",
                        "wards": [
                            "GITOTHUA",
                            "BIASHARA",
                            "GATONGORA",
                            "KAHAWA SUKARI",
                            "KAHAWA WENDANI",
                            "KIUU",
                            "MWIKI",
                            "MWIHOKO",
                        ],
                    },
                    {
                        "constituency_name": "GITHUNGURI",
                        "wards": [
                            "GITHUNGURI",
                            "GITHIGA",
                            "IKINU",
                            "NGEWA",
                            "KOMOTHAI",
                        ],
                    },
                    {
                        "constituency_name": "KIAMBU",
                        "wards": ["TING'ANG'A", "NDUMBERI", "RIABAI", "TOWNSHIP"],
                    },
                    {
                        "constituency_name": "KIAMBAA",
                        "wards": ["CIANDA", "KARURI", "NDENDERU", "MUCHATHA", "KIHARA"],
                    },
                    {
                        "constituency_name": "KABETE",
                        "wards": ["GITARU", "MUGUGA", "NYADHUNA", "KABETE", "UTHIRU"],
                    },
                    {
                        "constituency_name": "KIKUYU",
                        "wards": ["KARAI", "NACHU", "SIGONA", "KIKUYU", "KINOO"],
                    },
                    {
                        "constituency_name": "LIMURU",
                        "wards": [
                            "BIBIRIONI",
                            "LIMURU CENTRAL",
                            "NDEIYA",
                            "LIMURU EAST",
                            "NGECHA TIGONI",
                        ],
                    },
                    {
                        "constituency_name": "LARI",
                        "wards": [
                            "KINALE",
                            "KIJABE",
                            "NYANDUMA",
                            "KAMBURU",
                            "LARI/KIRENGA",
                        ],
                    },
                ],
            },
            {
                "county_name": "Turkana",
                "constituencies": [
                    {
                        "constituency_name": "TURKANA_NORTH",
                        "wards": [
                            "KAERIS",
                            "LAKE ZONE",
                            "LAPUR",
                            "KAALENG/KAIKOR",
                            "KIBISH",
                            "NAKALALE",
                        ],
                    },
                    {
                        "constituency_name": "TURKANA_WEST",
                        "wards": [
                            "KAKUMA",
                            "LOPUR",
                            "LETEA",
                            "SONGOT",
                            "KALOBEYEI",
                            "LOKICHOGGIO",
                            "NANAAM",
                        ],
                    },
                    {
                        "constituency_name": "TURKANA_CENTRAL",
                        "wards": [
                            "KERIO DELTA",
                            "KANG'ATOTHA",
                            "KALOKOL",
                            "LODWAR TOWNSHIP",
                            "KANAMKEMER",
                        ],
                    },
                    {
                        "constituency_name": "LOIMA",
                        "wards": [
                            "KOTARUK/LOBEI",
                            "TURKWEL",
                            "LOIMA",
                            "LOKIRIAMA/LORENGIPPI",
                        ],
                    },
                    {
                        "constituency_name": "TURKANA_SOUTH",
                        "wards": [
                            "KAPUTIR",
                            "KATILU",
                            "LOBOKAT",
                            "KALAPATA",
                            "LOKICHAR",
                        ],
                    },
                    {
                        "constituency_name": "TURKANA_EAST",
                        "wards": ["KAPEDO/NAPEITOM", "KATILIA", "LOKORI/KOCHODIN"],
                    },
                ],
            },
            {
                "county_name": "WestPokot",
                "constituencies": [
                    {
                        "constituency_name": "KAPENGURIA",
                        "wards": [
                            "RIWO",
                            "KAPENGURIA",
                            "MNAGEI",
                            "SIYOI",
                            "ENDUGH",
                            "SOOK",
                        ],
                    },
                    {
                        "constituency_name": "SIGOR",
                        "wards": ["SEKERR", "MASOOL", "LOMUT", "WEIWEI"],
                    },
                    {
                        "constituency_name": "KACHELIBA",
                        "wards": [
                            "SUAM",
                            "KODICH",
                            "KASEI",
                            "KAPCHOK",
                            "KIWAWA",
                            "ALALE",
                        ],
                    },
                    {
                        "constituency_name": "POKOT_SOUTH",
                        "wards": ["CHEPARERIA", "BATEI", "LELAN", "TAPACH"],
                    },
                    {
                        "constituency_name": "TURKANA_SOUTH",
                        "wards": [
                            "KAPUTIR",
                            "KATILU",
                            "LOBOKAT",
                            "KALAPATA",
                            "LOKICHAR",
                        ],
                    },
                    {
                        "constituency_name": "TURKANA_EAST",
                        "wards": ["KAPEDO/NAPEITOM", "KATILIA", "LOKORI/KOCHODIN"],
                    },
                ],
            },
            {
                "county_name": "Samburu",
                "constituencies": [
                    {
                        "constituency_name": "SAMBURU_WEST",
                        "wards": [
                            "LODOKEJEK",
                            "SUGUTA MARMAR",
                            "MARALAL",
                            "LOOSUK",
                            "PORO",
                        ],
                    },
                    {
                        "constituency_name": "SAMBURU_NORTH",
                        "wards": [
                            "EL-BARTA",
                            "NACHOLA",
                            "NDOTO",
                            "NYIRO",
                            "ANGATA NANYOKIE",
                            "BAAWA",
                        ],
                    },
                    {
                        "constituency_name": "SAMBURU_EAST",
                        "wards": ["WASO", "WAMBA WEST", "WAMBA EAST", "WAMBA NORTH"],
                    },
                ],
            },
            {
                "county_name": "TransNzoia",
                "constituencies": [
                    {
                        "constituency_name": "KWANZA",
                        "wards": ["KAPOMBOI", "KWANZA", "KEIYO", "BIDII"],
                    },
                    {
                        "constituency_name": "ENDEBESS",
                        "wards": ["CHEPCHOINA", "ENDEBESS", "MATUMBEI"],
                    },
                    {
                        "constituency_name": "SABOTI",
                        "wards": ["KINYORO", "MATISI", "TUWANI", "SABOTI", "MACHEWA"],
                    },
                    {
                        "constituency_name": "KIMININI",
                        "wards": [
                            "KIMININI",
                            "WAITALUK",
                            "SIRENDE",
                            "HOSPITAL",
                            "SIKHENDU",
                            "NABISWA",
                        ],
                    },
                    {
                        "constituency_name": "CHERANGANY",
                        "wards": [
                            "SINYERERE",
                            "MAKUTANO",
                            "KAPLAMAI",
                            "MOTOSIET",
                            "CHERANGANY/SUWERWA",
                            "CHEPSIRO/KIPTOROR",
                            "SITATUNGA",
                        ],
                    },
                ],
            },
            {
                "county_name": "UasinGishu",
                "constituencies": [
                    {
                        "constituency_name": "SOY",
                        "wards": [
                            "MOI'S BRIDGE",
                            "KAPKURES",
                            "ZIWA",
                            "SEGERO/BARSOMBE",
                            "KIPSOMBA",
                            "SOY",
                            "KUINET/KAPSUSWA",
                        ],
                    },
                    {
                        "constituency_name": "TURBO",
                        "wards": [
                            "NGENYILEL",
                            "TAPSAGOI",
                            "KAMAGUT",
                            "KIPLOMBE",
                            "KAPSAOS",
                            "HURUMA",
                        ],
                    },
                    {
                        "constituency_name": "MOIBEN",
                        "wards": [
                            "TEMBELIO",
                            "SERGOIT",
                            "KARUNA/MEIBEKI",
                            "MOIBEN",
                            "KIMUMU",
                        ],
                    },
                    {
                        "constituency_name": "AINABKOI",
                        "wards": ["KAPSOYA", "KAPTAGAT", "AINABKOI/OLARE"],
                    },
                    {
                        "constituency_name": "KAPSERET",
                        "wards": [
                            "SIMAT/KAPSERET",
                            "KIPKENYO",
                            "NGERIA",
                            "MEGUN",
                            "LANGAS",
                        ],
                    },
                    {
                        "constituency_name": "KESSES",
                        "wards": [
                            "RACECOURSE",
                            "CHEPTIRET/KIPCHAMO",
                            "TULWET/CHUIYAT",
                            "TARAKWA",
                        ],
                    },
                ],
            },
            {
                "county_name": "ElgeyoMarakwet",
                "constituencies": [
                    {
                        "constituency_name": "MARAKWET_EAST",
                        "wards": [
                            "KAPYEGO",
                            "SAMBIRIR",
                            "ENDO",
                            "EMBOBUT/EMBULOT",
                            "LELAN",
                            "SENGWER",
                        ],
                    },
                    {
                        "constituency_name": "MARAKWET_WEST",
                        "wards": [
                            "CHERANG'ANY/CHEBORORWA",
                            "MOIBEN/KUSERWO",
                            "KAPSOWAR",
                            "ARROR",
                        ],
                    },
                    {
                        "constituency_name": "KEIYO_NORTH",
                        "wards": ["EMSOO", "KAMARINY", "KAPCHEMUTWA", "TAMBACH"],
                    },
                    {
                        "constituency_name": "KEIYO_SOUTH",
                        "wards": [
                            "KAPTARAKWA",
                            "CHEPKORIO",
                            "SOY NORTH",
                            "SOY SOUTH",
                            "KABIEMIT",
                            "METKEI",
                        ],
                    },
                ],
            },
            {
                "county_name": "Nandi",
                "constituencies": [
                    {
                        "constituency_name": "TINDERET",
                        "wards": [
                            "SONGHOR/SOBA",
                            "TINDIRET",
                            "CHEMELIL/CHEMASE",
                            "KAPSIMOTWO",
                        ],
                    },
                    {
                        "constituency_name": "ALDAI",
                        "wards": [
                            "KABWARENG",
                            "TERIK",
                            "KEMELOI-MARABA",
                            "KOBUJOI",
                            "KAPTUMO-KABOI",
                            "KOYO-NDURIO",
                        ],
                    },
                    {
                        "constituency_name": "NANDI_HILLS",
                        "wards": [
                            "NANDI HILLS",
                            "CHEPKUNYUK",
                            "OL'LESSOS",
                            "KAPCHORUA",
                        ],
                    },
                    {
                        "constituency_name": "CHESUMEI",
                        "wards": [
                            "CHEMUNDU/KAPNG'ETUNY",
                            "KOSIRAI",
                            "LELMOKWO/NGECHEK",
                            "KAPTEL/KAMOIYWO",
                            "KIPTUYA",
                        ],
                    },
                    {
                        "constituency_name": "EMGWEN",
                        "wards": ["CHEPKUMIA", "KAPKANGANI", "KAPSABET", "KILIBWONI"],
                    },
                    {
                        "constituency_name": "MOSOP",
                        "wards": [
                            "CHEPTERWAI",
                            "KIPKAREN",
                            "KURGUNG/SURUNGAI",
                            "KABIYET",
                            "NDALAT",
                            "KABISAGA",
                            "SANGALO/KEBULONIK",
                        ],
                    },
                ],
            },
            {
                "county_name": "Baringo",
                "constituencies": [
                    {
                        "constituency_name": "TIATY",
                        "wards": [
                            "TIRIOKO",
                            "KOLOWA",
                            "RIBKWO",
                            "SILALE",
                            "LOIYAMOROCK",
                            "TANGULBEI/KOROSSI",
                            "CHURO/AMAYA",
                        ],
                    },
                    {
                        "constituency_name": "BARINGO_NORTH",
                        "wards": [
                            "BARWESSA",
                            "KABARTONJO",
                            "SAIMO/KIPSARAMAN",
                            "SAIMO/SOI",
                            "BARTABWA",
                        ],
                    },
                    {
                        "constituency_name": "BARINGO_CENTRAL",
                        "wards": [
                            "KABARNET",
                            "SACHO",
                            "TENGES",
                            "EWALEL/CHAPCHAP",
                            "KAPROPITA",
                        ],
                    },
                    {
                        "constituency_name": "BARINGO_SOUTH",
                        "wards": ["MARIGAT", "ILCHAMUS", "MOCHONGOI", "MUKUTANI"],
                    },
                    {
                        "constituency_name": "MOGOTIO",
                        "wards": ["MOGOTIO", "EMINING", "KISANANA"],
                    },
                    {
                        "constituency_name": "ELDAMA_RAVINE",
                        "wards": [
                            "LEMBUS",
                            "LEMBUS KWEN",
                            "RAVINE",
                            "MUMBERES/MAJI MAZURI",
                            "LEMBUS/PERKERRA",
                            "KOIBATEK",
                        ],
                    },
                ],
            },
            {
                "county_name": "Laikipia",
                "constituencies": [
                    {
                        "constituency_name": "LAIKIPIA_WEST",
                        "wards": [
                            "OL-MORAN",
                            "RUMURUTI TOWNSHIP",
                            "GITHIGA",
                            "MARMANET",
                            "IGWAMITI",
                            "SALAMA",
                        ],
                    },
                    {
                        "constituency_name": "LAIKIPIA_EAST",
                        "wards": [
                            "NGOBIT",
                            "TIGITHI",
                            "THINGITHU",
                            "NANYUKI",
                            "UMANDE",
                        ],
                    },
                    {
                        "constituency_name": "LAIKIPIA_NORTH",
                        "wards": ["SOSIAN", "SEGERA", "MUGOGODO WEST", "MUGOGODO EAST"],
                    },
                ],
            },
            {
                "county_name": "Nakuru",
                "constituencies": [
                    {
                        "constituency_name": "MOLO",
                        "wards": ["MARIASHONI", "ELBURGON", "TURI", "MOLO"],
                    },
                    {
                        "constituency_name": "NJORO",
                        "wards": [
                            "MAU NAROK",
                            "MAUCHE",
                            "KIHINGO",
                            "NESSUIT",
                            "LARE",
                            "NJORO",
                        ],
                    },
                    {
                        "constituency_name": "NAIVASHA",
                        "wards": [
                            "BIASHARA",
                            "HELLS GATE",
                            "LAKE VIEW",
                            "MAI MAHIU",
                            "MAIELLA",
                            "OLKARIA",
                            "NAIVASHA EAST",
                            "VIWANDANI",
                        ],
                    },
                    {
                        "constituency_name": "GILGIL",
                        "wards": [
                            "GILGIL",
                            "ELEMENTAITA",
                            "MBARUK/EBURU",
                            "MALEWA WEST",
                            "MURINDATI",
                        ],
                    },
                    {
                        "constituency_name": "KURESOI_SOUTH",
                        "wards": ["AMALO", "KERINGET", "KIPTAGICH", "TINET"],
                    },
                    {
                        "constituency_name": "KURESOI_NORTH",
                        "wards": ["KIPTORORO", "NYOTA", "SIRIKWA", "KAMARA"],
                    },
                    {
                        "constituency_name": "SUBUKIA",
                        "wards": ["SUBUKIA", "WASEGES", "KABAZI"],
                    },
                    {
                        "constituency_name": "RONGAI",
                        "wards": ["MENENGAI WEST", "SOIN", "VISOI", "MOSOP", "SOLAI"],
                    },
                    {
                        "constituency_name": "BAHATI",
                        "wards": [
                            "DUNDORI",
                            "KABATINI",
                            "KIAMAINA",
                            "LANET/UMOJA",
                            "BAHATI",
                        ],
                    },
                    {
                        "constituency_name": "NAKURU_TOWN_WEST",
                        "wards": [
                            "BARUT",
                            "LONDON",
                            "KAPTEMBWO",
                            "KAPKURES",
                            "RHODA",
                            "SHAABAB",
                        ],
                    },
                    {
                        "constituency_name": "NAKURU_TOWN_EAST",
                        "wards": [
                            "BIASHARA",
                            "KIVUMBINI",
                            "FLAMINGO",
                            "MENENGAI",
                            "NAKURU EAST",
                        ],
                    },
                ],
            },
            {
                "county_name": "Narok",
                "constituencies": [
                    {
                        "constituency_name": "KILGORIS",
                        "wards": [
                            "KILGORIS CENTRAL",
                            "KEYIAN",
                            "ANGATA BARIKOI",
                            "SHANKOE",
                            "KIMINTET",
                            "LOLGORIAN",
                        ],
                    },
                    {
                        "constituency_name": "EMURUA_DIKIRR",
                        "wards": ["ILKERIN", "OLOlMASANI", "MOGONDO", "KAPSASIAN"],
                    },
                    {
                        "constituency_name": "NAROK_NORTH",
                        "wards": [
                            "OLPUSIMORU",
                            "OLOKURTO",
                            "NAROK TOWN",
                            "NKARETA",
                            "OLORROPIL",
                            "MELILI",
                        ],
                    },
                    {
                        "constituency_name": "NAROK_EAST",
                        "wards": ["MOSIRO", "ILDAMAT", "KEEKONYOKIE", "SUSWA"],
                    },
                    {
                        "constituency_name": "NAROK_SOUTH",
                        "wards": [
                            "MAJIMOTO/NAROOSURA",
                            "OLOLULUNG'A",
                            "MELELO",
                            "LOITA",
                            "SOGOO",
                            "SAGAMIAN",
                        ],
                    },
                    {
                        "constituency_name": "NAROK_WEST",
                        "wards": ["ILMOTIOK", "MARA", "SIANA", "NAIKARRA"],
                    },
                ],
            },
            {
                "county_name": "Kajiado",
                "constituencies": [
                    {
                        "constituency_name": "KAJIADO_NORTH",
                        "wards": [
                            "OLKERI",
                            "ONGATA RONGAI",
                            "NKAIMURUNYA",
                            "OLOOLUA",
                            "NGONG",
                        ],
                    },
                    {
                        "constituency_name": "KAJIADO_CENTRAL",
                        "wards": [
                            "PURKO",
                            "ILDAMAT",
                            "DALALEKUTUK",
                            "MATAPATO NORTH",
                            "MATAPATO SOUTH",
                        ],
                    },
                    {
                        "constituency_name": "KAJIADO_EAST",
                        "wards": [
                            "KAPUTIEI NORTH",
                            "KITENGELA",
                            "OLOOSIRKON/SHOLINKE",
                            "KENYAWA-POKA",
                            "IMARORO",
                        ],
                    },
                    {
                        "constituency_name": "KAJIADO_WEST",
                        "wards": [
                            "KEEKONYOKIE",
                            "ILOODOKILANI",
                            "MAGADI",
                            "EWUASO OoNKIDONG'I",
                            "MOSIRO",
                        ],
                    },
                    {
                        "constituency_name": "KAJIADO_SOUTH",
                        "wards": [
                            "ENTONET/LENKISIM",
                            "MBIRIKANI/ESELENKEI",
                            "KUKU",
                            "ROMBO",
                            "KIMANA",
                        ],
                    },
                ],
            },
            {
                "county_name": "Kericho",
                "constituencies": [
                    {
                        "constituency_name": "KIPKELION_EAST",
                        "wards": [
                            "LONDIANI",
                            "KEDOWA/KIMUGUL",
                            "CHEPSEON",
                            "TENDENO/SORGET",
                        ],
                    },
                    {
                        "constituency_name": "KIPKELION_WEST",
                        "wards": ["KUNYAK", "KAMASIAN", "KIPKELION", "CHILCHILA"],
                    },
                    {
                        "constituency_name": "AINAMOI",
                        "wards": [
                            "KAPSOIT",
                            "AINAMOI",
                            "KAPKUGERWET",
                            "KIPCHEBOR",
                            "KIPCHIMCHIM",
                            "KAPSAOS",
                        ],
                    },
                    {
                        "constituency_name": "BURETI",
                        "wards": [
                            "KISIARA",
                            "TEBESONIK",
                            "CHEBOIN",
                            "CHEMOSOT",
                            "LITEIN",
                            "CHEPLANGET",
                            "KAPKATET",
                        ],
                    },
                    {
                        "constituency_name": "BELGUT",
                        "wards": [
                            "WALDAI",
                            "KABIANGA",
                            "CHEPTORORIET/SERETUT",
                            "CHAIK",
                            "KAPSUSER",
                        ],
                    },
                    {
                        "constituency_name": "SIGOWET/SOIN",
                        "wards": ["SIGOWET", "KAPLELARTET", "SOLIAT", "SOIN"],
                    },
                ],
            },
            {
                "county_name": "Bomet",
                "constituencies": [
                    {
                        "constituency_name": "SOTIK",
                        "wards": [
                            "NDANAI/ABOSI",
                            "CHEMAGEL",
                            "KIPSONOI",
                            "KAPLETUNDO",
                            "RONGENA/MANARET",
                        ],
                    },
                    {
                        "constituency_name": "CHEPALUNGU",
                        "wards": [
                            "KONG'ASIS",
                            "NYANGORES",
                            "SIGOR",
                            "CHEBUNYO",
                            "SIONGIROI",
                        ],
                    },
                    {
                        "constituency_name": "BOMET_EAST",
                        "wards": ["MERIGI", "KEMBU", "LONGISA", "KIPRERES", "CHEMANER"],
                    },
                    {
                        "constituency_name": "BOMET_CENTRAL",
                        "wards": [
                            "SILIBWET TOWNSHIP",
                            "NDARAWETA",
                            "SINGORWET",
                            "CHESOEN",
                            "MUTARAKWA",
                        ],
                    },
                    {
                        "constituency_name": "KONOIN",
                        "wards": [
                            "CHEPCHABAS",
                            "KIMULOT",
                            "MOGOGOSIEK",
                            "BOITO",
                            "EMBOMOS",
                        ],
                    },
                ],
            },
            {
                "county_name": "Kakamega",
                "constituencies": [
                    {
                        "constituency_name": "LUGARI",
                        "wards": [
                            "MAUTUMA",
                            "LUGARI",
                            "LUMAKANDA",
                            "CHEKALINI",
                            "CHEVAYWA",
                            "LWANDETI",
                        ],
                    },
                    {
                        "constituency_name": "LIKUYANI",
                        "wards": ["LIKUYANI", "SANGO", "KONGONI", "NZOIA", "SINOKO"],
                    },
                    {
                        "constituency_name": "MALAVA",
                        "wards": [
                            "WEST KABRAS",
                            "CHEMUCHE",
                            "EAST KABRAS",
                            "BUTALI/CHEGULO",
                            "MANDA-SHIVANGA",
                            "SHIRUGU-MUGAI",
                            "SOUTH KABRAS",
                        ],
                    },
                    {
                        "constituency_name": "LURAMBI",
                        "wards": [
                            "BUTSOTSO EAST",
                            "BUTSOTSO SOUTH",
                            "BUTSOTSO CENTRAL",
                            "SHEYWE",
                            "MAHIAKALO",
                            "SHIRERE",
                        ],
                    },
                    {
                        "constituency_name": "NAVAKHOLO",
                        "wards": [
                            "INGOSTSE-MATHIA",
                            "SHINOYI-SHIKOMARI-ESUMEYIA",
                            "BUNYALA WEST",
                            "BUNYALA EAST",
                            "BUNYALA CENTRAL",
                        ],
                    },
                    {
                        "constituency_name": "MUMIAS_WEST",
                        "wards": [
                            "MUMIAS CENTRAL",
                            "MUMIAS NORTH",
                            "ETENJE",
                            "MUSANDA",
                        ],
                    },
                    {
                        "constituency_name": "MUMIAS_EAST",
                        "wards": [
                            "LUSHEYA/LUBINU",
                            "MALAHA/ISONGO/MAKUNGA",
                            "EAST WANGA",
                        ],
                    },
                    {
                        "constituency_name": "MATUNGU",
                        "wards": [
                            "KOYONZO",
                            "KHOLERA",
                            "KHALABA",
                            "MAYONI",
                            "NAMAMALI",
                        ],
                    },
                    {
                        "constituency_name": "BUTERE",
                        "wards": [
                            "MARAMA WEST",
                            "MARAMA CENTRAL",
                            "MARENYO - SHIANDA",
                            "MARAMA NORTH",
                            "MARAMA SOUTH",
                        ],
                    },
                    {
                        "constituency_name": "KHWISERO",
                        "wards": [
                            "KISA NORTH",
                            "KISA EAST",
                            "KISA WEST",
                            "KISA CENTRAL",
                        ],
                    },
                    {
                        "constituency_name": "SHINYALU",
                        "wards": [
                            "ISUKHA NORTH",
                            "MURHANDA",
                            "ISUKHA CENTRAL",
                            "ISUKHA SOUTH",
                            "ISUKHA EAST",
                            "ISUKHA WEST",
                        ],
                    },
                    {
                        "constituency_name": "IKOLOMANI",
                        "wards": [
                            "IDAKHO SOUTH",
                            "IDAKHO EAST",
                            "IDAKHO NORTH",
                            "IDAKHO CENTRAL",
                        ],
                    },
                ],
            },
            {
                "county_name": "Vihiga",
                "constituencies": [
                    {
                        "constituency_name": "VIHIGA",
                        "wards": [
                            "LUGAGA-WAMULUMA",
                            "SOUTH MARAGOLI",
                            "CENTRAL MARAGOLI",
                        ],
                    },
                    {
                        "constituency_name": "SABATIA",
                        "wards": [
                            "MUNGOMA",
                            "LYADUYWA/IZAVA",
                            "WEST SABATIA",
                            "CHAVAKALI",
                            "NORTH MARAGOLI",
                            "WODANGA",
                            "BUSALI",
                        ],
                    },
                    {
                        "constituency_name": "HAMISI",
                        "wards": [
                            "SHIRU",
                            "GISAMBAI",
                            "SHAMAKHOKHO",
                            "BANJA",
                            "MUHUDU",
                            "TAMBUA",
                            "JEPKOYAI",
                        ],
                    },
                    {
                        "constituency_name": "LUANDA",
                        "wards": [
                            "LUANDA TOWNSHIP",
                            "WEMILABI",
                            "MWIBONA",
                            "LUANDA SOUTH",
                            "EMABUNGO",
                        ],
                    },
                    {
                        "constituency_name": "EMUHAYA",
                        "wards": [
                            "NORTH EAST BUNYORE",
                            "CENTRAL BUNYORE",
                            "WEST BUNYORE",
                        ],
                    },
                ],
            },
            {
                "county_name": "Bungoma",
                "constituencies": [
                    {
                        "constituency_name": "MT.ELGON",
                        "wards": [
                            "CHEPTAIS",
                            "CHESIKAKI",
                            "CHEPYUK",
                            "KAPKATENY",
                            "KAPTAMA",
                            "ELGON",
                        ],
                    },
                    {
                        "constituency_name": "SIRISIA",
                        "wards": ["NAMWELA", "MALAKISI/SOUTH KULISIRU", "LWANDANYI"],
                    },
                    {
                        "constituency_name": "KABUCHAI",
                        "wards": [
                            "KABUCHAI/CHWELE",
                            "WEST NALONDO",
                            "BWAKE/LUUYA",
                            "MUKUYUNI",
                        ],
                    },
                    {
                        "constituency_name": "BUMULA",
                        "wards": [
                            "SOUTH BUKUSU",
                            "BUMULA",
                            "KHASOKO",
                            "KABULA",
                            "KIMAETI",
                            "WEST BUKUSU",
                            "SIBOTI",
                        ],
                    },
                    {
                        "constituency_name": "KANDUYI",
                        "wards": [
                            "BUKEMBE WEST",
                            "BUKEMBE EAST",
                            "TOWNSHIP",
                            "KHALABA",
                            "MUSIKOMA",
                            "EAST SANG'ALO",
                            "MARAKARU/TUUTI",
                            "WEST SANG'ALO",
                        ],
                    },
                    {
                        "constituency_name": "WEBUYE_EAST",
                        "wards": ["MIHUU", "NDIVISI", "MARAKA"],
                    },
                    {
                        "constituency_name": "WEBUYE_WEST",
                        "wards": ["MISIKHU", "SITIKHO", "MATULO", "BOKOLI"],
                    },
                    {
                        "constituency_name": "KIMILILI",
                        "wards": ["KIBINGEI", "KIMILILI", "MAENI", "KAMUKUYWA"],
                    },
                    {
                        "constituency_name": "TONGAREN",
                        "wards": [
                            "MBAKALO",
                            "NAITIRI/KABUYEFWE",
                            "MILIMA",
                            "NDALU/TABANI",
                            "TONGAREN",
                            "SOYSAMBU/MITUA",
                        ],
                    },
                ],
            },
            {
                "county_name": "Busia",
                "constituencies": [
                    {
                        "constituency_name": "TESO_NORTH",
                        "wards": [
                            "MALABA CENTRAL",
                            "MALABA NORTH",
                            "ANG'URAI SOUTH",
                            "ANG'URAI NORTH",
                            "ANG'URAI EAST",
                            "MALABA SOUTH",
                        ],
                    },
                    {
                        "constituency_name": "TESO_SOUTH",
                        "wards": [
                            "ANG'OROM",
                            "CHAKOL SOUTH",
                            "CHAKOL NORTH",
                            "AMUKURA WEST",
                            "AMUKURA EAST",
                            "AMUKURA CENTRAL",
                        ],
                    },
                    {
                        "constituency_name": "NAMBALE",
                        "wards": [
                            "NAMBALE TOWNSHIP",
                            "BUKHAYO NORTH/WALTSI",
                            "BUKHAYO EAST",
                            "BUKHAYO CENTRAL",
                        ],
                    },
                    {
                        "constituency_name": "MATAYOS",
                        "wards": [
                            "BUKHAYO WEST",
                            "MAYENJE",
                            "MATAYOS SOUTH",
                            "BUSIBWABO",
                            "BURUMBA",
                        ],
                    },
                    {
                        "constituency_name": "BUTULA",
                        "wards": [
                            "MARACHI WEST",
                            "KINGANDOLE",
                            "MARACHI CENTRAL",
                            "MARACHI EAST",
                            "MARACHI NORTH",
                            "ELUGULU",
                        ],
                    },
                    {
                        "constituency_name": "FUNYULA",
                        "wards": [
                            "NAMBOBOTO NAMBUKU",
                            "NANGINA",
                            "AGENG'A NANGUBA",
                            "BWIRI",
                        ],
                    },
                    {
                        "constituency_name": "BUDALANGI,",
                        "wards": [
                            "BUNYALA CENTRAL",
                            "BUNYALA NORTH",
                            "BUNYALA WEST",
                            "BUNYALA SOUTH",
                        ],
                    },
                ],
            },
            {
                "county_name": "Siaya",
                "constituencies": [
                    {
                        "constituency_name": "UGENYA",
                        "wards": [
                            "WEST UGENYA",
                            "UKWALA",
                            "NORTH UGENYA",
                            "EAST UGENYA",
                        ],
                    },
                    {
                        "constituency_name": "UGUNJA",
                        "wards": ["SIDINDI", "SIGOMERE", "UGUNJA"],
                    },
                    {
                        "constituency_name": "ALEGO_USONGA",
                        "wards": [
                            "USONGA",
                            "WEST ALEGO",
                            "CENTRAL ALEGO",
                            "SIAYA TOWNSHIP",
                            "NORTH ALEGO",
                            "SOUTH EAST ALEGO",
                        ],
                    },
                    {
                        "constituency_name": "GEM",
                        "wards": [
                            "NORTH GEM",
                            "WEST GEM",
                            "CENTRAL GEM",
                            "YALA TOWNSHIP",
                            "EAST GEM",
                            "SOUTH GEM",
                        ],
                    },
                    {
                        "constituency_name": "BONDO",
                        "wards": [
                            "WEST YIMBO",
                            "CENTRAL SAKWA",
                            "SOUTH SAKWA",
                            "YIMBO EAST",
                            "WEST SAKWA",
                            "NORTH SAKWA",
                        ],
                    },
                    {
                        "constituency_name": "RARIEDA",
                        "wards": [
                            "EAST ASEMBO",
                            "WEST ASEMBO",
                            "NORTH UYOMA",
                            "SOUTH UYOMA",
                            "WEST UYOMA",
                        ],
                    },
                ],
            },
            {
                "county_name": "Kisumu",
                "constituencies": [
                    {
                        "constituency_name": "KISUMU_EAST",
                        "wards": [
                            "KAJULU",
                            "KOLWA EAST",
                            "MANYATTA 'B'",
                            "NYALENDA 'A'",
                            "KOLWA CENTRAL",
                        ],
                    },
                    {
                        "constituency_name": "KISUMU_WEST",
                        "wards": [
                            "SOUTH WEST KISUMU",
                            "CENTRAL KISUMU",
                            "KISUMU NORTH",
                            "WEST KISUMU",
                            "NORTH WEST KISUMU",
                        ],
                    },
                    {
                        "constituency_name": "KISUMU_CENTRAL",
                        "wards": [
                            "RAILWAYS",
                            "MIGOSI",
                            "SHAURIMOYO KALOLENI",
                            "MARKET MILIMANI",
                            "KONDELE",
                            "NYALENDA B",
                        ],
                    },
                    {
                        "constituency_name": "SEME",
                        "wards": [
                            "WEST SEME",
                            "CENTRAL SEME",
                            "EAST SEME",
                            "NORTH SEME",
                        ],
                    },
                    {
                        "constituency_name": "NYANDO",
                        "wards": [
                            "EAST KANO/WAWIDHI",
                            "AWASI/ONJIKO",
                            "AHERO",
                            "KABONYO/KANYAGWAL",
                            "KOBURA",
                        ],
                    },
                    {
                        "constituency_name": "MUHORONI",
                        "wards": [
                            "MIWANI",
                            "OMBEYI",
                            "MASOGO/NYANG'OMA",
                            "CHEMELIL",
                            "MUHORONI/KORU",
                        ],
                    },
                    {
                        "constituency_name": "NYAKACH",
                        "wards": [
                            "SOUTH WEST NYAKACH",
                            "NORTH NYAKACH",
                            "CENTRAL NYAKACH",
                            "WEST NYAKACH",
                            "SOUTH EAST NYAKACH",
                        ],
                    },
                ],
            },
            {
                "county_name": "HomaBay",
                "constituencies": [
                    {
                        "constituency_name": "KASIPUL",
                        "wards": [
                            "WEST KASIPUL",
                            "SOUTH KASIPUL",
                            "CENTRAL KASIPUL",
                            "EAST KAMAGAK",
                            "WEST KAMAGAK",
                        ],
                    },
                    {
                        "constituency_name": "KABONDO_KASIPUL",
                        "wards": [
                            "KABONDO EAST",
                            "KABONDO WEST",
                            "KOKWANYO/KAKELO",
                            "KOJWACH",
                        ],
                    },
                    {
                        "constituency_name": "KARACHUONYO",
                        "wards": [
                            "WEST KARACHUONYO",
                            "NORTH KARACHUONYO",
                            "CENTRAL",
                            "KANYALUO",
                            "KIBIRI",
                            "WANGCHIENG",
                            "KENDU BAY TOWN",
                        ],
                    },
                    {
                        "constituency_name": "RANGWE",
                        "wards": ["WEST GEM", "EAST GEM", "KAGAN", "KOCHIA"],
                    },
                    {
                        "constituency_name": "HOMA_BAY_TOWN",
                        "wards": [
                            "HOMA BAY CENTRAL",
                            "HOMA BAY ARUJO",
                            "HOMA BAY WEST",
                            "HOMA BAY EAST",
                        ],
                    },
                    {
                        "constituency_name": "NDHIWA",
                        "wards": [
                            "KWABWAI",
                            "KANYADOTO",
                            "KANYIKELA",
                            "KABUOCH NORTH",
                            "KABUOCH SOUTH/PALA",
                            "KANYAMWA KOLOGI",
                            "KANYAMWA KOSEWE",
                        ],
                    },
                    {
                        "constituency_name": "SUBA_NORTH",
                        "wards": [
                            "MFANGANO ISLAND",
                            "RUSINGA ISLAND",
                            "KASGUNGA",
                            "GEMBE",
                            "LAMBWE",
                        ],
                    },
                    {
                        "constituency_name": "SUBA_SOUTH",
                        "wards": [
                            "GWASSI SOUTH",
                            "GWASSI NORTH",
                            "KAKSINGRI WEST",
                            "RUMA-KAKSINGRI",
                        ],
                    },
                ],
            },
            {
                "county_name": "Migori",
                "constituencies": [
                    {
                        "constituency_name": "RONGO",
                        "wards": [
                            "NORTH KAMAGAMBO",
                            "CENTRAL KAMAGAMBO",
                            "EAST KAMAGAMBO",
                            "SOUTH KAMAGAMBO",
                        ],
                    },
                    {
                        "constituency_name": "AWENDO",
                        "wards": [
                            "NORTH SAKWA",
                            "SOUTH SAKWA",
                            "WEST SAKWA",
                            "CENTRAL SAKWA",
                        ],
                    },
                    {
                        "constituency_name": "SUNA_EAST",
                        "wards": ["GOD JOPE", "SUNA CENTRAL", "KAKRAO", "KWA"],
                    },
                    {
                        "constituency_name": "SUNA_WEST",
                        "wards": ["WIGA", "WASWETA II", "RAGANA-ORUBA", "WASIMBETE"],
                    },
                    {
                        "constituency_name": "URIRI",
                        "wards": [
                            "WEST KANYAMKAGO",
                            "NORTH KANYAMKAGO",
                            "CENTRAL KANYAMKAGO",
                            "SOUTH KANYAMKAGO",
                            "EAST KANYAMKAGO",
                        ],
                    },
                    {
                        "constituency_name": "NYATIKE",
                        "wards": [
                            "KACHIEN'G",
                            "KANYASA",
                            "NORTH KADEM",
                            "MACALDER/KANYARWANDA",
                            "KALER",
                            "GOT KACHOLA",
                            "MUHURU",
                        ],
                    },
                    {
                        "constituency_name": "KURIA_WEST",
                        "wards": [
                            "BUKIRA EAST",
                            "BUKIRA CENTRL/IKEREGE",
                            "ISIBANIA",
                            "MAKERERO",
                            "MASABA",
                            "TAGARE",
                            "NYAMOSENSE/KOMOSOKO",
                        ],
                    },
                    {
                        "constituency_name": "KURIA_EAST",
                        "wards": [
                            "GOKEHARAKA/GETAMBWEGA",
                            "NTIMARU WEST",
                            "NTIMARU EAST",
                            "NYABASI EAST",
                            "NYABASI WEST",
                        ],
                    },
                ],
            },
            {
                "county_name": "Kisii",
                "constituencies": [
                    {
                        "constituency_name": "BONCHARI",
                        "wards": ["BOMARIBA", "BOGIAKUMU", "BOMORENDA", "RIANA"],
                    },
                    {
                        "constituency_name": "SOUTH_MUGIRANGO",
                        "wards": [
                            "TABAKA",
                            "BOIKANG'A",
                            "BOGETENGA",
                            "BORABU/CHITAGO",
                            "MOTICHO",
                            "GETENGA",
                        ],
                    },
                    {
                        "constituency_name": "BOMACHOGE_BORABU",
                        "wards": [
                            "BOMBABA BORABU",
                            "BOOCHI BORABU",
                            "BOKIMONGE",
                            "MAGENCHE",
                        ],
                    },
                    {
                        "constituency_name": "BOBASI",
                        "wards": [
                            "MASIGE WEST",
                            "MASIGE EAST",
                            "BASI CENTRAL",
                            "NYACHEKI",
                            "BASI BOGETAORIO",
                            "BOBASI CHACHE",
                            "SAMETA/MOKWERERO",
                            "BOBASI BOITANGARE",
                        ],
                    },
                    {
                        "constituency_name": "BOMACHOGE_CHACHE",
                        "wards": ["MAJOGE BASI", "BOOCHI/TENDERE", "BOSOTI/SENGERA"],
                    },
                    {
                        "constituency_name": "NYARIBARI_MASABA",
                        "wards": [
                            "ICHUNI",
                            "NYAMASIBI",
                            "MASIMBA",
                            "GESUSU",
                            "KIAMOKAMA",
                        ],
                    },
                    {
                        "constituency_name": "NYARIBARI_CHACHE",
                        "wards": [
                            "BOBARACHO",
                            "KISII CENTRAL",
                            "KEUMBU",
                            "KIOGORO",
                            "BIRONGO",
                            "IBENO",
                        ],
                    },
                    {
                        "constituency_name": "KITUTU_CHACHE_NORTH",
                        "wards": ["MONYERERO", "SENSI", "MARANI", "KEGOGI"],
                    },
                    {
                        "constituency_name": "KITUTU_CHACHE_SOUTH",
                        "wards": [
                            "BOGUSERO",
                            "BOGEKA",
                            "NYAKOE",
                            "KITUTU   CENTRAL",
                            "NYATIEKO",
                        ],
                    },
                ],
            },
            {
                "county_name": "Nyamira",
                "constituencies": [
                    {
                        "constituency_name": "KITUTU_MASABA",
                        "wards": [
                            "RIGOMA",
                            "GACHUBA",
                            "KEMERA",
                            "MAGOMBO",
                            "MANGA",
                            "GESIMA",
                        ],
                    },
                    {
                        "constituency_name": "WEST_MUGIRANGO",
                        "wards": [
                            "NYAMAIYA",
                            "BOGICHORA",
                            "BOSAMARO",
                            "BONYAMATUTA",
                            "TOWNSHIP",
                        ],
                    },
                    {
                        "constituency_name": "NORTH_MUGIRANGO",
                        "wards": [
                            "ITIBO",
                            "BOMWAGAMO",
                            "BOKEIRA",
                            "MAGWAGWA",
                            "EKERENYO",
                        ],
                    },
                    {
                        "constituency_name": "BORABU",
                        "wards": ["MEKENENE", "KIABONYORU", "NYANSIONGO", "ESISE"],
                    },
                ],
            },
            {
                "county_name": "Nairobi",
                "constituencies": [
                    {
                        "constituency_name": "WESTLANDS",
                        "wards": [
                            "KITISURU",
                            "PARKLANDS/HIGHRIDGE",
                            "KARURA",
                            "KANGEMI",
                            "MOUNTAIN VIEW",
                        ],
                    },
                    {
                        "constituency_name": "DAGORETTI_NORTH",
                        "wards": [
                            "KILIMANI",
                            "KAWANGWARE",
                            "GATINA",
                            "KILELESHWA",
                            "KABIRO",
                        ],
                    },
                    {
                        "constituency_name": "DAGORETTI_SOUTH",
                        "wards": [
                            "MUTU-INI",
                            "NGANDO",
                            "RIRUTA",
                            "UTHIRU/RUTHIMITU",
                            "WAITHAKA",
                        ],
                    },
                    {
                        "constituency_name": "LANGATA",
                        "wards": [
                            "KAREN",
                            "NAIROBI WEST",
                            "MUGUMU-INI",
                            "SOUTH C",
                            "NYAYO HIGHRISE",
                        ],
                    },
                    {
                        "constituency_name": "KIBRA",
                        "wards": [
                            "LAINI SABA",
                            "LINDI",
                            "MAKINA",
                            "WOODLEY/KENYATTA GOLF COURSE",
                            "SARANGOMBE",
                        ],
                    },
                    {
                        "constituency_name": "ROYSAMBU",
                        "wards": [
                            "GITHURAI",
                            "KAHAWA WEST",
                            "ZIMMERMAN",
                            "ROYSAMBU",
                            "KAHAWA",
                        ],
                    },
                    {
                        "constituency_name": "KASARANI",
                        "wards": ["CLAY CITY", "MWIKI", "KASARANI", "NJIRU", "RUAI"],
                    },
                    {
                        "constituency_name": "RUARAKA",
                        "wards": [
                            "BABA DOGO",
                            "UTALII",
                            "MATHARE NORTH",
                            "LUCKY SUMMER",
                            "KOROGOCHO",
                        ],
                    },
                    {
                        "constituency_name": "EMBAKASI_SOUTH",
                        "wards": [
                            "IMARA DAIMA",
                            "KWA NJENGA",
                            "KWA REUBEN",
                            "PIPELINE",
                            "KWARE",
                        ],
                    },
                    {
                        "constituency_name": "EMBAKASI_NORTH",
                        "wards": [
                            "KARIOBANGI NORTH",
                            "DANDORA AREA I",
                            "DANDORA AREA II",
                            "DANDORA AREA III",
                            "DANDORA AREA IV",
                        ],
                    },
                    {
                        "constituency_name": "EMBAKASI_CENTRAL",
                        "wards": [
                            "KAYOLE NORTH",
                            "KAYOLE CENTRAL",
                            "KAYOLE SOUTH",
                            "KOMAROCK",
                            "MATOPENI/SPRING VALLEY",
                        ],
                    },
                    {
                        "constituency_name": "EMBAKASI_EAST",
                        "wards": [
                            "UPPER SAVANNAH",
                            "LOWER SAVANNAH",
                            "EMBAKASI",
                            "UTAWALA",
                            "MIHANGO",
                        ],
                    },
                    {
                        "constituency_name": "EMBAKASI_WEST",
                        "wards": ["UMOJA I", "UMOJA II", "MOWLEM", "KARIOBANGI SOUTH"],
                    },
                    {
                        "constituency_name": "MAKADARA",
                        "wards": [
                            "MARINGO/HAMZA",
                            "VIWANDANI",
                            "HARAMBEE",
                            "MAKONGENI",
                        ],
                    },
                    {
                        "constituency_name": "KAMUKUNJI",
                        "wards": [
                            "PUMWANI",
                            "EASTLEIGH NORTH",
                            "EASTLEIGH SOUTH",
                            "AIRBASE",
                            "CALIFORNIA",
                        ],
                    },
                    {
                        "constituency_name": "STAREHE",
                        "wards": [
                            "NAIROBI CENTRAL",
                            "NGARA",
                            "PANGANI",
                            "ZIWANI/KARIOKOR",
                            "LANDIMAWE",
                            "NAIROBI SOUTH",
                        ],
                    },
                    {
                        "constituency_name": "MATHARE",
                        "wards": [
                            "HOSPITAL",
                            "MABATINI",
                            "HURUMA",
                            "NGEI",
                            "MLANGO KUBWA",
                            "KIAMAIKO",
                        ],
                    },
                ],
            },
        ]

        # for county in counties:
        #     county = County(county_name=county["county_name"])
        #     county.save()
        #     for constituency in county["constituencies"]:
        #         constituency = Constituency(county=county, constituency_name=constituency["constituency_name"])
        #         constituency.save()
        #         for ward in constituency["wards"]:
        #             ward = Ward(county=county, constituency=constituency, ward_name=ward)
        #             ward.save()

        for county_data in kenyan_data:
            county_name = county_data["county_name"]
            county, created = County.objects.get_or_create(name=county_name)
            if not created:
                print(f"County {county_name} already exists")
                continue

            for constituency_data in county_data["constituencies"]:
                constituency_name = constituency_data["constituency_name"]
                constituency, created = Constituency.objects.get_or_create(
                    county=county, name=constituency_name
                )
                if not created:
                    print(f"Constituency {constituency_name} already exists")
                    continue

                for ward_name in constituency_data["wards"]:
                    Ward.objects.create(name=ward_name, constituency=constituency)

        self.stdout.write(
            self.style.SUCCESS(
                "Successfully loaded county, constituency, and ward data."
            )
        )