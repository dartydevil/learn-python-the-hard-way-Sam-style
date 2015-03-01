ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

le len(stuff) != 10:
 next_one = more_stuff.pop()
 print "Adding: ", next_one
 stuff.append(next_one)
 print "There are %d items now." % len(stuff)

nt "There we go: ", stuff

nt "Let's do some things with stuff."

nt stuff[1]
nt stuff[-1] #whoa! fancy
nt stuff.pop()
nt ' '.join(stuff) #what? cool!
nt '#'.join(stuff[3:5]) # super stellar!
