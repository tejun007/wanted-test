class CompanySearchResponse(object):
    SUCCESS_COMPANIES = [dict(id=1,
                              name_ko='원티드랩',
                              name_en='Wantedlab',
                              name_ja='',
                              tag_ko='태그_4|태그_20|태그_16',
                              tag_en='tag_4|tag_20|tag_16',
                              tag_ja='タグ_4|タグ_20|タグ_16')]

    RESPONSES = [
        dict(success=False, reason='ParamsMissing', companies=[]),
        dict(success=True, reason='SUCCESS', companies=SUCCESS_COMPANIES),
        dict(success=True, reason='SUCCESS', companies=SUCCESS_COMPANIES),
        dict(success=True, reason='SUCCESS', companies=SUCCESS_COMPANIES),
        dict(success=True, reason='SUCCESS', companies=SUCCESS_COMPANIES),

        dict(success=True, reason='SUCCESS', companies=SUCCESS_COMPANIES),
        dict(success=True, reason='SUCCESS', companies=SUCCESS_COMPANIES),
        dict(success=True, reason='SUCCESS', companies=SUCCESS_COMPANIES),
        dict(success=True, reason='SUCCESS', companies=[]),
        dict(success=True, reason='SUCCESS', companies=SUCCESS_COMPANIES),
    ]


class AddCompanyTagsResponse(object):
    RESPONSES = [
        dict(success=False, reason='NoCompanyFound'),
        dict(success=True, reason='SUCCESS'),
        dict(success=True, reason='SUCCESS'),
        dict(success=True, reason='SUCCESS'),
        dict(success=True, reason='SUCCESS'),

        dict(success=False, reason='NoCompanyFound'),
        dict(success=True, reason='SUCCESS'),
        dict(success=True, reason='SUCCESS'),
        dict(success=True, reason='SUCCESS'),
        dict(success=True, reason='SUCCESS'),
    ]


class DeleteCompanyTagsResponse(object):
    RESPONSES = [
        dict(success=False, reason='NoCompanyFound'),
        dict(success=True, reason='SUCCESS'),
        dict(success=True, reason='SUCCESS'),
        dict(success=True, reason='SUCCESS'),
        dict(success=True, reason='SUCCESS'),

        dict(success=False, reason='NoCompanyFound'),
        dict(success=True, reason='SUCCESS'),
        dict(success=True, reason='SUCCESS'),
        dict(success=True, reason='SUCCESS'),
        dict(success=True, reason='SUCCESS'),
    ]
