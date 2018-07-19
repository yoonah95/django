class Version(models.Model):
	version = model.CharField(max_length=10)

	def __str__(self):
		return self.version