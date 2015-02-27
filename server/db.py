import motor

_db_instance = motor.MotorClient().auto_release

def Instance():
	return _db_instance