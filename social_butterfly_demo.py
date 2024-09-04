import streamlit as st
import os
from openai import OpenAI

# Set up OpenAI client (you'll need to set your API key)
client = OpenAI(api_key="your-api-key-here")

# Set page config
st.set_page_config(layout="wide", page_title="Social Butterfly AI")

# Custom CSS with updated font color for all headers
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
    
    body {
        font-family: 'Roboto', sans-serif;
        color: #E0E0E0;
        background-color: #1E1E1E;
    }
    .stButton>button {
        font-family: 'Roboto', sans-serif;
        color: #4CAF50;
        border-radius: 20px;
        border: 2px solid #4CAF50;
        background-color: transparent;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #4CAF50;
        color: white;
    }
    .stTextInput>div>div>input {
        font-family: 'Roboto', sans-serif;
        color: #E0E0E0;
        background-color: #2E2E2E;
        border-radius: 20px;
    }
    .stSelectbox>div>div>select {
        font-family: 'Roboto', sans-serif;
        color: #E0E0E0;
        background-color: #2E2E2E;
        border-radius: 20px;
    }
    h1, h2, h3, .feature-header {
        font-family: 'Roboto', sans-serif;
        color: #fa6c4 !important;
    }
    .feature-text {
        color: #E0E0E0;
    }
</style>
""", unsafe_allow_html=True)

# Header Image
header_image_path = "social butterfly headshot.png"
if os.path.exists(header_image_path):
    st.image(header_image_path, use_column_width=True)
else:
    st.write(f"Header image not found. Make sure '{header_image_path}' is in the same folder as your Python script.")

# Main content
st.title("🦋 Social Butterfly AI")

# Hero Section
st.markdown("""
<h2>Elevate Your Social Media Presence</h2>
<p>Harness the power of AI to revolutionize your social media strategy. 
From content creation to analytics, we've got you covered.</p>
""", unsafe_allow_html=True)

# Feature Thumbnails
st.subheader("Our Features")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div style='background-color: #2E2E2E; padding: 20px; border-radius: 10px;'>
        <h3 class="feature-header">Content Creation</h3>
        <p class="feature-text">AI-powered content generation for all your social media needs.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style='background-color: #2E2E2E; padding: 20px; border-radius: 10px;'>
        <h3 class="feature-header">Analytics Dashboard</h3>
        <p class="feature-text">Comprehensive insights into your social media performance.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style='background-color: #2E2E2E; padding: 20px; border-radius: 10px;'>
        <h3 class="feature-header">SEO Optimization</h3>
        <p class="feature-text">Boost your content's visibility with AI-driven SEO strategies.</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div style='background-color: #2E2E2E; padding: 20px; border-radius: 10px;'>
        <h3 class="feature-header">Trend Analysis</h3>
        <p class="feature-text">Stay ahead of the curve with real-time trend insights.</p>
    </div>
    """, unsafe_allow_html=True)

# Chat Option
st.header("Chat with Social Butterfly AI")
user_input = st.text_input("Ask me anything about social media strategy:")
if st.button("Get Answer") and user_input:
    # Here we'll provide a more detailed mock response
    response = f"To dominate in content creation, consider these key strategies:\n\n" \
               f"1. Understand your audience: Research their preferences and pain points.\n" \
               f"2. Develop a consistent brand voice: This helps in building recognition.\n" \
               f"3. Create a content calendar: Plan your posts in advance for consistency.\n" \
               f"4. Use a mix of content types: Incorporate text, images, videos, and infographics.\n" \
               f"5. Engage with your audience: Respond to comments and encourage discussions.\n" \
               f"6. Analyze and adapt: Use analytics to understand what works and refine your strategy.\n\n" \
               f"Remember, dominating content creation is about providing value consistently and engaging meaningfully with your audience."
    st.write(response)

# Create Artwork Section
st.header("Create Artwork")
prompt = st.text_input("Describe the artwork you want to generate:")
if st.button("Generate Artwork") and prompt:
    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        image_url = response.data[0].url
        st.image(image_url, caption="Generated Artwork")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Call-to-Action
st.markdown("""
<div style='background-color: #2E2E2E; padding: 20px; border-radius: 10px; text-align: center; margin-top: 30px;'>
    <h2>Ready to Transform Your Social Media Strategy?</h2>
    <p>Sign up now to access all features and start your journey to social media success!</p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div style='text-align: center; margin-top: 50px;'>
    <p>© 2023 Social Butterfly AI. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)
