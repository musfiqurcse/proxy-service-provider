class OutputMaker:

    def response_builder(self, message=None, result=None, output=None):
        response_data = {
            "message": message,
            "result": result,
            "output": output
        }
        return response_data
