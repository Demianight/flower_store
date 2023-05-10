from django.contrib import admin
from .models import Offer, Trade, OfferReview, SellerReview


class OfferAdmin(admin.ModelAdmin):
    pass


class TradeAdmin(admin.ModelAdmin):
    pass


class OfferReviewAdmin(admin.ModelAdmin):
    pass


class SellerReviewAdmin(admin.ModelAdmin):
    pass


admin.site.register(Offer, OfferAdmin)
admin.site.register(Trade, TradeAdmin)
admin.site.register(OfferReview, OfferReviewAdmin)
admin.site.register(SellerReview, SellerReviewAdmin)
