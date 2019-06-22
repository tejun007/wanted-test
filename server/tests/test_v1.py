import json
import sys

from flask import url_for

from server.tests.testcases.requests import (AddCompanyTagsRequest, CompanySearchRequest,
                                             DeleteCompanyTagsRequest)
from server.tests.testcases.responses import (AddCompanyTagsResponse, CompanySearchResponse,
                                              DeleteCompanyTagsResponse)


def test_api_ping(client):
    res = client.get(url_for('ping'))
    assert res.json == {'pong': 'pong'}


def test_company_search(client, company_search):
    for i, params in enumerate(CompanySearchRequest.PARAMS):
        res = client.get(url_for('api_v1.company_search_api', **params))
        assert res.json == CompanySearchResponse.RESPONSES[i]


def test_add_company_tags(client, add_company_tags):
    for i, params in enumerate(AddCompanyTagsRequest.PARAMS):
        res = client.put(url_for('api_v1.company_tags_api', company_id=params['company_id']),
                         data=json.dumps(dict(**params)))
        assert res.json == AddCompanyTagsResponse.RESPONSES[i]


def test_delete_company_tags(client, delete_company_tags):
    for i, params in enumerate(DeleteCompanyTagsRequest.PARAMS):
        res = client.delete(url_for('api_v1.company_tags_api', company_id=params['company_id']),
                            data=json.dumps(dict(**params)))
        assert res.json == DeleteCompanyTagsResponse.RESPONSES[i]
