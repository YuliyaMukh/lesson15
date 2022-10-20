import task00

def main():
    password = input("Input your strong password: ")
    result = strong_password(password)

    msg = f"Your password is{result}" if isinstance(result, str) \
        else "User data invalid"

    print("Your password is "+ msg)

if __name__=="__main__":
    main()