
class TableData():



	users = """ 
	CREATE TABLE IF NOT EXISTS users (			
	id integer PRIMARY KEY AUTOINCREMENT,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	email TEXT NOT NULL,
	phone_number TEXT NOT NULL,
	social_number TEXT NOT NULL,
	image TEXT NOT NULL,
	password TEXT NOT NULL,
	role INTEGER NOT NULL DEFAULT 1,
	orders TEXT,
	cart TEXT
	); """


	orders = """ 
	CREATE TABLE IF NOT EXISTS orders (
	id integer PRIMARY KEY AUTOINCREMENT,
	foods TEXT,
	order_date TEXT NOT NULL,
	deliver_date TEXT NOT NULL,
	payment_method INTEGER DEFAULT 1,
	reference_number TEXT,
	account_number TEXT,
	delivered INTEGER DEFAULT 0,
	confirmed INTEGER DEFAULT 0,
	user_id INTEGER NOT NULL
	
	); """


	menus = """
	CREATE TABLE IF NOT EXISTS menus (
	id integer PRIMARY KEY AUTOINCREMENT,
	title TEXT,
	foods TEXT,
	date TEXT NOT NULL
	); """


	gift_cards = """
	CREATE TABLE IF NOT EXISTS gift_cards (
	id integer PRIMARY KEY AUTOINCREMENT,
	code TEXT NOT NULL,
	start_date TEXT NOT NULL,
	expiration_date TEXT NOT NULL,
	amount integer NOT NULL,
	sent integer NOT NULL
	); """


	foods = """
	CREATE TABLE IF NOT EXISTS foods (
	id integer PRIMARY KEY AUTOINCREMENT,
	title TEXT NOT NULL,
	stock INTEGER NOT NULL DEFAULT 1,
	fixed_price INTEGER NOT NULL,
	sale_price INTEGER NOT NULL,
	description TEXT,
	category TEXT NOT NULL,
	materials TEXT NOT NULL,
	image TEXT NOT NULL
	); """


	comments = """
	CREATE TABLE IF NOT EXISTS comments (
	id integer PRIMARY KEY AUTOINCREMENT,
	comment TEXT NOT NULL,
	datetime TEXT NOT NULL,
	user_id INTEGER NOT NULL,
	food_id INTEGER NOT NULL
	);"""


	messages = """
	CREATE TABLE IF NOT EXISTS messages (
	id integer PRIMARY KEY AUTOINCREMENT,
	message TEXT NOT NULL,
	datetime TEXT NOT NULL,
	admin_email TEXT NOT NULL
	);"""


	Tables = [
		users,
		orders,
		menus,
		gift_cards,
		foods,
		comments,
		messages,
	]

