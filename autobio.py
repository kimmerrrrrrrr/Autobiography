import streamlit as st
import folium
import base64
from streamlit_folium import st_folium

st.set_page_config(layout="wide")

st.sidebar.title("Go To: ")
if 'section' not in st.session_state:
    st.session_state.section = "Autobiography"

if st.sidebar.button("Autobiography"):
    st.session_state.section = "Autobiography"
if st.sidebar.button("Portfolio"):
    st.session_state.section = "Portfolio"
if st.sidebar.button("Contact"):
    st.session_state.section = "Contact"

if st.session_state.section == "Autobiography":
    st.title("About Me")

    with open(r"orangeme.png", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()

    html_content = f"""
    <div style="display: flex; margin-bottom: 20px;">
        <div style="flex: 1; margin-right: 20px;">
            <div>
                <img src="data:image/png;base64,{encoded_string}" style="border-radius: 15px; width: 100%; max-width: 300px;">
            </div>
        </div>
        <div style="flex: 2;">
            <div>
                <h3>Vargas Kim B.</h3>
                <p><strong>Birthday: </strong>October 11, 2000</p>
                <p><strong>Address: </strong>Brgy. Campina, Hilongos, Leyte.</p>
                <p><strong>Phone Number: </strong>+639672880301</p>
                <p><strong>Institutional Email: </strong>kim.vargas@cit.edu</p>
                <p><strong>Personal Email: </strong>vargaskim0@gmail.com</p>
            </div>
        </div>
    </div>

    <div style="margin-bottom: 20px;">
        <details>
            <summary style="font-weight: bold; cursor: pointer;">Education</summary>
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; padding: 10px; background-color: #ADEDBF; border: 1px solid #dee2e6; border-radius: 5px;">
                <div style="background-color:#C6F4E3; padding: 10px; border-radius: 5px;">
                    <h4>Junior High School</h4>
                    <p><b>Hilongos National Vocational School</b></p>
                    <p>Majored in PC Hardware Servicing</p>
                </div>
                <div style="background-color:#C6F4E3; padding: 10px; border-radius: 5px;">
                    <h4>Senior High School</h4>
                    <p><b>Hilongos National Vocational School</b></p>
                    <p>Strand: Science, Technology, Engineering, and Mathematics</p>
                </div>
                <div style="background-color:#C6F4E3; padding: 10px; border-radius: 5px;">
                    <h4>College</h4>
                    <p><b>Cebu Institute of Technology University</b></p>
                    <p>Bachelor of Science in Information Technology</p>
                </div>
            </div>
        </details>
    </div>
    """

    st.markdown(html_content, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div style="background-color: #B3E7D0; border: 1px solid #B3E7D0; border-radius: 5px; padding: 10px; margin-bottom: 10px;">
            <details>
                <summary style="font-weight: bold; cursor: pointer;">👋 Hello!</summary>
                <p>Hi! I'm Kim Vargas, currently a college student majoring in BS in Information Technology. Most of my days are filled with coding, coding, and a bit of coding!</p>
            </details>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="background-color: #82DFC6; border: 1px solid #82DFC6; border-radius: 5px; padding: 10px; margin-bottom: 10px;">
            <details>
                <summary style="font-weight: bold; cursor: pointer;">👨‍👩‍👧‍👧 My Family</summary>
                <p>- <strong>Mother:</strong> Anna Lissa Bulfa, who is an OFW in Malaysia.</p>
                <p>- <strong>Father:</strong> Edgar Vargas, known for being rude when drunk and is now dead.</p>
                <p>- <strong>Sisters:</strong> Ria Marie Vargas and Rhona Mae Vargas, who are striving in their own lives.</p>
            </details>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="background-color: #82DFC6; border: 1px solid #82DFC6; border-radius: 5px; padding: 10px; margin-bottom: 10px;">
            <details>
                <summary style="font-weight: bold; cursor: pointer;">🎨 Favorite Color</summary>
                <p>My favorite colors are the different shades of green, which I find to be relaxing and fresh.</p>
            </details>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="background-color: #B3E7D0; border: 1px solid #B3E7D0; border-radius: 5px; padding: 10px; margin-bottom: 10px;">
            <details>
                <summary style="font-weight: bold; cursor: pointer;">🚀 Future Goals</summary>
                <p>Looking ahead, I'm excited to have my frontal lobe develop and make more serious decisions in life. My time in college is all about exploring new interests and making the most out of every opportunity.</p>
            </details>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="background-color: #B3E7D0; border: 1px solid #B3E7D0; border-radius: 5px; padding: 10px; margin-bottom: 10px;">
            <details>
                <summary style="font-weight: bold; cursor: pointer;">🔮 My Zodiac Sign</summary>
                <p>I am a Libra, which means I always strive for harmony in life.</p>
            </details>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="background-color: #82DFC6; border: 1px solid #82DFC6; border-radius: 5px; padding: 10px; margin-bottom: 10px;">
            <details>
                <summary style="font-weight: bold; cursor: pointer;">🎨 Hobbies</summary>
                <p>In my free time, I love to play online games (DOTA2, HOK). Some of my favorite pastimes include reading fictional books, painting, and bed-rotting.</p>
            </details>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="background-color: #82DFC6; border: 1px solid #82DFC6; border-radius: 5px; padding: 10px; margin-bottom: 10px;">
            <details>
                <summary style="font-weight: bold; cursor: pointer;">🍎 Favorite Fruits</summary>
                <p>I absolutely adore fruits! Some of my favorites are Oranges, Watermelons, Grapes, Kiwis, Rambutans, Mangosteens, and more. One of my dreams is to travel the world so that I can taste every fruit that exists.</p>
            </details>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="background-color: #B3E7D0; border: 1px solid #B3E7D0; border-radius: 5px; padding: 10px; margin-bottom: 10px;">
            <details>
                <summary style="font-weight: bold; cursor: pointer;">📚 My Academic Journey</summary>
                <p>My college journey has been a whirlwind. In 2019 I originally enrolled as an Architecture student but then the Covid-19 pandemic hit and affected my mental health. I just accepted that I had lost my passion and hope it'll come back in the future.</p>
                <p>I've explored subjects from Solid Mensuration, Statics, Architectural Designs, and Building Utilities to Data Structures, Object-Oriented Programming, Data Analytics, and other IT-related ones.</p>
            </details>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background-color: #52D5B2; border: 1px solid #52D5B2; border-radius: 5px; padding: 10px; margin-bottom: 20px;">
        <details>
            <summary style="font-weight: bold; cursor: pointer;">🎉 Fun Facts About Me</summary>
            <ul>
                <li>I'm always up for anything spontaneous.</li>
                <li>I like complaining about coding hahaha</li>
                <li>Listening to music while doing anything is a big part of me.</li>
            </ul>
        </details>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("My Hometown")
        latitude = 10.371087
        longitude = 124.783260

        mymap = folium.Map(location=[latitude, longitude], zoom_start=17)
        folium.Marker([latitude, longitude], popup="Campina, Hilongos, Leyte").add_to(mymap)
        st_folium(mymap, width=500, height=300)

    with col2:
        st.subheader("My Current Place")
        latitude = 10.295059
        longitude = 123.889283

        mymap = folium.Map(location=[latitude, longitude], zoom_start=17)
        folium.Marker([latitude, longitude], popup="JM Basa, San Nicholas Central, Cebu").add_to(mymap)
        st_folium(mymap, width=500, height=300)

elif st.session_state.section == "Portfolio":
    st.title("Portfolio")

    col1, col2 = st.columns([3, 2])

    with col1:
        st.subheader("School Projects and other stuff")
        st.write("1. **Bayad Uy!!**: This is a project I made in our mobile dev subject. ")
        st.write("2. **Calculator**: A practice exercise in the past.")
        st.write("3. **MilestoneMate**: An unfinished project during our App Dev")
        st.write("4. **Dashboard**: A dashboard of the CebuStay website.")
        st.write("5. **Color Sequence Game**: A fun little game during IE 1.")

    with col2:
        st.subheader("Here:")
        st.markdown("[Bayad Uy!!](https://cebuinstituteoftechnology-my.sharepoint.com/:u:/g/personal/kim_vargas_cit_edu/Eb3abwjqE_1HtweqlbsFx-MBd8AIb_VkBEFtYKdPWjV_5A?e=2inDpG)")
        st.markdown("[Calculator](https://github.com/kimmerrrrrrrr/Calculator.git)")
        st.markdown("[MilestoneMate](https://github.com/kimmerrrrrrrr/MilestoneMate.git)")
        st.markdown("[CebuStay](https://github.com/kimmerrrrrrrr/Dashboard2.git)")
        st.markdown("[Color Sequence](https://github.com/kimmerrrrrrrr/Color-Sequence.git)")


elif st.session_state.section == "Contact":
    st.title("Contact Me")
    
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submit = st.form_submit_button("Send")

        if submit:
            st.write(f"Thank you, {name}! Your message has been sent.")
    
    st.write("You can also find me on:")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/kim-vargas-a28070310/)")
    st.markdown("[GitHub](https://github.com/kimmerrrrrrrr)")
    st.markdown("[Facebook](https://www.facebook.com/kim.vargas.75098364?mibextid=ZbWKwL)")


st.markdown("---")
st.write("© Vargas, Kim - All Rights Reserved")
