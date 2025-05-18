label lbl_mybedroompc_changelog_020:
    call screen scr_mybedroompc_changelog_020

screen scr_mybedroompc_changelog_020():
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
            text "Alpha 0.20a - The Townsville Update" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Spelling and Grammar Fixes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+New Writer on the Team" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Main Story Progression" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Converted Some Dialogue to Fit with Patreon's Guidelines" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Reworded the archive so that small file replacement hotfixes are possible" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added 8 New Characters (6 Females & 2 Males)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Disclaimer when trying to load old save files" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Age Restriction Disclaimer in the splashscreen" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Pulsing Effect to Speaking Characters" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Lip-syncing Images to the Camgurl Confession Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Additional Dialogue to Funnel the Player to check the 2nd Floor of the School" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Throwaway Line for Miss Allaway in the Side Story" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added 3 Throwaway Lines each for 4 of the new characters" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added 15 Throwaway Lines for Miss Lashley" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Updated the Dialogue Box so Text with no Characters assigned to it will not have a name box" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Updated Movie Genres from Mystery and Test Screening to Sci-fi and Indie Arthouse (no added content)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Updated and Improved Alanna's and Hitomi's sprites" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Updated the Choice Menu Boxes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bug during 20Q Scene where it refers to [sister] as the wrong thing" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bug during 69 Scene where the result of you winning or losing is switched" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Minor Bug during Argument with Mom in the bedroom where it sets a trigger to go back 3 chapters instead of reducing 3 relationship points" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Stamina and Strength Max Limit Bar" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Incorrect Frame during Miss Allaway Cafe Date Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Incorrect Violette Sprite Position" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Background when [sister] wakes up late in the basement" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Throwaway Lines are absent for 4 of the new characters" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Miss Allaway and Lashley's ‘Shocked' Sprite isn't implemented" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Multiple Scenes not rendered" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-New Characters don't have proper individual interactive buttons" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-You can enter the basement through the Main Story without having progressed Sister's Story far enough" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Alpha 0.20b" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed a trigger bug for bumping into Jacob and Effie at the front of school in the Main Story" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed a trigger bug for meeting with Miss Lashley in her office in the Main Story" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Alpha 0.20c" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed a disappearing map after Effie's Milkshake Date" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text ""

label lbl_mybedroompc_changelog_019:
    call screen scr_mybedroompc_changelog_019

screen scr_mybedroompc_changelog_019():
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
            text "Alpha 0.19a - The Locked In Update" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Minor [sister] Story Progression" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Allaway Story Progression" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Spelling and Grammar Fixes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bug where the Game crashes when you visit the School during Sister's Story" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Alpha 0.19b" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Grammar and Spelling Error" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Point Increase when you tell Mom that she doesn't owe you anything for the Smart TV Box" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bug where Beach in the Sexworld is still occupied with people when you visit before going to school" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Amount that Mom pays you back for the Smart TV Box" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed ‘fbpwmag' bug when mom visits you at night for some fun while you sleep." color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Trigger for when you talk to Mom in the hallway about her eye looking healed." color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Naming for the porno title on Mom's PC" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Naming for the text that you get from [sister] in the school hallway" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bug during the Softcore H-scene when Trapped with Miss Allaway" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Alpha 0.19c" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added a Report a Bug Link in the Game" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Updated the Background for the Main Menu and In Game Menu" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Updated Pre Main Menu Message" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Cam Stream Username Bug" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Infinite Loop when exiting the Classroom during Sister's Story" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Undefined variable bug when talking to Miss Allaway in the School Cafeteria" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text ""

label lbl_mybedroompc_changelog_018:
    call screen scr_mybedroompc_changelog_018

screen scr_mybedroompc_changelog_018():
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
            text "Alpha 0.18a – The Closer Update" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Miss Allaway Story Progression" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Jane Story Progression" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added and updated onto the fight between Mom and MC after seeing the parents in the livingroom at night" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Throwaway Chat with Violette" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Customer to the Adult Store" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Students in Hallway 2 of the School" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Students in the Cafeteria Button in Hallway 2 of the School" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Outing Outfit for Miss Allaway" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Art Asset for Allaway at the Cafe Date Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Mom paying you back for the Smart TV Box" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Mom Romance Dream Sequence" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added [sister] paying you back for her Phone Bill" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Improved Effie's Mutual Masturbation Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Improved Effie's Missionary Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-[sister] button in the Living Room not yet created" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-[sister] additional scene in the fort doesn't have lip syncing" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Violette doesn't have shocked sprites" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Alpha 0.18b" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added preset-load for Alpha 0.17" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed ‘trustandsafety_shield' bug" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Sister's trigger to continue on with the story" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Effie's BJ Options send you to Jane's H-scene in the Box Fort" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Alpha 0.18c" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Added Shocked Sprites for Violette" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Replaced ‘Sis' button in the Living Room with ‘Jane'" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Fixed Bug that sent you to Jane's H-scene in the Box Fort from Effie's H-scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Fixed Sprite Placement of [sister] when confronting her in the livingroom" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Alpha 0.18.5c" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Removed any incest references" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added options and the ability to choose and name who the household characters are" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Grammar and Spelling Fixes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added additional dialogue stating the age of several characters" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Replaced [sister] Button in the Living Room" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bug where if you have fun with Effie on a Sunday, it tries to load an 8th day of the week" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Throwaway Conversation with Mom so she doesn't ask about your job before you have one" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Image Bug where it shows Davendithas when you choose to verse Lord Kevlamin" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Image Bug where it shows Jack when you choose to fight against Brock" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Image Bug where Normal and Intense Studying is the Same" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed and Added a Time Change after MIss Allaway picks on you in class" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed it so it has to be the afternoon before you can ask Miss Allaway about After school Tutoring" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed it so that if you talk to Miss Allaway at the Cafe in the morning, Effie doesn't show up after Brock. (Depending on the time, depends on who shows up afterwards)." color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed and Added Skill Points Levelling Up and Calendar Date Progression after a night with Effie" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed it so that you can't pick up the crumbled piece of paper in Sister's room while she's in there" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Throwaway Chat with Jacob so that he only asks about the magazine if you've bought it" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Trigger Bug when you don't pull your pants down for Sister" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text ""

label lbl_mybedroompc_changelog_017:
    call screen scr_mybedroompc_changelog_017

screen scr_mybedroompc_changelog_017():
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
            text "Alpha 0.17a – The Outburst Update" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Miss Allaway Story Progression" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Miss Allaway Casual Outfit" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Miss Allaway to the Cafe as a Talkable Character" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Crowd on the Dance Floor at the Nightclub" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Casual Wear for Dad" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Mom Horror Dream Sequence" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Mom Action Dream Sequence" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Throwaway Chat with Dad in the Living Room" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Throwaway Chat with Dad in the Parents Bedroom" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Throwaway Chat with Miss Allaway at the Cafe (Need Buttons)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Throwaway Chat with Davendithas" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Throwaway Chat with Crugeon" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Throwaway Chat with Lord Kevlamin" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Bar Counter for Steve's Sprite" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Office Desk for Miss Lashley' Sprite" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Store Counter for Hazel's Sprite" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Replaced the Exit sign in the Nightclub with a Street Navigation Button" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Replaced and Updated Grundle Sam's Store" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Updated the Phone layout so that there isn't an Achievements Tab" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Updated and Improved Grundle Sam's Sprite Proportions" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Updated and Improved Cafe Outside location" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Updated and Improved Cafe Worker Buttons" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Effie appearing at the Park at night on the first night and when you ask her to have some fun at her house any other night" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed and Improved the Phone Skill Tab" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bug where nothing happens when you try to Access Sister's Stream at correct time with no story trigger" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Mom's Romance Dream Sequence not added" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Crugeon Shocked Sprite not added" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Lord Kevlamin Shocked Sprite not added" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Mom's mouth doesn't talk during Saving Scene in Action Dream" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Alpha 0.17b" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Disabled Developer Mode" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Compressed the New Scenes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Some Spelling and Grammar Fixes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Crugeon Shocked Sprite" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Lord Kevlamin Shocked Sprite" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Lip Sync to Mom during the Action Dream Sequence" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Lip Sync to the [sister] scene before the basement kiss and after the 20q sequence" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Conversation Lines to Effie and Jacob's Cafe and Comic Book Store Invitation" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Changed dialogue option with Miss Allaway about having sex with Effie to ‘staying over'" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Changed Effie's text trigger so you have to meet certain characters around town first" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Mom's conversation about your job before you get a job" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bug where you can run across Miss Lashley behind the rocks before you formally met her." color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Jacob Sprite location when meeting the Role Players" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Incorrect Sprite in Lord Kev's Throwaway Chat" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Incorrect Sprite in Conversation with Mom and [sister] about getting a job" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bug with Jacob's Throwaway Chat in the Comic Book Store" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bug where Parents are in their room and in the living room at the same time" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Popup Notification Text when dad counter-tackles you with a reason as to you ‘losing' points rather than ‘using' points" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bug where Effie is on the Park Bench at night in the Sex World" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bug where after Mom gives you a handy in bed and you cum, it takes you to your bedroom at night instead of the next morning" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bug where Grundle Sam just says ‘stuff' when you talk to him instead of having chat options" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bug where Dad is still at home on the weekend when he's supposed to be out of town" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Incorrect Dialogue with Mom's Anal Scene at the Desk" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bug where during the 20Q with Sister, it occasionally says ‘qc'" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed and Improved Kiss Rejection after 20Q with Sister" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed bug so that Mom isn't in the living room when you're supposed to meeting [sister] in the basement" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed bug where if you choose not to stay with [sister] in the box fort, the phone objectives says ‘Head upstairs'" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed bug where you can visit the cinema location when you're meant to head straight to school in the Sex World" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed bug where Grundle Sam's store isn't accessible in the sex world" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed bug where Mom is in other parts of the house when she's supposed to be in her room flicking the bean" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Timing with Notifications after meeting dad in the first morning" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text ""

label lbl_mybedroompc_changelog_016:
    call screen scr_mybedroompc_changelog_016

screen scr_mybedroompc_changelog_016():
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
            text "Alpha 0.16a – The Troublemaking Update" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Complied to Patreon's Guidelines by disabling the ability to go down any of the banned routes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+[sister] Story Progression" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Compressed Town Map and Phone Assets" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Grammar and Typo Fixes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added New Characters (Mina, Grundle Sam, Steve) (Paul Minor Character)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added the Roleplayers as clickable characters in the Comic book store backroom" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Effie as a clickable character at the park at Night" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Effie as a clickable character in the classroom in the Morning" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Steve in the Nightclub" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Miss Lashley to the Director's Office" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Grundle Sam and an introduction conversation in the Stuff and Things Store" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Skill Items Assets" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Dialogue with Hitomi where she mentions the Adult Store" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Dialogue with [sister] where the MC mentions interacting with the bartender" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Art Asset for Cheer Mom Up Errand Scenes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Art Asset for Sister's 20Q Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Art Asset for [sister] in the Adult Store Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Adult Store Backroom BG" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Director's Office as an accessible room in the school after you visit the fight club" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Website Link to the Game's Main Menu" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Completed Adult Store" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Improve Miss Allaway button in the Classroom" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Trigger in the Sex World so you can't initiate any [sister] Side Story" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bug in the Sex World where dad is meant to be there sleeping with mom" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Mom Cunnilingus' trigger scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bug that assumes you already asked Mom out on a Dinner Date and awaits for you to buy a suit" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Map Disabling Bug before asking Mom out on a Dinner Date" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Jacob's Sprite position so he's facing right when touring the MC in the comic book store" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Mom's Dialogue where she treats the anal scene as if it was her vagene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Sister's Phone Objectives" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bug when accessing Sister's stream at the wrong time and or day" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bug where Mom is in bed sleeping when she's suppose to be out in the Park" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bug at the cinema where you gain $60 if you ask your date to pay for the movie" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bug that didn't allow allow an option before watching a Romance Movie with Mom" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text ""

label lbl_mybedroompc_changelog_015:
    call screen scr_mybedroompc_changelog_015

screen scr_mybedroompc_changelog_015():
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
            text "Alpha 0.15a – The 20Q Update" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+[sister] Story Progression" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added 3 New Randomized Title screen Backgrounds" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Boxfort to the Basement after it has been built" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added New Character (Hazel)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added 2 New Locations (‘Adult Store' & ‘Grundle Sam's Things & Stuff')" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added ‘Force Enable Map' Cheat Button and ‘No Skill Max Limit' Cheat Button to Phone" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Jacob in the School Hallways to Talk To" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Jacob in the Comic Book Store to Talk To" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added 15 Mini-throwaway Dialogues with Jacob" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Redone the Skill System" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Redone the Basement so it's more spacious to fit the Boxfort" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Redone and Improved Effie's Kissing Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Redone and Improved Effie's Bj Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Redone and Improved Effie's Mutual Masturbation Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Redone and Improved Effie's Post-Sex Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Redone and Improved Beach Change Rooms so it's now scheduled rather than RNG" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Improved Mom's Movie scenes so scenes are choosable based on your RP with Mom and scenes are longer" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bug where accessing Sister's cam stream sometimes sends you to a beach changeroom sequence" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bug where the map is gone after having sex with Effie" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bug related to a choice made with [sister] in the Fort" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bug that shows the kitchen buttons in the livingroom if you pre-maturely let mom know you're ready for the dinner date" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Sister's Side Story has Unfinished CG Art" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Effie's Missionary Scene needs to be Redone and Improved" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Skill Items assets not Created" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Adult Store asset not Complete" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-New Store in Mall's assets not Complete" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Hazel (Manager) Store Button not Complete" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-New Store in Mall's Owner not Complete" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Phone Skills Page doesn't automatically update when using Cheats" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Alpha 0.15b" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed and Organised the PC Options" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Map so it's enabled after 20Q with Sister" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Undefined Variables in the Changerooms" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Graphical Bug with Effie's Mutual Masturbation Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bug where you can interact with Mom in the Living Room before talking to her in the Kitchen about your new job" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text ""

label lbl_mybedroompc_changelog_014:
    call screen scr_mybedroompc_changelog_014

screen scr_mybedroompc_changelog_014():
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
            text "Alpha 0.14a – The Fortress Update" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+General Code Optimization" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+[sister] Story Progression" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Compressed Scene Assets and Reduced the Game size by almost half" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Disabled ONLY the map in appropriate places instead of all the entire hud" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added [sister] in her Room to Talk to" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added 15 Mini-throwaway Dialogues with Sister" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Mom in the Living Room to Talk to" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Mom in her Room to Talk to" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added 15 Mini-throwaway Dialogues with Mom" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Parents Sleeping in their Room" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Roleplayers as Card Game Opponents" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Art for Researching at the PC Sequence" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Point Increase when successfully climaxing with Mom in the Bath" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Improved Sister's Sprites (Minor Changes)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Improved Visibility of Paper in Sister's Room and Made the Objective more clear" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Improved Art for Studying in Class (Int Skill)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Improved Art for Running at the Park (Sta Skill)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Improved Art for Playing Cards (Luc Skill)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Improved Art for Fight Club (Str Skill)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Improved Art for Dance Club (Cha Skill)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Adjusted Point Increase and Decrease during Mom's Fight Scene in your bedroom" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bug that allowed you to choose ‘Test Screening' and ‘Mystery Movie' at the cinema even if you have less than $60" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed the Calendar so the date is accurate to the day of the week and added a trigger to forward the date after Effie's Sex Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Mom's Objective from ‘Go about your day' to ‘Sleep at night' after scene in her room" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed and Updated Mom's location appearance, triggers, and dialogue throughout the house" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed the Size of the Front Door in the Living Room" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Notification after Dinner Date with Mom so it displays the correct amount you owe her if you split the bill" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed ‘Sex Dimension' option choice when unlocking the door so it's only available if you've been there" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Logic Bug where you have to wait for Monday Afternoon to talk to mom but she's in the shower. Move the day to Tuesday Afternoon." color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Logic Bug where Mom gives you a BJ in the cinema before your first supposed BJ from her in the park" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Incorrect Anal Scene Cumming Dialogue with Mom" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixes with Notifications, Dialogue, Objectives and Incorrect Sprite Placement" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Boxfort in the Basement isn't built, continuity error" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Alpha 0.14b" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bug where the map doesn't re-enable after Effie's H-scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Graphical Bug where dad is in the bedroom when he's supposed to be out of town" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-When trying to access the sister's cam stream, sometimes it jumps you to a changeroom scene or even brings you to the title screen" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-After talking to Mom in the livingroom about fixing the computer, the sprites are still displayed in the navigation screen" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Logic bug that shows [sister] in the bath and in the bedroom at the same time" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Alpha 0.14c" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Re-enabling Map Bug after Effie's H-scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Access to Sister's Cam Stream Bug" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Sprite still present bug when talking to mom in the Living Room" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Fail-Safe so it works when the cheatcode is successfully inputted instead of that AND the cheats have to be toggled on" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text ""

label lbl_mybedroompc_changelog_013:
    call screen scr_mybedroompc_changelog_013

screen scr_mybedroompc_changelog_013():
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
            text "Alpha 0.13a – The Camgurl Update" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+47,600 words" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+[sister] Progress" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+General Code Restructuring" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+General Fix of Mom's Story Trigger Points" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Text Fixes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added New Location" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Incest Porno with Mom Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Anal Missionary Scene in Mom's H-scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Anal Bent Over Scene in Mom's H-scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Mom Movie Date Handjob Scenes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Mom Movie BJ Scenes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Mom Midnight Magazine-Triggered Grinding Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added a Research Section for Story Progressing Purposes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Proper Transition Conversations based on outcome after Mom's Dinner Date" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added a ‘Next Week' option for Effie's Text to Meet at the Park" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Improved Notification at the end of Mom's Dinner Date" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Improved Mom Objective about ‘Waiting till Friday'" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Optimized sprite coding in scenes with 3 people" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Trigger points for Mom Watching Porno Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Temporary Mom Trigger to Revisit the Home Run Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Shopping feature so that items can only be bought once" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Missing Art include: Dreams about Mom" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Alpha 0.13b" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Spelling and Typo Fixes and Dialogue Improvements/ Changes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added a ‘Fail-Safe' feature that allows you to skip over a blockade or errors in the game" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added IceCream'py Counter when checking on Alanna about the Job" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Shaking Effects" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Minor Throwaway Lines to fit the mood of the Miss Allaway" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Carpet to Mom Cuddling Scene in the Living Room" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Outcome for when you don't have enough money during the first camgurl stream" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Improved Visibility of the Paper in Sister's Room" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Trigger so [sister] doesn't show up in the Hallway after being Scolded by Mom" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Trigger that allows you to skip nights with Mom without her feeling mad" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Trigger about the conversation that you have with Mom about her Healed Eye" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Trigger Bug that doesn't allow you to learn how to pick a lock" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Infinite Loop outside the Cafe at night" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Zoom in on the Hospital at Night at the Start" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Some Notification Popups" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Some Transitions" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bug where Mom is in the Bath when you just got out after watching Sister's Stream" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Optimized sprite coding in scenes with 3 people" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Locked Sister's Bedroom in the Afternoon on a Wednesday to fit with the story" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text ""

label lbl_mybedroompc_changelog_012:
    call screen scr_mybedroompc_changelog_012

screen scr_mybedroompc_changelog_012():
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
            text "Alpha 0.12a – The Movie Update" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+General Code Restructuring" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Mom Side Story Progress" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Option to start a new game or load a preset state to mimic the end of a previous version" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Calendar in Bedroom" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Year System" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Money Cheat to Bag accessible with Cheat Code" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added CG Scene for Conversation with [sister] in her Bedroom" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added CG Scene when giving Mom a Strip Tease" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added 2 Locations (Hospital, Street Alleyway)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Sexworld Versions of 2 Locations (Mall and Retail Store)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Sexworld Interaction with Janae" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Laptop Background" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Notification to funnel the player into triggering the conversation about getting a job" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Dog to pet at the park" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Additional Violette Interaction where she tells you off for going behind the rocks while still clothed" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Updated Town Map" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Changed Sister's Camgirl Username from Plushibun2 to LittleBowPeep" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Changed time to be set to afternoon after getting a camgurl text from Sister" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Disabled Map in the School Gym at night to funnel the player to trigger Miss Allaway's story" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Disabled Ability to buy another Antivirus after using it to fix Mom's PC" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Hyperspeed bug with Skinny Dipping H-scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Logic Bug where Jacob's Random Encounter in the school hallway can happen after he says he'll go meet Hitomi in the schoolyard" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Logic Bug where you can sit with Miss Allaway at the Cafeteria in the Sex World" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Logic Bug where Jacob talks to you about the magazine in the Sex World" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bug where you can wait for Mom in the Living Room in the Sex World to watch TV" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bug where you can have the Bath with Mom conversation again when you refuse to masturbate with her" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bug where Skill Leveling doesn't Reset after Sleeping with Mom after the fight with Dad." color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bug where you can zoom into the Police Station at the start of the game" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bug where you can visit the Office and Police Station on the first day of school" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bug where you can see [sister] behind Jacob's Sprite in the Schoolyard scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bug where it shows that you lost $500 whether you had that much money or not" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bug where talking to Brock in the Cafe twice in a row is both like a first interaction" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Funneling System so that you can't go to the Garden after your night with Effie" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Navigation Bug where clicking on the Blue Roofed House goes to Effie's House" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Missing Art include: Mom Scenes at the movies, Mom watching Porn, Dreams about Mom, Homerun Anal Scenes with Mom" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Nothing is actually scheduled to the calander system yet." color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Alpha 0.12b" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Loop Bug at the Park with Mom" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bug where [sister] appears at the very start of the game" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Navigation Bug with the Alleyway" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Other Related Trigger Fixes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Typography Fixes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Alpha 0.12c" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Navigation to the Hospital" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Infinite loops in Gloryhole Scenes" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Miss Allaway Cafeteria Trigger" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Mom giving head in the middle of the night trigger" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bug of mompastsunset_attend not being defined" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bug that disabled a temporary fix to allow revisiting Mom's Home Run Scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Disabled Violette talking to you in the sex world about undressing" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Planned out “Random Encounters” in a Calendar System instead of RNG" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text ""

label lbl_mybedroompc_changelog_011:
    call screen scr_mybedroompc_changelog_011

screen scr_mybedroompc_changelog_011():
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
            text "Alpha 0.11a – The Homerun Update" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Code Restructuring and Optimization" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Homerun with Mom" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added [sister] Side Story Progress" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Miss Allaway Side Story Progress" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added 7 Tracks of Music" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Random Title Screen Feature" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Clothing Retail Section" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Choice to Go to Bedroom or Front of house from Map" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added 6.5 Locations ( Jacob's House, Office, Police Station, Director's Office, Male and Female School Bathrooms, Mall Outside at Night)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Improved and Updated the Skill System so it doesn't use RNG and it doubles points you gain and lose if you're not at a high enough level" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Improved and Updated Dialogue Box" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Improved and Updated Choice Menu Box" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Improved and Updated Notification Box" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Improved and Updated A Town Uncovered Logo" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Improved Art for Effie Milkshake Date" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Hitomi not appearing at the beach" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bill preview during Dinner Date" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Game crashing when visiting the Cinema at Night" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed some incorrect spirtes in conversations" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed the Dining Room mowed grass exterior in the window" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Bill Reaction in Mom's Dinner Date scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Choices with longer lengths will go over the choice frame" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-[sister] Art or Sprites not present when talking to her in her room at night" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-The Town Music restarts whenever you click on the Map" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Alpha 0.11b" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Game Crashing Error in Effie's Room and House" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Game Crashing Error when leaving voyeurism scenes in the bathroom" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Game Music so that the town music doesn't repeat whenever the townmap is clicked" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Game Breaking Bug where conversation with mom about getting a job doesn't happen" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Choices with longer lengths will go over the choice frame" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-[sister] Art or Sprites not present when talking to her in her room at night" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Town Roaming music doesn't loop properly (minor bug)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Bug in Mall Navigation" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Infinite Loop Bug in the bedroom in the morning after the cuddle scene with mom (work around by working at icecreampy)" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-When [sister] asks for money in the schoolyard, error happens involving the luck skill" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Alpha 0.11c" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Music During When going to the kitchen for the first time in the morning" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added ability to replay Mom's H-scene in the bedroom" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Infinite Loop happening in the hallway and livingroom on a Tuesday" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Infinite Loop happening in the bedroom in the morning after talking to mom after cuddle scene" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Error with Mall Navigation" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Town Roaming Music so it loops correctly" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed bug during chat with [sister] about borrowing money involving the luck skill" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Endless loop with Lillian in the Gloryhole scene at the beach" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Choices with longer lengths will go over the choice frame" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-[sister] Art or Sprites not present when talking to her in her room at night" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Infinite Loop in the bedroom related to Mom's Side Story" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-If you go anywhere at night in the sex world, the map disappears" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Mom's H-scene's pace is strangely at hyper speed" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Sprites aren't present in Jacob's conversation with the MC in the schoolyard" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Alpha 0.11d" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Jacob and MC sprites in conversation in the schoolyard after sister's conversation" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Added Note about missing CG scene in Sister's Bedroom" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Infinite Loop in the bedroom during the day that is related to mom's side story" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Map not showing up in the sex world at night" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Spelling Errors" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Infinite Loop that occurs when you pick ‘no' when asked to wait for Effie outside." color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Infinite Loop that occurs when you pick ‘no' when asked to wait for Mom in the livingroom" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Infinite Loop that occurs when you pick ‘no' when asked to sit with Miss Allaway in the cafeteria" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Incorrect Sprite placement during Conversation with [sister] in the Schoolyard" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Mom's H-scene's pace is strangely at hyper speed? For some people?" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-Choices with longer lengths will go over the choice frame" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "-[sister] Art not present when talking to her in her room at night" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text "Alpha 0.11e" color "#131212" size 50 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Mom's H-scene Speed" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Fixed Choice box size to fit longer text" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text "+Minor code and naming convention fixes in the files" color "#131212" size 35 font "fonts/KGSorryNotSorryChub.ttf"
            text ""
            text ""
