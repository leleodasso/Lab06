from database.DB_connect import DBConnect
from model.product import Product
from model.retailer import Retailer
from model.sales import Sales


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


    @staticmethod
    def getBrand():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select distinct Product_brand
                    from go_products """

        cursor.execute(query)

        res = [row["Product_brand"] for row in cursor.fetchall()]

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getRetail():
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

    @staticmethod
    def FiltroTop(anno, brand, retailer):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """ SELECT * 
                            FROM go_daily_sales
                            WHERE YEAR(`Date`) = %s
                            AND Retailer_code = %s
                            AND Product_number IN (
                                SELECT Product_number 
                                FROM go_products gp  
                                WHERE gp.Product_brand = %s );
                        """

        cursor.execute(query, (anno, retailer, brand))
        res = []
        for row in cursor:
            res.append(Sales(**row))

        cursor.close()
        cnx.close()
        return res


if __name__ == '__main__':
    print(DAO.getAnno())
    print(DAO.getBrand())
    print(DAO.getRetail())
