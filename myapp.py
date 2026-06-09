import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Rutwik More | Portfolio",
    page_icon="💼",
    layout="wide"
)

# Header
st.title("👨‍💻 Rutwik More")
st.subheader("Site Reliability Engineer | Application Support Engineer | Cloud & Database Enthusiast")

# Contact Section
st.markdown("""
📍 Pune, Maharashtra  
📧 mrrutwikmore@gmail.com  
📱 +91 7040430010  
🔗 LinkedIn: https://www.linkedin.com/in/rutwikmore/
""")

st.divider()

# Professional Summary
st.header("📝 Professional Summary")

st.write("""
Experienced Site Reliability Engineer with expertise in Linux, Unix, SQL, Oracle Database,
Cloud Platforms (AWS & Azure), Monitoring Tools, ITSM Processes, and Application Support.
Strong background in Incident Management, Root Cause Analysis, Automation, Monitoring,
and Production Support.
""")

# Skills
st.header("🛠️ Technical Skills")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Databases")
    st.write("""
    - Oracle Database
    - Oracle SQL
    - PL/SQL
    - Snowflake SQL
    - SQL Server
    - T-SQL
    """)

with col2:
    st.subheader("Cloud & DevOps")
    st.write("""
    - AWS
    - Azure
    - Azure Data Factory
    - CI/CD
    - Control-M
    - Active Batch
    """)

with col3:
    st.subheader("Monitoring & Tools")
    st.write("""
    - Splunk
    - Grafana
    - LogicMonitor
    - Power BI
    - Jira
    - ServiceNow
    - BMC Remedy
    - Postman
    """)

st.divider()

# Experience
st.header("💼 Professional Experience")

with st.expander("Global Payments Inc. | Site Reliability Engineer | 2025 - Present", expanded=True):
    st.markdown("""
    - Implemented monitoring and alerting solutions.
    - Developed SLA/SLO dashboards and reporting frameworks.
    - Built Power BI and Looker Studio dashboards.
    - Designed ETL processes and operational data pipelines.
    - Performed Incident Management and Root Cause Analysis.
    - Automated operational processes using Power Automate.
    - Supported CI/CD pipelines and cloud infrastructure.
    """)

with st.expander("Capgemini | Senior Software Engineer | 2024 - 2025"):
    st.markdown("""
    - L1/L2 Application and Production Support.
    - Incident Management using ServiceNow and Remedy.
    - SQL and Oracle troubleshooting.
    - Linux/Unix administration support.
    - Snowflake and Azure Data Factory operations.
    - Batch Monitoring using Control-M.
    - Knowledge Base documentation.
    """)

with st.expander("Kyndryl | Software Engineer | 2022 - 2024"):
    st.markdown("""
    - Production Support for Vodafone-Idea applications.
    - Oracle SQL, PL/SQL and Snowflake troubleshooting.
    - Control-M Job Monitoring.
    - Splunk Log Analysis.
    - Unix/Linux Server Support.
    - Incident and Problem Management.
    - Grafana Dashboard Monitoring.
    """)

st.divider()

# Achievements
st.header("🏆 Achievements")

st.success("Outstanding Performance Award - Exceptional Contribution (September 2023)")
st.success("Certificate of Appreciation for Hard Work, Commitment, Ownership & Contribution")

st.divider()

# Projects / Implementations
st.header("🚀 Key Implementations")

st.markdown("""
### 🔹 BASE64 Utility Suite
Developed:
- Base64 to Image Converter
- Image to Base64 Converter
- JSON Validator
- XML Validator

### 🔹 Automated Monitoring Scripts
- SQL Based Monitoring
- Linux Monitoring Scripts
- 50% Faster Response Time
- 40% Improved Uptime

### 🔹 Power BI Dashboards
- Weekly Client Reporting
- KPI Visualization
- Operational Insights
""")

st.divider()

# Certifications
st.header("📜 Certifications")

certs = [
    "Microsoft Certified: Azure Fundamentals (AZ-900)",
    "Introduction to Service Management with ITIL 4"
]

for cert in certs:
    st.write(f"✅ {cert}")

st.divider()

# Education
st.header("🎓 Education")

st.markdown("""
### B.Tech - Computer Engineering
**ATS Sanjay Bhokare Group of Institutes, Miraj**

2018 - 2022

**CGPA: 8.83 / 10**
""")

st.divider()

# Contact Form
st.header("📩 Contact Me")

with st.form("contact_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")

    submitted = st.form_submit_button("Send")

    if submitted:
        st.success("Thank you! Your message has been submitted.")

# Footer
st.divider()

st.markdown(
    """
    <center>
    <h4>Made with ❤️ using Streamlit</h4>
    </center>
    """,
    unsafe_allow_html=True
)