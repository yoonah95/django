class VersionViewSet(viewsets.ModelViewSet):
	queryset = Version.objects.all()
	serializer_class = VersionSerializer
