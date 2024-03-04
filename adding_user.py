import getpass
import subprocess

def create_user():
    """Creates a new user account with improved security and user experience."""

    while True:
        username = input("Enter a desired username (lowercase letters, numbers, underscores only): ")
        if not username.isalnum() or "_" not in username:
            print("Username must consist of lowercase letters, numbers, and underscores.")
            continue

        # Check for existing user (enhanced with error handling)
        try:
            subprocess.run(["id", username], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print("Username '" + username + "' already exists. Please choose another.")
        except subprocess.CalledProcessError:
            # Username does not exist, proceed

            # Prompt for password (securely with getpass)
            password = getpass.getpass("Enter a strong password (use upper/lowercase letters, numbers, symbols): ")

            # Confirm password (securely with getpass)
            password_confirm = getpass.getpass("Confirm your password: ")
            if password != password_confirm:
                print("Passwords do not match. Please re-enter.")
                continue

            # Create the user account with appropriate shell (enhanced security)
            subprocess.run(["sudo", "useradd", "-m", "-s", "/bin/bash", username])

            # Set the user's password (enhanced security using recommended command)
            subprocess.run(["sudo", "passwd", username])

            print("User '" + username + "' created successfully!")
            break

if __name__ == "__main__":
    create_user()
