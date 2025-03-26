import streamlit as st
import string
import random
import re

def generate_password(length, use_digits, use_special_characters):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits

    if use_special_characters:
        characters += string.punctuation

    return ''.join(random.choice(characters) for i in range (length))


def check_password_strength(password):
    score = 0
    common_Passwords = ["12345678","äbc123","Khan123","pakistan123","password"]
    if password in common_Passwords:
        return "❌ This password is too common. Choose a more unique one.", "Weak"
    
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔹 Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1 
    else:
        feedback.append("🔹 Include both uppercase and lowercase letters.")
        
    if re.search(r"\d",password):
        score += 1
    else:
        feedback.append("🔹 Add at least one number (0-9).")
        
    if re.search(r"[!@#$%^&*]",password):
        score += 1
    else:
        feedback.append("🔹 Include at least one special character (!@#$%^&*).")
    
    if score == 4:
        return "✅ Strong Password!", "Strong"
    elif score == 3:
        return "⚠️ Moderate Password - Consider adding more security features.", "Moderate"
    else:
        return "\n".join(feedback),"Weak"

check_password = st.text_input("Enter your password", type = "password")
if st.button("Check Strength"):
    if check_password:
        result , Strength = check_password_strength(check_password)
        if Strength == "Strong":
            st.success(result)
            st.balloons()
        elif Strength == "Moderate":
            st.warning(result)
        else:
            st.error("Weak Password! Improve your password using these tips:")
            for tip in result.split("\n"):
                st.write(tip)

    else:
        st.warning("Please enter a password")


length = st.number_input("Enter the length of the password", min_value = 8, max_value = 15, value = 10) 
use_digits = st.checkbox("Use digits (0-9)")
use_special_characters = st.checkbox("Use special characters (!@#$%^&*)")
if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special_characters)
    st.success(f"Your password is: {password}")
