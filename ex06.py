
#Python function pulls the value although its not announced anywhere else
#string in a string 1
x = "There are %d types of people." % 10
#naming variable
binary = "binary"
#naming variable
do_not = "don't"

#assigning sentence to variable and calling other assigned variables
#string in a string 2
y = "Those who know %s and those who %s." % (binary, do_not)

#printing sentences by their variables
print x
print y

#prints left side of sentence, calls a format and assignes variable which completes the rest of the sentence
#string in a string 3
print "I said: %r" % x
print "I also said: '%s'" % y

#names variable hilarious to false
hilarious = False

#names variable to rep a sentence and include the ref to another variable to be named
#string in a string 4
joke_evaluation = "Isn't that joke so funny?! %r"

#calls upon 2 variables and puts them side-by-side
#string in a string 5
print joke_evaluation % hilarious

#calls variables rep by parts of a sentence
w = "This is the left side of ..."
e = "a string with a right side."

#adds the first variable's value to the other in the same order
#w+e makes a longer string because the two assigned sentences assigned to the variables are long
print w + e
