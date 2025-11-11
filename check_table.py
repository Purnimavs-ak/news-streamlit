import psycopg2

# Replace these with your actual RDS credentials
host = "your-rds-endpoint"
database = "your-database-name"
user = "your-username"
password = "your-password"

try:
    # Connect to RDS
    conn = psycopg2.connect(
        host="news-sentiment-db.coh8oyk4wij8.us-east-1.rds.amazonaws.com",
        database="news-sentiment-db",
        user="purnima_admin",
        password="AlwysFrvr07"
    )
    cur = conn.cursor()

    # Check if table exists
    cur.execute("""
        SELECT table_name 
        FROM information_schema.tables 
        WHERE table_name = 'news_data';
    """)

    result = cur.fetchone()
    if result:
        print("✅ Table 'news_data' exists!")
    else:
        print("❌ Table 'news_data' does NOT exist.")

except Exception as e:
    print("Error:", e)

finally:
    if cur:
        cur.close()
    if conn:
        conn.close()
