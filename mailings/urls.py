from django.urls import path

from mailings.views import CampaignListView, CampaignListActiveView, CampaignListCreatedView, CampaignListCompletedView, \
    CampaignDetailView, CampaignCreateView, CampaignUpdateView, CampaignDeleteView, StartEmailAttemptView, \
    StopEmailAttemptView, EmailAttemptListView, EmailAttemptSuccessfulListView, EmailAttemptFailedListView, \
    EmailAttemptDeleteView, EmailAttemptDetailView, CampaignBreakAllView, CampaignStartAllView, ContactsTemplateView

app_name = "newsletter"

urlpatterns = [
    path("campaigns/all/", CampaignListView.as_view(), name="campaign_list"),
    path("campaign/<int:pk>/", CampaignDetailView.as_view(), name="campaign_detail"),
    path("campaign/new/", CampaignCreateView.as_view(), name="campaign_create"),
    path("campaign/<int:pk>/edit/", CampaignUpdateView.as_view(), name="campaign_edit"),
    path("campaign/<int:pk>/delete/", CampaignDeleteView.as_view(), name="campaign_delete"),
    path("campaign/start/<int:pk>/", StartEmailAttemptView.as_view(), name="start_email"),
    path("campaign/stop/<int:pk>/", StopEmailAttemptView.as_view(), name="stop_email"),
    path("campaigns/break/", CampaignBreakAllView.as_view(), name="campaign_break"),
    path("campaigns/start/", CampaignStartAllView.as_view(), name="campaign_start"),
    path("campaigns/active/", CampaignListActiveView.as_view(), name="campaign_list_active"),
    path("campaigns/created/", CampaignListCreatedView.as_view(), name="campaign_list_created"),
    path("campaigns/compleated/", CampaignListCompletedView.as_view(), name="campaign_list_compleated"),
    path("emailattempts/", EmailAttemptListView.as_view(), name="emailattempt_list"),
    path("emailattempts/successful/", EmailAttemptSuccessfulListView.as_view(), name="emailattempt_list_successful"),
    path("emailattempts/failed/", EmailAttemptFailedListView.as_view(), name="emailattempt_list_failed"),
    path("emailattempt/<int:pk>/", EmailAttemptDetailView.as_view(), name="emailattempt_detail"),
    path("emailattempt/<int:pk>/delete/", EmailAttemptDeleteView.as_view(), name="emailattempt_delete"),
    path("contacts/", ContactsTemplateView.as_view(), name="contacts")]
