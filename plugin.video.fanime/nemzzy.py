# Python code obfuscated by www.development-tools.net 
 

import base64, codecs
magic = 'IyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMNIyMjIyMjIyMjIyMjQ09ERSBCWSBATkVNWlpZNjY4IyMjIyMjIyMjIyMNIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMNaW1wb3J0IHhibWMseGJtY2FkZG9uLHhibWNndWkseGJtY3BsdWdpbix1cmxsaWIsdXJsbGliMixvcyxyZSxzeXMsYmFzZTY0LGpzb24sdGltZSxyZXF1ZXN0cyxpbXBvcnRsaWIscmVzb2x2ZXVybA1mcm9tIHJlc291cmNlcy5saWJzLmNvbW1vbl9hZGRvbiBpbXBvcnQgQWRkb24NZnJvbSBiczQgaW1wb3J0IEJlYXV0aWZ1bFNvdXANZnJvbSBkYXRldGltZSBpbXBvcnQgZGF0ZXRpbWUNZnJvbSByZXNvdXJjZXMubGlicy5tb2R1bGVzIGltcG9ydCBjbGVhbnRleHQNcmVsb2FkKHN5cykNc3lzLnNldGRlZmF1bHRlbmNvZGluZygidXRmLTgiKQ0jIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIw1hZGRvbl9pZCAgICAgICAgICAgID0gJ3BsdWdpbi52aWRlby5mYW5pbWUnDWFkZG9uICAgICAgICAgICAgICAgPSBBZGRvbihhZGRvbl9pZCwgc3lzLmFyZ3YpDXNlbGZBZGRvbiAgICAgICAgICAgPSB4Ym1jYWRkb24uQWRkb24oaWQ9YWRkb25faWQpDUFkZG9uVGl0bGUgICAgICAgICAgPSAnW0NPTE9SIG1hZ2VudGFdW0JdRkFOaW1lWy9DT0xPUl1bL0JdJw1BZGRvbmZhbmFydCAgICAgICAgID0geGJtYy50cmFuc2xhdGVQYXRoKG9zLnBhdGguam9pbignc3BlY2lhbDovL2hvbWUvYWRkb25zLycgKyBhZGRvbl9pZCwgJ2ZhbmFydC5qcGcnKSkNQWRkb25pY29uICAgICAgICAgICA9IHhibWMudHJhbnNsYXRlUGF0aChvcy5wYXRoLmpvaW4oJ3NwZWNpYWw6Ly9ob21lL2FkZG9ucy8nICsgYWRkb25faWQsICdpY29uLnBuZycpKQ1BZGRvbkRlc2MgICAgICAgICAgID0gJ1tDT0xPUiBtYWdlbnRhXVtCXUZBTmltZSBXYXMgQ3JlYXRlZCBCeSBATmVtenp5NjY4ICggRm9sbG93IE9uIFR3aXR0ZXIgKVsvQ09MT1JdWy9CXScNZHAgICAgICAgICAgICAgICAgICA9IHhibWNndWkuRGlhbG9nUHJvZ3Jlc3MoKQ1kaWFsb2cgICAgICAgICAgICAgID0geGJtY2d1aS5EaWFsb2coKQ0jIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIw1kZWYgR2V0TWVudSgpOg0JYWRkRGlyKCdbQ09MT1IgbWFnZW50YV1bQl1SZWNlbnQgUmVsZWFzZXNbL0NPTE9SXVsvQl0nLCdodHRwczovL3d3dzE3LmdvZ29hbmltZS5pby9hbmltZS1saXN0Lmh0bWwnLDIsQWRkb25pY29uLEFkZG9uZmFuYXJ0LEFkZG9uRGVzYykNCWFkZERpcignW0NPTE9SIG1hZ2VudGFdW0JdQSB0byBaWy9DT0xPUl1bL0JdJywnaHR0cHM6Ly93d3cxNy5nb2dvYW5pbWUuaW8vYW5pbWUtbGlzdC5odG1sJywzLEFkZG9uaWNvbixBZGRvbmZhbmFydCxBZGRvbkRlc2MpDQlhZGREaXIoJ1tDT0xPUiBtYWdlbnRhXVtCXUdlbnJlc1svQ09MT1JdWy9CXScsJ2h0dHBzOi8vd3d3MTcuZ29nb2FuaW1lLmlvLycsNSxBZGRvbmljb24sQWRkb25mYW5hcnQsQWRkb25EZXNjKQ0JYWRkRGlyKCdbQ09MT1IgbWFnZW50YV1bQl1OZXcgU2Vhc29uc1svQ09MT1JdWy9CXScsJ2h0dHBzOi8vd3d3MTcuZ29nb2FuaW1lLmlvL25ldy1zZWFzb24uaHRtbCcsNixBZGRvbmljb24sQWRkb25mYW5hcnQsQWRkb25EZXNjKQ0JYWRkRGlyKCdbQ09MT1IgbWFnZW50YV1bQl1PbmdvaW5nIFNlcmllc1svQ09MT1JdWy9CXScsJ2h0dHBzOi8vd3d3MTcuZ29nb2FuaW1lLmlvJyw3LEFkZG9uaWNvbixBZGRvbmZhbmFydCxBZGRvbkRlc2MpDQlhZGREaXIoJ1tDT0xPUiBtYWdlbnRhXVtCXVJlY2VudGx5IEFkZGVkIFNlcmllc1svQ09MT1JdWy9CXScsJ2h0dHBzOi8vd3d3MTcuZ29nb2FuaW1lLmlvJyw4LEFkZG9uaWNvbixBZGRvbmZhbmFydCxBZGRvbkRlc2MpDQlhZGREaXIoJ1tDT0xPUiBtYWdlbnRhXVtCXU1vdmllc1svQ09MT1JdWy9CXScsJ2h0dHBzOi8vd3d3MTcuZ29nb2FuaW1lLmlvL2FuaW1lLW1vdmllcy5odG1sJyw2LEFkZG9uaWNvbixBZGRvbmZhbmFydCxBZGRvbkRlc2MpDQlhZGREaXIoJ1tDT0xPUiBtYWdlbnRhXVtCXVBvcHVsYXJbL0NPTE9SXVsvQl0nLCdodHRwczovL3d3dzE3LmdvZ29hbmltZS5pby9wb3B1bGFyLmh0bWwnLDYsQWRkb25pY29uLEFkZG9uZmFuYXJ0LEFkZG9uRGVzYykNCWFkZERpcignW0NPTE9SIGFxdWFdW0JdU0VBUkNIWy9DT0xPUl1bL0JdJywndXJsJyw5LEFkZG9uaWNvbixBZGRvbmZhbmFydCxBZGRvbkRlc2MpDWRlZiBTZWFyY2goKToNCXN0cmluZyA9JycNCVNlYXJjaFVybCA9ICgnaHR0cHM6Ly93d3cxNy5nb2dvYW5pbWUuaW8vL3NlYXJjaC5odG1sP2tleXdvcmQ9JXMnKQ0Ja2V5Ym9hcmQgPSB4Ym1jLktleWJvYXJkKHN0cmluZywgJ1tDT0xPUiBtYWdlbnRhXVtCXVdoYXQgV291bGQgWW91IExpa2UgVG8gU2VhcmNoIEZvcj9bL0JdWy9DT0xPUl0nKQ0Ja2V5Ym9hcmQuZG9Nb2RhbCgpDQlpZiBrZXlib2FyZC5pc0NvbmZpcm1lZCgpOg0JCXN0cmluZyA9IGtleWJvYXJkLmdldFRleHQoKQ0JCWlmIGxlbihzdHJpbmcpPjE6DQkJCXN0cmluZyA9IHN0cmluZy5yZXBsYWNlKCcgJywnLScpDQkJCVNlYXJjaCA9IChTZWFyY2hVcmwgJXN0cmluZykNCQkJTWFpbkNvbnRlbnQoU2VhcmNoKQ0JCWVsc2U6IGRpYWxvZy5ub3RpZmljYXRpb24oQWRkb25UaXRsZSwgJ1tDT0xPUiBnb2xkXU5vIFRlcm0gRW50ZXJlZFsvQ09MT1JdJywgQWRkb25pY29uLCAyNTAwKQ0JZWxzZTogZGlhbG9nLm5vdGlmaWNhdGlvbihBZGRvblRpdGxlLCAnW0NPTE9SIGdvbGRdU2VhcmNoIENhbmNlbGxlZFsvQ09MT1JdJywgQWRkb25pY29uLCAyNTAwKQ1kZWYgUmVjZW50KHVybCk6DQloZWFkZXJzID0geydVc2VyLUFnZW50JzogJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS82MC4wLjMxMTIuMTEzIFNhZmFyaS81MzcuMzYnfQ0JbGluayA9IHJlcXVlc3RzLmdldCh1cmwsaGVhZGVycz1oZWFkZXJzKS5jb250ZW50DQlzb3VwID0gQmVhdXRpZnVsU291cChsaW5rLCdodG1sLnBhcnNlcicpDQlkYXRhID0gc291cC5maW5kKCduYXYnLCBjbGFzc189eydtZW51X3JlY2VudCd9KQ0JYmFzZV9kb21haW4gPSAnaHR0cHM6Ly93d3cxNy5nb2dvYW5pbWUuaW8nDQlmb3IgaSBpbiBkYXRhLmZpbmRfYWxsKCdsaScpOg0JCW5hbWUgPSBpLmFbJ3RpdGxlJ10uZW5jb2RlKCd1dGYtOCcpDQkJdXJsMiA9IGkuYVsnaHJlZiddDQkJdXJsMiA9IGJhc2VfZG9tYWluK3VybDIgaWYgdXJsMi5zdGFydHN3aXRoKCcvJykgZWxzZSB1cmwyDQkJaWNvbiA9IGkuZmluZCgnZGl2JywgY2xhc3NfPXsndGh1bWJuYWlsLXJlY2VudCd9KQ0JCWljb24gPSByZS5maW5kYWxsKHInJycoaHR0cC4qPylbJyJdJycnLHN0cihpY29uKSlbMF0NCQllcGkgPSBpLnAudGV4dC5lbmNvZGUoJ3V0Zi04JykNCQlhZGREaXIoJ1tDT0xPUiBtYWdlbnRhXVtCXSVzIHwgJXNbL0NPTE9SXVsvQl0nICUgKG5hbWUsZXBpKSx1cmwyLDIwLGljb24sQWRkb25mYW5hcnQsZGVzY3JpcHRpb249JycpDWRlZiBBVE9aKHVybCk6DQloZWFkZXJzID0geydVc2VyLUFnZW50JzogJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS82MC4wLjMxMTIuMTEzIFNhZmFyaS81MzcuMzYnfQ0JbGluayA9IHJlcXVlc3RzLmdldCh1cmwsaGVhZGVycz1oZWFkZXJzKS5jb250ZW50DQlzb3VwID0gQmVhdXRpZnVsU291cChsaW5rLCdodG1sLnBhcnNlcicpDQlkYXRhID0gc291cC5maW5kX2FsbCgnbGknLCBjbGFzc189eydmaXJzdC1jaGFyJ30pDQliYXNlX2RvbWFpbiA9ICdodHRwczovL3d3dzE3LmdvZ29hbmltZS5pbycNCWZvciBpIGluIGRhdGE6DQkJbmFtZSA9IGkuYS50ZXh0DQkJdXJsMiA9IGkuYVsnaHJlZiddDQkJdXJsMiA9IGJhc2VfZG9tYWluK3VybDIgaWYgdXJsMi5zdGFydHN3aXRoKCcvJykgZWxzZSB1cmwyDQkJYWRkRGlyKCdbQ09MT1IgbWFnZW50YV1bQl0lc1svQ09MT1JdWy9CXScgJSBuYW1lLHVybDIsNCxBZGRvbmljb24sQWRkb25mYW5hcnQsQWRkb25EZXNjKQ1kZWYgQVRPWkNvbnRlbnQodXJsKToNCWhlYWRlcnMgPSB7J1VzZXItQWdlbnQnOiAnTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hy'
love = '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'
god = 'aHJvbWUvNjAuMC4zMTEyLjExMyBTYWZhcmkvNTM3LjM2J30NCWJhc2VfZG9tYWluID0gJ2h0dHBzOi8vd3d3MTcuZ29nb2FuaW1lLmlvJw0JbGluayA9IHJlcXVlc3RzLmdldCh1cmwsaGVhZGVycz1oZWFkZXJzKS5jb250ZW50DQlzb3VwID0gQmVhdXRpZnVsU291cChsaW5rLCdodG1sLnBhcnNlcicpDQlkYXRhID0gc291cC5maW5kKCJkaXYiLCAgY2xhc3NfPXsnb3ZlcnZpZXcnfSkNCWZvciBpIGluIGRhdGEuZmluZF9hbGwoJ2xpJyk6DQkJbmFtZSA9IGkuYVsndGl0bGUnXS5lbmNvZGUoJ3V0Zi04JykNCQl1cmwyID0gaS5hWydocmVmJ10NCQl1cmwyID0gYmFzZV9kb21haW4rdXJsMiBpZiB1cmwyLnN0YXJ0c3dpdGgoJy8nKSBlbHNlIHVybDINCQlhZGREaXIoJ1tDT0xPUiBtYWdlbnRhXVtCXSVzWy9DT0xPUl1bL0JdJyAlIG5hbWUsdXJsMiwxMCxBZGRvbmljb24sQWRkb25mYW5hcnQsZGVzY3JpcHRpb249JycpDWRlZiBSZWNlbnRseUFkZGVkKHVybCk6DQloZWFkZXJzID0geydVc2VyLUFnZW50JzogJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS82MC4wLjMxMTIuMTEzIFNhZmFyaS81MzcuMzYnfQ0JYmFzZV9kb21haW4gPSAnaHR0cHM6Ly93d3cxNy5nb2dvYW5pbWUuaW8nDQlsaW5rID0gcmVxdWVzdHMuZ2V0KHVybCxoZWFkZXJzPWhlYWRlcnMpLmNvbnRlbnQNCXNvdXAgPSBCZWF1dGlmdWxTb3VwKGxpbmssJ2h0bWwucGFyc2VyJykNCWRhdGEgPSBzb3VwLmZpbmQoImRpdiIsICBjbGFzc189eydhZGRlZF9zZXJpZXNfYm9keSBmaW5hbCd9KQ0JZm9yIGkgaW4gZGF0YS5maW5kX2FsbCgnbGknKToNCQluYW1lID0gaS5hWyd0aXRsZSddLmVuY29kZSgndXRmLTgnKQ0JCXVybDIgPSBpLmFbJ2hyZWYnXQ0JCXVybDIgPSBiYXNlX2RvbWFpbit1cmwyIGlmIHVybDIuc3RhcnRzd2l0aCgnLycpIGVsc2UgdXJsMg0JCWFkZERpcignW0NPTE9SIG1hZ2VudGFdW0JdJXNbL0NPTE9SXVsvQl0nICUgbmFtZSx1cmwyLDEwLEFkZG9uaWNvbixBZGRvbmZhbmFydCxkZXNjcmlwdGlvbj0nJykNZGVmIExpbmtHZXR0ZXIobmFtZSx1cmwsaWNvbmltYWdlLGRlc2NyaXB0aW9uKToNCWhlYWRlcnMgPSB7J1VzZXItQWdlbnQnOiAnTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzYwLjAuMzExMi4xMTMgU2FmYXJpLzUzNy4zNid9DQlsaW5rID0gcmVxdWVzdHMuZ2V0KHVybCxoZWFkZXJzPWhlYWRlcnMpLmNvbnRlbnQNCXNvdXAgPSBCZWF1dGlmdWxTb3VwKGxpbmssJ2h0bWwucGFyc2VyJykNCWRhdGEgPSBzb3VwLmZpbmQoJ2RpdicsIGNsYXNzXz17J2FuaW1lX211dGlfbGluayd9KQ0JZm91bmQgPSAwDQlmb3IgaSBpbiBkYXRhLmZpbmRfYWxsKCdhJyk6DQkJc291cmNlcyA9IGlbJ2RhdGEtdmlkZW8nXQ0JCXNvdXJjZXMgPSAnaHR0cHM6Jytzb3VyY2VzIGlmIHNvdXJjZXMuc3RhcnRzd2l0aCgnLy8nKSBlbHNlIHNvdXJjZXMNCQlpZiByZXNvbHZldXJsLkhvc3RlZE1lZGlhRmlsZShzb3VyY2VzKToNCQkJZm91bmQgKz0gMQ0JCQluYW1lID0gKCdTb3VyY2UgJXMnICUgZm91bmQpDQkJCWFkZExpbmsoJ1tDT0xPUiBtYWdlbnRhXVtCXSVzWy9DT0xPUl1bL0JdJyAlIG5hbWUsc291cmNlcyw5OSxpY29uaW1hZ2UsQWRkb25mYW5hcnQsZGVzY3JpcHRpb24pDWRlZiBQTEFZTElOSyhuYW1lLGxpbmssaWNvbmltYWdlKToNCWRpYWxvZy5ub3RpZmljYXRpb24oQWRkb25UaXRsZSwgJ1tDT0xPUiB5ZWxsb3ddSHVudGluZyBMaW5rIE5vdyBCZSBQYXRpZW50Wy9DT0xPUl0nLCBBZGRvbmljb24sIDI1MDApDQl0cnk6DQkJaG1mID0gcmVzb2x2ZXVybC5Ib3N0ZWRNZWRpYUZpbGUodXJsKQ0JCWlmIGhtZi52YWxpZF91cmwoKTogbGluayA9IGhtZi5yZXNvbHZlKCkNCQlpZiBub3QgJ3VzZXItYWdlbnQnIGluIGxpbmsubG93ZXIoKTogbGluayA9IGxpbmsrJ3xVc2VyLUFnZW50PU1vemlsbGEvNS4wIChXaW5kb3dzOyBVOyBXaW5kb3dzIE5UIDUuMTsgZW4tR0I7IHJ2OjEuOS4wLjMpIEdlY2tvLzIwMDgwOTI0MTcgRmlyZWZveC8zLjAuMycNCQl4Ym1jcGx1Z2luLnNldFJlc29sdmVkVXJsKGludChzeXMuYXJndlsxXSksIFRydWUsIHhibWNndWkuTGlzdEl0ZW0ocGF0aD1saW5rKSkNCQlxdWl0KCkNCWV4Y2VwdCBFeGNlcHRpb24sIGU6DQkJZGlhbG9nLm5vdGlmaWNhdGlvbihBZGRvblRpdGxlLCJbQl1bQ09MT1IgeWVsbG93XSVzWy9CXVsvQ09MT1JdIiAlIHN0cihlKSxBZGRvbmljb24sNTAwMCkNCQlxdWl0KCkNZGVmIENMRUFOVVAodGV4dCk6DQl0ZXh0ID0gc3RyKHRleHQpDQl0ZXh0ID0gdGV4dC5yZXBsYWNlKCdcXHInLCcnKQ0JdGV4dCA9IHRleHQucmVwbGFjZSgnXFxuJywnJykNCXRleHQgPSB0ZXh0LnJlcGxhY2UoJ1xcdCcsJycpDQl0ZXh0ID0gdGV4dC5yZXBsYWNlKCdcXCcsJycpDQl0ZXh0ID0gdGV4dC5yZXBsYWNlKCc8YnIgLz4nLCdcbicpDQl0ZXh0ID0gdGV4dC5yZXBsYWNlKCc8aHIgLz4nLCcnKQ0JdGV4dCA9IHRleHQucmVwbGFjZSgnJiMwMzk7JywiJyIpDQl0ZXh0ID0gdGV4dC5yZXBsYWNlKCcmIzM5OycsIiciKQ0JdGV4dCA9IHRleHQucmVwbGFjZSgnJnF1b3Q7JywnIicpDQl0ZXh0ID0gdGV4dC5yZXBsYWNlKCcmcnNxdW87JywiJyIpDQl0ZXh0ID0gdGV4dC5yZXBsYWNlKCcmYW1wOycsIiYiKQ0JdGV4dCA9IHRleHQucmVwbGFjZSgnJiM4MjExOycsIiYiKQ0JdGV4dCA9IHRleHQucmVwbGFjZSgnJiM4MjE3OycsIiciKQ0JdGV4dCA9IHRleHQucmVwbGFjZSgnJiMwMzg7JywiJiIpDQl0ZXh0ID0gdGV4dC5yZXBsYWNlKCcmIzgyMTE7JywiLSIpDQl0ZXh0ID0gdGV4dC5yZXBsYWNlKCcmbmJzcDsnLCIiKQ0JdGV4dCA9IHRleHQucmVwbGFjZSgnJmhlbGxpcDsnLCIuLi4iKQ0JdGV4dCA9IHRleHQucmVwbGFjZSgnJiM4MjIwOycsIlwiIikNCXRleHQgPSB0ZXh0LnJlcGxhY2UoJyYjODIzMDsnLCIuLi4iKQ0JdGV4dCA9IHRleHQucmVwbGFjZSgnJiM4MjIxOycsIlwiIikNCXRleHQgPSB0ZXh0LmxzdHJpcCgnICcpDQl0ZXh0ID0gdGV4dC5sc3RyaXAoJwknKQ0JcmV0dXJuIHRleHQNZGVmIGFkZERpcihuYW1lLHVybCxtb2RlLGljb25pbWFnZSxmYW5hcnQsZGVzY3JpcHRpb249JycpOg0JdHJ5OiBkZXNjcmlwdGlvbiA9IGRlc2NyaXB0aW9uLmVuY29kZShlbmNvZGluZz0nVVRGLTgnLGVycm9ycz0nc3RyaWN0JykNCWV4Y2VwdCA6IHBhc3MNCXU9c3lzLmFyZ3ZbMF0rIj91cmw9Iit1cmxsaWIucXVvdGVfcGx1cyh1cmwpKyImbW9kZT0iK3N0cihtb2RlKSsiJm5hbWU9Iit1cmxsaWIucXVvdGVfcGx1cyhuYW1lKSsiJmljb25pbWFnZT0iK3VybGxpYi5xdW90ZV9wbHVzKGljb25pbWFnZSkrIiZmYW5hcnQ9Iit1cmxsaWIucXVvdGVfcGx1cyhmYW5hcnQpKyImZGVzY3JpcHRpb249Iit1cmxsaWIucXVvdGVfcGx1cyhkZXNjcmlwdGlvbikNCW9rPVRydWUNCWxpej14Ym1jZ3VpLkxpc3RJdGVtKG5hbWUsIGljb25JbWFnZT1pY29uaW1hZ2UsIHRodW1ibmFpbEltYWdlPWljb25pbWFnZSwpDQlsaXouc2V0UHJvcGVydHkoICJmYW5hcnRfSW1hZ2UiLCBmYW5hcnQgKQ0JbGl6LnNldFByb3BlcnR5KCAiaWNvbl9JbWFnZSIsIGljb25pbWFnZSApDQlsaXouc2V0SW5mbygndmlkZW8nLCB7J1Bsb3QnOiBkZXNjcmlwdGlvbn0pDQl2aWV3PXhibWNwbHVnaW4uc2V0Q29udGVudChpbnQoc3lzLmFyZ3ZbMV0pLCAnbW92aWVzJykNCW9rPXhibWNwbHVnaW4uYWRkRGlyZWN0b3J5SXRlbShoYW5kbGU9aW50KHN5cy5hcmd2WzFdKSx1cmw9dSxsaXN0aXRlbT1saXosaXNGb2xkZXI9VHJ1ZSkNCXJldHVybiBvaw1kZWYgYWRkTGluayhuYW1lLCB1cmwsIG1vZGUsIGljb25pbWFnZSwgZmFuYXJ0LCBkZXNjcmlwdGlvbj0nJyxmYW1pbHk9JycpOg0JaWYgbm90IGRlc2NyaXB0aW9uOiBkZXNjcmlwdGlvbiA9ICdGQU5pbWUgV2FzIENyZWF0ZWQgQnkgQE5lbXp6eTY2OCAoIEZvbGxvdyBPbiBUd2l0dGVyICknDQl1PXN5cy5hcmd2WzBdKyI/dXJsPSIrdXJsbGliLnF1b3RlX3BsdXModXJsKSsiJm1vZGU9IitzdHIobW9kZSkrIiZuYW1lPSIrdXJsbGliLnF1b3RlX3BsdXMobmFtZSkrIiZpY29uaW1hZ2U9Iit1cmxsaWIucXVvdGVfcGx1cyhpY29uaW1hZ2UpKyImZmFuYXJ0PSIrdXJsbGliLnF1b3RlX3BsdXMoZmFuYXJ0KQ0Jb2s9VHJ1ZQ0J'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))