
import streamlit as st
import requests
import pandas as pd
from PIL import Image
from io import BytesIO
from openai import OpenAI
import time
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

def fetch_and_display_image(image_url):
    try:
        response = requests.get(image_url)
        response.raise_for_status()  # Checks for HTTP errors
        image_bytes = BytesIO(response.content)
        image = Image.open(image_bytes)
        st.image(image, caption="Image from Bytes", use_column_width=True)
    except requests.exceptions.HTTPError as http_err:
        st.error(f"HTTP error occurred while fetching the image: {http_err}")
    except requests.exceptions.RequestException as req_err:
        st.error(f"An error occurred during the request to get the image: {req_err}")
    except IOError as e:
        st.error(f"An error occurred while trying to open the image: {e}")


def welcome_page():
    st.title("Welcome to Our Application")
    st.write("This is the home page of the application. Navigate using the sidebar to access other tools.")

def value_optimizer():
    # Example to get an image from a web API
    image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/WHU_Logo.svg/800px-WHU_Logo.svg.png"
    fetch_and_display_image(image_url)
    
    st.title("Comprehensive Value Proposition Optimizer")
    st.write("""
            This advanced tool methodically optimizes the value proposition of your company based on a deep, AI-powered analysis of the market and customer feedback. Each step in the prompt chain leverages integrating agents for thorough research and data synthesis.
            """)

    # Secure inputs
    api_key = st.text_input('Enter your OpenAI API key:', type="password")
    company_name = st.text_input('Enter Company Name:', placeholder="Company Name")
    industry = st.text_input('Enter Industry/Market:', placeholder="Industry/Market")
    initial_value_prop = st.text_area('Enter the Initial Value Proposition:', placeholder="Value Proposition", height=150)
    venture_summary = st.text_area('Summary of Core Observations from Venture Research:' , placeholder="Venture Summary", height=300)

    # Button to trigger the optimization process
    analyze_clicked = st.button('Analyze and Optimize')

    if analyze_clicked:
        if api_key and company_name and industry and initial_value_prop and venture_summary:

            st.info("Processing your inputs to conduct extensive research and optimize the value proposition.")
            # Call to function that performs AI interaction and additional research
            if company_name.lower() == {"cuitini", "cuitinni", "kwitini", "quitini", "Cuitini"}:
                # Handle information extraction from an attached document for "cuitini"
                document_path = "documents/Top 500 active Business Angels EU .xlsx"
                try:
                    # Assuming the document is an Excel sheet
                    df = pd.read_excel(document_path)
                    st.write(f"Information from the attached document for {company_name}:")
                    st.dataframe(df)
                    return
                except Exception as e:
                    st.error(f"Failed to load document for {company_name}: {e}")
       
            # Initializing the Chat API
            chat = ChatOpenAI(api_key=api_key)
            current_analysis = initial_value_prop

            # Step 0: Inital Training
            st.markdown('**Step 0: Analyisis of the current Value Proposition**')
            prompt_description = f"You are an AI trained to analyze and enhance company value propositions. Using initial inputs and conducting further online research, provide a comprehensive analysis for the company '{company_name}' in the industry '{industry}'. Consider the initial value proposition '{initial_value_prop}' and venture summary '{venture_summary}', and train yourself to be an expert for this company to elaborate during the next steps based the input and on external data sources."
            system_message = SystemMessagePromptTemplate.from_template(prompt_description)
            human_message = HumanMessagePromptTemplate.from_template(f"Initial Value Proposition: {initial_value_prop}\nVenture Summary: {venture_summary}")
            chat_prompt = ChatPromptTemplate.from_messages([system_message, human_message])
            request = chat_prompt.format_prompt().to_messages()
            result = chat.invoke(request)
            current_analysis = result.content
            st.write(current_analysis)

            # Step 1: Describe the current value proposition
            st.markdown('**Step 1: Describe the Current Value Proposition**')
            prompt_description = f"Describe the current value proposition of {company_name}. Include details on the target audience, key benefits, and how it differentiates from competitors."
            system_message = SystemMessagePromptTemplate.from_template(prompt_description)
            human_message = HumanMessagePromptTemplate.from_template(f"Initial Value Proposition: {initial_value_prop}\nVenture Summary: {venture_summary}")
            chat_prompt = ChatPromptTemplate.from_messages([system_message, human_message])
            request = chat_prompt.format_prompt().to_messages()
            result = chat.invoke(request)
            current_analysis = result.content
            st.write(current_analysis)

            # Step 2: Identify customer segments
            st.markdown('**Step 2: Identify Customer Segments**')
            prompt_description = f"Identify the primary and secondary customer segments for {company_name}. List their main needs, preferences, and pain points related to the company's offerings."
            system_message = SystemMessagePromptTemplate.from_template(prompt_description)
            human_message = HumanMessagePromptTemplate.from_template(f"Venture Summary: {venture_summary}")
            chat_prompt = ChatPromptTemplate.from_messages([system_message, human_message])
            request = chat_prompt.format_prompt().to_messages()
            result = chat.invoke(request)
            current_analysis = result.content
            st.write(current_analysis)

            # Step 3: Analyze the competitive landscape
            st.markdown('**Step 3: Analyze the Competitive Landscape**')
            prompt_description = f"Analyze the competitive landscape for {company_name} in {industry}. Highlight key competitors and compare their value propositions with that of {company_name}."
            system_message = SystemMessagePromptTemplate.from_template(prompt_description)
            human_message = HumanMessagePromptTemplate.from_template(f"Venture Summary: {venture_summary}")
            chat_prompt = ChatPromptTemplate.from_messages([system_message, human_message])
            request = chat_prompt.format_prompt().to_messages()
            result = chat.invoke(request)
            current_analysis = result.content
            st.write(current_analysis)

            # Step 4: Summarize customer feedback
            st.markdown('**Step 4: Summarize Customer Feedback**')
            prompt_description = f"Summarize customer feedback and reviews for {company_name}, focusing on customer satisfaction with the current value proposition. Include any recurring themes or suggestions."
            system_message = SystemMessagePromptTemplate.from_template(prompt_description)
            human_message = HumanMessagePromptTemplate.from_template(f"Venture Summary: {venture_summary}")
            chat_prompt = ChatPromptTemplate.from_messages([system_message, human_message])
            request = chat_prompt.format_prompt().to_messages()
            result = chat.invoke(request)
            current_analysis = result.content
            st.write(current_analysis)

            # Step 5: Conduct a SWOT analysis
            st.markdown('**Step 5: Conduct a SWOT Analysis**')
            prompt_description = f"Conduct a SWOT analysis (Strengths, Weaknesses, Opportunities, Threats) for {company_name} based on the current value proposition and market conditions."
            system_message = SystemMessagePromptTemplate.from_template(prompt_description)
            human_message = HumanMessagePromptTemplate.from_template(f"Venture Summary: {venture_summary}")
            chat_prompt = ChatPromptTemplate.from_messages([system_message, human_message])
            request = chat_prompt.format_prompt().to_messages()
            result = chat.invoke(request)
            current_analysis = result.content
            st.write(current_analysis)

            # Step 6: Propose enhancements to the value proposition
            st.markdown('**Step 6: Propose Enhancements to the Value Proposition**')
            prompt_description = f"Based on the analysis in the previous steps, propose enhancements to the value proposition of {company_name} that align with customer needs and market opportunities."
            system_message = SystemMessagePromptTemplate.from_template(prompt_description)
            human_message = HumanMessagePromptTemplate.from_template(f"Venture Summary: {venture_summary}")
            chat_prompt = ChatPromptTemplate.from_messages([system_message, human_message])
            request = chat_prompt.format_prompt().to_messages()
            result = chat.invoke(request)
            optimized_value_proposition = result.content
            st.write(optimized_value_proposition)
            # Step 7: New optmized Value Proposition
            st.markdown('**Step 7: New optmized Value Proposition**')
            prompt_description = f"Based on the comprehensive analysis of customer needs, market trends, competitive positioning, and internal strengths and weaknesses conducted in the previous steps, craft a new, optimized value proposition for {company_name}. This proposition should clearly state the unique benefits, target customer segments, and how it differentiates from competitors. Also, include rationale for why this new value proposition will meet market demands more effectively and how it aligns with the company’s strategic goals."
            system_message = SystemMessagePromptTemplate.from_template(prompt_description)
            human_message = HumanMessagePromptTemplate.from_template(f"Venture Summary: {venture_summary}")
            chat_prompt = ChatPromptTemplate.from_messages([system_message, human_message])
            request = chat_prompt.format_prompt().to_messages()
            result = chat.invoke(request)
            optimized_value_proposition = result.content
            st.write(optimized_value_proposition)
        else:
            st.error("Please ensure all fields are filled and the API key is provided before proceeding.")
    else:
        st.write("Please fill out all fields and click the button to start the analysis process.")

def chatbot_page():
    st.title('Welcome to the Cuitini Chatbot! - A Chatbot powered by OpenAI')

    # Ask user for api key in password mode and the question

    api_key = st.text_input('Enter your OpenAI API key', type='password')
    user_question = st.text_input("What's your question?", "")
    # Main app logic
    if st.button('Ask'):

        st.info("Processing your inputs to conduct extensive research and optimize the value proposition.")
        #defining the client and the assistant ID
        client = OpenAI(api_key=api_key)
        assistant_id = "asst_AhcbZwpExG3a7ui7oUPfLUtx"  
        thread = client.beta.threads.create()
        if user_question:
            #defining the client and the assistant ID
            
            # Sending the question to OpenAI
            message = client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content= user_question,
            )
            run = client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=assistant_id,
            )
            run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
            )
        # wait until run is completed
            while run.status != 'completed':
                #wait 3 seconds
                time.sleep(3)
                run = client.beta.threads.runs.retrieve(
                    thread_id=thread.id,
                    run_id=run.id
                )
                messages = client.beta.threads.messages.list(
                thread_id=thread.id
                )
            output = messages.data[0].content[0].text.value
            st.text_area("Answer", value=output)
        else:
            st.error("Please enter a question before asking.")


def main():
    st.sidebar.title("DDE Group Assignment")
    selection = st.sidebar.radio("Go to", ["Welcome", "Value Optimizer", "Chatbot"])

    if selection == "Welcome":
        welcome_page()
    elif selection == "Value Optimizer":
        value_optimizer()
    elif selection == "Chatbot":
        chatbot_page()

if __name__ == "__main__":
    main()