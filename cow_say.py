import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("Hello, " + sys.argv[1])
elif len(sys.argv) < 2:
    cowsay.cow("I am hungry, give me a name!")
else:
    cowsay.cow("I am just a cow! Human. I cannot read a lot.")
