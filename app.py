import streamlit as st
import random
from datetime import date

st.set_page_config(page_title="Brain Trust Admission", page_icon="🎓")

st.title("🎓 NEW BRAIN TRUST")
st.title("ENGLISH MEDIUM SCHOOL")
st.markdown("<h3 style='text-align:center; color:#F2A900;'>Maina, Mwanza | +255 666316803</h3>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;'>📝 Online Admission Form 2026</h4>", unsafe_allow_html=True)
st.info("💰 Registration Fee: **5,000 TZS** - Pay after filling form. Admission Number will be generated instantly.")
st.divider()

with st.form("admission_form"):
    st.subheader("1. Pupil Information")
    pupil_name = st.text_input("Full Name of Pupil *")
    dob = st.date_input("Date of Birth", value=date(2018,1,1), max_value=date.today())
    gender = st.selectbox("Gender", ["Male", "Female"])
    class_applying = st.selectbox("Class Applying For", ["Baby Class", "Middle Class", "Pre-Unit", "Standard 1", "Standard 2", "Standard 3", "Standard 4", "Standard 5", "Standard 6", "Standard 7"])
    prev_school = st.text_input("Previous School (if any)")
    st.subheader("2. Parent / Guardian Information")
    parent_name = st.text_input("Parent / Guardian Full Name *")
    parent_phone = st.text_input("Parent Phone Number *", placeholder="e.g. 0666316803")
    parent_location = st.text_input("Home Location / Street", placeholder="e.g. Maina, Mwanza")
    st.subheader("3. Payment")
    pay_method = st.selectbox("Payment Method for 5,000 TZS", ["M-Pesa", "Tigo Pesa", "Airtel Money", "Cash at School"])
    agree = st.checkbox("I confirm information is correct")
    submitted = st.form_submit_button("✅ SUBMIT APPLICATION", use_container_width=True)

if submitted:
    if not pupil_name or not parent_name or not parent_phone or not agree:
        st.error("⚠️ Please fill all * fields and tick the checkbox.")
    else:
        adm_no = f"BT-2026-{random.randint(1000,9999)}"
        st.success("🎉 CONGRATULATIONS! Application Received!")
        st.balloons()
        st.markdown(f"""
        ### Admission Slip
        **Admission No:** `{adm_no}`
        **Pupil:** {pupil_name}
        **Class:** {class_applying}
        **Parent:** {parent_name} - {parent_phone}
        **Fee to Pay:** 5,000 TZS via {pay_method}
        **School:** New Brain Trust English Medium School, Maina, Mwanza
        **Contact:** +255 666316803
        ---
        📸 **Take a screenshot of this slip and bring it to school with 5,000 TZS.**
        """)

st.divider()
st.markdown("<p style='text-align:center;'>© 2026 New Brain Trust English Medium School - Maina, Mwanza</p>", unsafe_allow_html=True)