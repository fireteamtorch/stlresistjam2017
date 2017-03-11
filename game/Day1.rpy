
label Day1Block:
    scene black
    with dissolve

    play music "tempDayTitleShortestDeNoise.mp3" noloop

    #image top_text = ParameterizedText(text = "Week 1\n\nNew Faces", xalign=0.5, yalign=0.0, text_size = 80)

    #show text "Week 1\nNew Faces" at truecenter with text_size = 80
    show text "Week 1" at Transform(xalign = 0.5, yalign = 0.47) as text1
    #show top_text at truecenter
    with Dissolve(2.0)
    show text "New Faces" at Transform(xalign = 0.5, yalign = 0.53) as text2
    with Dissolve(2.0)
    
    pause 1

    hide text1
    hide text2
    with Dissolve(2.0)

    
    
return