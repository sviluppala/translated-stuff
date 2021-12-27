"""tool to get simple operation with the staging db"""

from services.mysql_db_worker import MySqlDbWorker


class MySqlDbUtility:

    db_worker = None

    def __init__(self, connection):
        self.db_worker = MySqlDbWorker(connection)

    def get_parsed_offer(self, creation_date, sender_mail):
        """:return offer info in a friendly format"""
        offer = self.db_worker.get_offer(creation_date, sender_mail)
        parsed_offer = []
        if offer:
            offer = offer[0]
            parsed_offer.append((offer[0],   # id
                                 offer[3],   # id_project
                                 offer[8],   # author_name
                                 offer[1],   # important
                                 offer[2],   # notarization
                                 offer[4],   # id_auto_request
                                 offer[5],   # id_customer
                                 offer[6],   # customer_type
                                 offer[8],   # requester_name
                                 offer[9],   # requester_tel
                                 offer[10],  # lang
                                 offer[11],  # am
                                 offer[13],  # am_fetch_datetime
                                 offer[14],  # response_date
                                 offer[15],  # target_response_date
                                 offer[16],  # sys_response_date
                                 offer[19],  # fax_confirm_request
                                 offer[22],  # fax_confirm_date
                                 offer[23],  # first_offer
                                 offer[24],  # current_offer
                                 offer[25],  # accepted_offer
                                 offer[28]   # suggested_translator
                                 ))
        return parsed_offer
