import sqlite3

if __name__ == '__main__':

	conn = sqlite3.connect('../dnd_brain/dnd.db')
	crsr = conn.cursor()
	crsr.execute(
		'CREATE TABLE user (user_id text, age real, health real, '
		'money real, evil real, ch_status text, city text)')

	crsr.execute(
		'CREATE TABLE symptoms (user_id text, disease text, '
		'year real, damage real)')
	
	crsr.execute(
		'CREATE TABLE items (user_id text, name text, weight real)')

	crsr.execute(
		'CREATE TABLE drug_symptom (drug text, symptom text, year real)')

	crsr.execute(
		'CREATE TABLE drug_price (drug text, drug_price real)')

	crsr.execute(
		'CREATE TABLE crime_record (user_id text, crime_name text)')

	conn.commit()
	conn.close()
