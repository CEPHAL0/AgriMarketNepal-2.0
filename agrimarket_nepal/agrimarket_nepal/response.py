from rest_framework import renderers
from rest_framework.response import Response


class APIResponse(Response):
    def __init__(self, data=None, status=None, message=None, **kwargs):
        super().__init__(data=data, status=status, **kwargs)
        self.message = message


class BaseApiRenderer(renderers.JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        status_code = renderer_context["response"].status_code
        message = getattr(renderer_context["response"], "message", None)

        response = {"status": "success", "data": data, "message": message}

        if not str(status_code).startswith("2"):
            response["status"] = "error"
            response["data"] = None

            if not message:
                response["message"] = "An error occured"

        return super(BaseApiRenderer, self).render(
            response, accepted_media_type, renderer_context
        )
