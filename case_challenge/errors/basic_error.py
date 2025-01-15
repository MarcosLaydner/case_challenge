class BasicError(Exception):
    def __init__(
        self,
        status: int = 500,
        msg="API handled error",
    ):
        super().__init__(msg)
        self.status = status
        self.msg = msg

    def as_dict(self):
        return {"msg": self.msg, "status": self.status}
