class queue:

    @staticmethod
    def put(log):
        data = log.__dict__
        data["messages"] = log.messages
        print(data)
        #Please assume that this will be implemented already.
