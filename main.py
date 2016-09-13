#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi
from caesar import encrypt

rot_head = """<h1>Enter whatever</h1>"""
rot_form = """
<form method="post">
    <div>
        <label for="rot">Rotate by:</label>
        <input type="text" name="rot" value="0">
    </div>
    <textarea name="text" style="height: 100px; width: 400px;">%(text)s</textarea>
    <br>
    <input type="submit">
</form>
"""

class Index(webapp2.RequestHandler):
    def writeit(self, text="", rot="0"):
        self.response.out.write(rot_head + rot_form % {"text": cgi.escape(text, quote=True), "rot": cgi.escape(rot,quote=True)})

    def get(self):
        self.writeit()

    def post(self):
        user_text = self.request.get("text")
        user_rot = self.request.get("rot")
        rottext = encrypt(user_text,int(user_rot))
        esctext = cgi.escape(rottext, quote=True)
        self.writeit(esctext)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
