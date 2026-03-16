from database import get_connection
from validation import validate_isci

def add_isci(ad, maas):

    validate_isci(ad, maas)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO isciler(ad, maas) VALUES (:1, :2)",
        (ad, maas)
    )

    conn.commit()
    conn.close()


def get_all_isciler():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM isciler")

    data = cursor.fetchall()

    conn.close()

    return data