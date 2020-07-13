# -*- coding: utf-8 -*-

import graphene
from graphene_django.debug import DjangoDebug


# class Query(
#     ApplicationSettingsQuery,
#     CommissionManagementQuery,
#     DeprecatedCommissionManagementQuery,
#     DeprecatedDjangoAdminQuery,
#     DeprecatedPublisherDashboardQuery,
#     DeprecatedVendorDashboardQuery,
#     DjangoAdminQuery,
#     GiftingQuery,
#     LinkSystemQuery,
#     ProductQuery,
#     ProfileQuery,
#     PublisherDashboardQuery,
#     ScorecardQuery,
#     VendorContractQuery,
#     VendorDashboardQuery,
#     VendorQuery,
#     graphene.ObjectType
# ):
#
#     debug = graphene.Field(DjangoDebug, name='__debug')
#
#
# class Mutation(graphene.ObjectType):
#     create_a_link = CreateALinkMutation.Field()
#     product_like = ProductLikeMutation.Field()
#     hijack = HijackMutation.Field()
#     byejack = ByejackMutation.Field()
#     create_session = CreateSessionMutation.Field()
#     delete_session = DeleteSessionMutation.Field()
#     reset_password = ResetPasswordMutation.Field()
#     gdpr_consent = GdprConsentMutation.Field()
#     apply_invitation = ApplyForInvitationMutation.Field()
#     publisher_signup_request = PublisherSignUpRequestMutation.Field()
#     activate_user = ActivateUserMutation.Field()
#     send_confirmation_email = SendConfirmationEmailMutation.Field()
#     user_tracking = UserTrackingMutation.Field()
#     visit_tracking = VisitTrackingMutation.Field()
#     upgrade_premium = UpgradePremiumMutation.Field()
#     click_commissions = DeprecatedClickCommissionsMutation.Field()
#     group_click_commissions = GroupClickCommissionsMutation.Field()
#     group_order_commission = GroupOrderCommissionMutation.Field()
#     group_order_commissions = GroupOrderCommissionMutation.Field()
#     individual_click_commissions = IndividualClickCommissionsMutation.Field()
#     individual_order_commission = IndividualOrderCommissionMutation.Field()
#     user_application = UserApplicationMutation.Field()
#     verify_user_application_email = VerifyUserApplicationEmailMutation.Field()
#     create_user_from_application = CreateUserFromApplicationMutation.Field()
#     gifting_setup = GiftingSetupMutation.Field()
#
#
# schema = graphene.Schema(query=Query, mutation=Mutation)
