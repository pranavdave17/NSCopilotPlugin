from openapi_core import OpenAPI
# from openapi_core.validation.request.validators import RequestValidator
# from openapi_core.validation.response.validators import ResponseValidator
# from openapi_core.templating.paths.finders import PathFinder
from openapi_core.contrib.requests import RequestsOpenAPIRequest, RequestsOpenAPIResponse
import requests
import yaml

# Load OpenAPI Specification
with open("OpenAPI_spec_timeAPI.yaml", "r") as spec_file:
    spec_dict = yaml.safe_load(spec_file)

spec = OpenAPI.from_dict(spec_dict)

# Initialize Validators
# request_validator = RequestValidator(spec)
# response_validator = ResponseValidator(spec)

# Example: Validate a Request
def validate_request():
    # Simulate a request using the `requests` library
    url = "https://www.timeapi.io/api/time/current/zone"
    headers = {}
    params = {"timeZone": "UTC"}
    request = requests.Request("GET", url, headers=headers, params=params)
    prepared_request = request.prepare()

    # Convert to OpenAPI request
    openapi_request = RequestsOpenAPIRequest(prepared_request)

    # Validate the request
    result = spec.validate_request(openapi_request)
    # if result.errors:
    #     print("Request validation errors:", result.errors)
    # else:
    #     print("Request is valid!")

# Example: Validate a Response
def validate_response():
    # Simulate a response
    response = requests.Response()
    response.status_code = 200
    response._content = b'{"year": 2025, "month": 6, "day": 3, "hour": 11, "minute": 44, "seconds": 6, "milliSeconds": 554, "dateTime": "2025-06-03T11:44:06.5547003", "date": "06/03/2025", "time": "11:44", "timeZone": "UTC", "dayOfWeek": "Tuesday", "dstActive": false}'
    response.headers["Content-Type"] = "application/json"

    # Convert to OpenAPI response
    openapi_response = RequestsOpenAPIResponse(response)
    
    url = "https://www.timeapi.io/api/time/current/zone"
    headers = {}
    params = {"timeZone": "UTC"}
    request = requests.Request("GET", url, headers=headers, params=params)
    prepared_request = request.prepare()

    # Convert to OpenAPI request
    openapi_request = RequestsOpenAPIRequest(prepared_request)

    # Validate the response
    openapi_request = RequestsOpenAPIRequest(prepared_request)
    result = spec.validate_response(openapi_request, openapi_response)
    # if result.errors:
    #     print("Response validation errors:", result.errors)
    # else:
    #     print("Response is valid!")

# Run validation examples
validate_request()
validate_response()



# 4. use the start and end datetime to search netskope data using `NetskopeDataSearch` skill and provide a summary.
#                    - limit - required
#                    - timeout - required
#                    - starttime - required
#                    - endtime - required
#                    - offset - required
#                    - sublimit - not-required
#                    - groupbys - not-required
#                    - subgroupbys - not-required
#                    - orderbys - not-required
#                    - fields - not-required
#                    - query - not-required

#                    For getuci
#                     - capPerUser - not-required default is 1
#                     - fromTime - not-required default is 0
#                     - users - required - list of users [user1, user2, user3]
                
#                 provide details output of operations done at each stage.
        #   - "NetskopeDataSearch"
        
        

#   /api/v2/incidents/uba/getuci:
#     post:
#       summary: Get confidence index or UCI score for a user or multiple users
#       description: |
#         get confidence index or UCI score for a user or multiple users.
#         #PromptExample: get confidence index for xyz@gmail.com
#         #PromptExample: fetch UCI score for user.name
#         #PromptExample: What is the UCI score for abc.efg@domain.com?
#         #PromptExample: WHat is the <user>'s confidence index?
#       requestBody:
#         content:
#           application/json:
#             schema:
#               type: object
#               properties:
#                 capPerUser:
#                   description: >-
#                     It is an optional parameter. The default value is 7. Be notice the
#                     parameter with the size of users will affects the performance of
#                     the API
#                   format: int32
#                   type: integer
#                   default: 1
#                 fromTime:
#                   format: int64
#                   type: integer
#                   default: 0
#                 users:
#                   description: a list of users. The length of the list should not bigger than 512
#                   items:
#                     type: string
#                   type: array
#               required:
#                 - users
#                 - fromTime
#         required: true
#       responses:
#         '200':
#           content:
#             application/json:
#               schema:
#                 "$ref": "#/components/schemas/ConfidenceTimeSeries"
#           description: successful request
#         '400':
#           content:
#             application/json:
#               schema:
#                 "$ref": "#/components/schemas/ErrorResponse"
#           description: invalid request
#       tags:
#       - incidents
