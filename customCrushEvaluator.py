print("\nWelcome to the boy evaluator, where you can evaluate your crush's qualities to find out if you should ask him or her out!\n")


print("Now, think of 5 qualities you want in a boy/girl.")
print("\nEnter the first quality:")
q1 = input()

print("\nEnter the second quality:")
q2 = input()

print("\nEnter the third quality:")
q3 = input()

print("\nEnter the fourth quality:")
q4 = input()

print("\nEnter the fifth quality:")
q5 = input()

print("\nThe 5 qualities you chose are: 1.) " + q1 + ", 2.) " + q2 + ", 3.) " + q3 + ", 4.) " + q4 + ", and 5.) " + q5 + ".\n")
print("To change a quality, type a number ('1' to change the first quality, etc). To confirm the qualities, type 'confirm'.")
changeQuality = input()
if changeQuality == "1":
    print("\nRe-enter the first quality:")
    q1 = input()
    print("You changed the first quality to: " + q1 +".")
elif changeQuality == "2":
    print("\nRe-enter the second quality:")
    q2 = input()
    print("You changed the second quality to: " + q2 +".")
elif changeQuality == "3":
    print("\nRe-enter the third quality:")
    q3 = input()
    print("You changed the third quality to: " + q3 +".")
elif changeQuality == "4":
    print("\nRe-enter the fourth quality:")
    q4 = input()
    print("You changed the fourth quality to: " + q4 +".")
elif changeQuality == "5":
    print("\nRe-enter the fifth quality:")
    q5 = input()
    print("You changed the fifth quality to: " + q5 +".")
else:
    print("You confirmed the qualities!")

print("Now, enter your crush's name.")
boyName = input()
print("Your crush's name is " + boyName+"\n")

print("\nNow, for each question, answer \"yes,\" \"no,\" or \"I don't know.\"\n")

print("Does " + str(boyName) + " have the quality: " + str(q1)+ "?")
isQ1 = input()
print("You answered " +isQ1+".\n")

print("Does " + str(boyName) + " have the quality: " + str(q2)+ "?")
isQ2 = input()
print("You answered " +isQ2+".\n")

print("Does " + str(boyName) + " have the quality: " + str(q3)+ "?")
isQ3 = input()
print("You answered " +isQ3+".\n")

print("Does " + str(boyName) + " have the quality: " + str(q4)+ "?")
isQ4 = input()
print("You answered " +isQ4+".\n")

print("Does " + str(boyName) + " have the quality: " + str(q5)+ "?")
isQ5 = input()
print("You answered " +isQ5+".\n")

def evaluateBoy(name, firstQuality, secondQuality, thirdQuality, fourthQuality, fifthQuality):
    counter = 0
    name = boyName
    firstQuality = isQ1
    secondQuality = isQ2
    thirdQuality = isQ3
    fourthQuality = isQ4
    fifthQuality = isQ5

    if isQ1 == "yes":
        counter += 1
        print(name + " has the quality " + q1 + ".")
        print(name +" has met "+ str(counter) + " conditions so far.\n")
    else:
        print(name + " doesn't have the quality " + q1 + ".")
        print(name + " has met "+ str(counter) + " conditions so far.\n")
    if isQ2 ==  "yes":
        counter += 1
        print(name + " has the quality " + q2 + ".")
        print(name + " has met "+ str(counter) + " conditions so far.\n")
    else:
        print(name + " doesn't have the quality " + q2 + ".")
        print(name + " has met "+ str(counter) + " conditions so far.\n")
    if isQ3 ==  "yes":
        counter += 1
        print(name + " has the quality " + q3 + ".")
        print(name + " has met "+ str(counter) + " conditions so far.\n")
    else:
        print(name + " doesn't have the quality " + q3 + ".")
        print(name + " has met "+ str(counter) + " conditions so far.\n")
    if isQ4 ==  "yes":
        counter += 1
        print(name + " has the quality " + q4 + ".")
        print(name + " has met "+ str(counter) + " conditions so far.\n")
    else:
        print(name + " doesn't have the quality " + q4 + ".")
        print(name + " has met "+ str(counter) + " conditions so far.\n")
    if isQ5 ==  "yes":
        counter += 1
        print(name + " has the quality " + q5 + ".")
        print(name + " has met "+ str(counter) + " conditions so far.\n")
    else:
        print(name + " doesn't have the quality " + q5 + ".")
        print(name + " has met "+ str(counter) + " conditions so far.\n")

    return counter

def shouldYouDate(name, counter, conditions):
    crushName = name
    numberCondMet = counter
    conditionCount = conditions
    conditionReq = conditionCount - 1
    print(name +" met " + str(counter) + " of " + str(conditionCount) + " conditions.")
    if counter >= conditionReq:
        print("Congrats! " + name + " is worthy to date you!\n")
    else:
        print("You should find someone else who meets more conditions.\n")

count = evaluateBoy(boyName, isQ1, isQ2, isQ3, isQ4, isQ5)

shouldYouDate(boyName, count, 5)
