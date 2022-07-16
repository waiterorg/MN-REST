from rest_framework.generics import GenericAPIView


class CustomGenericAPIView(GenericAPIView):
    """
    Add method and custom to GenericAPIView
    """

    def check_authentication_for_filter_objects(self, queryset):
        """
        check if user is authenticated can get all filter objects
        but is anonymous can get only one filter object .
        """
        if self.request.user.is_authenticated:
            filtered_queryset = self.filter_queryset(queryset)
            return filtered_queryset
        filtered_queryset = self.filter_queryset(queryset)[:1]
        return filtered_queryset

    def check_pagination_page(self, paginated_queryset, queryset):
        """
        check if paginated queryset does exist would be serializer
        and if does not exist queryset without pagination would be serializer .
        """
        if paginated_queryset is not None:
            serializer = self.get_serializer(paginated_queryset, many=True)
            return serializer
        serializer = self.get_serializer(queryset, many=True)
        return serializer
