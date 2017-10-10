name='Zed A. Shaw'
age=35 #not a lie
height = 74 #in
weight = 180 #lbs
metric_height = height * 2.54
metric_weight = weight * .45359
eyes='Blue'
teeth='White'
hair='Brown'

print "Let's talk about %s." % name
print "He's %s inches tall." % height
print "He's %s pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, and %d I get %d." % (
    age, weight, age + weight)
print "He's %r centimeters tall." % metric_height
print "He's %r kilograms heavy." % metric_weight
