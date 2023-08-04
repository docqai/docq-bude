"""Page: Admin / Manage User Groups."""

from st_pages import add_page_title
from utils.layout import auth_required, create_user_group_ui, list_user_groups_ui

auth_required(requiring_admin=True)

add_page_title()

create_user_group_ui()
list_user_groups_ui()