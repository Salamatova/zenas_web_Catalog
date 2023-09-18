import streamlit as st
import snowflake.connector

# Set the Streamlit app title
st.title("My Parent's New Healthy Diner")

# Get the Snowflake secrets from Streamlit secrets
snowflake_secrets = st.secrets["snowflake"]

# Create a Snowflake connection using the secrets
try:
    conn = snowflake.connector.connect(
        user=snowflake_secrets["user"],
        password=snowflake_secrets["password"],
        account=snowflake_secrets["account"],
        warehouse=snowflake_secrets["warehouse"],
        database=snowflake_secrets["database"],
        schema=snowflake_secrets["schema"]
    )

    cursor = conn.cursor()

    # Execute a Snowflake query
    cursor.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
    data_row = cursor.fetchone()

    # Display the Snowflake query result in Streamlit
    st.text("Hello from Snowflake:")
    st.text(data_row)

except Exception as e:
    st.error(f"Error: {str(e)}")

finally:
    # Close the Snowflake cursor and connection
    cursor.close()
    conn.close()
