import pyodbc

class DataBase:
    def __init__(self, name='system.db'):
        self.name = name
        self.connection = None

    def connect(self):
        try:
            self.connection = pyodbc.connect(driver='SQL Server', server='NB\SQLEXPRESS', database='Canteen', uid='user-admin', pwd='password123')
        except pyodbc.Error as e:
            print("Error connecting to the database:", e)

    def close_connection(self):
        if self.connection:
            try:
                self.connection.close()
            except pyodbc.Error as e:
                print("Error closing the database connection:", e)

    #########################################################################################
    # WORKING WITH ACCOUNTS

    def register_account(self, full_data_set):
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO Account (client_name, client_cpf, client_email, client_phone, balance) VALUES (?, ?, ?, ?, ?)", full_data_set)
            self.connection.commit()
            return "OK"
        except pyodbc.Error as e:
            print("Error registering account:", e)
            return "Error"

    def get_all_accounts(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Account ORDER BY account_id")
            accounts = cursor.fetchall()
            return accounts
        except pyodbc.Error as e:
            print("Error retrieving all accounts:", e)

    def delete_account(self, account_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM Account WHERE account_id = ?", account_id)
            self.connection.commit()
            return "Client account successfully deleted!"
        except pyodbc.Error as e:
            print("Error deleting account:", e)
            return "Error deleting account!"

    def update_account(self, full_data_set):
        try:
            cursor = self.connection.cursor()
            for data in full_data_set:
                cursor.execute(f"UPDATE Account SET client_name=?, client_cpf=?, client_email=?, client_phone=?, balance=? WHERE account_id=?", data)
            self.connection.commit()
            return 'OK'
        except pyodbc.Error as e:
            print("Error updating account:", e)
            return 'Error'

    #########################################################################################
    # WORKING WITH ORDERS

    def get_product_id(self, product_name):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT product_id FROM Product WHERE product_name = ?", (product_name))
            product_id_tuple = cursor.fetchone()
            
            if product_id_tuple:
                return product_id_tuple[0]

            else:
                print("Product not found")
                return None
        except pyodbc.Error as e:
            print("Error getting product ID:", e)
            return None


    def get_product_price(self, product_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT product_price FROM Product WHERE product_id = ?", product_id)
            price_tuple = cursor.fetchone()
            if price_tuple:

                return price_tuple[0]
            else:
                print("Price not found!")
                return None
            
        except pyodbc.Error as e:
            print("Error getting product price:", e)

    def get_account(self, cpf):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT client_cpf, client_phone, client_name, balance FROM Account WHERE client_cpf=?", cpf)
            account_data = cursor.fetchall()
            return account_data
        except pyodbc.Error as e:
            print("Error retrieving account data:", e)
            return 'Error'

    def get_account_id(self, cpf):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT account_id FROM Account WHERE client_cpf=?", cpf)
            account_id = cursor.fetchone()[0]
            return account_id
        except pyodbc.Error as e:
            print("Error retrieving account ID:", e)
            return 'Error'

    def register_order(self, full_data_set):
        placeholders = "?, ?, ?, ?"
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"INSERT INTO [Order] (order_date, order_value, paid_value, change_value) VALUES ({placeholders})", full_data_set)
            self.connection.commit()
            return "OK"
        except pyodbc.Error as e:
            print("Error registering order:", e)
            return "Error"

    def get_last_order_id(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT MAX(order_id) FROM [Order]")
            order_id = cursor.fetchone()[0]
            return order_id
        except pyodbc.Error as e:
            print("Error retrieving last order ID:", e)
            return "Error"

    def register_order_item(self, full_data_set):
        try:
            placeholders = "?,?,?"
            cursor = self.connection.cursor()
            cursor.execute(f"INSERT INTO OrderItem (order_id, product_id, quantity) VALUES ({placeholders})", full_data_set)
            self.connection.commit()
            return "OK"
        except pyodbc.Error as e:
            print("Error adding order item:", e)
            return "Error"

    def get_cash_balance(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT closing_balance FROM CashRegister WHERE cash_register_id = (SELECT MAX(cash_register_id) FROM CashRegister)")
            previous_balance = cursor.fetchone()[0]

            return previous_balance
        except pyodbc.Error as e:
            print("Error retrieving cash balance:", e)
            return "Error"

    def register_cash(self, full_data_set):
        try:
            placeholders = "?,?,?"
            cursor = self.connection.cursor()
            cursor.execute(f"INSERT INTO CashRegister (cash_register_date, opening_balance, closing_balance) VALUES ({placeholders})", full_data_set)
            self.connection.commit()
            return "OK"
        except pyodbc.Error as e:
            print("Error inserting cash data:", e)
            return "Error"

    def get_account_balance(self, account_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT balance FROM Account WHERE account_id=?", account_id)
            account_balance = cursor.fetchone()[0]
            return account_balance
        except pyodbc.Error as e:
            print("Error retrieving account balance:", e)
            return 'Error'

    def update_account_balance(self, account_id, new_balance):
        try:
            cursor = self.connection.cursor()
            cursor.execute("UPDATE Account SET balance=? WHERE account_id=?", (new_balance, account_id))
            self.connection.commit()
        except pyodbc.Error as e:
            print('Error updating account balance:', e)

    def get_all_cash_data(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM CashRegister")
            cash_data = cursor.fetchall()
            return cash_data
        except pyodbc.Error as e:
            print("Error retrieving cash data:", e)
            return 'Error'

    def get_all_orders(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM [Order]")
            order_data = cursor.fetchall()
            return order_data
        except pyodbc.Error as e:
            print("Error retrieving orders:", e)
            return 'Error'

    def get_all_order_items(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM OrderItem")
            order_item_data = cursor.fetchall()
            return order_item_data
        except pyodbc.Error as e:
            print("Error retrieving order items:", e)
            return 'Error'

    def get_product_name(self, product_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT product_name FROM Product WHERE product_id=?", product_id)
            product_name = cursor.fetchone()[0]
            return product_name
        except pyodbc.Error as e:
            print("Error retrieving product name:", e)
            return 'Error'