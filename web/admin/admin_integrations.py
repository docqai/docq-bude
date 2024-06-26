"""Slack install handler."""

import streamlit as st

from web.utils.layout import render_integrations, render_slack_installation_button, tracer


@tracer.start_as_current_span("admin_integrations_page")
def admin_integrations_page() -> None:
    """Admin integrations section."""
    integrations = [
        {
            "name": "Slack",
            "description": "Slack is a business communication platform that allows teams to communicate and collaborate.",
            "icon": "slack",
            "url": "/api/integration/slack/v1/install",
        },
        {
            "name": "Teams",
            "description": "Google Drive is a file storage and synchronization service developed by Google.",
            "icon": "google-drive",
            "url": "/api/integration/google-drive/v1/install",
        },
    ]

    integration = st.selectbox(
        "Select an integration to get started",
        options=[integration["name"] for integration in integrations],
    )

    if integration == "Slack":
        render_slack_installation_button()

        render_integrations()

    else:
        st.info("Coming soon!")
