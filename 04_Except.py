while True:
    try:
        number = int(input('Enter your favourite Number\n'))
        print(5/number)
        break
    except ValueError:
        print('Please Enter a valid Number')
    except ZeroDivisionError:
        print("Don't Enter ZERO")
    finally:
        print ('Loop Complete')


