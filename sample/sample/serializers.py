class VersionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Version
		fields = ('version',)