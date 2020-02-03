L_100 = [
'100 Continue',
'101 Switching Protocols',
'102 Processing',
'103 Early Hints']

L_200 = [
'200 OK',
'201 Created',
'202 Accepted',
'203 Non-Authoritative Information',
'204 No Content',
'205 Reset Content',
'206 Partial Content',
'207 Multi-Status',
'208 Already Reported',
'226 IM Used'
]

L_300 = [
'3xx Redirection',
'300 Multiple Choices',
'301 Moved Permanently',
'302 Found (Previously "Moved temporarily")',
'303 See Other',
'304 Not Modified',
'305 Use Proxy (since HTTP/1.1)',
'306 Switch Proxy',
'307 Temporary Redirect (since HTTP/1.1)',
'308 Permanent Redirect']

L_400 = [
'400 Bad Request',
'401 Unauthorized',
'402 Payment Required',
'403 Forbidden',
'404 Not Found',
'405 Method Not Allowed',
'406 Not Acceptable',
'407 Proxy Authentication Required',
'408 Request Timeout',
'409 Conflict',
'410 Gone',
'411 Length Required',
'412 Precondition Failed',
'413 Payload Too Large',
'414 URI Too Long',
'415 Unsupported Media Type',
'416 Range Not Satisfiable',
'417 Expectation Failed',
'418 I''m a teapot',
'421 Misdirected Request',
'422 Unprocessable Entity',
'423 Locked',
'424 Failed Dependency',
'425 Too Early',
'426 Upgrade Required',
'428 Precondition Required',
'429 Too Many Requests',
'431 Request Header Fields Too Large',
'451 Unavailable For Legal Reasons']

L_500 = [
'500 Internal Server Error',
'501 Not Implemented',
'502 Bad Gateway',
'503 Service Unavailable',
'504 Gateway Timeout',
'505 HTTP Version Not Supported',
'506 Variant Also Negotiates',
'507 Insufficient Storage',
'508 Loop Detected',
'510 Not Extended',
'511 Network Authentication Required']

L_unof = [
'103 Checkpoint',
'218 This is fine (Apache Web Server)',
'419 Page Expired (Laravel Framework)',
'420 Method Failure (Spring Framework)',
'420 Enhance Your Calm (Twitter)',
'430 Request Header Fields Too Large (Shopify)',
'450 Blocked by Windows Parental Controls (Microsoft)',
'498 Invalid Token (Esri)',
'499 Token Required (Esri)',
'509 Bandwidth Limit Exceeded (Apache Web Server/cPanel)',
'526 Invalid SSL Certificate',
'529 Site is overloaded',
'530 Site is frozen',
'598 (Informal convention) Network read timeout error']

L_IIS_codes = [
'440 Login Time-out',
'449 Retry With',
'451 Redirect']

L_nginx_codes = [
'444 No Response',
'494 Request header too large',
'495 SSL Certificate Error',
'496 SSL Certificate Required',
'497 HTTP Request Sent to HTTPS Port',
'499 Client Closed Request']

L_cloudflare_codes = [
'520 Web Server Returned an Unknown Error',
'521 Web Server Is Down',
'522 Connection Timed Out',
'523 Origin Is Unreachable',
'524 A Timeout Occurred',
'525 SSL Handshake Failed',
'526 Invalid SSL Certificate',
'527 Railgun Error',
'530 What antoher code']

L_AWS_Elastic_codes = [
'460 Client closed the connection with the load balancer before the idle timeout period elapsed',
'463 The load balancer received an X-Forwarded-For request header with more than 30 IP addresses'
]

def get_all_codes():
    return L_100, L_200, L_300, L_400, L_500, L_unof, L_IIS_codes, L_nginx_codes, L_cloudflare_codes, L_AWS_Elastic_codes
