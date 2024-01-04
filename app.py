import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai_api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=genai_api_key)
model = genai.GenerativeModel("gemini-pro")

def main():
    st.set_page_config(page_title="SQL Query Generator", page_icon=":robot:")
    st.markdown(
    """
        <div style="text-align: center;">
            <h1>SQL Query Generator</h1>
            <h3>I can Generate SQL query for you</h3>
            <h4>With explaination as well</h4>
            <p>This tool is a simple tool that allows you to generate SQL queries based on our prompts.</p>
            
        </div>
    """,
    unsafe_allow_html=True
    )
    
    text_input = st.text_area("Enter your query here in plain english")
    
    submit = st.button("Generate SQL Query")
    if submit:
        with st.spinner("Generating SQL Query..."):
            template = """
            Create a SQL query snippet using the below text:
            
            ```
                {text_input}
            ``` 
            I just want a SQL query
            
            """
            formatted_template = template.format(text_input=text_input)
            
            response = model.generate_content(formatted_template)
            sql_query = response.text
            sql_query = sql_query.strip().replace("```sql", "").replace("```", "")
            
            expected_output = """
            What would be the expected response of the above query snippet:
                ```
                    {sql_query}
                ```
            Provide sample tabular response with no explaination
            """
            expected_output_formatted = expected_output.format(sql_query=sql_query)
            eoutput = model.generate_content(expected_output_formatted)
            eoutput = eoutput.text
            
            explaination = """
            Explain this sql query:
                ```
                    {sql_query}
                ```
            Please provide the simplest explanation:
            """
            explaination_formatted = explaination.format(sql_query=sql_query)
            explanation = model.generate_content(explaination_formatted)
            explanation = explanation.text
            
            # Display the generated SQL query, expected output, and explanation
            st.success("SQL Query Generated Successfully! Here is your query below")
            st.code(sql_query, language="sql")
            st.success("Expected Output of this SQL query will be:")
            st.markdown(eoutput)
            st.success("Explanation of this SQL query:")
            st.markdown(explanation)

if __name__ == "__main__":
    main()
