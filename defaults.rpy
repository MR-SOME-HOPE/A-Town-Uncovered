## Characters
define ala = Character("Alanna", color="ae9466")
define ara = Character("Ara Asika", color="b35a57")
define ashm = Character("Mrs Ketchum", color="b35a57")
define bra = Character("Bradley", color="93b488")
define bro = Character("Brock", color="ae9466")
define car = Character("Carmen", color="e1c08e")
define chi = Character("Chieghan", color="dfb6cf")
define clas = Character("Class", color="dbdbdb")
define clasf = Character("Girl", color="dbdbdb")
define clasf1 = Character("Girl #1", color="dbdbdb")
define clasf2 = Character("Girl #2", color="dbdbdb")
define clasm = Character("Guy", color="dbdbdb")
define clasm1 = Character("Guy #1", color="dbdbdb")
define clasm2 = Character("Guy #2", color="dbdbdb")
define chrltt = Character("Charlotte", color="d46363")
define coa = Character("Coach Fistem", color="c9c6be")
define cor = Character("Corrine", color="83ba7b")
define col = Character("Cole", color="a1b7d4")
define cru = Character("Crugeon", color="dd7070")
define crowd = Character("Crowd", color="dbdbdb")
define dan = Character("Daniel", color="785f83")
define dav = Character("Davendithas", color="785f83")
define ded = Character("Dede", color="785f83")
define drug = Character("Drunk Girl", color="e3a668")
define edw = Character("Edward", color="dbae76")
define eff = Character("Effie", color="c87370")
define effdad = Character("Effie's Dad", color="dbdbdb")
define elo = Character("Eloise", color="7E6279")
define evi = Character("Evie", color="dbdbdb")
define eri = Character("Erica", color="dbdbdb")
define glo = Character("Gloria", color="ab87a1")
define goon = Character("Goon", color="dbdbdb")
define haz = Character("Hazel", color="e39ab8")
define hit = Character("Hitomi", color="a0d68f")
define how = Character("Howie", color="9fc2c6")
define ian = Character("Ian", color="dd7070")
define icman = Character("Manager", color="ae9466")
define idk = Character("???", color="c7c7c7")
define ix = Character("IX", color="#eee7e7")
define jac = Character("Jacob", color="9c81b5")
define jacdad = Character("Jacob's Dad", color="9c81b5")
define isac = Character("Isaac", color="9c81b5")
define jack = Character("Jack", color="7196d6")
define jai = Character("Jaiden", color="80a588")
define jan = Character("Janae", color="bc5350")
define kan = Character("Kanako", color="c3aca5")
define lai = Character("Lailah", color="f5c3d9")
define lill = Character("Lillian", color="b35a57")
define lor = Character("Lord Kevlamin", color="e5ce6d")
define lun = Character("Luna", color="cc6e6e")
define mas = Character("Master Buukakki", color="#eee7e7")
define meg = Character("Meghan", color="df9d80")
define mina = Character("Officer Mina", color="8eaec8")
define mis = Character("Miss Allaway", color="788492")
define mrf = Character("Mr Fistem", color="a5b0c7")
define news = Character("Newscaster", color="#eee1db")
define nur = Character("Nurse Hollick", color="d46363")
define pas = Character("PA System", color="dbdbdb")
define pau = Character("Officer Paul", color="e7ddb9")
define phi = Character("Phil", color="f3dd5e")
define pol = Character("Police Officer", color="8eaec8")
define pri = Character("Dir. Lashley", color="ceb78b")
define radio = Character("Radio", color="#eee1db")
define raul = Character("Raul", color="b15c5c")
define rcrdo = Character("Ricardo", color="7196d6")
define sam = Character("Grundle Sam", color="c87370")
define sis = Character("[sister]", color="#e89ab4")
define sky = Character("Skylar", color="d0ab91")
define ste = Character("Steve", color="f29d7c")
define studf = Character("Female Student", color="dbdbdb")
define studm = Character("Male Student", color="dbdbdb")
define studp = Character("Perverted Student", color="dbdbdb")
define swdad = Character("Sexworld [dadname]", color="c9cdce")
define teg = Character("Teghan", color="e7d981")
define tv = Character("TV", color="#eee1db")
define ush = Character("Usher", color="b15c5c")
define vi = Character("VI", color="#eee7e7")
define vio = Character("Violette", color="b75a49")
define wai = Character("Waiter", color="b15c5c")
define xin = Character("Xina", color="#eee1db")
define zar = Character("Zariah", color="ad75c1")
define voic = Character("Voice", color="dbdbdb")
define rprtr = Character("Reporter", color="ae9466")
define karis = Character("Karis", color="#eee1db")
define dor = Character("Dorothea", color="#eee1db")
define dru = Character("Drunk Girl", color="#eee1db")
#TODO geeseki - define strange man - to replace "Strange Man" in lashley toilet scenes

## define narrator = Character(None, window_style="window_narr")

## Pulsing Effect
define config.speaking_attribute = "talk"

transform pulse:
    zoom 1.0
    easein 0.4 zoom 1.015
    pause 0.1
    easeout 0.4 zoom 1.0

## Cheat mode (0 = off, 1 = on, 2 = unavailable (code needed), 3 = unavailable (coded NOT needed))
default cheat_on = 2

## Calander
default month = 0
default date = 0
default day = 0
default gtime = 0

## Story progression
default main_story = 0
default mum_path = 0
default violette_path = 0
default jack_path = 0
default lordkevlamin_path = 0
default hitomi_path = 0
default sister_path = 0
default effie_path = 0
default effiesdad_path = 0
default jacob_path = 0
default jacobsdad_path = 0
default lailah_path = 0
default dad_path = 0
default brock_path = 0
default alanna_path = 0
default janae_path = 0
default missallaway_path = 0
default principallashley_path = 0
default steve_path = 0
default hazel_path = 0
default mina_path = 0
default grundlesam_path = 0
default phil_path = 0
default meghan_path = 0
default chieghan_path = 0
default cole_path = 0
default jaiden_path = 0
default eloise_path = 0
default edward_path = 0
default teghan_path = 0
default zariah_path = 0
default luna_path = 0
default xina_path = 0
default mumsis_path = 0
default mumsiscamp_path = 1

## Character points
default violette_points = 0
default brock_points = 0
default lordkevlamin_points = 0
default crugeon_points = 0
default davendithas_points = 0
default hitomi_points = 0
default nursehollick_points = 0
default alanna_points = 0
default janae_points = 0
default mum_points = 0
default dad_points = 0
default sister_points = 0
default jacob_points = 0
default effie_points = 0
default missallaway_points = 0
default coachfistem_points = 0
default jack_points = 0
default principallashley_points = 0
default dog_points = 0
default hazel_points = 0
default phil_points = 0
default effiesdad_points = 0
default meghan_points = 0
default chieghan_points = 0
default cole_points = 0
default jaiden_points = 0
default eloise_points = 0
default grundlesam_points = 0
default jacobsdad_points = 0
default lailah_points = 0
default edward_points = 0
default teghan_points = 0
default zariah_points = 0
default luna_points = 0
default steve_points = 0
default mina_points = 0
default xina_points = 0

## Skill stats
default skill_int = 0
default skill_cha = 0
default skill_str = 0
default skill_sta = 0
default skill_luc = 0
default skill_intmax = 5
default skill_chamax = 5
default skill_strmax = 5
default skill_stamax = 5
default skill_lucmax = 5
default skill_int_times = 0
default skill_sta_times = 0
default skill_luc_times = 0

## HUD stuff
default hud_enabled = 1
default townmap_enabled = 1
default phone_tab = "Contacts"

## Misc Stuff
default acx_answer = "cum"
default thetext_ready = 0
default randomencounter = 0
default nextday_ajob = 0
default phoneobjectives_sidestory = 0
default beach_naked = 0
default beachchangeroom_fishbite = 0
default beachchangeroom_visit = 0
default beachgloryhole_visit = 0
default inventory = Inventory()
default mowed_lawn = 0
default savemomfromdad_tackle = 2
default store_counter = 1
default mommidnightfun = 0
default premoviedate_changemind = 0
default moviedate = 0 #(1 = Mom, 2 = Sister, 3 = Miss Allaway, 4 = Principal Lashley)
default moviedate_choice = 0
default fbpwmag1 = 0 #(1 = Mom, 2 = Sister)
default usname = "Hugh_GeeCock"
default insexworld = 0
default hitomibeach_day = 0
default newspaper = 0
default vrheadset_chest = 0
default gachamachine = 1

## Sex Around Town
default sexaroundtownbeach = 0
default sexaroundtownpark = 0
default sexaroundtownstreet = 0
default sexaroundtowncomicbookstore = 0
default sexaroundtowncafe = 0
default sexaroundtownretailstore = 0

## winc
default winc = 0

## crossroads variables
default kidnapping_assembly_crossroad = 0

## phone variables
default max_phone_objectives = 7
default effie_objectives_unlocked = False

##inventory variables
default selecteditem = None
default hitomi_gift_like_level = 0
default effie_gift_like_level = 0
default mum_gift_like_level = 0
default sister_gift_like_level = 0
default missallaway_gift_like_level = 0
default principallashley_gift_like_level = 0

## Sugar Service Trailer 2023
image sugarservicetrailer = Movie(play="/assets/sstrailer.webm",size=(1680,945), loop=False)

init python:
    tempvar_counter = 0

init 1 python:# vince's functions
    def IsAllawayInClass():
        if missallaway_path in (3,13) and gtime == 1:
            return False
        elif missallaway_path in (4, 19, 21) and insexworld == 0:
            return False

        elif (17 <= missallaway_path <= 18 and day < 4) and insexworld == 0:
            return False
        else:
            return True

    def MapBlockCheck(location):
        global hitomi_path
        if hitomi_path == 11:
            if location == "myhouse":
                return False
            else:
                return True
        elif hitomi_path == 15:
            if location == "street":
                return False
            else:
                return True

## TEMPLATE NOTIFCATION
# $ renpy.notify("New Objective: Meet Effie Outside her House at Night")
# $ renpy.notify("Current Balance: $[inventory.money]")
# $ renpy.notify("New Item Obtained: Fuck Bitches Pay Weekly Magazine")

# $ renpy.notify("Relationship with Character Increased")
# $ renpy.pause(1,hard=False)
# $ renpy.notify("Relationship with Character Increased by 2")

# $ renpy.notify("Your Charisma Points Increased")
# $ renpy.notify("Your Charisma Points Increased by 3")

# $ renpy.notify("You Used 3 Charisma Points")
# $ renpy.notify("You Lost 3 Charisma Points")
# $ renpy.notify("You Need 3 Charisma Points")

# $ renpy.notify("New Item Obtained: Fuck Bitches Pay Weekly Magazine")
# $ renpy.notify("Current Balance: $[inventory.money]")

## Sex World
# if insexworld == 1
## Not in Sex World
# if insexworld == 0
