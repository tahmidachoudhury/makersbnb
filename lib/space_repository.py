from lib.space import Space

class SpaceRepository():
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * from spaces')
        spaces = []
        for row in rows:
            row = Space(row["id"], row["name"], row["location"], row["price"], row["description"], row["user_id"])
            spaces.append(row)
        return spaces
    

    def find(self, id):
        rows = self._connection.execute("SELECT * FROM spaces WHERE id = %s", [id])
        row = rows[0]
        return Space(row["id"], row["name"], row["location"], row["price"], row["description"], row["user_id"])

    def find_by_user_id(self, user_id):
        rows = self._connection.execute("SELECT * FROM spaces WHERE user_id = %s", [user_id])
        row = rows[0]
        return Space(row["id"], row["name"], row["location"], row["price"], row["description"], row["user_id"])
    
    def create(self, space):
        self._connection.execute('INSERT INTO spaces (name, location, price, description, user_id) VALUES (%s, %s, %s, %s, %s)', [space.name, space.location, space.price, space.description, space.user_id])
        return None

    def delete(self, space_id):
        self._connection.execute('DELETE FROM spaces WHERE id = %s', [space_id])
        return None
    
    def update(self, space):
        self._connection.execute('UPDATE spaces SET name = %s, location = %s, price = %s, description = %s, user_id = %s WHERE id = %s', [space.name, space.location, space.price, space.description, space.user_id, space.id])
        