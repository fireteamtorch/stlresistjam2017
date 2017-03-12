label Day6Block:

    scene black
    with dissolve

    play music "jingle_dayTitleDenoise.wav" noloop

    show text "Week 6" at Transform(xalign = 0.5, yalign = 0.47) as text1
    #show top_text at truecenter
    with Dissolve(2.0)
    show text "Picking up the pieces" at Transform(xalign = 0.5, yalign = 0.53) as text2
    with Dissolve(2.0)
    
    pause 1

    hide text1
    hide text2
    with Dissolve(2.0)

    scene bgBarNight
    show bgCounterTop
    with dissolve

    play music "noir_v002_lpf_LOOPedit.wav"
    # play music "lux_v001_lpf_LOOPedit.wav" fadein 1.0
    
    "Braxton walks in and takes a seat at the bar."
    
    braxton "Evening."
    
    bartender "How's it hanging?"
    
    braxton "To the left."
    
    bartender "Should a teacher be talking like that?"
    
    braxton "I'm off hours. Need to get it out of my system. I watch what I say very closely when around the students."
    
    bartender "Don't you teach middle school?"
    
    braxton "Oh yeah. Which reminds me, can I get some whiskey? A double."
    
    bartender "That bad?"
    
    "You pour Braxton a double whiskey and hand it to him. He takes a long sip then gulps the rest down. He motions for another one."
    
    braxton "Do you know about the mating habits of walruses?"
    
    bartender "Yeah, but I'm not caught up on the current literature."
    
    "You pour Braxton a second double." 
    
    braxton "Yeah, yeah, smart guy. I popped into a science class a few days ago and they were watching some nature documentary about it."
    
    braxton "All these asshole males will fight each other until there's one alpha and meanwhile the kids, 'calves' in this case, are the ones getting trampled and hurt."
    
    bartender "I'm guessing chaos because of the water thing?"
    
    braxton "Got kids earlier in the week daring each other to drink the bad water."
    
    bartender "Jesus..."
    
    braxton "The parents are busy dealing with their own problems right now. Nobody was prepared for this. We're normally understaffed anyways, and this just made it worse."
    
    braxton "How about for you?"
    
    bartender "What water thing? Forgot all about it."
    
    braxton "Heh, I get enough sarcasm from the kids. Seriously."
    
    bartender "Jens cut his vacation short. He and the fianceé are rushing back."
    
    braxton "Rough. Not a great way to end the vacation."
    
    bartender "Yeah... And the diner's taking a hit. They say the water is just safe enough if you filter it, but no one believes it."
    
    "Elysia comes through the door, opening it with slightly more force than usual."
    
    elysia "You guys committing crimes in here?"
    
    braxton "No, Officer."
    
    elysia "Mmmm, I've got my eyes on you two."
    
    "Elysia walks over and takes a seat next to Braxton."
    
    braxton "Shit, Elli, what happened to your lip?"
    
    elysia "Is it that noticeable?"
    
    bartender "Want some ice for it? We still got some cubes left."
    
    elysia "I think I'm good. Just a scrape is all."
    
    braxton "What happened?"
    
    elysia "Nothing to get worried about."
    
    bartender "Well, let us hear it then."
    
    elysia "Pass me those nuts first."
    
    "You hand them some bar nuts. Elysia grabs a few and starts eating them one by one."
    
    elysia "All right, so I'm on patrol when I get a call, something about a disturbance at the water relief line. I get there and two women in line are hollering."
    
    elysia "I get them separated, and one of them accuses the other of cutting in line. I'm trying to break them up but one of them goes for a haymaker and catches my lip."
    
    braxton "Shit."
    
    elysia "So I take her down and cuff her. And that's when I hear it."
    
    bartender "Hear what?"
    
    elysia "Hey, is the kitchen still open? I could use a burger right about now."
    
    bartender "We've got a very limited menu right now."
    
    elysia "Damn, I could go for a mushroom 'n swiss. Pickle on the side."
    
    braxton "Elli, I know what you're doing, come out with it."
    
    elysia "All right, all right. Behind me I hear a kid crying."
    
    braxton "That woman's kid?"
    
    "Elysia nods."
    
    elysia "Little boy just bawling his eyes out. Couldn't have been more than six or seven."
    
    braxton "Jesus."
    
    elysia "I let her go. Registered a warning and told her to take her kid and go home."
    
    bartender "This whole thing is fucked up..."
    
    elysia "This water thing is stressing everyone out. Can't make it worse."
    
    braxton "Well, that's good karma. Barkeep, one of your finest, cheapest, domestic beers for the officer here."
    
    elysia "Oh, you spoil me. By the way, have you seen Charles around?"
    
    braxton "He's...avoiding people."
    
    elysia "Why?"
    
    braxton "Remember how we talked about bringing back jobs?... The new governor is going to get a new plastics processing plant built here."
    
    elysia "That's...go on."
    
    braxton "If you look at the other new plants, it's mostly automated, and the specialists to run it..."
    
    elysia "Out-of-state..."
    
    braxton "Right. The businesses might see some short term boost from the influx of workers for the construction, but as soon as that dries up..."
    
    "Elysia nods at you appreciatively for the beer before taking a sip. She winces due to the injured lip but sighs appreciatively after the cold sip."
    
    elysia "So..."
    
    braxton "Charles found out that they are rolling back some environmental protection regulations..."
    
    bartender "What?"
    
    elysia "ARE YOU SHITTING ME? We've JUST started getting some clean water again."
    
    braxton "As part of the negotiations for the new plant... But you know what? 'Secured new plant to stimulate economy' looks great on a politician's resume."
             
    braxton "All the negotiating happened before the spill but...it might still go through."
    
    elysia "There'll be some protests in the streets when people find out."
    
    braxton "I think he's feeling guilty about running the exposé..."
    
    elysia "Poor Charles..."
    
    "Another long day..."
    
    "Jens should be getting back soon..."

    scene black
    with dissolve

    stop music fadeout 1.0
    pause 1
    show text "End of Day" at truecenter as text3
    with dissolve
    play music "jingle_endOfDayDenoise.wav" noloop
    pause 2
    hide text3
    with dissolve
    pause 3

return