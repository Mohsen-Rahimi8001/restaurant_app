
class TableData:

    users = """ CREATE TABLE IF NOT EXISTS users (
					id integer PRIMARY KEY,
					first_name TEXT NOT NULL,
					last_name TEXT NOT NULL,
					email TEXT NOT NULL,
					phone_number TEXT NOT NULL,
					social_number TEXT NOT NULL,
					image TEXT NOT NULL
					password TEXT NOT NULL,
                    role INTEGER NOT NULL DEFAULT 1
                    orders TEXT,
                    cart TEXT,
					); """


    orders = """ CREATE TABLE IF NOT EXISTS orders (
    				id integer PRIMARY KEY,
    				foods TEXT,
    				date TEXT NOT NULL,
    				paid INTEGER DEFAULT 0,
    				reference_number TEXT,
    				delivered INTEGER DEFAULT 0,
    				); """


    menus = """ CREATE TABLE IF NOT EXISTS menus (
        			id integer PRIMARY KEY,
        			foods TEXT,
        			date TEXT NOT NULL,
        			); """


    gift_cards = """ CREATE TABLE IF NOT EXISTS gift_cards (
            		id integer PRIMARY KEY,
            		code TEXT NOT NULL,
            		expiration_date TEXT NOT NULL,
            		); """


    foods = """ CREATE TABLE IF NOT EXISTS foods (
					id integer PRIMARY KEY,
					title TEXT NOT NULL,
					stock INTEGER NOT NULL DEFAULT 1
					fixed_price INTEGER NOT NULL
					sale_price INTEGER NOT NULL
					description TEXT
					category TEXT NOT NULL
					materials TEXT NOT NULL
					image TEXT NOT NULL
					); """


