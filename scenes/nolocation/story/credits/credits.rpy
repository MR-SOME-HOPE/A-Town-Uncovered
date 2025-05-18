## Credits
default credit_length = 0

label lbl_credits:
    $ credit_length = 60

    scene black
    show credits_scroll
    # centered "The End"
    # centered "Thank you for playing."
    
    # Force an autosave
    $ renpy.force_autosave()

    # Show the credits (you can customize this part)
    $ renpy.pause(credit_length, hard=True)  # Optional pause for a couple of seconds before transitioning

    # Send player to the main menu
    $ renpy.full_restart()

    return

image credits_scroll:
    Text([
        "{i}Game by{/i} \n \n"
        "GeeSeki \n \n \n \n \n"

        "{i}Story Lead{/i} \n \n"
        "GeeSeki \n \n \n \n \n"

        "{i}Dialogue Writer{/i} \n \n"
        "Robert Hawkins \n \n \n \n \n"

        "{i}Lead Artist{/i} \n \n"
        "GeeSeki \n \n \n \n \n"

        "{i}Art Assistance{/i} \n \n"
        "Smear \n"
        "Dexter \n"
        "Rivinca \n \n \n \n \n"

        "{i}Music by{/i} \n \n"
        "Marek Domagala \n"
        "Fealow \n \n \n \n \n"

        "{i}Coding Structure by{/i} \n \n"
        "Cipheos \n \n \n \n \n"

        "{i}Story Programmer{/i} \n \n"
        "Wabeesabi \n"
        "Epadder \n \n \n \n \n"

        "{i}QA Tester{/i} \n \n"
        "DarkMage \n \n \n \n \n"

        "{i}Built Using Ren'Py{/i} \n \n \n \n \n"

        "{i}Special Thanks:{/i} \n \n"
        "Dav, KIDD, Non, Cole, DX88, STDK, MDGE, UKPH, Andy, Maru, Selix, Fares, Rob C, \n"
        "Xana, Chris, Hefty, Mydus, Tadhg, Darkd, Matty, Smaug, Albert, What?, Chisps, \n"
        "Castor, Sampix, Nekoli, Gray85, Mcleod, Askard, Seraph, Misery, Bustin, Kakuga, \n"
        "Joseph, sfnc45, boof57, Z Payne, Lagoon, W00LLY, Jakaa9, Tarakis, Itiipau, Valen S., \n"
        "Cipheos, Rohoma, Neolust, Zurakci, Xalibur, Evillak, XIX XHIX, Roseguy, Burnsey, \n"
        "DrNearo, Nacario, MrMelon, Itchiesr, Nemo032, Wes8226, Allen Ray, Lancer86, Willtero, \n"
        "Koroshi1, Toneds80, Joepanda, Desertfox, Logbuilul, Annier34, Jonny Lee, Saulatear, \n"
        "Dusti_333, Kidd Video, Confuddle, Cereal Yum, Houa Yang, Epictoasta, Samwitch, \n"
        "jkornacki, Kindering, Spiderdadd, Driftdevil, Darkseid98, Roninaura, Frostiorca, \n"
        "Garlendolf, Devastator, Dunhill542, Rickyrich98, Mazterlith, Carter Otto, Racalan942, \n"
        "370HSSV123, Slayerfreak, Omni Omega, OG_Hazarrd, Purple Flare, Gdogger777, CruelKairos, \n"
        "Giantbacon, WallEWorld, Darththorn, Kingu Korin, Tigerknight, Cheesemasta, Austin Yang, \n"
        "The_Spegget, Alex Patreon, John Myer Jr, YandereKxng, TheGuardian, Masterglitch, \n"
        "Seymour Nuts, Travis Bowen, Devon Ramsey, Coldbluecrow, Fenryl Saylem, Acosmicotaku, \n"
        "ZacEfronFan3, SoulfulCobalt, GamerNerd247, Fabulous Aura, Eric Bollacker, Zach Johnson, \n"
        "Dark Wanderer, Sural Argnois, George's Chins, Jae Hyung Park, Moviebuff3000, \n"
        "Jeff 'Gray Fox' S., Distinktknopf, Aldo Longdong, Tahxickannoli, Jessica Nohava, \n"
        "Grimm Kurosaki, Cthuluplays21, Trucker_Guy257, Harry Fukogawa, MasterKenobi43, \n"
        "Jayden Sherman, Nightingale172, Jairo Palomares, Hallowed_Ghost, Crimsondeath45, \n"
        "Gabriel Withers, Whiskey-Fanatic, Biohazard Victim, Nightpopcorn456, Andrew J Pollara, \n"
        "Blackmageshadow, Shadow Lockheart, Thelastatalntian, MasteringTheBlaze, AzTheDemonIntern, \n"
        "Therealriasgremory, Dillion Washington, Georges Big Ol' Chins, TheKillerCreamCheese, \n"
        "Bruno Thought Leader, Bigbootydongerbanger\n \n \n"
        "And You\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n"
        "Thank you for loving A Town Uncovered \n \n \n \n \n \n \n"
        ], text_align=0.5
    )
    anchor (0.5, 0.0)
    pos (0.5, 1.0)
    linear credit_length ypos 0.0 yanchor 1.0
