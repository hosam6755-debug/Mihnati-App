import streamlit as st
from pyairtable import Table

# --- إعدادات الربط ---
# انسخ الـ Token الذي يبدأ بـ pat وضعه هنا
AIRTABLE_API_KEY = "patBbzsl2buj1SOx4.fa07df2841811092dd219045b043c14d0bdfa0900e69d6dd42269c563a840191"
BASE_ID = "appHOruhiQ3mRfUZs"
TABLE_NAME = "Table 1"

# الاتصال بالجدول
table = Table(AIRTABLE_API_KEY, BASE_ID, TABLE_NAME)

st.set_page_config(page_title="تطبيق مهنتي", page_icon="💼")

# --- واجهة التطبيق ---
st.title("💼 إضافة إعلان وظيفي")

with st.form("job_form", clear_on_submit=True):
    title = st.text_input("المسمى الوظيفي")
    company = st.text_input("اسم الشركة")
    city = st.text_input("المدينة")
    description = st.text_area("وصف الوظيفة والمتطلبات")
    
    submit = st.form_submit_button("حفظ ونشر")

    if submit:
        if title and company:
            # إرسال البيانات إلى Airtable
            table.create({
                "title": title,
                "company": company,
                "city": city,
                "description": description
            })
            st.balloons()
            st.success("تم نشر إعلانك بنجاح وحفظه في القاعدة!")
        else:
            st.error("يرجى ملء الحقول الأساسية (المسمى والشركة)")

st.markdown("---")
st.subheader("🔍 الوظائف المضافة حديثاً")

# جلب الوظائف من Airtable وعرضها
try:
    records = table.all()
    for record in records:
        job = record['fields']
        with st.expander(f"📌 {job.get('title')} - {job.get('company')}"):
            st.write(f"📍 *المدينة:* {job.get('city')}")
            st.write(f"📝 *الوصف:* {job.get('description')}")
except:
    st.info("اكتب أول وظيفة لتظهر هنا!")