from fastapi import Query, Depends


class PagesPaginationParams:
    def __init__(
            self,
            limit: int = Query(50, ge=0, le=1_000),
            offset: int = Query(0, ge=0, alias='skip'),
    ) -> None:
        self.limit = limit
        self.offset = offset
