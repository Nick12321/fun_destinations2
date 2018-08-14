from funplace.models import Places
from django.db import DatabaseError

class FunplaceController:

	def getFunplaces(self):
		return Places.objects.all()

	def savePlace(self, name, country):
		if not name or not country:
			return False
		place = Places(name = name, country =country)
		try:
			place.save()
		except DatabaseError:
			return False
		return True
