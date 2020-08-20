import pymysql

try:
    db = pymysql.Connect(
        host = "localhost",
        port = 3306,
        user = "root",
        passwd = "12345",
        db = "ecommerce",
        charset= 'utf8'
    )

    cursor = db.cursor()

    sql = """
        update product set discount_price = 34560
        where product_code = '215673140'
    """

    if cursor.execute(sql):
        db.commit()
        print("수정성공")
    else:
        db.rollback()
        print("수정실패")
except Exception as e:
    print(e)
finally:
    db.close()