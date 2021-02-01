import streamlit as st

ds, aws, fs = [], [], []

st.title('Path Advisor')

st.write("Select which of the following do you know")
ch1 = st.checkbox("Git")
ch2 = st.checkbox("SQL Basics")
ch3 = st.checkbox("Linux Essentials")
ch4 = st.checkbox("Python")

coding_dict = {"I love too much": {"ds": 2, "aws": 1, "fs": 3},
               "I like": {"ds": 1, "aws": 2, "fs": 3},
               "So so": {"ds": 3, "aws": 2, "fs": 1},
               "I don't like": {"ds": 2, "aws": 3, "fs": 1}}

coding = st.selectbox("Grade your coding", list(coding_dict.keys()))

ds.append(coding_dict[coding]["ds"])
aws.append(coding_dict[coding]["aws"])
fs.append(coding_dict[coding]["fs"])

acad_back_dict = {"Math/Statistics": {"ds": 3, "aws": 1, "fs": 2},
                  "Engineer": {"ds": 2, "aws": 1, "fs": 3},
                  "Balanced": {"ds": 2, "aws": 3, "fs": 1},
                  "Social": {"ds": 1, "aws": 3, "fs": 2}}

acad = st.selectbox("Select your academical background", list(acad_back_dict.keys()))

ds.append(acad_back_dict[acad]["ds"])
aws.append(acad_back_dict[acad]["aws"])
fs.append(acad_back_dict[acad]["fs"])

com_skill_dict = {"Very good": {"ds": 3, "aws": 1, "fs": 2},
                  "Good": {"ds": 3, "aws": 2, "fs": 1},
                  "So so": {"ds": 1, "aws": 2, "fs": 3},
                  "Bad": {"ds": 1, "aws": 3, "fs": 2}}

com_skill = st.selectbox("Select your communication skill level", list(com_skill_dict.keys()))

ds.append(com_skill_dict[com_skill]["ds"])
aws.append(com_skill_dict[com_skill]["aws"])
fs.append(com_skill_dict[com_skill]["fs"])

eng_level_dict = {"Advanced": {"ds": 3, "aws": 1, "fs": 2},
                  "High Intermediate": {"ds": 2, "aws": 1, "fs": 3},
                  "Intermediate": {"ds": 2, "aws": 3, "fs": 1},
                  "Beginner": {"ds": 1, "aws": 3, "fs": 2}}

eng_level = st.selectbox("Select your English level", list(eng_level_dict.keys()))

ds.append(eng_level_dict[eng_level]["ds"])
aws.append(eng_level_dict[eng_level]["aws"])
fs.append(eng_level_dict[eng_level]["fs"])

job_urgency_dict = {"Very urgent": {"ds": 1, "aws": 3, "fs": 2},
                    "Urgent": {"ds": 2, "aws": 3, "fs": 1},
                    "So so": {"ds": 2, "aws": 1, "fs": 3},
                    "No Urgency": {"ds": 3, "aws": 1, "fs": 2}}

job_urgency = st.selectbox("Select your finding job urgency", list(job_urgency_dict.keys()))

ds.append(job_urgency_dict[job_urgency]["ds"])
aws.append(job_urgency_dict[job_urgency]["aws"])
fs.append(job_urgency_dict[job_urgency]["fs"])

it_back_dict = {"Advanced": {"ds": 2, "aws": 1, "fs": 3},
                "High Intermediate": {"ds": 3, "aws": 1, "fs": 2},
                "Intermediate": {"ds": 1, "aws": 3, "fs": 2},
                "Beginner": {"ds": 2, "aws": 3, "fs": 1}}

it_back = st.selectbox("Select your IT background level", list(it_back_dict.keys()))

ds.append(it_back_dict[it_back]["ds"])
aws.append(it_back_dict[it_back]["aws"])
fs.append(it_back_dict[it_back]["fs"])

path_dict = {"Data Science": sum(ds),
             "AWS & DevOps": sum(aws),
             "Full Stack Development": sum(fs)}

result = sorted(path_dict.items(), key=lambda x: x[1], reverse=True)[0][0]

url_dict = {"Data Science": "https://clarusway.com/data-science/",
            "AWS & DevOps": "https://clarusway.com/aws-devops/",
            "Full Stack Development": "https://clarusway.com/full-stack-developer/"}

if st.button("Recommend"):
    if all([ch2, ch3, ch4]):
        st.success(f"You can pass IT Fundamentals Program and We recommend you '{result}' Program.")
        path_link = "<a href='"+url_dict[result]+"'>Go to '"+result+"' page</a>"
        st.markdown(path_link, unsafe_allow_html=True)
    else:
        st.error("We recommend you 'IT Career Programs for Beginners'")
        path_link = "<a href='https://clarusway.com/beginner/'>Go to 'IT Career Programs for Beginners' page</a>"
        st.markdown(path_link, unsafe_allow_html=True)
