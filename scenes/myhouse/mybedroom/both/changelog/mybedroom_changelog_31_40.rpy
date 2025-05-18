label lbl_mybedroompc_changelog_040:
    call screen scr_mybedroompc_changelog_040

screen scr_mybedroompc_changelog_040():
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
            text "Alpha 0.40a - The Infiltration Update" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Main story progress" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Spelling, grammar, italics fixes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added train station location" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added townhouse entrance location" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added forest safehouse interior location" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added office tasks minigames to Main Story" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added BG & CG asset for tour scene with Eloise" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added CG assets for quick reminder main story scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added CG assets for knockout news main story scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added forest safehouse exterior location" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Missus kitchen seatfun H-Scene (talk to her in kitchen after end of her side story)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Teghan female bathroom H-Scene (random encounter at Uni on Tuesday or Friday)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Lailah H-scene when you visit Jacob’s house during the day (random occurrence)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Updated Meghan female bathroom H-scene encounter rate (Uni on Monday or Thursday)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Updated researching CG asset" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Updated remaining menu screens with update UI assets" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed repeating scene at the office after the tour with Eloise" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Edward’s Tapes CG assets not final rendered" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Edward’s Scene in Truth Comes Out CG asset not included yet" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Alpha 0.40b" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Various Bug Fixes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text ""

label lbl_mybedroompc_changelog_039:
    call screen scr_mybedroompc_changelog_039

screen scr_mybedroompc_changelog_039():
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
            text "Alpha 0.39a - The Insight Update" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Updated UI elements" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Main story progress" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added main menu BGM" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added new office BGM" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added dev note on save and load page on how to delete save files" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added final email proofreading minigame assets" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added final copy machine minigame assets" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added missing remaining assets for movie threesome with Missus x Jane (H-scene)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Mc x Jane eating Effie out (H-scene, talk to Jane in the morning on a weekend)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Jane movie date" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Updated Miss Allaway objectives" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed incorrect sprite when asking Director Lashley out to the movies" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed coffee run office task not working" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed character name typo when hanging with Missus watching dramas" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed phone objective text that goes over the box" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Miss Allaway’s normal to casual wear sprite at the cafe" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed event not triggering in the alleyway in Director Lashley’s storyline" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed HUD not showing up during Missus x Jane x MC storyline" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Jane post-movie dream sequences not added" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Lashley post-movie dream sequences not added" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Some menu screens still use old design" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text ""

label lbl_mybedroompc_changelog_038:
    call screen scr_mybedroompc_changelog_038

screen scr_mybedroompc_changelog_038():
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
            text "Alpha 0.38a - The Red Ribbon Update" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Main Story Progress" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Updated More H-Scenes to new H-Scene Code Structure" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Office Copy Machine Mini-game" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Email Proofreading Mini-game" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Post Nut Clarity CG Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Lashley’s Eye 2 Eye Kiss CG" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Patron-voted H-Scene #1 (Missus x Jane x MC in Boxfort)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Patron-voted H-Scene #2 (Lashley visits you on a sunday after the 20th)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Lashley’s Bedroom Interior BG" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Eloise’s Office Location" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Office Supply Room Location" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Lashley Movie Dates" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Edward’s Actual VR Headset Mini-side story" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Townhouse button lighting bug" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Lashley’s Objective too long bug" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Alanna showing up when she’s on break bug" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Corner Store pushing you to the map bug" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Restaurant pushing you to the wrong map section bug" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Wabee Cheat Bug" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed and Clarified Some Objective Prompts" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Lashley Post-Movie Dream Sequences not added" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Office Copy Machine Mini-game Assets Temporary" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Email Proofreading Mini-game Assets Temporary" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Alpha 0.38b" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Minor Bug Fixes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text ""

label lbl_mybedroompc_changelog_037:
    call screen scr_mybedroompc_changelog_037

screen scr_mybedroompc_changelog_037():
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
            text "Alpha 0.37a - The Memory Update" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Updated the Rest of the H-Scene Code to Have it Loopable" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Main Story Progress" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Spelling and Grammar Fixes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Pre-Load Options for Lashley" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Mall Stores Interior Final Assets" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Night Version of Office Floor" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Remaining Sprite work for Lashley’s Side Story" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Lashley’s Hunger CG Scene & H-scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Psycho Breakdown CG Scene & H-scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Evie Character Sprite" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Evie Button in Eloise’s Lobby" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Updated Elevator Assets" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Lashley’s Post Nut Clarity CG Complete but not Fully Coded" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Zariah’s Party VIP Section H-Scene still need to be Rendered" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-2x Uptown Locations still need to be Rendered" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-2x Office Minigames Incomplete" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-2x Office Locations still need to be Rendered" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text ""

label lbl_mybedroompc_changelog_036:
    call screen scr_mybedroompc_changelog_036

screen scr_mybedroompc_changelog_036():
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
            text "Alpha 0.36a - The Drunk Update" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Completed Lashley’s Storyline" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Updated Some H-Scene Code to Have it Loopable" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added School Parking Lot BG for Lashley’s Story Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Safety and Home Life CG" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Lashley Drunk and Frisky Fingering H-Scenes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Lashley Drunk and Frisky BJ H-Scenes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Lashley Drunk and Frisky Cunnilingus H-Scenes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Lashley Drunk and Frisky Boobjob H-Scenes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Lashley Drunk and Frisky Post CG Assets" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Lashley Aftermath CG Assets" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Funky Teas CG Assets" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Character Button Assets for Zariah’s Party" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Dorothea Character for Zariah’s Party Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Spritework for Multiple Lashley Scenes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added and Fixed some lines for continuity" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-2x Uptown Locations still need to be Rendered" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Mall Stores Interior Final Assets Incomplete" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Lashley’s Hunger Scene CG Incomplete" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "Lashley’s Ending Scene CG Incomplete" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Alpha 0.36b" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Lashley End of Story Trigger" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed clashing story triggers between Jane and Director Lashley" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text ""

label lbl_mybedroompc_changelog_035:
    call screen scr_mybedroompc_changelog_035

screen scr_mybedroompc_changelog_035():
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
            text "Alpha 0.35a - The Church Update" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Spelling and Grammar Fixes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Minor Trigger Bug Fixes and Continuity Improvements." color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Lashley Story Progression (Incomplete)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Dusting Scene During the Naked Chores Punishment" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Mayor’s Estate BG Asset" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Motel BG Asset" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Lashley Mansion BG Asset" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Church Interior BG Asset" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added CG for Lashley’s Side Story ‘Allaway’s Happy Accident’" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added CG for Lashley’s Side Story ‘Natural Urges’" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added CG for Lashley’s Side Story ‘Distractions’" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added CG for Lashley’s Side Story ‘Trapped in the Stalls’" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added CG for Lashley’s Side Story ‘Secret Between Stalls’" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added CG for Lashley’s Side Story ‘Four Freaking Hours’" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Cole Throwaway Dialogue Spritework" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Luna Throwaway Dialogue Spritework" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Italic Action Dialogues" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-2x Uptown Locations still need to be Rendered" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Mall Stores Interior Final Assets Incomplete" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Lashley CG Scenes Rendered but not Coded" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Alpha 0.35b" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Text Cleanup" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed and Added Sprites in Office Elevator" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Violette Shocked Talking sprite" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed End of Main Story bug (end as of this version)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed repeating dialogue bug throughout game" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Lashley Church scene and can now be reachable" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Waking up alone scene after movie night threesome sprites and background" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed intersecting scene triggers in the Jane and Main Story" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Various Minor Bug Fixes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text ""

label lbl_mybedroompc_changelog_034:
    call screen scr_mybedroompc_changelog_034

screen scr_mybedroompc_changelog_034():
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
            text "Alpha 0.34a - The Outdoor Update" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Director Lashley Story Progression" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Updated the Up Town Map Day & Night Version" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Updated CG Scene of ‘Post-Breakfast News’" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Updated Police Station Exterior at Night Art" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Updated Office Building Exterior Map Asset and Background" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Updated Office Floor with Furnished Conference Room & Manager’s Office" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added ‘Cum Out’ Option for Hitomi at the Beach H-Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added CG Scene for You Can Freak Out Now Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added CG Scene for Bottoms Up Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added CG Scene for The Lashley Aftermath Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added CG Scene for Hints of a Problem Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added CG Scene for Distractions Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Dishes and Vacuum Scenes During the Naked Chores Punishment" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Music to the Nightclub and the Street at Night" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Lashley Manor’s in Uptown" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Office Conference Room Art" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Manager’s Office Art" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Office Bathroom Art" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Eloise’s Floor Lobby Art" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Abandoned Lot Art" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Cliff Art" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Forest Art" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Mine Entrance Art" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Corner Store Art" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Apartments Art" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Restaurant Art" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Church Art" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Graveyard Art" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Neighbour (Left) Art" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Neighbour (Right) Art" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Navigation Buttons for Street, Abandoned Lot, and Cinema Locations" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Navigation Buttons for Cafe and Corner Store" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Cole Throwaway Chat Dialogue" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Luna Throwaway Chat Dialogue" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Ambience Playing when leaving the Gym at Night" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Luna Throwaway Sprites not complete" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Cole Throwaway Sprites not complete" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Lashley Story Sprite Work To Be Done" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-4x Uptown Locations still need to be Rendered" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Mall Stores Interior Final Assets Incomplete" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Dusting Scene for Naked Chores Punishment Scene Incomplete" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text ""

label lbl_mybedroompc_changelog_033:
    call screen scr_mybedroompc_changelog_033

screen scr_mybedroompc_changelog_033():
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
            text "Alpha 0.33a - The Lobby Update" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Director Lashley Story Progression" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Updated & Rendered Uptown Map" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Updated University Cafeteria Assets" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Various Main Story CG Scenes have been Rendered & Added" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Sprite Work Added for Various Main Story Scenes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Rendered The Office Lobby" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Rendered The Office Elevator" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Rendered The Office Floor" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Office Lobby Counters" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added 3 New FBPW Magazines" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added ‘Be Right Back’ scene for getting getting a job to force people to speak to Grundle Sam" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Miss Allaway Button in School Cafeteria for her Side Story" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Gacha Machine at the Mall" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Gift Card Rack at the Retail Store" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added & Rendered Mowing and Cooking Scenes During the Naked Chores Punishment" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Lashley Manor still left for Uptown Map" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Lashley Story Sprite Work To Be Done" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Many Uptown Locations still need to be Rendered" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Conference Room & Manager’s Office Unrendered in Office Floor" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Store Interior Final Assets Incomplete" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Alpha 0.33b" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Fake ID Item (Can’t get it yet)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Updated Last Chapter (of this update) of Lashley’s Story (Dialogue Only)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Updated Alcohol Purchase at Mall so you need a Fake ID" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bugged Timejump Not Triggering Missus x Sis Story in Hallway" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Beach Naked Bug" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text ""

label lbl_mybedroompc_changelog_032:
    call screen scr_mybedroompc_changelog_032

screen scr_mybedroompc_changelog_032():
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
            text "Alpha 0.32a - The Uptown Update" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added an Uptown Area" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added 8 New Uptown Locations: Motel, Restaurant, Townhouses, Church, Mayor’s Estate, Graveyard, Forest, Cliff, Abandoned MInes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added 5 New Main Town Locations: Neighbour1, Neighbour 2, Corner Store, Apartments, Abandoned Lot" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added 9 New Office Interior Locations: Main Lobby, Elevator, Main Office Floor, Conference Room, Unisex Bathroom, Supply Room, Manager’s Office, Eloise’s Office, Eloise’s Floor Lobby" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added 8 New Office Characters: Carmen, Skylar, Corrine, Gloria, Kanako, Bradley, Howie, Mr Fistem" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Main Story Progression" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Spelling & Grammar Fixes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Sprites Added to Scenes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Input Box for Naming Characters" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Shopping Menu for Hendai’s Comic Book Store" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Shopping Menu for Grundle Sam’s Things & Stuff Store" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Minor Logic Fixes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Minor Scene Transition Improvements" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Uptown Map Incomplete" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Many Locations Still Need to be Rendered" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-New Main Story Content written but not coded in" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Store Interior Final Assets Incomplete" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Gift Cards and Gacha Items Unavailable" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Alpha 0.32b" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Early Missus x Jane x MC chapter triggers" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Alpha 0.32c" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+ACTUALLY Fixed Early Missus x Jane x MC chapter triggers" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text ""

label lbl_mybedroompc_changelog_031:
    call screen scr_mybedroompc_changelog_031

screen scr_mybedroompc_changelog_031():
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
            text "Alpha 0.31a - The Gift Giving Update" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Minor Main Story Progression" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Minor Logic Fixes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Spelling & Grammar Fixes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added New Area in the Mall" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Sprites for Pre Mission Briefing" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added New Section of the Mall" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Gift Giving System for 6 Characters" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Sound Effects for Map, Phone, Bag, and when you Sleep" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Fade Effect for Town Map" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added H-scene with Violette at the Beach" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added H-scene with Jane in the Bathroom" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added H-scene with Officer Mina at the Police Station" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Sprites for Hang at the Mall Now" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added 24 New Items" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Sprites to Some Main Story Scenes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Updated Special Thanks Credits into Code instead of an Image" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Updated and Added New Asset for Sister Bathroom Voyeur Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Updated Main Menu Options and Game Menu Options and Button Fonts" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Updated Natural Urges Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Error where Day Music continues to play at Night" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Sign at the University at Night" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed ‘Leave them be’ message from Missus x Jane storyline in the living room at night" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Endless Loop when doing Anal with Jane after participating in Camgurl Stream" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-New Main Story Content written but not coded in" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Store Interior Final Assets Incomplete" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Store Menus Final Assets Incomplete" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Gift Cards and Gacha Items Unavailable" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text ""
