import streamlit as st

st.set_page_config(page_title="تطبيق مهنتي", page_icon="💼")

# تهيئة ذاكرة تخزين مؤقتة للوظائف
if 'jobs_list' not in st.session_state:
    st.session_state['jobs_list'] = [
        {"المسمى": "محاسب", "الشركة": "شركة الحلول", "المدينة": "الرياض", "الوصف": "خبرة سنتين"}
    ]

st.title("💼 تطبيق مـهـنـتـي")

menu = ["تصفح الوظائف", "إضافة وظيفة جديدة"]
choice = st.sidebar.selectbox("القائمة", menu)

if choice == "تصفح الوظائف":
    st.subheader("🔍 الوظائف المتاحة")
    for job in st.session_state['jobs_list']:
        with st.expander(f"📌 {job['المسمى']} - {job['الشركة']}"):
            st.write(f"📍 *المدينة:* {job['المدينة']}")
            st.write(f"📝 *الوصف:* {job['الوصف']}")

elif choice == "إضافة وظيفة جديدة":
    st.subheader("🏢 إضافة إعلان وظيفي")
    with st.form("job_form", clear_on_submit=True):
        title = st.text_input("المسمى الوظيفي")
        company = st.text_input("اسم الشركة")
        city = st.text_input("المدينة")
        desc = st.text_area("وصف الوظيفة")
        submit = st.form_submit_button("حفظ ونشر")
        
        if submit:
            new_job = {"المسمى": title, "الشركة": company, "المدينة": city, "الوصف": desc}
            st.session_state['jobs_list'].append(new_job)
            st.success(f"تم نشر وظيفة '{title}' بنجاح! اذهب لقسم التصفح لرؤيتها.")