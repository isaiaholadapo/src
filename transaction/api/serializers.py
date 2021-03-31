from rest_framework import serializers

from transaction.models import AccountDetail


class AccountDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountDetail
        fields = ['account_number', 'balance', 'account_type', 'user_name']