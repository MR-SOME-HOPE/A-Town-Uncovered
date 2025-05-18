## Changelog - Changelog of the game ##
label lbl_mybedroompc_changelog:
    call screen scr_mybedroompc_changelog

screen scr_mybedroompc_changelog():
    add "img mybedroompc_blankwindow" align(0.5,0.407)
    imagebutton auto "btn mybedroompc_windowclose_%s" xpos 1784 ypos 89 focus_mask True action Jump("lbl_mybedroom_desk_1")
    vpgrid:
        cols 6
        xysize (1900, 832)
        draggable True
        mousewheel True
        scrollbars "vertical"
        # Since we have scrollbars, we have to position the side, rather
        # than the vpgrid proper.
        side_xalign 0.49
        side_yalign 0.49
        imagebutton auto "btn changelog_56_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_056")
        imagebutton auto "btn changelog_55_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_055")
        imagebutton auto "btn changelog_54_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_054")
        imagebutton auto "btn changelog_53_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_053")
        imagebutton auto "btn changelog_52_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_052")
        imagebutton auto "btn changelog_51_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_051")
        imagebutton auto "btn changelog_50_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_050")
        imagebutton auto "btn changelog_49_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_049")
        imagebutton auto "btn changelog_48_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_048")
        imagebutton auto "btn changelog_47_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_047")
        imagebutton auto "btn changelog_46_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_046")
        imagebutton auto "btn changelog_45_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_045")
        imagebutton auto "btn changelog_44_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_044")
        imagebutton auto "btn changelog_43_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_043")
        imagebutton auto "btn changelog_42_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_042")
        imagebutton auto "btn changelog_41_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_041")
        imagebutton auto "btn changelog_40_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_040")
        imagebutton auto "btn changelog_39_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_039")
        imagebutton auto "btn changelog_38_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_038")
        imagebutton auto "btn changelog_37_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_037")
        imagebutton auto "btn changelog_36_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_036")
        imagebutton auto "btn changelog_35_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_035")
        imagebutton auto "btn changelog_34_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_034")
        imagebutton auto "btn changelog_33_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_033")
        imagebutton auto "btn changelog_32_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_032")
        imagebutton auto "btn changelog_31_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_031")
        imagebutton auto "btn changelog_30_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_030")
        imagebutton auto "btn changelog_29_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_029")
        imagebutton auto "btn changelog_28_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_028")
        imagebutton auto "btn changelog_27_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_027")
        imagebutton auto "btn changelog_26_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_026")
        imagebutton auto "btn changelog_25_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_025")
        imagebutton auto "btn changelog_24_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_024")
        imagebutton auto "btn changelog_23_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_023")
        imagebutton auto "btn changelog_22_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_022")
        imagebutton auto "btn changelog_21_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_021")
        imagebutton auto "btn changelog_20_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_020")
        imagebutton auto "btn changelog_19_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_019")
        imagebutton auto "btn changelog_18_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_018")
        imagebutton auto "btn changelog_17_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_017")
        imagebutton auto "btn changelog_16_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_016")
        imagebutton auto "btn changelog_15_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_015")
        imagebutton auto "btn changelog_14_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_014")
        imagebutton auto "btn changelog_13_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_013")
        imagebutton auto "btn changelog_12_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_012")
        imagebutton auto "btn changelog_11_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_011")
        imagebutton auto "btn changelog_10_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_010")
        imagebutton auto "btn changelog_09_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_009")
        imagebutton auto "btn changelog_08_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_008")
        imagebutton auto "btn changelog_07_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_007")
        imagebutton auto "btn changelog_06_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_006")
        imagebutton auto "btn changelog_05_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_005")
        imagebutton auto "btn changelog_04_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_004")
        imagebutton auto "btn changelog_03_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_003")
        imagebutton auto "btn changelog_02_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_002")
        imagebutton auto "btn changelog_01_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroompc_changelog_001")


label lbl_mybedroompc_changelog_056:
    call screen scr_mybedroompc_changelog_056

screen scr_mybedroompc_changelog_056():
    add "img mybedroompc_blankwindow" align(0.5,0.407)
    imagebutton auto "btn mybedroompc_windowclose_%s" xpos 1784 ypos 89 focus_mask True action Jump("lbl_mybedroom_desk_1")
    viewport:
        xysize (1600, 835)
        draggable True
        mousewheel True
        scrollbars "vertical"
        xanchor 1.0
        yanchor 0.5
        xalign 0.949
        yalign 0.498
        vbox spacing 10 xanchor 1.0 xalign 1.0 xmaximum 1500:
            text ""
            text "Version 1.0 - The Full Update" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Completed and polished the game." color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Version 1.01" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Missus' VR Headset Icon opening up Effie's page instead bug" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed 'in construction' areas (discontinued content)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed entering transition for some locations" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Version 1.02" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Effie chapter 17 bug that sends the main story back to chapter 18" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed 'Drunk and Frisky Oral' bug with Lashley" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Main Story only showing 'next' and 'back' bug" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Version 1.03" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Receptions at Office sending you to the beach change rooms." color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Miss Allaway showing up instead of Dean Lashley when going on a movie date." color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Hitomi's Frisbee beach scene bug where if you successfully caught the frisbee, you'd still bump into her." color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed taking Jane to the movies sends you to the beach changerooms." color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed various 'Dev Note' sections." color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Version 1.04" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed pathing when choosing to 'sacrifice yourself' instead of Effie during Main Story." color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text ""


label lbl_mybedroompc_changelog_055:
    call screen scr_mybedroompc_changelog_055

screen scr_mybedroompc_changelog_055():
    add "img mybedroompc_blankwindow" align(0.5,0.407)
    imagebutton auto "btn mybedroompc_windowclose_%s" xpos 1784 ypos 89 focus_mask True action Jump("lbl_mybedroom_desk_1")
    viewport:
        xysize (1600, 835)
        draggable True
        mousewheel True
        scrollbars "vertical"
        xanchor 1.0
        yanchor 0.5
        xalign 0.949
        yalign 0.498
        vbox spacing 10 xanchor 1.0 xalign 1.0 xmaximum 1500:
            text ""
            text "Alpha 0.55a - The Finalizing Update" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added BJ H-scene for Hitomi's storyline" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Cunninglingus H-scene for Hitomi's storyline" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Spooning H-scene for Hitomi's storyline" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added CG for 'Confessions Over A Recording' chapter in Hitomi's storyline" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added CG for 'Lifeguard Training' chapter in Violette's stoyline" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added CG for 'Unexpected Crisis' chapter in Violette's stoyline" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added CG for 'Love in the Spotlight' chapter in Violette's stoyline" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added CG for 'Ara Asika' chapter in Violette's stoyline" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added CG for 'Close To You Like This' chapter in Effie's stoyline" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added CG for 'Dateish Night' chapter in Effie's stoyline" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added BG for 'Artistic Expression' chapter in Effie's stoyline" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added BG for 'Beach Party Prelude' chapter in Effie's stoyline" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Updated 'The Polaroid' CG" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text ""

label lbl_mybedroompc_changelog_054:
    call screen scr_mybedroompc_changelog_054

screen scr_mybedroompc_changelog_054():
    add "img mybedroompc_blankwindow" align(0.5,0.407)
    imagebutton auto "btn mybedroompc_windowclose_%s" xpos 1784 ypos 89 focus_mask True action Jump("lbl_mybedroom_desk_1")
    viewport:
        xysize (1600, 835)
        draggable True
        mousewheel True
        scrollbars "vertical"
        xanchor 1.0
        yanchor 0.5
        xalign 0.949
        yalign 0.498
        vbox spacing 10 xanchor 1.0 xalign 1.0 xmaximum 1500:
            text ""
            text "Alpha 0.54a - The Main Story Rework Update" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Updated and reworked Main Story to condense Act 3 into 15 chapters."
            text "+Fixed creating a new save marks it as an old version save" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Violette beach chapter bug" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed various minor bugs" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text ""

label lbl_mybedroompc_changelog_053:
    call screen scr_mybedroompc_changelog_053

screen scr_mybedroompc_changelog_053():
    add "img mybedroompc_blankwindow" align(0.5,0.407)
    imagebutton auto "btn mybedroompc_windowclose_%s" xpos 1784 ypos 89 focus_mask True action Jump("lbl_mybedroom_desk_1")
    viewport:
        xysize (1600, 835)
        draggable True
        mousewheel True
        scrollbars "vertical"
        xanchor 1.0
        yanchor 0.5
        xalign 0.949
        yalign 0.498
        vbox spacing 10 xanchor 1.0 xalign 1.0 xmaximum 1500:
            text ""
            text "Alpha 0.53a - The House Fun Update" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Missus x Jane x MC H-scene in the Living Room (Talk to Missus in the living room in the afternoon)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Missus x Jane x MC H-scene in Missus' bedroom (Talk to Missus in the kitchen in the morning)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Missus x Jane x MC H-scene in your bedroom (Talk to Missus in her bedroom in the evening)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added developer message & link to Sugar Service trailer on the in-game PC" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Violette 'Love in the spotlight' bug" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed various minor bugs" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text ""

label lbl_mybedroompc_changelog_052:
    call screen scr_mybedroompc_changelog_052

screen scr_mybedroompc_changelog_052():
    add "img mybedroompc_blankwindow" align(0.5,0.407)
    imagebutton auto "btn mybedroompc_windowclose_%s" xpos 1784 ypos 89 focus_mask True action Jump("lbl_mybedroom_desk_1")
    viewport:
        xysize (1600, 835)
        draggable True
        mousewheel True
        scrollbars "vertical"
        xanchor 1.0
        yanchor 0.5
        xalign 0.949
        yalign 0.498
        vbox spacing 10 xanchor 1.0 xalign 1.0 xmaximum 1500:
            text ""
            text "Alpha 0.52a - The Clean Up Update" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added More of Hitomi's Story Scenes CG Polish" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Hitomi Story H-Scene #1 (Counter Cunnilingus - Ending)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Hitomi Story H-Scene #2 (Entrance Doggy - Ending)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added More of Violette's Story Scenes CG Polish" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Spritework for Violette Story Scenes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Violette Story H-Scene #1 (Ara Asika Full Nelson)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Hitomi Chapter Skips Director Lashley instead of Hitomi Bug" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Violette storyline" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Effie Couch on Phone H-scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Main Story Chapter 133 Bug" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed crashing bug after choosing to sacrifice Effie or yourself" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Attempted to fix various bugs, can't recreate, find, or the report wasn't specific enough." color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text ""

label lbl_mybedroompc_changelog_051:
    call screen scr_mybedroompc_changelog_051

screen scr_mybedroompc_changelog_051():
    add "img mybedroompc_blankwindow" align(0.5,0.407)
    imagebutton auto "btn mybedroompc_windowclose_%s" xpos 1784 ypos 89 focus_mask True action Jump("lbl_mybedroom_desk_1")
    viewport:
        xysize (1600, 835)
        draggable True
        mousewheel True
        scrollbars "vertical"
        xanchor 1.0
        yanchor 0.5
        xalign 0.949
        yalign 0.498
        vbox spacing 10 xanchor 1.0 xalign 1.0 xmaximum 1500:
            text ""
            text "Alpha 0.51a - The Camping Day 2 Update" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Day 2 of Missus x Jane x MC Camping Story" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Story H-Scene #1 (Naked Yoga with Missus)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Story H-Scene #2 (Creek Fuck with Jane)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Story H-Scene #3 (Reverse Cowgirl with Missus)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Story H-Scene #4 (Backseat Car Fucking with Jane)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Various Bug Fixes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Alpha 0.51b" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Jane Lockpick Bug" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed GUI for Android version" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Violette storyline" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Anatomy Book bugs" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Missus x Jane Boxfort H-scene bug" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Effie Couch H-scene bug" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Various minor bug fixes and quality of life improvements" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text ""

label lbl_mybedroompc_changelog_050:
    call screen scr_mybedroompc_changelog_050

screen scr_mybedroompc_changelog_050():
    add "img mybedroompc_blankwindow" align(0.5,0.407)
    imagebutton auto "btn mybedroompc_windowclose_%s" xpos 1784 ypos 89 focus_mask True action Jump("lbl_mybedroom_desk_1")
    viewport:
        xysize (1600, 835)
        draggable True
        mousewheel True
        scrollbars "vertical"
        xanchor 1.0
        yanchor 0.5
        xalign 0.949
        yalign 0.498
        vbox spacing 10 xanchor 1.0 xalign 1.0 xmaximum 1500:
            text ""
            text "Alpha 0.50a - The Camping Day 1 Update" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Day 1 of Missus x Jane x MC Camping Story" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Story H-Scene #1 (Natural Spring Handjobs & Fingering)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Story H-Scene #2 (Meadow Cock Worship)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Story H-Scene #3 (Cuddlefucking)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text ""


label lbl_mybedroompc_changelog_049:
    call screen scr_mybedroompc_changelog_049

screen scr_mybedroompc_changelog_049():
    add "img mybedroompc_blankwindow" align(0.5,0.407)
    imagebutton auto "btn mybedroompc_windowclose_%s" xpos 1784 ypos 89 focus_mask True action Jump("lbl_mybedroom_desk_1")
    viewport:
        xysize (1600, 835)
        draggable True
        mousewheel True
        scrollbars "vertical"
        xanchor 1.0
        yanchor 0.5
        xalign 0.949
        yalign 0.498
        vbox spacing 10 xanchor 1.0 xalign 1.0 xmaximum 1500:
            text ""
            text "Alpha 0.49a - The Violette Update" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Violette Complete Story" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Violette Story H-Scene #1 (BJ Behind the Rocks)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Violette Story H-Scene #2 (69 Behind the Rocks)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Violette Story H-Scene #3 (Reverse Cowgirl)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Violette Story H-Scene #4 (Mating Press)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Violette Story H-Scene #4 (Arched Doggy)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Some Violette Story Temp CG Assets" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Lots of Main Story Temp CG Assets Missing" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text ""


label lbl_mybedroompc_changelog_048:
    call screen scr_mybedroompc_changelog_048

screen scr_mybedroompc_changelog_048():
    add "img mybedroompc_blankwindow" align(0.5,0.407)
    imagebutton auto "btn mybedroompc_windowclose_%s" xpos 1784 ypos 89 focus_mask True action Jump("lbl_mybedroom_desk_1")
    viewport:
        xysize (1600, 835)
        draggable True
        mousewheel True
        scrollbars "vertical"
        xanchor 1.0
        yanchor 0.5
        xalign 0.949
        yalign 0.498
        vbox spacing 10 xanchor 1.0 xalign 1.0 xmaximum 1500:
            text ""
            text "Alpha 0.48a - The Effie Update" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Effie Story Progression (20 chapters, 5 chapters left)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Effie H-Scene #1 (Handjob at Park during Story)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Effie H-Scene #2 (Cowgirl on her Bed during Story)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Effie H-Scene #3 (POV Doggy in Living Room during Story)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Effie H-Scene #4 (Lotus at Park during Story)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Some Effie Story Temp CG Assets" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Lots of Main Story Temp CG Assets Missing" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text ""


label lbl_mybedroompc_changelog_047:
    call screen scr_mybedroompc_changelog_047

screen scr_mybedroompc_changelog_047():
    add "img mybedroompc_blankwindow" align(0.5,0.407)
    imagebutton auto "btn mybedroompc_windowclose_%s" xpos 1784 ypos 89 focus_mask True action Jump("lbl_mybedroom_desk_1")
    viewport:
        xysize (1600, 835)
        draggable True
        mousewheel True
        scrollbars "vertical"
        xanchor 1.0
        yanchor 0.5
        xalign 0.949
        yalign 0.498
        vbox spacing 10 xanchor 1.0 xalign 1.0 xmaximum 1500:
            text ""
            text "Alpha 0.47a - The Conclusion Update" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Main Story Progression (45+ chapters, 5 chapters left)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Cult Mask, Cloak & BDSM Sprites for MC" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Cult Mask, Cloak & BDSM Sprites for Effie" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Nude & Cult Mask, Cloak & BDSM Sprites for Cole" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Nude & Cult Mask, Cloak & BDSM Sprites for Jacob" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Nude & Cult Mask, Cloak & BDSM Sprites for Edward" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Regular World Sprites for Nurse Hollick" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Assaulted Sprites for Lashley" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Sprites for Master Buukakki" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added sprite work for all previous main story scenes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Action Video Game Gift Item" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Dating Sim Video Game Gift Item" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Shooter Video Game Gift Item" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Chocolate Box Gift Item" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Box of BDSM Gear Item" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Lots of Temp CG Assets" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Lots of Temp CG Assets Missing (Focusing on writing and completing the main story)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text ""

label lbl_mybedroompc_changelog_046:
    call screen scr_mybedroompc_changelog_046

screen scr_mybedroompc_changelog_046():
    add "img mybedroompc_blankwindow" align(0.5,0.407)
    imagebutton auto "btn mybedroompc_windowclose_%s" xpos 1784 ypos 89 focus_mask True action Jump("lbl_mybedroom_desk_1")
    viewport:
        xysize (1600, 835)
        draggable True
        mousewheel True
        scrollbars "vertical"
        xanchor 1.0
        yanchor 0.5
        xalign 0.949
        yalign 0.498
        vbox spacing 10 xanchor 1.0 xalign 1.0 xmaximum 1500:
            text ""
            text "Alpha 0.46a - The Second Visit Update" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Main Story Progression (24+ chapters)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added sprite work for all previous main story scenes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Lots of Temp CG Assets (Focusing on writing and completing the main story)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text ""


label lbl_mybedroompc_changelog_045:
    call screen scr_mybedroompc_changelog_045

screen scr_mybedroompc_changelog_045():
    add "img mybedroompc_blankwindow" align(0.5,0.407)
    imagebutton auto "btn mybedroompc_windowclose_%s" xpos 1784 ypos 89 focus_mask True action Jump("lbl_mybedroom_desk_1")
    viewport:
        xysize (1600, 835)
        draggable True
        mousewheel True
        scrollbars "vertical"
        # Since we have scrollbars, we have to position the side, rather
        # than the vpgrid proper.
        xanchor 1.0
        yanchor 0.5
        xalign 0.949
        yalign 0.498
        vbox spacing 10 xanchor 1.0 xalign 1.0 xmaximum 1500:
            text ""
            text "Alpha 0.45a - The Main Progression Update" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Spelling and grammar updates" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Main Story Progression" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added sprite work for various main story scenes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added sprite work for Luna’s throwaway dialogue" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added some triggers to some events for the time travel feature" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added noses to MC and Jane during household dinner scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Drunk Girl character sprite" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Updated Mall stores button with final asset" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Updated Office Elevator location asset" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Updated Investigation Scene with Violette so MC is nude" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Updated MC assets when meeting Jacob behind Beach rocks" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Drunk Girl character dialogue code" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Edward not leaving scene when discussing cameras" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Main Story triggers when loading a preset save" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Removed Edward’s sprite from Office scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Lots of Temp CG Assets (Focusing on writing and completing the main story)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text ""


label lbl_mybedroompc_changelog_044:
    call screen scr_mybedroompc_changelog_044

screen scr_mybedroompc_changelog_044():
    add "img mybedroompc_blankwindow" align(0.5,0.407)
    imagebutton auto "btn mybedroompc_windowclose_%s" xpos 1784 ypos 89 focus_mask True action Jump("lbl_mybedroom_desk_1")
    viewport:
        xysize (1600, 835)
        draggable True
        mousewheel True
        scrollbars "vertical"
        # Since we have scrollbars, we have to position the side, rather
        # than the vpgrid proper.
        xanchor 1.0
        yanchor 0.5
        xalign 0.949
        yalign 0.498
        vbox spacing 10 xanchor 1.0 xalign 1.0 xmaximum 1500:
            text ""
            text "Alpha 0.44a - The Hitomi Update" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Hitomi Story Complete" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added most Hitomi Story sprite work" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Effie H-Scene (Hitomi’s Story)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Hitomi H-Scene (VIP Heart To Heart)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Hitomi H-Scene (Comic Book Backroom Press)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed missing trigger for Hitomi Story" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Replaced temp assets for Missus x Jane x MC chores scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Some Hitomi CG Not Yet Complete" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Drunk Girl Sprite Incomplete" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Alpha 0.44b - The Hitomi Update" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed HD Camera Bug" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text ""

label lbl_mybedroompc_changelog_043:
    call screen scr_mybedroompc_changelog_043

screen scr_mybedroompc_changelog_043():
    add "img mybedroompc_blankwindow" align(0.5,0.407)
    imagebutton auto "btn mybedroompc_windowclose_%s" xpos 1784 ypos 89 focus_mask True action Jump("lbl_mybedroom_desk_1")
    viewport:
        xysize (1600, 835)
        draggable True
        mousewheel True
        scrollbars "vertical"
        # Since we have scrollbars, we have to position the side, rather
        # than the vpgrid proper.
        xanchor 1.0
        yanchor 0.5
        xalign 0.949
        yalign 0.498
        vbox spacing 10 xanchor 1.0 xalign 1.0 xmaximum 1500:
            text ""
            text "Alpha 0.43a - The Breakfast Update" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Hitomi side story progression (7 Scenes)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Missus under the dining table trio H-Scene (Dining Room Morning on Saturday)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Lashley bent over desk (Lashley Office on Weekday)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Luna doggy bedroom (Talk to Luna in the School Hallway 2)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed various minor bug fixes and optimization" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Alpha 0.43b" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed missing missus under the dining table trio bug" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text ""

label lbl_mybedroompc_changelog_042:
    call screen scr_mybedroompc_changelog_042

screen scr_mybedroompc_changelog_042():
    add "img mybedroompc_blankwindow" align(0.5,0.407)
    imagebutton auto "btn mybedroompc_windowclose_%s" xpos 1784 ypos 89 focus_mask True action Jump("lbl_mybedroom_desk_1")
    viewport:
        xysize (1600, 835)
        draggable True
        mousewheel True
        scrollbars "vertical"
        # Since we have scrollbars, we have to position the side, rather
        # than the vpgrid proper.
        xanchor 1.0
        yanchor 0.5
        xalign 0.949
        yalign 0.498
        vbox spacing 10 xanchor 1.0 xalign 1.0 xmaximum 1500:
            text ""
            text "Alpha 0.42a - The Modelling Update" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Hitomi side story progression" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added night assets for Office Lobby" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added ‘How to Model Effectively for Aritst’ in ‘For Idiots’ section on PC" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added ‘Drawing Anatomy’ item for Hitomi’s Story" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added sprite work for various scenes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added CG scene for ‘Warehouse Foreshadowing’ main story scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added H-scene ‘Missus Mating Press’ (talk to Missus after completing her side story)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added H-scene ‘Janae Plowed Over Boxes’ (talk to Janae at the retail store)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added H-scene ‘Hazel Backroom Cowgirl’ (talk to Hazel at the adult store)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Updated Mall background with updated assets" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed mis-trigger bug with Jane’s storyline in the hallway at night" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed various minor bug fixes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Alpha 0.42b" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed inventory bug" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed minor bugs" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text ""

label lbl_mybedroompc_changelog_041:
    call screen scr_mybedroompc_changelog_041

screen scr_mybedroompc_changelog_041():
    add "img mybedroompc_blankwindow" align(0.5,0.407)
    imagebutton auto "btn mybedroompc_windowclose_%s" xpos 1784 ypos 89 focus_mask True action Jump("lbl_mybedroom_desk_1")
    viewport:
        xysize (1600, 835)
        draggable True
        mousewheel True
        scrollbars "vertical"
        # Since we have scrollbars, we have to position the side, rather
        # than the vpgrid proper.
        xanchor 1.0
        yanchor 0.5
        xalign 0.949
        yalign 0.498
        vbox spacing 10 xanchor 1.0 xalign 1.0 xmaximum 1500:
            text ""
            text "Alpha 0.41a - The Chase Update" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Main Story Progression" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Hitomi Side Story" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Zariah DJ Booth Sprite" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Edward’s Tapes CG Assets" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Zariah Reverse Seated Cowgirl H-Scene at the Nightclub (Talk to her at nightclub)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Missus Standing Shower H-Scene (Go in when finding her taking a shower)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Effie Couch H-Scene (Visit her on a Saturday morning)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added ability to assign Mr Smith’s role individually" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added spritework to Main Story" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed BG asset for Eloise’s lobby assistant" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed email mini-game’s vertical alignment" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed copy machine mini-game being marked as coffee run being complete" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Various other minor bug fixes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-End of main story assets not added in" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Alpha 0.41b" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Disabled Email Minigame for the Office" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Coffee Run Minigame Bug" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "NOTE: If you're still getting the email bug, replay the minigame but fail it on purpose as the bug only occurs when you succeed." color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Alpha 0.41c" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Missus & Jane preset load options" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed some item bugs in the mall" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed some main story triggers" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed soft lock where you can’t make coffee orders while Effie is out of action taking care of Jane" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed intersecting trigger bugs with fort being destroyed and Missus wanting ice cream" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Other minor continuity bug fixes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Temporary ‘Drawing Anatomy’ Book asset is a ‘Kids Wholey Bible’ at Mockingjay’s" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Temporary ‘Model for Idiots’ asset is ‘Lockpicking for Idiots’ on the PC" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Some Hitomi scenes don’t have sprite work yet" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text ""
