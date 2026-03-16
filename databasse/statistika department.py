from database import get_connection

def en_yuksek_maas():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM isciler
        ORDER BY maas DESC
        FETCH FIRST 1 ROWS ONLY
    """)

    result = cursor.fetchone()

    conn.close()

    return result