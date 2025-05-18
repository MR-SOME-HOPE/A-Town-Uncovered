label lbl_mybedroompc_changelog_010:
    call screen scr_mybedroompc_changelog_010

screen scr_mybedroompc_changelog_010():
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
            text "Alpha 0.10a – The Teddy Bear Update" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Code Restructuring and Optimization" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Mom Progression" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added 2 Minor Characters (Usher and Waiter)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added 3 New Sprites (Formal MC, Formal Mom, and Casual Mom)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added 4 Locations (Frontyard, Backyard, Dining Room, Cinema)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added 9 Quest Items (4x Icecreams, 3 bears, Smart TV Box, and a Suit)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Toggle-able Store Counters" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Retail Store Customers" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Another Retail Store Section" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Crowd to the Street at night" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added 3 Changeroom Gloryhole Attendees (Lillian, Nurse Hollick and Miss Allaway)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added 1 Character Event Behind the Rocks" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Appropriate Furniture at Girl at the Door Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Appropriate Furniture at Mom Fallen Asleep Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Appropriate Furniture at Save Mom from Dad Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added New Team Members in Credits" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Improved Gloryhole BJ Length" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Improved 2 Locations (Sister's Room & Living Room)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Improved Brock's Sprite" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Improved Wake Up [sister] Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Improved Bathroom Voyeur Scenes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Living Room button in Kitchen to match updated Living Room" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Fence and Sky colours outside the Kitchen Window to match the backyard" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed some Grammar and Spelling" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Mother Dinner Scene's CG is not complete" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Clothing Area of Retail Store not added" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Achievements Phone Tab not working" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Alpha 0.10b" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Button navigating from Kitchen to Dining Room" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Updated Mom's Side Story" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Card Playing Table Bug" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Wall Button in Bathroom when spying on Mom and Sister" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bug where nothing happens after giving Mom a Teddy Bear" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Lillian BJ Gloryhold Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Nurse Hollick BJ Gloryhole Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Buying a Suit from Janae Bug" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Price and Button placement in the Retail Store Section" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Some Alanna Sprites when buying icecream from her" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed and Improved Cheer Mom Up Dialogue" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bath H-Scene with Mom" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Got rid of wrong End of Mom Story Message" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Got rid of Mom in the shower and kitchen while she's supposed to be in her room" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Got rid of Mom shown in the livingroom at night on the first Tuesday when she's not there" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-If you reload the game, the game won't detect the quest items you bought" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Cum Button in the bath scene with mom doesn't work" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-In the sex world, the Street BG changes from Sexworld to Regular world BG" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Innacurate End of Mom Story Messages" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Can't Buy Smart TV Box" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Buying Icecream at Icecreampy doesnt have Icecreampy Background" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Black Screen when Telling mom the Smart TV Box won't cost her" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Alpha 0.10c" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Remaining Art for Dinner Date scene with Mom" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Icecreampy Background when buying Icecream for Mom" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bug where Game couldn't detect items when the game is reloaded" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Can't Buy Smart TV Box Bug" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Black Screen when Telling mom the Smart TV Box won't cost her" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bath with Mom Cum Button" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Street Background in the Sex World" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Got rid of Inaccurate End of Mom Story Messages" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Going to the cinema at night crashes the game" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Bar and VIP section of the club crashes the game" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Bill during the Dinner Date scene only flashes for a split second" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Lillian in the Gloryhole goes into an endless loop" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text ""

label lbl_mybedroompc_changelog_009:
    call screen scr_mybedroompc_changelog_009

screen scr_mybedroompc_changelog_009():
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
            text "Alpha 0.09a – The Violent Update" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Main Story Progression" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Mom Side Story Progression" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added 2 New Characters (One unnamed)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added 3 Gloryhole Participants" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added 3 Changeroom Participants" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Locations (School Cafeteria)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Jack Bumping into MC Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Functional Objectives Tab in the phone for Main story and Side story" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Xray Option" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Xray and Cum Inside Sequence for Skinny Dipping Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Completed Location (Hallway 2)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Improved MC's Bedroom" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Improved Quit Screen Patreon Girl" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Improved Changeroom Randomized Attendees" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Mom Side Story Triggering in Livingroom after accepting text from Effie" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Achievement Tab in phone is not usable" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Retail Store Customers not added" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Hitomi Gangbang Scenes CG not added" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Hitomi's Changeroom CG not added" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Changeroom Bugs" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Mom Side Story Trigger Bug" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Alpha 0.09b" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Effie Gloryhole Scene Bug" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Night Changeroom Bug" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Changeroom in the Sex World Bug" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Mom's Side Story Trigger Bug" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Alpha 0.09c" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Major Mom Side Story Fix" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Add Counters in front of sprites" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Mom's Phone Objectives" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Violette Randomly Appearing after Main Story" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Changeroom Emptiness Bug After Mainstory Ends" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Hitomi (Not Available #2) Side Story Objectives on Phone Bug" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Got rid of incorrect Mom Story End Message" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Alpha 0.09d" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Some Grammar and Spelling Fixes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed and Improved Mom and MC's argument scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Hitomi's Phone Objective Section Bug" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bug where you can see Mom in the livingroom from the kitchen but isn't actually there when you have accepted Effie's Park Invitation via Text" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed undefined variable bug that determines what mom says before she goes to bed with you" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bedroom at night after sleeping after having a fight with mom bug" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Made a morning transition after mom's story ends in bed" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Made Bumping into Jack an afternoon event as Miss Lashley is “going for lunch”" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Made Effie's Text to you appear only once a night for as long as you decline" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Got rid of [sister] in the shower even when she said she's off to work after coming back from Effie's" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Got rid of ability to go out of the house before your conversation with mom after your cuddling session the night before" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text ""

label lbl_mybedroompc_changelog_008:
    call screen scr_mybedroompc_changelog_008

screen scr_mybedroompc_changelog_008():
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
            text "Alpha 0.08a – The Cradle Update" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Mom Side Story Progression" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Mom visible in the living room from the Kitchen at Night when watching TV" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Hospital Room BG" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Parents Room" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Quest Item" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Choices for Hitomi Gangbang Scene in the Sex World" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Ability to work at Ice Creampy" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Nurse Hollick Contact" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Retail Store" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Electronics Cabinet at Retail Store" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Crowd to the Mall" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added 2 Glory Hole Scenes at the beach" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added New Character" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Icecream'py Background to Alanna's Conversation" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added screen shake in some areas" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Improved Mother in the Kitchen Button" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Improved Mother Drama Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Improved and Updated the Phone GUI" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Improved and Readjusted the size of Ice Creampy and the railing at the Mall" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Dialogue Italics" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Skill Success Percentage Rate" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Made Hitomi Gangbang not compulsory to forward the story" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Objective and Achievement Tab in phone is not usable" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Retail Store Customers not added" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Hitomi Gangbang Scenes CG not added" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Jack bumping into MC CG not added" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Hitomi's Changeroom CG not added" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Alpha 0.08b" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Minor Bug Fixes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Mom and Sister's Bathroom Schedule Bug" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Amount of money you make with two shifts" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Updated Quit Screen Credits" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text ""

label lbl_mybedroompc_changelog_007:
    call screen scr_mybedroompc_changelog_007

screen scr_mybedroompc_changelog_007():
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
            text "Alpha 0.07a – The Sex World Update" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Main Story Progression" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Minor Mom Story Progression" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added New Location: Hospital Room" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added New Character: Nurse Hollick" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added 2 Softcore H-scenes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Behind the Rocks at the Beach at Night" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Notification about Points Needed in Hitomi Conversation at the Beach" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Point Notification for the Skinny Dipping Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added SexWorld Versions of Locations: (Beach & Comic Book Store are empty), Café, Schoolyard, Park, School Hallway 1, and Classroom)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Shocked Sprites for MC, Mom, and Effie" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Effie appearing at the Café in the Morning bug" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Mom in the Kitchen while in the Bathroom bug" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Random Number showing up Behind the Rocks" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Skill Activity Reset when sleeping with Effie bug" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Clothed MC during Naked Hitomi Conversation at the Beach" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Clothed Hitomi Conversation occurring at the Beach after getting naked in the Change rooms" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Parents' Room triggering Sister's Room after Mom's Drama Conversation" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Wrong Skill Point Notification when Increasing Charisma Skill" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Students at Schoolyard on the Weekends" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Reoccurring Hitomi Conversation at the Beach after passing it the first time" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed All Beach Changerooms at Night goes to Red when Violette hasn't been met yet and her changeroom attendance is triggered" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Changed/Improved the Skill Upgrading Mechanic" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Disabled Maps in some areas for a pipeline play through instead of accidentally skipping important scenes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Violette in the Change rooms at night only occur after you've met her during the day" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Skinny Dipping Scene not complete" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-The Mysterious Figure and Drowning Scene not complete" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Violette Saving You and Hospital Checkup Scene not complete" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Alpha 0.07b" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added New Changeroom Attendee" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Miss Allaway Optional Conversation in Sexyverse" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Completed Mysterious Figure at the Park Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Completed Violette Saving You Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Completed Text from Effie Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Completed Skinny Dipping Scene at the Beach" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Completed Hospital Check-up Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Completed Drowning Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Sister's Room at night triggering the day cycle with a NaN time bug" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Effie's Text triggering on a Friday or a Saturday (because the required school scene the next day would've ended up on a weekend)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Skill Upgrading System" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Sprites, Notifications, Font Style" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Removed Mom's Bathroom Scene on a Wednesday Morning after the Hospital Scene (because she's present in the kitchen)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Removed Sister's Bathroom Scene on a Tuesday and Friday Morning after the Hospital Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Improved Hitomi's Beach Conversation" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Improved Skinny Dipping Scene at the Beach and added an Easter Egg" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Figure at the door after Mom and MC last conversation in main story not added" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Hospital Room Background not added" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Hitomi's Changeroom CG not added" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Jack bumping into MC CG not added" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Nurse Hollick phone contact not added" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text ""

label lbl_mybedroompc_changelog_006:
    call screen scr_mybedroompc_changelog_006

screen scr_mybedroompc_changelog_006():
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
            text "Alpha 0.06a – The Exploration Update" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Background People in 5 Locations (Café, Classroom, School Hallway 1, Comic Book Store, Park, School Yard, Street)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Popup Notifications" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added New Intro Sequence" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added [sister] in Bathroom Sequence" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Mother in Bathroom Sequence" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added More Hitomi Side Story as a Random Event at the Beach" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Random Encounter with Effie at the Mall" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Random Encounter with Violette at the Park at Night" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Random Encounter with Jacob in the School Hallway 2" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Random Encounter with Miss Allaway in the School Hallway 1" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Violette as a Changeroom Attendee" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Fades to Naps and Sleeps" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Fuck Bitches Pay Weekly Magazine Item" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Sequence so the player can only go home after Effie's H-Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed and Improved Dialogue and Sequences to fit with the New Story" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Italicized All Main Character's Thoughts" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Improved Sister's Wake Up Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Improve Sprites for ALL Characters" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Completed the Comic Book Store" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Completed the Café Interior" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-There's a bug with Item and Money disappearing when game is refreshed" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-There's a bug with the Park at Night where the RNG doesn't work so Violette shows up 100% of the time" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Behind the Rocks locations not added" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Patron's character 69 request behind the rocks not added" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Skinny dipping scene not added" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Hitomi's Changeroom CG not added" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Jack bumping into MC CG not added" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Alpha 0.06b" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Password input at night fixed to update password" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Random Number notification box in the park at night is fixed" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Hitomi random event at the beach fix" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Getting a job at the mall before visiting the comic book store bug fixed" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Conversation with Mom and [sister] only triggers in the afternoon so the whole day isn't wasted" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added more varied messages about location at the very beginning for first time players." color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Increased random encounter rate from 5% to 20%" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Buying Magazine off Hitomi bug fixed" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Hitomi's one-on-one conversation mapping has a loop." color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Inventory system is still bugged" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Alpha 0.06c" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Location (Behind Rocks at the Beach)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added End of Main Story Screen" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Violette 69ing with a girl Behind the Rocks at the Beach (Patron Reward Request)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added More Kitchen Chalkboard Messages (Patron Reward Request)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Hitomi one-on-one conversation in the comic book store mapping" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Inventory System (items doesn't disappear and money doesn't revert back to its default state)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Violette's random encounter in the Park at night 100% appear rate bug" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Kitchen Chalkboard changing after conversation bug" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Improved Mother and [sister] Bathroom Sequence" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Violette Random Encounter at the Park only triggers when entered from the Map" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Hitomi's Changeroom CG not added" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Jack bumping into MC CG not added" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Behind the Rock at Night not added" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Skinny Dipping Scene is not completed" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text ""

label lbl_mybedroompc_changelog_005:
    call screen scr_mybedroompc_changelog_005

screen scr_mybedroompc_changelog_005():
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
            text "Alpha 0.05a – The Drama Update" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Cheat System for $5+ Patrons" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Secret Code to enable Phone Cheats" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Bag and Wallet GUI" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added more Main Story sequences" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added 1st part of Mom's Side Story" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Hitomi, Effie, Brock as Clickable Characters" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added minor Hitomi Side Story" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added replayable Effie's H-Scene sequence" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added option to skip Effie's H-Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added introductory sequence to Fight Club" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added 9 Characters (Lord Kevlamin, Davendithas, Crugeon, Miss Lashley, Coach Fistem, Brock, Jack, Hitomi, Alanna)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added 6 Character Sprites (3 Roleplayers, Miss Lashley, Hitomi, Jack)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Skill Feature so that you can only increase INT, LUK, and STA once per day." color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Porno Magazine Item not added" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-New Changeroom Attendees not added" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Effie Sex in MC Bedroom Scene CG not added" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Jack bumping into you CG not added" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Alpha 0.05b" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Street Access Bug" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Throwaway Conversation Images with Mom in the Kitchen" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Alpha 0.05c" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added New Beach Changeroom Attendees" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Davendithas Phone Contact" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Coach Fistem Phone Cheat" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Grammar and Improved Conversation with Coach Fistem" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text ""

label lbl_mybedroompc_changelog_004:
    call screen scr_mybedroompc_changelog_004

screen scr_mybedroompc_changelog_004():
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
            text "Alpha 0.04a – The Skills Update" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Skill Point System" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added 7 Locations (Street, Park, School Gym, Comic Book Store, Comic Book Backroom, Club, Mall)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Scenes for Increasing Skills (INT, STA, STR, CHA, LUC)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added 3 Characters (Phil, Jack, Brock)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Miss Allaway Clickable Character" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Crowds for (Main Beach)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Background for the Outside of the Café" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Effie Date Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Splash Screen and End of Main Story Notice" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed points with Effie when it goes below 0 pts" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed the Time/Energy GUI so it's easier to read" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Completely filled in Café Menu Board" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Completely filled the Town Map with buildings and other entities" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Improved the Quit Screen Font" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Improved the Missing Poster" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Improved Dialogue Box to easier see sprites waist area" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Nropexin is added to the team as an assistant-programmer" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Alpha 0.04b" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed the Phone GUI mis-clicked button bug" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text ""

label lbl_mybedroompc_changelog_003:
    call screen scr_mybedroompc_changelog_003

screen scr_mybedroompc_changelog_003():
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
            text "Alpha 0.03a – The Milkshake Update" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added 7 Locations (Café Inside, Café Outside, Outside Effie's House, Effie's Hallway, Effie's Room, Main Beach, Beach Change Rooms)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added 4 H-Scenes (Kiss, Blowjob, Mutual Masturbation, Missionary)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added 2 Characters (Effie's Dad, Violette)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added 6 Character Sprites (POV Naked, Effie Naked, Effie Work, Sister, [sister] Naked, Violette)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Ability to name ‘Sister'." color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added 2 Beach Change room Attendees" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Violette side story" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Phone Contacts section to keep track of your relationship points." color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added ‘???' name for unrevealed character names" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+5,700 words" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Effie Milkshake Date has no CG" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Phone Calls aren't functional and Skills section on the phone is not working." color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Sister's Bedroom has daytime outside her window at night" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Café Menu Board isn't full" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Sister's name colour is the same as MC's name" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Alpha 0.03b" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Sister's Window at night fixed" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Sister's Name Colour has been fixed" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Grammar fixed" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text ""

label lbl_mybedroompc_changelog_002:
    call screen scr_mybedroompc_changelog_002

screen scr_mybedroompc_changelog_002():
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
            text "Alpha 0.02a – The Uni Update" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added outlines for the character in the intro scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Characters (Dad, Jacob, Effie, Teacher)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Town Map Screen" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Main GUI (Map, Phone, Bag, Clock)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added 8 Locations (Bathroom, Classroom, Front of Classroom, Sister's Room, Living Room, School Hallway 1, School Hallway 2. School Yard)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Day/Night cycle for existing locations excluding the classroom" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Disclaimer at the start" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Changed the Textbox" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Phone and Bag aren't useable" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Sister's Bedroom has daytime outside her window at night" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text ""

label lbl_mybedroompc_changelog_001:
    call screen scr_mybedroompc_changelog_001

screen scr_mybedroompc_changelog_001():
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
            text "Alpha 0.01a – The Bed Update" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Menu Button Name Change" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Quit Screen" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Intro cut scene (4 Frames)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Wake up [sister] scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Randomized Chalkboard for Patrons in My Kitchen" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added 2 Character (Player, Mother)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added 3 Locations (My Bedroom, My Hallway, My Kitchen)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Alpha 0.01b" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Improved [sister] Wake Up Scene (Line Clean Up)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Improvements in the dialogue" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Alpha 0.01c" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Improved [sister] Wake Up Scene (Body Outline)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text ""
