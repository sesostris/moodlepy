from moodle import BaseMoodle, BaseBlog, BaseMessage, BaseUser, BaseWebservice


class Core(BaseMoodle):
    def __post_init__(self, moodle) -> None:
        self._blog = BaseBlog(moodle)
        self._message = BaseMessage(moodle)
        self._user = BaseUser(moodle)
        self._webservice = BaseWebservice(moodle)

    @property
    def blog(self) -> BaseBlog:
        return self._blog

    @property
    def message(self) -> BaseMessage:
        return self._message

    @property
    def user(self) -> BaseUser:
        return self._user

    @property
    def webservice(self) -> BaseWebservice:
        return self._webservice