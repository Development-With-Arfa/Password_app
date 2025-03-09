import streamlit as st
import random
import string
import os
import re

def password_gen(size):
    characters = string.digits + string.ascii_letters + string.punctuation
    generated_pswd = "".join(random.choice(characters) for x in range(size))
    return generated_pswd

def main():
    st.title("Password Strength Classifier")
    st.subheader("With Streamlit")

    activities = ["Classify Password", "Generate Password"]
    choice = st.sidebar.selectbox("Select Activity", activities)

    if choice == "Classify Password":
        st.subheader("Classifying Password")
        password = st.text_input("Enter the password", type="password")
        feedback = []
        score = 0
        if password:
            if len(password) >= 8:
                score += 1
            else:
                feedback.append("❌Password must be at least 8 characters long")

            if re.search(r"[A-Z]", password) and (r"[a-z]", password):
                score += 1
            else:
                feedback.append("❌Password should contain both upper case anf lower case characters")

            if re.search(r"\d", password):
                score += 1
            else:
                feedback.append("❌Password should contain at least one number")

            if re.search(r"[!@#$%^&*]", password):
                score +=1
            else:
                feedback.append("❌Password should contain at least one special character")

            if score == 4:
                st.success("✅ Password is strong.🎉")
            elif score == 3:
                feedback.append("⚠️ Password is medium. It could be stronger.")
            else:
                st.error("❌Password is weak")

            if feedback:
                st.markdown("## Improvement Suggestions")
                for tip in feedback:
                    st.write(tip)
        else:
            st.info("Please Enter your passsword to get started.")
    


    elif choice == "Generate Password":
        st.subheader("Generate Random Password")
        number = st.number_input("Enter the length of password",8,25)
        st.write(number)
        if st.button("Generate"):
            custom_password = password_gen(number)
            st.write(custom_password)
    
if __name__=="__main__":
    main()