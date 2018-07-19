class Version(models.Model):
	version = models.CharField(max_length=10)

	def __str__(self):
		return self.version