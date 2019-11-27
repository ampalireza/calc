while 1==1 :
    print("                               celcom to amp calculator")

    print ("enter '+' tow numbera")
    print ("enter '-' tow numbera")
    print ("enter '*' tow numbera")
    print ("enter '/' tow numbera")
    print ("enter 'exit' tow numbera")
    user_input = input(print(":  "))
    if user_input == "quit" :
        print("exit")
        break
    elif user_input == "+":
        num1 = float (input(print("first number: ")))
        num2 = float (input(print("plaes inter secnd number: ")))
        result = str(num1 + num2)
        print("result="+result)
    elif user_input == "-":
        num1 =float ( input(print("first number: ")))
        num2 = float (input(print("plaes inter secnd number: ")))
        result = str(num1 - num2)
        print("result="+result)
    elif user_input == "*":
        num1 = float (input(print("first number: ")))
        num2 = float (input(print("plaes inter secnd number: ")))
        result = str(num1 * num2)
        print("result="+result)
    elif user_input == "/":
        num1 =float ( input(print("first number: ")))
        num2 =float ( input(print("plaes inter secnd number: ")))
        result = str(num1 / num2)
        print("result="+result)
    else:
        print ("plaes enter correct value")
