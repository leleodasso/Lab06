from database.DB_connect import DBConnect
from model.Retailer import Retailer


class DAO():

    @staticmethod
    def getAnno():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select distinct  year(gds.Date)
            from go_daily_sales gds  """

        cursor.execute(query)

        res = [row['year(gds.Date)'] for row in cursor.fetchall()]

        cursor.close()
        cnx.close()
        return res



    @classmethod
    def getBrand(cls):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select distinct Product_brand
                    from go_products  """

        cursor.execute(query)

        res = [row["Product_brand"] for row in cursor.fetchall()]

        cursor.close()
        cnx.close()
        return res

    @classmethod
    def getRetail(cls):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select * from go_retailers  """

        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Retailer(**row))


        cursor.close()
        cnx.close()
        return res



if __name__ == '__main__':
    print(DAO.getAnno())
    print(DAO.getBrand())
    print(DAO.getRetail())
