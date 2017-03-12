label Day6Block:

    scene black
    with dissolve

    play music "tempDayTitleShortestDeNoise.mp3" noloop

    show text "Week 6" at Transform(xalign = 0.5, yalign = 0.47) as text1
    #show top_text at truecenter
    with Dissolve(2.0)
    show text "Picking up the pieces" at Transform(xalign = 0.5, yalign = 0.53) as text2
    with Dissolve(2.0)
    
    pause 1

    hide text1
    hide text2
    with Dissolve(2.0)

    scene bgBarDay
    show bgCounterTop
    with dissolve

    #play music "noir_v002_lpf_LOOPedit.wav"
    play music "lux_v001_lpf_LOOPedit.wav"








    stop music fadeout 1.0
    pause 1
    show text "End of Day" at truecenter as text3
    with dissolve
    play music "tempEndofDay.mp3" noloop
    pause 2
    hide text3
    with dissolve
    pause 3

return