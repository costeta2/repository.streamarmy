# Python code obfuscated by www.development-tools.net 
 

import base64, codecs
magic = 'aW1wb3J0IHhibWMKCmltcG9ydCB4Ym1jYWRkb24KCmltcG9ydCB4Ym1jZ3VpCgppbXBvcnQgeGJtY3BsdWdpbgoKaW1wb3J0IHN5cwoKCgppbXBvcnQgb3MKCmltcG9ydCByZQoKaW1wb3J0IHJlcXVlc3RzCgpmcm9tIGNvbW1vbl9hZGRvbiBpbXBvcnQgQWRkb24KCmRpYWxvZyA9IHhibWNndWkuRGlhbG9nKCkKCkFkZG9uVGl0bGUgPSAnW0NPTE9SIHJlZF1bQl1FW0NPTE9SIHllbGxvd11udGVyVGFpbiBNZVsvQl1bL0NPTE9SXScKCmFkZG9uX2lkICAgICAgICAgICAgPSAncGx1Z2luLnZpZGVvLkVudGVydGFpbk1lJwoKYWRkb24gICAgICAgICAgICAgICA9IEFkZG9uKGFkZG9uX2lkLCBzeXMuYXJndikKCnNlbGZBZGRvbiAgICAgICAgICAgPSB4Ym1jYWRkb24uQWRkb24oaWQ9YWRkb25faWQpCgpkZWYgY2hlY2t1cGRhdGVzKC'
love = 'x6PtbWpTyhVQ0tp2IfMxSxMT9hYzqyqSAyqUEcozpbW3OcovpcPtycMvOjnJ4tCG0tWlp6VUOcovN9VPqSJSOWHxIRWjbWnJLtpTyhVQ09VPqSJSOWHxIRWmbXPDymMJkzDJExo24hp2I0H2I0qTyhMltapTyhqKAyMPpfW0MuoUAyWlxXPDyxnJSfo2pho2fbDJExo25HnKEfMFjvJ0ACGR9FVUyyoTkiq11BMKptH2y0MFjtGx8tGH9FEFODG1NtIIOGVFODoTIup2HtqzymnKDtJ0ACGR9FVTkcoJIqnUE0pUZ6Yl9jnJ5mrKA0MJ0hL28hqJgoD09ZG1VtrJIfoT93KFO0olOaMJ5ypzS0MFOuovOOL2Ayp3ZtIT9eMJ4tEz9lVSgQG0kCHvOfnJ1yKHIhqTIlqTScox1yJ0ACGR9FVUyyoTkiq10tqTuyovOyoaEypvOcqPOuMaEypvOwoTywn2yhMlOin1fiD09ZG1WqVvxXPDymqUWcozptCFpaPtxWn2I5Lz9upzDtCFO4Lz1wYxgyrJWiLKWxXUA0'
god = 'cmluZywgJ1tDT0xPUiByZWRdUGxlYXNlIEVudGVyIFBpbiBHZW5lcmF0ZWQgRnJvbSBXZWJzaXRlKENhc2UgU2Vuc2l0aXZlKVsvQ09MT1JdJykKCQlrZXlib2FyZC5kb01vZGFsKCkKCQlpZiBrZXlib2FyZC5pc0NvbmZpcm1lZCgpOgoJCQlzdHJpbmcgPSBrZXlib2FyZC5nZXRUZXh0KCkKCQkJaWYgbGVuKHN0cmluZyk+MToKCQkJCXRlcm0gPSBzdHJpbmcudGl0bGUoKQoJCQkJc2VsZkFkZG9uLnNldFNldHRpbmcoJ3BpbicsdGVybSkKCQkJCWNoZWNrdXBkYXRlcygpCgkJCWVsc2U6IHF1aXQoKQoJCWVsc2U6CgkJCXF1aXQoKQoJaWYgbm90ICdFWFBJUkVEJyBpbiBwaW46CgkJcGludXJsY2hlY2sgPSAoJ2h0dHBzOi8vcGluc3lzdGVtLmNvLnVrL3NlcnZpY2UucGhwP2NvZGU9JXMmcGx1Z2luPVJuVmphMWx2ZFNFJyAlIHBpbi'
destiny = 'xXPDyfnJ5eVQ0tpzIkqJImqUZhM2I0XUOcoaIloTAbMJAeXF5wo250MJ50PtxWnJLtoTIhXTkcozfcVQj9ZvOipvNaHTyhVRI4pTylMJDaVTyhVTkcozf6PtxWPKAyoTMOMTEiov5mMKEGMKE0nJ5aXPqjnJ4aYPqSJSOWHxIRWlxXPDxWL2uyL2g1pTEuqTImXPxXPDyyoUAyBtbWPDylMJqcp3EypaOcovN9VUAyoTMOMTEiov5aMKEGMKE0nJ5aXPqjnJ51p2IxWlxXPDxWnJLtpzIanKA0MKWjnJ4tCG0tW0MuoUAyWmbXPDxWPKElrGbXPDxWPDylMKS1MKA0pl5aMKDbW2u0qUOmBv8ipTyhp3ymqTIgYzAiYaIeY2AbMJAeMKVhpTujC2AiMTH9BGx5BGxzpTk1M2yhCHIhqTIlqTScox1yWlxhL29hqTIhqNbWPDxWPKAyoTMOMTEiov5mMKEGMKE0nJ5aXPqjnJ51p2IxWljaIUW1MFpcPtxWPDyyrTAypUD6VUOup3ZXPDxWMJkmMGbtpTSmpjb='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))