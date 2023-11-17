import pickle 
from pathlib import Path

import streamlit_authenticator as stauth


names =["Matthias Maia ", "Helena Navis"]
usernames = ["matthias.maia", "helena.navis"]
passwords = ["matthias123", "helena123"]

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent /"hashed_pw.pkl"
with file_path.open('wb') as file:
    pickle.dump(hashed_passwords,file)
