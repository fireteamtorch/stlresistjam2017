label Day5Block:

    scene black
    with dissolve

    play music "jingle_dayTitleDenoise.wav" noloop

    show text "{size=90}Week 5{/size}" at Transform(xalign = 0.5, yalign = 0.45) as text1
    #show top_text at truecenter
    with Dissolve(2.0)
    show text "{size=70}Crisis{/size}" at Transform(xalign = 0.5, yalign = 0.55) as text2
    with Dissolve(2.0)
    
    pause 1

    hide text1
    hide text2
    with Dissolve(2.0)

    scene bgBarDay
    show bgCounterTop
    with dissolve

    # play music "noir_v002_lpf_LOOPedit.wav" fadein 1.0
    play music "lux_v001_lpf_LOOPedit.wav" fadein 1.0

    "Frank walks in, looking disheveled."

    show frank angry lookLeft at Seat2
    with Dissolve(disFactor)

    frank "You got any water?"

    bartender "Just the kind that comes in bottles."

    show frank angry lookRight at Seat2
    with Dissolve(disFactor)

    frank "Christ, you too?"

    bartender "It's the whole county, Frank. Actually... 9 counties."

    show frank angry lookLeft at Seat2
    with Dissolve(disFactor)

    frank "Fuck...!"

    bartender "Yeah...Just gotta sit tight and wait 'til it passes."

    show frank angry lookRight at Seat2
    with Dissolve(disFactor)

    frank "Can't be good for business though... I'd imagine."

    bartender "You want a beer?"

    show frank sit at Seat2
    with Dissolve(disFactor)

    "Frank hesitates and sits down."

    show frank smile at Seat2
    with Dissolve(disFactor)

    frank "Yeah."

    show frank smile beer at Seat2
    with Dissolve(disFactor)

    "You hand him a beer."  

    bartender "No water to wash the dishes, so gotta stick to cans..."

    show frank sit beer lookRight at Seat2
    with Dissolve(disFactor)

    frank "'s'bout the same as my fuckin' house."

    bartender "Frank, I don't wanna be insensitive, but what is that smell?"

    show frank smile beer at Seat2
    with Dissolve(disFactor)

    frank "Oh, you like it? It's some of my old cologne. Can't shower so I gotta cover up the musk somehow. Had to scrounge around the back of my closet for it."

    show frank sit beer lookPlayer at Seat2
    with Dissolve(disFactor)

    bartender "I think it's gone bad..."

    show frank smile beer at Seat2
    with Dissolve(disFactor)

    frank "It's just how fancy cologne is."

    bartender "Fancy cologne smells like old jockstrap?"

    show frank sit beer lookLeft at Seat2
    with Dissolve(disFactor)

    frank "Eh, what do you know?"


    show elysia sit lookRight at Seat4
    with Dissolve(disFactor)

    "Some time passes. Elli comes in and sniffs the air."

    show elysia sit lookLeft at Seat4
    with Dissolve(disFactor)

    elysia "Evening, gentlemen. Shit, Frank, what's that smell?"

    show frank smile beer at Seat2
    with Dissolve(disFactor)

    frank "'Eau de toilette'."

    show elysia smile lookLeft at Seat4
    with Dissolve(disFactor)

    elysia "You're making it too easy. Just wanted to come by, make sure nobody's using the water."



    bartender "For the toilets, yeah, but that's it."

    show elysia smile lookPlayer at Seat4
    with Dissolve(disFactor)

    elysia "Good to hear. Now, can I get a beer, please?" 

    "You hand her a can of beer." 

    show elysia sit lookRight at Seat4
    with Dissolve(disFactor)

    elysia "No mug?"

    show elysia sit lookLeft at Seat4
    show frank sit beer lookRight at Seat2
    with Dissolve(disFactor)

    frank "Can't wash mugs."

    show frank sit beer lookLeft at Seat2
    show elysia closed at Seat4
    with Dissolve(disFactor)

    elysia "Right... That makes sense. Still adjusting to this."

    show frank sit beer lookRight at Seat2
    with Dissolve(disFactor)

    frank "Can't you do something about this?"

    elysia "What do you want me to do?"

    show frank angry lookRight at Seat2
    show elysia closed at Seat4
    with Dissolve(disFactor)

    frank "Something. Arrest the assholes, anything!"

    show elysia sit lookLeft at Seat4
    with Dissolve(disFactor)

    elysia "Frank, you know I can't do that. I'm just a beat cop. The governor and the National Guard are working on a fix so we just have to sit tight. For now."

    show frank angry lookLeft at Seat2
    with Dissolve(disFactor)

    frank "'Sit tight?' 'Sit tight?' What kind of bullshit is this? Everybody's waiting, nobody's doing anything." 

    show frank angry lookRight at Seat2
    show elysia closed at Seat4
    with Dissolve(disFactor)

    elysia "People are sorting it out. Things are happening, we just gotta let it happen."

    show frank angry lookLeft at Seat2
    with Dissolve(disFactor)

    frank "Things are happening, pfft. In the old days, some asshole poisons the town well, the sheriff'd gun 'em down."

    show elysia sit lookLeft at Seat4
    with Dissolve(disFactor)

    elysia "This ain't the Wild West, Frank."

    show frank angry lookRight at Seat2
    with Dissolve(disFactor)

    frank "We're all just sitting here, twiddling our thumbs, waiting for someone else to decide what happens to us. That's bullshit."

    show frank angry lookLeft at Seat1 behind bgCounterTop
    with Dissolve(disFactor)

    "Frank stands up, scooting the stool he was sitting on back, almost tipping it over."

    elysia "Frank, where are you going?"

    show frank angry lookRight at Seat1
    with Dissolve(disFactor)

    frank "I'm gonna do something."

    elysia "Do what?"

    show frank angry lookLeft at Seat1
    with Dissolve(disFactor)

    frank "I don't know yet."

    elysia "Sit back down. Come on, you didn't even finish your beer."

    show frank angry lookRight at Seat1
    with Dissolve(disFactor)

    frank "No, I'm done sitting and I'm done drinking. 'I am the master of my fate. I am the captain of my soul.'"

    show elysia closed at Seat4
    with Dissolve(disFactor)

    elysia "Frank, if you don't come back down, you'll force my hand."

    frank "And why's that?"

    show elysia sit lookLeft at Seat3 behind bgCounterTop
    with Dissolve(disFactor)

    elysia "Because I'm worried you're going to hurt someone."

    show frank angry lookLeft at Seat1
    show elysia closed at Seat3
    with Dissolve(disFactor)

    frank "Elli, the fuck do you think I'm going to do?"

    show elysia sit lookLeft at Seat3
    with Dissolve(disFactor)

    elysia "I don't know, but I'm your friend and I want you to sit with me and relax."

    show frank sad at Seat1
    with Dissolve(disFactor)

    "Frank's shoulders droop."

    hide frank
    show frank sad at Seat2
    with Dissolve(disFactor)


    "He lumbers over and repositions the stool before sitting next to Elli."
    
    hide elysia
    show elysia sit lookLeft at Seat3
    with Dissolve(disFactor)

    frank "Ah, hell, look at us. Squabbling, keeping each other down. This is what they want us to do."

    show elysia smile lookLeft at Seat3
    with Dissolve(disFactor)

    elysia "I know, I know. I'll grab the next round, so you just relax. Hey, is the game on?"

    show braxton angry at Seat4
    show frank sit beer lookRight at Seat2
    show elysia sit lookRight at Seat3
    with Dissolve(disFactor)

    "Braxton enters, looking exhausted."


    show braxton sit lookLeft at Seat4
    with Dissolve(disFactor)

    braxton "Wow, it is a nuthouse out there."

    frank "What's happening?"

    show elysia sit lookRight at Seat3
    with Dissolve(disFactor)

    braxton "Well, the state said they're going to hold back on aid for now."
    
    braxton "They're hoping this thing passes, so folks were piling into Malmart trying to stock up on water while they still can."

    elysia "You manage to get anything?"

    braxton "A pack of bottled water and some sports drinks."

    show braxton smile lookLeft at Seat4 behind bgCounterTop
    with Dissolve(disFactor)

    "Braxton briefly mock fights."

    hide braxton
    show braxton smile lookLeft at Seat4
    with Dissolve(disFactor)

    braxton "People weren't messing around, things got really tense."

    show braxton sit lookLeft at Seat4
    with Dissolve(disFactor)

    bartender "Sports drinks?"

    show braxton smile lookPlayer at Seat4
    with Dissolve(disFactor)

    braxton "Yeah, not going to do me much good with bathing and stuff. At least they had my flavor: red."

    show elysia sit lookLeft at Seat3
    show braxton smile lookLeft at Seat4
    with Dissolve(disFactor)

    elysia "Oh, you don't have to worry about bathing. Learn a thing or two from Frank and douse yourself in some French shit."
    
    show frank angry lookRight at Seat2
    with Dissolve(disFactor)

    elysia "Can't worry about getting smelly if you're already reeking."

    bartender "Haha, that's enough. Leave Frank alone."

    show frank smile beer at Seat2
    with Dissolve(disFactor)

    frank "Thank you."

    show braxton smile lookLeft at Seat4 behind bgCounterTop
    with Dissolve(disFactor)

    braxton "Come here Frank, let me a get a whiff of you."
    
    show braxton sit lookLeft at Seat3half
    with Dissolve(disFactor)

    braxton "Oh, that is..."

    show braxton sit lookRight at Seat4half
    with Dissolve(disFactor)
    
    braxton "......"

    show frank angry lookRight at Seat2
    with Dissolve(disFactor)

    frank "..."

    #show braxton sit lookRight at Seat4half

    braxton "...potent."

    show frank angry lookLeft at Seat2
    with Dissolve(disFactor)

    frank "I think it's nice."

    show braxton angry at Seat4half
    with Dissolve(disFactor)

    braxton "Got my eyes watering here."

    show braxton sit lookRight at Seat4half
    with Dissolve(disFactor)

    frank "Oh, not you, too."

    show elysia sit lookRight at Seat3
    show braxton sit lookLeft at Seat4half
    with Dissolve(disFactor)

    braxton "My girl said I wasn't sensitive enough. Hell, two seconds with Frank brought out the waterworks."

    show elysia sit lookLeft at Seat3
    show frank angry lookLeft at Seat2
    with Dissolve(disFactor)

    frank "That's it, I'm going to sit at the end."

    show frank angry lookRight at Seat1
    with Dissolve(disFactor)

    "Frank stands up and moves to the farthest stool at the other end of the bar."

    elysia "Oh, Frank, no!"

    frank "Nope, I'm setting a flag here. Got my leper colony set up so none of you have to endure my odor. Just gonna sit here and enjoy the company of me, myself, and I."

    hide braxton
    show braxton smile lookLeft at Seat4
    with Dissolve(disFactor)

    braxton "Oh, Frank, don't be like that. We were just kidding, is all. We didn't mean no harm. Come back to us."

    show frank angry lookLeft at Seat1
    with Dissolve(disFactor)

    frank "No."

    elysia "Frank, you stubborn old mule. Come back here and drink with us."

    show frank angry lookLeft at Seat1
    with Dissolve(disFactor)

    frank "Okay. But I don't want to hear nothing else about my smell, can we agree to that?"

    show braxton smile lookPlayer at Seat4
    with Dissolve(disFactor)

    braxton "Fine by me."

    show braxton smile lookLeft at Seat4
    with Dissolve(disFactor)

    frank "Elli?"

    show  elysia smile lookLeft at Seat3
    with Dissolve(disFactor)

    elysia "You won't hear a peep outta me."

    show frank sit beer lookRight at Seat1
    with Dissolve(disFactor)

    frank "All right then."

    show frank sit beer lookRight at Seat2
    with Dissolve(disFactor)

    "Frank gets settled back into his seat."

    braxton "There, now isn't that better?"

    show elysia smile lookPlayer at Seat3
    with Dissolve(disFactor)

    elysia "Maybe we should get a fan going or something."

    show frank angry lookLeft at Seat2
    show elysia smile lookRight at Seat3
    show braxton smile lookRight at Seat4
    with Dissolve(disFactor)

    frank "Oh, for fuck's sake."


    scene black
    with dissolve

    stop music fadeout 1.0
    pause 1
    show text "{size=70}End of Day{/size}" at truecenter as text3
    with dissolve
    play music "jingle_endOfDayDenoise.wav" noloop
    pause 2
    hide text3
    with dissolve
    pause 3

    jump Day6Block

return