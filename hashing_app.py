
import streamlit_authenticator as stauth

# Title of the app
st.title("Password Hashing Tool")

# Define the list of plain-text passwords (you can replace these with your actual passwords)
plain_passwords = [
    "cheatham5a1", "cheatham5b2", "cheatham5c3", "cheatham5t4",
    "cheatham6a5", "cheatham6b6", "cheatham6c7", "cheatham6t8"
]

# Hash the passwords using stauth.Hasher
hashed_passwords = stauth.Hasher(plain_passwords).generate()

# Display the hashed passwords
st.write("Hashed Passwords:")
for password in hashed_passwords:
    st.text(password)  # Display each hashed password

# Optionally, you can provide a button to allow users to copy the hashes
st.download_button(
    label="Download Hashed Passwords",
    data="\n".join(hashed_passwords),
    file_name="hashed_passwords.txt",
    mime="text/plain"
)
