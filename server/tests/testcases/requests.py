class CompanySearchRequest(object):
    PARAMS = [
        dict(search_word='', tags=''),
        dict(search_word='원', tags=''),
        dict(search_word='티드', tags=''),
        dict(search_word='Want', tags=''),
        dict(search_word='', tags='태그_4'),

        dict(search_word='', tags='tag_20'),
        dict(search_word='', tags='タグ_16'),
        dict(search_word='티', tags='태그_5'),
        dict(search_word='원태', tags='태그_5'),
        dict(search_word='원티드', tags='태그_4'),
    ]


class AddCompanyTagsRequest(object):
    PARAMS = [
        dict(company_id='3', tag_ko='태그_1'),
        dict(company_id='1', tag_ko='태그_2', tag_en='tag_2'),
        dict(company_id='1', tag_ko='태그_3', tag_en='tag_3', tag_ja='タグ_6'),
        dict(company_id='1', tag_ko='태그_5', tag_en='tag_5', tag_ja='タグ_3'),
        dict(company_id='1', tag_ko='태그_6', tag_en='tag_6', tag_ja='タグ_5'),

        dict(company_id='4', tag_ko='테드_1'),
        dict(company_id='2', tag_ko='테드_2', tag_en='ted_2'),
        dict(company_id='2', tag_ko='테드_3', tag_en='ted_3', tag_ja='テッド_6'),
        dict(company_id='2', tag_ko='테드_5', tag_en='ted_5', tag_ja='テッド_3'),
        dict(company_id='2', tag_ko='테드_6', tag_en='ted_6', tag_ja='テッド_5'),
    ]


class DeleteCompanyTagsRequest(object):
    PARAMS = [
        dict(company_id='3', tag_ko='태그_1'),
        dict(company_id='1', tag_ko='태그_2', tag_en='tag_2'),
        dict(company_id='1', tag_ko='태그_3', tag_en='tag_3', tag_ja='タグ_6'),
        dict(company_id='1', tag_ko='태그_5', tag_en='tag_5', tag_ja='タグ_3'),
        dict(company_id='1', tag_ko='태그_6', tag_en='tag_6', tag_ja='タグ_5'),

        dict(company_id='4', tag_ko='테드_1'),
        dict(company_id='2', tag_ko='테드_2', tag_en='ted_2'),
        dict(company_id='2', tag_ko='테드_3', tag_en='ted_3', tag_ja='テッド_6'),
        dict(company_id='2', tag_ko='테드_5', tag_en='ted_5', tag_ja='テッド_3'),
        dict(company_id='2', tag_ko='테드_6', tag_en='ted_6', tag_ja='テッド_5'),
    ]
