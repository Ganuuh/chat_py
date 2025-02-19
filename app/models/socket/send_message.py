from typing import   Optional,  Dict ,  Any  ,List
import json
class SendMessage:
    def __init__(
        self,
        facebook_id: str,
        facebook: str,
        first_name: str,
        last_name: str,
        text_conversation: Optional[str],
        conversation: str,
        inbox_id: str,
        lead_source: str,
        content_type: str,
        file_names: Optional[List[Dict[str, Any]]],
        fb_reply_id: Optional[str],
        is_guest: bool,
        lead_type: str,
        lead_status: str,
        is_auto: bool,
        is_seen: bool,
    ):
        self.facebook_id = facebook_id
        self.facebook = facebook
        self.first_name = first_name
        self.last_name = last_name
        self.text_conversation = text_conversation
        self.conversation = conversation
        self.inbox_id = inbox_id
        self.lead_source = lead_source
        self.content_type = content_type
        self.file_names = file_names
        self.fb_reply_id = fb_reply_id
        self.is_guest = is_guest
        self.lead_type = lead_type
        self.lead_status = lead_status
        self.is_auto = is_auto
        self.is_seen = is_seen

    def to_json(self) -> str:
        """Convert the object to a JSON string."""
        return json.dumps(self.__dict__)