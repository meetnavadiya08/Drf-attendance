


class ExampleMiddleware:

    def __init__(self , get_response) -> None:
        self.get_response = get_response

    def __call__ (self,request):
        print("Request Path:", request.path)  # View પહેલાં ચાલશે
        response = self.get_response(request)
        print("Response Status:", response.status_code)  # View પછી ચાલશે
        return response