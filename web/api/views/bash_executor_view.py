from typing import Any
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from virtual_assistant.chains.bash.base import BashChain

class BashExecutorView(APIView):
    bash_executor: BashChain

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.bash_executor = BashChain()

    def post(self, request):
        input = request.data.get('input')

        if input is not None:
            output = self.bash_executor.run(input)
            return Response({"output": output}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Input is required."}, status=status.HTTP_400_BAD_REQUEST)
