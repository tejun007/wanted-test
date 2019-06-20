from flask_restplus import Model, fields

###################################################
# COMMON serializer
###################################################
response_serializer = Model('ResponseSerializer', {
    'success': fields.Boolean(description='응답되는 값이 성공적인 결과인지 여부'),
    'reason': fields.String(description='응답되는 값의 성공 여부에 대한 설명')
})

